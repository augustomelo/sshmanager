from enum import Enum, auto


class Protocol(Enum):
    SSH = auto()
    SSH2 = auto()

    def __st__(self):
        return f'Protocol [value: {self.value}]'
