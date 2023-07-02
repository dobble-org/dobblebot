from enum import Enum


class States(Enum):
    sending_photo = 'sending_photo'
    start_over = 'start_over'
    end = 'end'
