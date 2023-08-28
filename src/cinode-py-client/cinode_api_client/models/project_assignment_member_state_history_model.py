from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.project_assignment_member_state import ProjectAssignmentMemberState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentMemberStateHistoryModel")


@_attrs_define
class ProjectAssignmentMemberStateHistoryModel:
    """
    Attributes:
        state (Union[Unset, ProjectAssignmentMemberState]):

            Tillagd = 0

            Offererad = 10

            Avböjd av kund = 20

            Avböjd av oss = 30

            Pausad = 40
        note (Union[Unset, None, str]):
    """

    state: Union[Unset, ProjectAssignmentMemberState] = UNSET
    note: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        note = self.note

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, ProjectAssignmentMemberState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ProjectAssignmentMemberState(_state)

        note = d.pop("note", UNSET)

        project_assignment_member_state_history_model = cls(
            state=state,
            note=note,
        )

        return project_assignment_member_state_history_model
