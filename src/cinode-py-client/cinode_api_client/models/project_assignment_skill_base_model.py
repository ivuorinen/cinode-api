from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_model import KeywordModel
    from ..models.link import Link


T = TypeVar("T", bound="ProjectAssignmentSkillBaseModel")


@_attrs_define
class ProjectAssignmentSkillBaseModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        customer_id (Union[Unset, int]):
        project_id (Union[Unset, int]):
        project_assignment_id (Union[Unset, int]):
        keyword_id (Union[Unset, int]):
        level (Union[Unset, int]):
        keyword (Union[Unset, None, KeywordModel]):
        links (Union[Unset, None, List['Link']]):
    """

    company_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    project_assignment_id: Union[Unset, int] = UNSET
    keyword_id: Union[Unset, int] = UNSET
    level: Union[Unset, int] = UNSET
    keyword: Union[Unset, None, "KeywordModel"] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        customer_id = self.customer_id
        project_id = self.project_id
        project_assignment_id = self.project_assignment_id
        keyword_id = self.keyword_id
        level = self.level
        keyword: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict() if self.keyword else None

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
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_assignment_id is not UNSET:
            field_dict["projectAssignmentId"] = project_assignment_id
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if level is not UNSET:
            field_dict["level"] = level
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyword_model import KeywordModel
        from ..models.link import Link

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_assignment_id = d.pop("projectAssignmentId", UNSET)

        keyword_id = d.pop("keywordId", UNSET)

        level = d.pop("level", UNSET)

        _keyword = d.pop("keyword", UNSET)
        keyword: Union[Unset, None, KeywordModel]
        if _keyword is None:
            keyword = None
        elif isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = KeywordModel.from_dict(_keyword)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        project_assignment_skill_base_model = cls(
            company_id=company_id,
            customer_id=customer_id,
            project_id=project_id,
            project_assignment_id=project_assignment_id,
            keyword_id=keyword_id,
            level=level,
            keyword=keyword,
            links=links,
        )

        return project_assignment_skill_base_model
