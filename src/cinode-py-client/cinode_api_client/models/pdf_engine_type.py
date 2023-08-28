from enum import IntEnum


class PdfEngineType(IntEnum):
    VALUE_0 = 0
    VALUE_2 = 2

    def __str__(self) -> str:
        return str(self.value)
