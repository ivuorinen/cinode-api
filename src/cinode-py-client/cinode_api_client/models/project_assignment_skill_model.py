from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_base_model import CompanyBaseModel
    from ..models.company_customer_base_model import CompanyCustomerBaseModel
    from ..models.keyword_model import KeywordModel
    from ..models.keyword_synonym_model import KeywordSynonymModel
    from ..models.link import Link
    from ..models.project_assignment_base_model import ProjectAssignmentBaseModel
    from ..models.project_base_model import ProjectBaseModel


T = TypeVar("T", bound="ProjectAssignmentSkillModel")


@_attrs_define
class ProjectAssignmentSkillModel:
    """
    Attributes:
        project_assignment (Union[Unset, None, ProjectAssignmentBaseModel]):
        project (Union[Unset, None, ProjectBaseModel]):
        company (Union[Unset, None, CompanyBaseModel]):
        customer (Union[Unset, None, CompanyCustomerBaseModel]):
        keyword_synonym_id (Union[Unset, int]):
        keyword_synonym (Union[Unset, None, KeywordSynonymModel]):
        is_mandatory (Union[Unset, bool]):
        company_id (Union[Unset, int]):
        customer_id (Union[Unset, int]):
        project_id (Union[Unset, int]):
        project_assignment_id (Union[Unset, int]):
        keyword_id (Union[Unset, int]):
        level (Union[Unset, int]):
        keyword (Union[Unset, None, KeywordModel]):
        links (Union[Unset, None, List['Link']]):
    """

    project_assignment: Union[Unset, None, "ProjectAssignmentBaseModel"] = UNSET
    project: Union[Unset, None, "ProjectBaseModel"] = UNSET
    company: Union[Unset, None, "CompanyBaseModel"] = UNSET
    customer: Union[Unset, None, "CompanyCustomerBaseModel"] = UNSET
    keyword_synonym_id: Union[Unset, int] = UNSET
    keyword_synonym: Union[Unset, None, "KeywordSynonymModel"] = UNSET
    is_mandatory: Union[Unset, bool] = UNSET
    company_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    project_assignment_id: Union[Unset, int] = UNSET
    keyword_id: Union[Unset, int] = UNSET
    level: Union[Unset, int] = UNSET
    keyword: Union[Unset, None, "KeywordModel"] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_assignment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project_assignment, Unset):
            project_assignment = self.project_assignment.to_dict() if self.project_assignment else None

        project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict() if self.project else None

        company: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict() if self.company else None

        customer: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict() if self.customer else None

        keyword_synonym_id = self.keyword_synonym_id
        keyword_synonym: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword_synonym, Unset):
            keyword_synonym = self.keyword_synonym.to_dict() if self.keyword_synonym else None

        is_mandatory = self.is_mandatory
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
        if project_assignment is not UNSET:
            field_dict["projectAssignment"] = project_assignment
        if project is not UNSET:
            field_dict["project"] = project
        if company is not UNSET:
            field_dict["company"] = company
        if customer is not UNSET:
            field_dict["customer"] = customer
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if keyword_synonym is not UNSET:
            field_dict["keywordSynonym"] = keyword_synonym
        if is_mandatory is not UNSET:
            field_dict["isMandatory"] = is_mandatory
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
        from ..models.company_base_model import CompanyBaseModel
        from ..models.company_customer_base_model import CompanyCustomerBaseModel
        from ..models.keyword_model import KeywordModel
        from ..models.keyword_synonym_model import KeywordSynonymModel
        from ..models.link import Link
        from ..models.project_assignment_base_model import ProjectAssignmentBaseModel
        from ..models.project_base_model import ProjectBaseModel

        d = src_dict.copy()
        _project_assignment = d.pop("projectAssignment", UNSET)
        project_assignment: Union[Unset, None, ProjectAssignmentBaseModel]
        if _project_assignment is None:
            project_assignment = None
        elif isinstance(_project_assignment, Unset):
            project_assignment = UNSET
        else:
            project_assignment = ProjectAssignmentBaseModel.from_dict(_project_assignment)

        _project = d.pop("project", UNSET)
        project: Union[Unset, None, ProjectBaseModel]
        if _project is None:
            project = None
        elif isinstance(_project, Unset):
            project = UNSET
        else:
            project = ProjectBaseModel.from_dict(_project)

        _company = d.pop("company", UNSET)
        company: Union[Unset, None, CompanyBaseModel]
        if _company is None:
            company = None
        elif isinstance(_company, Unset):
            company = UNSET
        else:
            company = CompanyBaseModel.from_dict(_company)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, None, CompanyCustomerBaseModel]
        if _customer is None:
            customer = None
        elif isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CompanyCustomerBaseModel.from_dict(_customer)

        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        _keyword_synonym = d.pop("keywordSynonym", UNSET)
        keyword_synonym: Union[Unset, None, KeywordSynonymModel]
        if _keyword_synonym is None:
            keyword_synonym = None
        elif isinstance(_keyword_synonym, Unset):
            keyword_synonym = UNSET
        else:
            keyword_synonym = KeywordSynonymModel.from_dict(_keyword_synonym)

        is_mandatory = d.pop("isMandatory", UNSET)

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

        project_assignment_skill_model = cls(
            project_assignment=project_assignment,
            project=project,
            company=company,
            customer=customer,
            keyword_synonym_id=keyword_synonym_id,
            keyword_synonym=keyword_synonym,
            is_mandatory=is_mandatory,
            company_id=company_id,
            customer_id=customer_id,
            project_id=project_id,
            project_assignment_id=project_assignment_id,
            keyword_id=keyword_id,
            level=level,
            keyword=keyword,
            links=links,
        )

        return project_assignment_skill_model
