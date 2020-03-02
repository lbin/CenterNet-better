# centernet.res18.coco.512size  
## Evaluation results for bbox:  
```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.002
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.015
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.024
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.026
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.023
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.045
```  
|  AP   |  AP50  |  AP75  |  APs  |  APm  |  APl  |  
|:-----:|:------:|:------:|:-----:|:-----:|:-----:|  
| 0.171 | 0.491  | 0.082  | 0.061 | 0.507 | 0.279 |
### Per-category bbox AP:  

| category      | AP    | category     | AP    | category       | AP    |  
|:--------------|:------|:-------------|:------|:---------------|:------|  
| person        | 6.574 | bicycle      | 0.001 | car            | 0.007 |  
| motorcycle    | 0.012 | airplane     | 0.073 | bus            | 0.007 |  
| train         | 0.006 | truck        | 0.004 | boat           | 0.002 |  
| traffic light | 0.002 | fire hydrant | 0.006 | stop sign      | 0.220 |  
| parking meter | 0.000 | bench        | 0.001 | bird           | 0.070 |  
| cat           | 0.118 | dog          | 0.497 | horse          | 0.322 |  
| sheep         | 0.531 | cow          | 0.672 | elephant       | 0.593 |  
| bear          | 0.129 | zebra        | 0.667 | giraffe        | 0.056 |  
| backpack      | 0.001 | umbrella     | 0.000 | handbag        | 0.001 |  
| tie           | 0.000 | suitcase     | 0.000 | frisbee        | 0.010 |  
| skis          | 0.000 | snowboard    | 0.000 | sports ball    | 0.106 |  
| kite          | 0.012 | baseball bat | 0.000 | baseball glove | 0.007 |  
| skateboard    | 0.000 | surfboard    | 0.000 | tennis racket  | 0.003 |  
| bottle        | 0.015 | wine glass   | 0.000 | cup            | 0.036 |  
| fork          | 0.000 | knife        | 0.000 | spoon          | 0.000 |  
| bowl          | 0.674 | banana       | 0.033 | apple          | 0.073 |  
| sandwich      | 0.171 | orange       | 0.019 | broccoli       | 0.003 |  
| carrot        | 0.003 | hot dog      | 0.005 | pizza          | 0.279 |  
| donut         | 0.110 | cake         | 0.140 | chair          | 0.004 |  
| couch         | 0.000 | potted plant | 0.000 | bed            | 0.045 |  
| dining table  | 0.226 | toilet       | 0.233 | tv             | 0.000 |  
| laptop        | 0.000 | mouse        | 0.000 | remote         | 0.000 |  
| keyboard      | 0.000 | cell phone   | 0.000 | microwave      | 0.000 |  
| oven          | 0.000 | toaster      | 0.000 | sink           | 0.010 |  
| refrigerator  | 0.000 | book         | 0.001 | clock          | 0.865 |  
| vase          | 0.000 | scissors     | 0.000 | teddy bear     | 0.010 |  
| hair drier    | 0.000 | toothbrush   | 0.000 |                |       |
