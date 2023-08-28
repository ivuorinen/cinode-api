from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamMemberAddModel")


@_attrs_define
class TeamMemberAddModel:
    """
    Attributes:
        company_user_id (Union[Unset, int]):
        availability_percent (Union[Unset, None, int]):
    """

    company_user_id: Union[Unset, int] = UNSET
    availability_percent: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        availability_percent = self.availability_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if availability_percent is not UNSET:
            field_dict["availabilityPercent"] = availability_percent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_user_id = d.pop("companyUserId", UNSET)

        availability_percent = d.pop("availabilityPercent", UNSET)

        team_member_add_model = cls(
            company_user_id=company_user_id,
            availability_percent=availability_percent,
        )

        return team_member_add_model
