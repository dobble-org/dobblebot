from pathlib import Path

import torch

class YoloService:

    def __init__(self, weights_path: Path) -> None:
        self._detector = torch.hub.load('yolov5', 'custom', path=weights_path, source='local') 
    
    