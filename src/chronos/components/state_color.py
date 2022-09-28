# Copyright (C) 2022 Valerie GELBGRAS vgelbgra@gmail.com

from enum import Enum


class StateColor(Enum):
    START = 'success'
    PAUSE = 'danger'
    RESET = 'primary'
    LAPS = 'info'

    @property
    def state(self):
        return self.name
    
    @property
    def color(self):
        return self.value
