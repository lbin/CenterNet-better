# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
# Modified by Feng Wang
"""
Detection Training Script.

This scripts reads a given config file and runs the training or evaluation.
It is an entry point that is made to train standard models in dl_lib.

In order to let one script support training of many models,
this script contains logic that are specific to these built-in models and therefore
may not be suitable for your own project.
For example, your research project perhaps only needs a single "evaluator".

Therefore, we recommend you to use dl_lib as an library and take
this file as an example of how to use the library.
You may want to write your own script with your datasets and other customizations.
"""
import glob
import logging
import os
import re
import sys
sys.path.insert(0, '.')  # noqa: E402
from collections import OrderedDict

from detectron2.utils import comm
from dl_lib.configs.config import config
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.data import MetadataCatalog
from dl_lib.defaults import (DefaultTrainer2, default_setup)
from detectron2.engine.defaults import default_argument_parser
from detectron2.engine import hooks, SimpleTrainer, launch                    
from detectron2.evaluation import COCOEvaluator
from detectron2.evaluation.evaluator import DatasetEvaluator, DatasetEvaluators
from detectron2.evaluation.testing import verify_results
from dl_lib.centernet import build_model
from dl_lib.dataset_mapper import DatasetMapper
from detectron2.data import build_detection_test_loader, build_detection_train_loader

class Trainer(DefaultTrainer2):
    @classmethod
    def build_evaluator(cls, cfg, dataset_name, output_folder=None):
        if output_folder is None:
            output_folder = os.path.join(cfg.OUTPUT_DIR, "inference")
        return COCOEvaluator(dataset_name, cfg, True, output_folder)

    @classmethod
    def build_test_loader(cls, cfg, dataset_name):
        return build_detection_test_loader(cfg, dataset_name, mapper=DatasetMapper(cfg, False))

    @classmethod
    def build_train_loader(cls, cfg):
        return build_detection_train_loader(cfg, mapper=DatasetMapper(cfg, True))

def test_argument_parser():
    parser = default_argument_parser()
    parser.add_argument("--start-iter", type=int, default=0, help="start iter used to test")
    parser.add_argument("--end-iter", type=int, default=None,
                        help="end iter used to test")
    parser.add_argument("--debug", action="store_true", help="use debug mode or not")
    return parser
    
def main(args):
    config.merge_from_list(args.opts)
    cfg, logger = default_setup(config, args)
    if args.debug:
        batches = int(cfg.SOLVER.IMS_PER_BATCH / 8 * args.num_gpus)
        if cfg.SOLVER.IMS_PER_BATCH != batches:
            cfg.SOLVER.IMS_PER_BATCH = batches
            logger.warning("SOLVER.IMS_PER_BATCH is changed to {}".format(batches))

    if "MODEL.WEIGHTS" in args.opts:
        valid_files = [cfg.MODEL.WEIGHTS]
    else:
        list_of_files = glob.glob(os.path.join(cfg.OUTPUT_DIR, '*.pth'))
        assert list_of_files, "no pth file found in {}".format(cfg.OUTPUT_DIR)
        list_of_files.sort(key=os.path.getctime)
        latest_file = list_of_files[-1]
        if not args.end_iter:
            valid_files = [latest_file]
        else:
            files = [f for f in list_of_files if str(f) <= str(latest_file)]
            valid_files = []
            for f in files:
                try:
                    model_iter = int(re.split(r'(model_|\.pth)', f)[-3])
                except Exception:
                    logger.warning("remove {}".format(f))
                    continue
                if args.start_iter <= model_iter <= args.end_iter:
                    valid_files.append(f)
            assert valid_files, "No .pth files satisfy your requirement"

    # * means all if need specific format then *.csv
    for current_file in valid_files:
        cfg.MODEL.WEIGHTS = current_file
        model = build_model(cfg)

        DetectionCheckpointer(model, save_dir=cfg.OUTPUT_DIR).resume_or_load(
            cfg.MODEL.WEIGHTS, resume=args.resume
        )
        res = Trainer.test(cfg, model)
        if comm.is_main_process():
            verify_results(cfg, res)
        if cfg.TEST.AUG.ENABLED:
            res.update(Trainer.test_with_TTA(cfg, model))

    # return res


if __name__ == "__main__":
    args = test_argument_parser().parse_args()
    print("Command Line Args:", args)
    launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )
