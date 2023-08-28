import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.contract_type import ContractType
from ..models.extent_type import ExtentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_base_model import CompanyBaseModel
    from ..models.company_customer_base_model import CompanyCustomerBaseModel
    from ..models.currency_model import CurrencyModel
    from ..models.link import Link
    from ..models.project_assignment_member_model import ProjectAssignmentMemberModel
    from ..models.project_assignment_skill_base_model import ProjectAssignmentSkillBaseModel
    from ..models.project_base_model import ProjectBaseModel


T = TypeVar("T", bound="ProjectAssignmentModel")


@_attrs_define
class ProjectAssignmentModel:
    """
    Attributes:
        company (Union[Unset, None, CompanyBaseModel]):
        assigned (Union[Unset, None, ProjectAssignmentMemberModel]):
        prospects (Union[Unset, None, List['ProjectAssignmentMemberModel']]):
        seo_id (Union[Unset, None, str]):
        skills (Union[Unset, None, List['ProjectAssignmentSkillBaseModel']]):
        project_assignment_member_id (Union[Unset, None, int]):
        rate (Union[Unset, None, int]):
        oral_agreement_to_date (Union[Unset, None, datetime.datetime]):
        option_to_date (Union[Unset, None, datetime.datetime]):
        contract_type (Union[Unset, ContractType]):

            Timpris = 0

            Fastpris = 1
        is_assigned (Union[Unset, bool]):
        currency (Union[Unset, None, CurrencyModel]):
        company_id (Union[Unset, int]):
        customer_id (Union[Unset, int]):
        project_id (Union[Unset, int]):
        project (Union[Unset, None, ProjectBaseModel]):
        customer (Union[Unset, None, CompanyCustomerBaseModel]):
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        extent_type (Union[Unset, ExtentType]):

            Procent = 0

            Timmar = 1
        extent (Union[Unset, None, int]):
        links (Union[Unset, None, List['Link']]):
    """

    company: Union[Unset, None, "CompanyBaseModel"] = UNSET
    assigned: Union[Unset, None, "ProjectAssignmentMemberModel"] = UNSET
    prospects: Union[Unset, None, List["ProjectAssignmentMemberModel"]] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    skills: Union[Unset, None, List["ProjectAssignmentSkillBaseModel"]] = UNSET
    project_assignment_member_id: Union[Unset, None, int] = UNSET
    rate: Union[Unset, None, int] = UNSET
    oral_agreement_to_date: Union[Unset, None, datetime.datetime] = UNSET
    option_to_date: Union[Unset, None, datetime.datetime] = UNSET
    contract_type: Union[Unset, ContractType] = UNSET
    is_assigned: Union[Unset, bool] = UNSET
    currency: Union[Unset, None, "CurrencyModel"] = UNSET
    company_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    project: Union[Unset, None, "ProjectBaseModel"] = UNSET
    customer: Union[Unset, None, "CompanyCustomerBaseModel"] = UNSET
    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    extent_type: Union[Unset, ExtentType] = UNSET
    extent: Union[Unset, None, int] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict() if self.company else None

        assigned: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned, Unset):
            assigned = self.assigned.to_dict() if self.assigned else None

        prospects: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prospects, Unset):
            if self.prospects is None:
                prospects = None
            else:
                prospects = []
                for prospects_item_data in self.prospects:
                    prospects_item = prospects_item_data.to_dict()

                    prospects.append(prospects_item)

        seo_id = self.seo_id
        skills: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skills, Unset):
            if self.skills is None:
                skills = None
            else:
                skills = []
                for skills_item_data in self.skills:
                    skills_item = skills_item_data.to_dict()

                    skills.append(skills_item)

        project_assignment_member_id = self.project_assignment_member_id
        rate = self.rate
        oral_agreement_to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.oral_agreement_to_date, Unset):
            oral_agreement_to_date = self.oral_agreement_to_date.isoformat() if self.oral_agreement_to_date else None

        option_to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.option_to_date, Unset):
            option_to_date = self.option_to_date.isoformat() if self.option_to_date else None

        contract_type: Union[Unset, int] = UNSET
        if not isinstance(self.contract_type, Unset):
            contract_type = self.contract_type.value

        is_assigned = self.is_assigned
        currency: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict() if self.currency else None

        company_id = self.company_id
        customer_id = self.customer_id
        project_id = self.project_id
        project: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict() if self.project else None

        customer: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict() if self.customer else None

        id = self.id
        title = self.title
        description = self.description
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        extent_type: Union[Unset, int] = UNSET
        if not isinstance(self.extent_type, Unset):
            extent_type = self.extent_type.value

        extent = self.extent
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
        if company is not UNSET:
            field_dict["company"] = company
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if prospects is not UNSET:
            field_dict["prospects"] = prospects
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if skills is not UNSET:
            field_dict["skills"] = skills
        if project_assignment_member_id is not UNSET:
            field_dict["projectAssignmentMemberId"] = project_assignment_member_id
        if rate is not UNSET:
            field_dict["rate"] = rate
        if oral_agreement_to_date is not UNSET:
            field_dict["oralAgreementToDate"] = oral_agreement_to_date
        if option_to_date is not UNSET:
            field_dict["optionToDate"] = option_to_date
        if contract_type is not UNSET:
            field_dict["contractType"] = contract_type
        if is_assigned is not UNSET:
            field_dict["isAssigned"] = is_assigned
        if currency is not UNSET:
            field_dict["currency"] = currency
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project is not UNSET:
            field_dict["project"] = project
        if customer is not UNSET:
            field_dict["customer"] = customer
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if extent_type is not UNSET:
            field_dict["extentType"] = extent_type
        if extent is not UNSET:
            field_dict["extent"] = extent
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_base_model import CompanyBaseModel
        from ..models.company_customer_base_model import CompanyCustomerBaseModel
        from ..models.currency_model import CurrencyModel
        from ..models.link import Link
        from ..models.project_assignment_member_model import ProjectAssignmentMemberModel
        from ..models.project_assignment_skill_base_model import ProjectAssignmentSkillBaseModel
        from ..models.project_base_model import ProjectBaseModel

        d = src_dict.copy()
        _company = d.pop("company", UNSET)
        company: Union[Unset, None, CompanyBaseModel]
        if _company is None:
            company = None
        elif isinstance(_company, Unset):
            company = UNSET
        else:
            company = CompanyBaseModel.from_dict(_company)

        _assigned = d.pop("assigned", UNSET)
        assigned: Union[Unset, None, ProjectAssignmentMemberModel]
        if _assigned is None:
            assigned = None
        elif isinstance(_assigned, Unset):
            assigned = UNSET
        else:
            assigned = ProjectAssignmentMemberModel.from_dict(_assigned)

        prospects = []
        _prospects = d.pop("prospects", UNSET)
        for prospects_item_data in _prospects or []:
            prospects_item = ProjectAssignmentMemberModel.from_dict(prospects_item_data)

            prospects.append(prospects_item)

        seo_id = d.pop("seoId", UNSET)

        skills = []
        _skills = d.pop("skills", UNSET)
        for skills_item_data in _skills or []:
            skills_item = ProjectAssignmentSkillBaseModel.from_dict(skills_item_data)

            skills.append(skills_item)

        project_assignment_member_id = d.pop("projectAssignmentMemberId", UNSET)

        rate = d.pop("rate", UNSET)

        _oral_agreement_to_date = d.pop("oralAgreementToDate", UNSET)
        oral_agreement_to_date: Union[Unset, None, datetime.datetime]
        if _oral_agreement_to_date is None:
            oral_agreement_to_date = None
        elif isinstance(_oral_agreement_to_date, Unset):
            oral_agreement_to_date = UNSET
        else:
            oral_agreement_to_date = isoparse(_oral_agreement_to_date)

        _option_to_date = d.pop("optionToDate", UNSET)
        option_to_date: Union[Unset, None, datetime.datetime]
        if _option_to_date is None:
            option_to_date = None
        elif isinstance(_option_to_date, Unset):
            option_to_date = UNSET
        else:
            option_to_date = isoparse(_option_to_date)

        _contract_type = d.pop("contractType", UNSET)
        contract_type: Union[Unset, ContractType]
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = ContractType(_contract_type)

        is_assigned = d.pop("isAssigned", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, None, CurrencyModel]
        if _currency is None:
            currency = None
        elif isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = CurrencyModel.from_dict(_currency)

        company_id = d.pop("companyId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        project_id = d.pop("projectId", UNSET)

        _project = d.pop("project", UNSET)
        project: Union[Unset, None, ProjectBaseModel]
        if _project is None:
            project = None
        elif isinstance(_project, Unset):
            project = UNSET
        else:
            project = ProjectBaseModel.from_dict(_project)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, None, CompanyCustomerBaseModel]
        if _customer is None:
            customer = None
        elif isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CompanyCustomerBaseModel.from_dict(_customer)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _extent_type = d.pop("extentType", UNSET)
        extent_type: Union[Unset, ExtentType]
        if isinstance(_extent_type, Unset):
            extent_type = UNSET
        else:
            extent_type = ExtentType(_extent_type)

        extent = d.pop("extent", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        project_assignment_model = cls(
            company=company,
            assigned=assigned,
            prospects=prospects,
            seo_id=seo_id,
            skills=skills,
            project_assignment_member_id=project_assignment_member_id,
            rate=rate,
            oral_agreement_to_date=oral_agreement_to_date,
            option_to_date=option_to_date,
            contract_type=contract_type,
            is_assigned=is_assigned,
            currency=currency,
            company_id=company_id,
            customer_id=customer_id,
            project_id=project_id,
            project=project,
            customer=customer,
            id=id,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            extent_type=extent_type,
            extent=extent,
            links=links,
        )

        return project_assignment_model
