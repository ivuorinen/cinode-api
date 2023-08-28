from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamMemberEditModel")


@_attrs_define
class TeamMemberEditModel:
    """
    Attributes:
        availability_percent (Union[Unset, None, int]):
    """

    availability_percent: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        availability_percent = self.availability_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if availability_percent is not UNSET:
            field_dict["availabilityPercent"] = availability_percent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        availability_percent = d.pop("availabilityPercent", UNSET)

        team_member_edit_model = cls(
            availability_percent=availability_percent,
        )

        return team_member_edit_model
