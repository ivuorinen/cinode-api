from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamManagerEditModel")


@_attrs_define
class TeamManagerEditModel:
    """
    Attributes:
        team_id (Union[Unset, int]):
        company_user_id (Union[Unset, int]):
    """

    team_id: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        company_user_id = self.company_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("teamId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        team_manager_edit_model = cls(
            team_id=team_id,
            company_user_id=company_user_id,
        )

        return team_manager_edit_model
