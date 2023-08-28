from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.company_user_status import CompanyUserStatus
from ..models.company_user_type import CompanyUserType
from ..models.project_assignment_member_state import ProjectAssignmentMemberState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="ProjectAssignmentMemberModel")


@_attrs_define
class ProjectAssignmentMemberModel:
    """
    Attributes:
        company_user_id (Union[Unset, None, int]):
        company_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        seo_id (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        company_user_type (Union[Unset, None, CompanyUserType]):

            Medarbetare = 0

            Kandidat = 10

            Underkonsult = 20

            Api = 30

            Bot = 40
        status (Union[Unset, None, CompanyUserStatus]):

            Frånkopplad = 0

            Kommande = 2

            Aktiv = 3
        project_assignment_member_id (Union[Unset, int]):
        project_assignment_member_state (Union[Unset, None, ProjectAssignmentMemberState]):

            Tillagd = 0

            Offererad = 10

            Avböjd av kund = 20

            Avböjd av oss = 30

            Pausad = 40
        links (Union[Unset, None, List['Link']]):
    """

    company_user_id: Union[Unset, None, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    company_user_type: Union[Unset, None, CompanyUserType] = UNSET
    status: Union[Unset, None, CompanyUserStatus] = UNSET
    project_assignment_member_id: Union[Unset, int] = UNSET
    project_assignment_member_state: Union[Unset, None, ProjectAssignmentMemberState] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        company_id = self.company_id
        id = self.id
        seo_id = self.seo_id
        first_name = self.first_name
        last_name = self.last_name
        company_user_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.company_user_type, Unset):
            company_user_type = self.company_user_type.value if self.company_user_type else None

        status: Union[Unset, None, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        project_assignment_member_id = self.project_assignment_member_id
        project_assignment_member_state: Union[Unset, None, int] = UNSET
        if not isinstance(self.project_assignment_member_state, Unset):
            project_assignment_member_state = (
                self.project_assignment_member_state.value if self.project_assignment_member_state else None
            )

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
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if id is not UNSET:
            field_dict["id"] = id
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company_user_type is not UNSET:
            field_dict["companyUserType"] = company_user_type
        if status is not UNSET:
            field_dict["status"] = status
        if project_assignment_member_id is not UNSET:
            field_dict["projectAssignmentMemberId"] = project_assignment_member_id
        if project_assignment_member_state is not UNSET:
            field_dict["projectAssignmentMemberState"] = project_assignment_member_state
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        company_user_id = d.pop("companyUserId", UNSET)

        company_id = d.pop("companyId", UNSET)

        id = d.pop("id", UNSET)

        seo_id = d.pop("seoId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _company_user_type = d.pop("companyUserType", UNSET)
        company_user_type: Union[Unset, None, CompanyUserType]
        if _company_user_type is None:
            company_user_type = None
        elif isinstance(_company_user_type, Unset):
            company_user_type = UNSET
        else:
            company_user_type = CompanyUserType(_company_user_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, CompanyUserStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyUserStatus(_status)

        project_assignment_member_id = d.pop("projectAssignmentMemberId", UNSET)

        _project_assignment_member_state = d.pop("projectAssignmentMemberState", UNSET)
        project_assignment_member_state: Union[Unset, None, ProjectAssignmentMemberState]
        if _project_assignment_member_state is None:
            project_assignment_member_state = None
        elif isinstance(_project_assignment_member_state, Unset):
            project_assignment_member_state = UNSET
        else:
            project_assignment_member_state = ProjectAssignmentMemberState(_project_assignment_member_state)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        project_assignment_member_model = cls(
            company_user_id=company_user_id,
            company_id=company_id,
            id=id,
            seo_id=seo_id,
            first_name=first_name,
            last_name=last_name,
            company_user_type=company_user_type,
            status=status,
            project_assignment_member_id=project_assignment_member_id,
            project_assignment_member_state=project_assignment_member_state,
            links=links,
        )

        return project_assignment_member_model
