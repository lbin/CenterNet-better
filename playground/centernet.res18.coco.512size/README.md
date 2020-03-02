# centernet.res18.coco.512size  
## Evaluation results for bbox:  
```  
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.002
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.003
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.015
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.023
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.025
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.025
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.037
```  
|  AP   |  AP50  |  AP75  |  APs  |  APm  |  APl  |  
|:-----:|:------:|:------:|:-----:|:-----:|:-----:|  
| 0.161 | 0.505  | 0.062  | 0.052 | 0.271 | 0.315 |
### Per-category bbox AP:  

| category      | AP    | category     | AP    | category       | AP    |  
|:--------------|:------|:-------------|:------|:---------------|:------|  
| person        | 5.688 | bicycle      | 0.000 | car            | 0.008 |  
| motorcycle    | 0.001 | airplane     | 0.097 | bus            | 0.002 |  
| train         | 0.000 | truck        | 0.000 | boat           | 0.000 |  
| traffic light | 0.005 | fire hydrant | 0.006 | stop sign      | 0.010 |  
| parking meter | 0.016 | bench        | 0.000 | bird           | 0.032 |  
| cat           | 0.275 | dog          | 0.607 | horse          | 0.177 |  
| sheep         | 0.619 | cow          | 0.619 | elephant       | 0.540 |  
| bear          | 0.374 | zebra        | 0.492 | giraffe        | 0.282 |  
| backpack      | 0.000 | umbrella     | 0.000 | handbag        | 0.002 |  
| tie           | 0.000 | suitcase     | 0.000 | frisbee        | 0.075 |  
| skis          | 0.000 | snowboard    | 0.000 | sports ball    | 0.042 |  
| kite          | 0.033 | baseball bat | 0.000 | baseball glove | 0.005 |  
| skateboard    | 0.001 | surfboard    | 0.002 | tennis racket  | 0.015 |  
| bottle        | 0.001 | wine glass   | 0.000 | cup            | 0.034 |  
| fork          | 0.000 | knife        | 0.000 | spoon          | 0.000 |  
| bowl          | 0.263 | banana       | 0.050 | apple          | 0.009 |  
| sandwich      | 0.126 | orange       | 0.125 | broccoli       | 0.003 |  
| carrot        | 0.067 | hot dog      | 0.003 | pizza          | 0.497 |  
| donut         | 0.044 | cake         | 0.086 | chair          | 0.002 |  
| couch         | 0.000 | potted plant | 0.000 | bed            | 0.000 |  
| dining table  | 0.125 | toilet       | 0.318 | tv             | 0.000 |  
| laptop        | 0.005 | mouse        | 0.000 | remote         | 0.005 |  
| keyboard      | 0.000 | cell phone   | 0.012 | microwave      | 0.000 |  
| oven          | 0.000 | toaster      | 0.000 | sink           | 0.017 |  
| refrigerator  | 0.010 | book         | 0.000 | clock          | 1.024 |  
| vase          | 0.009 | scissors     | 0.000 | teddy bear     | 0.018 |  
| hair drier    | 0.000 | toothbrush   | 0.000 |                |       |
