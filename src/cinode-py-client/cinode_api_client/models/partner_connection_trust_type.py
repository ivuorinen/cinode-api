from enum import IntEnum


class PartnerConnectionTrustType(IntEnum):
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_30 = 30
    VALUE_40 = 40
    VALUE_50 = 50
    VALUE_60 = 60
    VALUE_70 = 70

    def __str__(self) -> str:
        return str(self.value)
