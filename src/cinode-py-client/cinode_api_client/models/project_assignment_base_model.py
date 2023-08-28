import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.extent_type import ExtentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_customer_base_model import CompanyCustomerBaseModel
    from ..models.link import Link
    from ..models.project_base_model import ProjectBaseModel


T = TypeVar("T", bound="ProjectAssignmentBaseModel")


@_attrs_define
class ProjectAssignmentBaseModel:
    """
    Attributes:
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
        from ..models.company_customer_base_model import CompanyCustomerBaseModel
        from ..models.link import Link
        from ..models.project_base_model import ProjectBaseModel

        d = src_dict.copy()
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

        project_assignment_base_model = cls(
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

        return project_assignment_base_model
