from enum import IntEnum


class EventEntityType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7

    def __str__(self) -> str:
        return str(self.value)
