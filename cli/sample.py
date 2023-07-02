from pathlib import Path
from tap import Tap

from dobblebot.services.yolov5 import YoloService


class SampleCLI(Tap):
    weights: Path
    image: Path

if __name__ == '__main__':
    ARGUMENTS = SampleCLI(underscores_to_dashes=True).parse_args()
    SERVICE = YoloService(ARGUMENTS.weights)
    SERVICE.detect(ARGUMENTS.image)

