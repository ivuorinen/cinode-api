from enum import IntEnum


class AccessLevel(IntEnum):
    VALUE_0 = 0
    VALUE_50 = 50
    VALUE_100 = 100
    VALUE_110 = 110
    VALUE_115 = 115
    VALUE_150 = 150
    VALUE_180 = 180
    VALUE_200 = 200
    VALUE_240 = 240
    VALUE_250 = 250
    VALUE_270 = 270
    VALUE_300 = 300
    VALUE_400 = 400
    VALUE_500 = 500

    def __str__(self) -> str:
        return str(self.value)
