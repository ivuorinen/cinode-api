from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.team_base_model import TeamBaseModel


T = TypeVar("T", bound="TeamManagerModel")


@_attrs_define
class TeamManagerModel:
    """
    Attributes:
        team_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        company_user (Union[Unset, None, CompanyUserBaseModel]):
        team (Union[Unset, None, TeamBaseModel]):
    """

    team_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    company_user: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    team: Union[Unset, None, "TeamBaseModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        company_user_id = self.company_user_id
        company_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company_user, Unset):
            company_user = self.company_user.to_dict() if self.company_user else None

        team: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict() if self.team else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if company_user is not UNSET:
            field_dict["companyUser"] = company_user
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.team_base_model import TeamBaseModel

        d = src_dict.copy()
        team_id = d.pop("teamId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        _company_user = d.pop("companyUser", UNSET)
        company_user: Union[Unset, None, CompanyUserBaseModel]
        if _company_user is None:
            company_user = None
        elif isinstance(_company_user, Unset):
            company_user = UNSET
        else:
            company_user = CompanyUserBaseModel.from_dict(_company_user)

        _team = d.pop("team", UNSET)
        team: Union[Unset, None, TeamBaseModel]
        if _team is None:
            team = None
        elif isinstance(_team, Unset):
            team = UNSET
        else:
            team = TeamBaseModel.from_dict(_team)

        team_manager_model = cls(
            team_id=team_id,
            company_user_id=company_user_id,
            company_user=company_user,
            team=team,
        )

        return team_manager_model
