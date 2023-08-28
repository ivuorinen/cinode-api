from enum import IntEnum


class ProjectPriority(IntEnum):
    VALUE_3 = 3
    VALUE_5 = 5
    VALUE_8 = 8

    def __str__(self) -> str:
        return str(self.value)
