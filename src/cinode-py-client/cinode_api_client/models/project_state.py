from enum import IntEnum


class ProjectState(IntEnum):
    VALUE_0 = 0
    VALUE_30 = 30
    VALUE_40 = 40
    VALUE_50 = 50
    VALUE_60 = 60

    def __str__(self) -> str:
        return str(self.value)
