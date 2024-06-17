from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.company_user_type import CompanyUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_customer_base_model import CompanyCustomerBaseModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyCustomerManagerModel")


@_attrs_define
class CompanyCustomerManagerModel:
    """An employee who is a manager (responsible) for a customer

    Attributes:
        company_customer_manager_id (Union[Unset, None, int]):
        customer_id (Union[Unset, None, int]):
        customer (Union[Unset, None, CompanyCustomerBaseModel]):
        id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        company_id (Union[Unset, None, int]):
        seo_id (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        company_user_type (Union[Unset, None, CompanyUserType]):

            Medarbetare = 0

            Kandidat = 10

            Underkonsult = 20

            Api = 30

            Bot = 40
        links (Union[Unset, None, List['Link']]):
    """

    company_customer_manager_id: Union[Unset, None, int] = UNSET
    customer_id: Union[Unset, None, int] = UNSET
    customer: Union[Unset, None, "CompanyCustomerBaseModel"] = UNSET
    id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    company_user_type: Union[Unset, None, CompanyUserType] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_customer_manager_id = self.company_customer_manager_id
        customer_id = self.customer_id
        customer: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict() if self.customer else None

        id = self.id
        company_user_id = self.company_user_id
        company_id = self.company_id
        seo_id = self.seo_id
        first_name = self.first_name
        last_name = self.last_name
        company_user_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.company_user_type, Unset):
            company_user_type = self.company_user_type.value if self.company_user_type else None

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
        if company_customer_manager_id is not UNSET:
            field_dict["companyCustomerManagerId"] = company_customer_manager_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer is not UNSET:
            field_dict["customer"] = customer
        if id is not UNSET:
            field_dict["id"] = id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company_user_type is not UNSET:
            field_dict["companyUserType"] = company_user_type
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_customer_base_model import CompanyCustomerBaseModel
        from ..models.link import Link

        d = src_dict.copy()
        company_customer_manager_id = d.pop("companyCustomerManagerId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, None, CompanyCustomerBaseModel]
        if _customer is None:
            customer = None
        elif isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CompanyCustomerBaseModel.from_dict(_customer)

        id = d.pop("id", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        company_id = d.pop("companyId", UNSET)

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

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_customer_manager_model = cls(
            company_customer_manager_id=company_customer_manager_id,
            customer_id=customer_id,
            customer=customer,
            id=id,
            company_user_id=company_user_id,
            company_id=company_id,
            seo_id=seo_id,
            first_name=first_name,
            last_name=last_name,
            company_user_type=company_user_type,
            links=links,
        )

        return company_customer_manager_model
