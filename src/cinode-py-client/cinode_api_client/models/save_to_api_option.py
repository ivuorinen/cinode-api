from enum import IntEnum


class SaveToApiOption(IntEnum):
    VALUE_3 = 3
    VALUE_5 = 5

    def __str__(self) -> str:
        return str(self.value)
