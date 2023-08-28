from enum import IntEnum


class TemplateAssetType(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_100 = 100

    def __str__(self) -> str:
        return str(self.value)
