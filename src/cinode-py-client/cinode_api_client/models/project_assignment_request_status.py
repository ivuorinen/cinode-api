from enum import IntEnum


class ProjectAssignmentRequestStatus(IntEnum):
    VALUE_0 = 0
    VALUE_10 = 10
    VALUE_20 = 20

    def __str__(self) -> str:
        return str(self.value)
