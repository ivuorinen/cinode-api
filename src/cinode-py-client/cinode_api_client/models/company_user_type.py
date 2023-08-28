from enum import IntEnum


class CompanyUserType(IntEnum):
    VALUE_0 = 0
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_30 = 30
    VALUE_40 = 40

    def __str__(self) -> str:
        return str(self.value)
