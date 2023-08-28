import datetime
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.project_state import ProjectState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_state_reason_model import ProjectStateReasonModel


T = TypeVar("T", bound="ProjectStateHistoryModel")


@_attrs_define
class ProjectStateHistoryModel:
    """
    Attributes:
        state (Union[Unset, ProjectState]):

            Öppen = 0

            Vunnen = 30

            Förlorad = 40

            Avböjd = 50

            Uppskjuten = 60
        updated (Union[Unset, datetime.datetime]):
        reason (Union[Unset, None, ProjectStateReasonModel]):
    """

    state: Union[Unset, ProjectState] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    reason: Union[Unset, None, "ProjectStateReasonModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        reason: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict() if self.reason else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if updated is not UNSET:
            field_dict["updated"] = updated
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_state_reason_model import ProjectStateReasonModel

        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, ProjectState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ProjectState(_state)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, None, ProjectStateReasonModel]
        if _reason is None:
            reason = None
        elif isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ProjectStateReasonModel.from_dict(_reason)

        project_state_history_model = cls(
            state=state,
            updated=updated,
            reason=reason,
        )

        return project_state_history_model
