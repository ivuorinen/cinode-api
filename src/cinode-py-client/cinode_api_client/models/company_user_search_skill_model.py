from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.company_user_status import CompanyUserStatus
from ..models.company_user_type import CompanyUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_subcontractor_group_base_model import CompanySubcontractorGroupBaseModel
    from ..models.skill_result_model import SkillResultModel
    from ..models.team_base_model import TeamBaseModel


T = TypeVar("T", bound="CompanyUserSearchSkillModel")


@_attrs_define
class CompanyUserSearchSkillModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        company_user_id (Union[Unset, None, int]):
        firstname (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        lastname (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        seo_id (Union[Unset, None, str]):
        address_id (Union[Unset, None, int]):
        address_display_name (Union[Unset, None, str]):
        teams (Union[Unset, None, List['TeamBaseModel']]):
        skills (Union[Unset, None, List['SkillResultModel']]):
        status (Union[Unset, None, CompanyUserStatus]):

            Frånkopplad = 0

            Kommande = 2

            Aktiv = 3
        company_candidate_id (Union[Unset, None, int]):
        groups (Union[Unset, None, List['CompanySubcontractorGroupBaseModel']]):
        company_user_type (Union[Unset, CompanyUserType]):

            Medarbetare = 0

            Kandidat = 10

            Underkonsult = 20

            Api = 30

            Bot = 40
    """

    company_id: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    firstname: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    lastname: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    address_id: Union[Unset, None, int] = UNSET
    address_display_name: Union[Unset, None, str] = UNSET
    teams: Union[Unset, None, List["TeamBaseModel"]] = UNSET
    skills: Union[Unset, None, List["SkillResultModel"]] = UNSET
    status: Union[Unset, None, CompanyUserStatus] = UNSET
    company_candidate_id: Union[Unset, None, int] = UNSET
    groups: Union[Unset, None, List["CompanySubcontractorGroupBaseModel"]] = UNSET
    company_user_type: Union[Unset, CompanyUserType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        company_user_id = self.company_user_id
        firstname = self.firstname
        first_name = self.first_name
        lastname = self.lastname
        last_name = self.last_name
        title = self.title
        seo_id = self.seo_id
        address_id = self.address_id
        address_display_name = self.address_display_name
        teams: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            if self.teams is None:
                teams = None
            else:
                teams = []
                for teams_item_data in self.teams:
                    teams_item = teams_item_data.to_dict()

                    teams.append(teams_item)

        skills: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skills, Unset):
            if self.skills is None:
                skills = None
            else:
                skills = []
                for skills_item_data in self.skills:
                    skills_item = skills_item_data.to_dict()

                    skills.append(skills_item)

        status: Union[Unset, None, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        company_candidate_id = self.company_candidate_id
        groups: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            if self.groups is None:
                groups = None
            else:
                groups = []
                for groups_item_data in self.groups:
                    groups_item = groups_item_data.to_dict()

                    groups.append(groups_item)

        company_user_type: Union[Unset, int] = UNSET
        if not isinstance(self.company_user_type, Unset):
            company_user_type = self.company_user_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if title is not UNSET:
            field_dict["title"] = title
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if address_id is not UNSET:
            field_dict["addressId"] = address_id
        if address_display_name is not UNSET:
            field_dict["addressDisplayName"] = address_display_name
        if teams is not UNSET:
            field_dict["teams"] = teams
        if skills is not UNSET:
            field_dict["skills"] = skills
        if status is not UNSET:
            field_dict["status"] = status
        if company_candidate_id is not UNSET:
            field_dict["companyCandidateId"] = company_candidate_id
        if groups is not UNSET:
            field_dict["groups"] = groups
        if company_user_type is not UNSET:
            field_dict["companyUserType"] = company_user_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_subcontractor_group_base_model import CompanySubcontractorGroupBaseModel
        from ..models.skill_result_model import SkillResultModel
        from ..models.team_base_model import TeamBaseModel

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        firstname = d.pop("firstname", UNSET)

        first_name = d.pop("firstName", UNSET)

        lastname = d.pop("lastname", UNSET)

        last_name = d.pop("lastName", UNSET)

        title = d.pop("title", UNSET)

        seo_id = d.pop("seoId", UNSET)

        address_id = d.pop("addressId", UNSET)

        address_display_name = d.pop("addressDisplayName", UNSET)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = TeamBaseModel.from_dict(teams_item_data)

            teams.append(teams_item)

        skills = []
        _skills = d.pop("skills", UNSET)
        for skills_item_data in _skills or []:
            skills_item = SkillResultModel.from_dict(skills_item_data)

            skills.append(skills_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, CompanyUserStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyUserStatus(_status)

        company_candidate_id = d.pop("companyCandidateId", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = CompanySubcontractorGroupBaseModel.from_dict(groups_item_data)

            groups.append(groups_item)

        _company_user_type = d.pop("companyUserType", UNSET)
        company_user_type: Union[Unset, CompanyUserType]
        if isinstance(_company_user_type, Unset):
            company_user_type = UNSET
        else:
            company_user_type = CompanyUserType(_company_user_type)

        company_user_search_skill_model = cls(
            company_id=company_id,
            company_user_id=company_user_id,
            firstname=firstname,
            first_name=first_name,
            lastname=lastname,
            last_name=last_name,
            title=title,
            seo_id=seo_id,
            address_id=address_id,
            address_display_name=address_display_name,
            teams=teams,
            skills=skills,
            status=status,
            company_candidate_id=company_candidate_id,
            groups=groups,
            company_user_type=company_user_type,
        )

        return company_user_search_skill_model
