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

import os
import sys
sys.path.insert(0, '.')  # noqa: E402

from colorama import Fore, Style

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

from dl_lib.config import add_centernet_config
from detectron2.config import get_cfg

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

def setup(args):
    """
    Create configs and perform basic setups.
    """
    cfg = get_cfg()
    add_centernet_config(cfg)
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    default_setup(cfg, args)
    return cfg

def main(args):
    # config.merge_from_list(args.opts)
    # cfg, logger = default_setup(config, args)

    cfg = setup(args)

    if args.eval_only:
        model = Trainer.build_model(cfg)
        DetectionCheckpointer(model, save_dir=cfg.OUTPUT_DIR).resume_or_load(
            cfg.MODEL.WEIGHTS, resume=args.resume
        )
        res = Trainer.test(cfg, model)
        if comm.is_main_process():
            verify_results(cfg, res)
        return res

    """
    If you'd like to do anything fancier than the standard training logic,
    consider writing your own training loop or subclassing the trainer.
    """
    trainer = Trainer(cfg)
    trainer.resume_or_load(resume=args.resume)

    return trainer.train()

if __name__ == "__main__":
    args = default_argument_parser().parse_args()
    print("soft link to {}".format(config.OUTPUT_DIR))
    config.link_log()
    print("Command Line Args:", args)
    launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )
