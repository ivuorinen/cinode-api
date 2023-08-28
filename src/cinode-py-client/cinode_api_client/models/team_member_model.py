from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.link import Link
    from ..models.team_base_model import TeamBaseModel


T = TypeVar("T", bound="TeamMemberModel")


@_attrs_define
class TeamMemberModel:
    """
    Attributes:
        team_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        company_user (Union[Unset, None, CompanyUserBaseModel]):
        team (Union[Unset, None, TeamBaseModel]):
        availability_percent (Union[Unset, None, int]):
        links (Union[Unset, None, List['Link']]):
    """

    team_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    company_user: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    team: Union[Unset, None, "TeamBaseModel"] = UNSET
    availability_percent: Union[Unset, None, int] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        company_user_id = self.company_user_id
        company_user: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company_user, Unset):
            company_user = self.company_user.to_dict() if self.company_user else None

        team: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict() if self.team else None

        availability_percent = self.availability_percent
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

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
        if availability_percent is not UNSET:
            field_dict["availabilityPercent"] = availability_percent
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.link import Link
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

        availability_percent = d.pop("availabilityPercent", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        team_member_model = cls(
            team_id=team_id,
            company_user_id=company_user_id,
            company_user=company_user,
            team=team,
            availability_percent=availability_percent,
            links=links,
        )

        return team_member_model
