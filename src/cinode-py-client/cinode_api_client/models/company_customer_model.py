from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.company_size import CompanySize
from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_customer_address_model import CompanyCustomerAddressModel
    from ..models.company_customer_attachment_model import CompanyCustomerAttachmentModel
    from ..models.company_customer_contact_base_model import CompanyCustomerContactBaseModel
    from ..models.company_customer_manager_model import CompanyCustomerManagerModel
    from ..models.company_tag_base_model import CompanyTagBaseModel
    from ..models.country_model import CountryModel
    from ..models.currency_model import CurrencyModel
    from ..models.link import Link
    from ..models.project_base_model import ProjectBaseModel


T = TypeVar("T", bound="CompanyCustomerModel")


@_attrs_define
class CompanyCustomerModel:
    """
    Attributes:
        phone (Union[Unset, None, str]):
        fax (Union[Unset, None, str]):
        homepage (Union[Unset, None, str]):
        corporate_identity_number (Union[Unset, None, str]):
        vat_number (Union[Unset, None, str]):
        contacts (Union[Unset, None, List['CompanyCustomerContactBaseModel']]):
        addresses (Union[Unset, None, List['CompanyCustomerAddressModel']]):
        projects (Union[Unset, None, List['ProjectBaseModel']]):
        intermediator (Union[Unset, None, bool]):
        attachments (Union[Unset, None, List['CompanyCustomerAttachmentModel']]):
        size (Union[Unset, None, CompanySize]):

            Egenföretagare = 0

            2-10 = 1

            11-50 = 2

            51-200 = 3

            201-500 = 4

            501-1 000 = 5

            1 001-5 000 = 6

            5 001-10 000 = 7

            10 001+ = 8
        country_id (Union[Unset, None, int]):
        country (Union[Unset, None, CountryModel]):
        turn_over (Union[Unset, None, int]):
        turn_over_currency_id (Union[Unset, None, int]):
        turn_over_currency (Union[Unset, None, CurrencyModel]):
        email (Union[Unset, None, str]):
        tags (Union[Unset, None, List['CompanyTagBaseModel']]):
        managers (Union[Unset, None, List['CompanyCustomerManagerModel']]):
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        identification (Union[Unset, None, str]):
        seo_id (Union[Unset, None, str]):
        status (Union[Unset, Status]):

            Inaktiv = 0

            Aktiv = 1
        links (Union[Unset, None, List['Link']]):
    """

    phone: Union[Unset, None, str] = UNSET
    fax: Union[Unset, None, str] = UNSET
    homepage: Union[Unset, None, str] = UNSET
    corporate_identity_number: Union[Unset, None, str] = UNSET
    vat_number: Union[Unset, None, str] = UNSET
    contacts: Union[Unset, None, List["CompanyCustomerContactBaseModel"]] = UNSET
    addresses: Union[Unset, None, List["CompanyCustomerAddressModel"]] = UNSET
    projects: Union[Unset, None, List["ProjectBaseModel"]] = UNSET
    intermediator: Union[Unset, None, bool] = UNSET
    attachments: Union[Unset, None, List["CompanyCustomerAttachmentModel"]] = UNSET
    size: Union[Unset, None, CompanySize] = UNSET
    country_id: Union[Unset, None, int] = UNSET
    country: Union[Unset, None, "CountryModel"] = UNSET
    turn_over: Union[Unset, None, int] = UNSET
    turn_over_currency_id: Union[Unset, None, int] = UNSET
    turn_over_currency: Union[Unset, None, "CurrencyModel"] = UNSET
    email: Union[Unset, None, str] = UNSET
    tags: Union[Unset, None, List["CompanyTagBaseModel"]] = UNSET
    managers: Union[Unset, None, List["CompanyCustomerManagerModel"]] = UNSET
    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    identification: Union[Unset, None, str] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    status: Union[Unset, Status] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        phone = self.phone
        fax = self.fax
        homepage = self.homepage
        corporate_identity_number = self.corporate_identity_number
        vat_number = self.vat_number
        contacts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            if self.contacts is None:
                contacts = None
            else:
                contacts = []
                for contacts_item_data in self.contacts:
                    contacts_item = contacts_item_data.to_dict()

                    contacts.append(contacts_item)

        addresses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            if self.addresses is None:
                addresses = None
            else:
                addresses = []
                for addresses_item_data in self.addresses:
                    addresses_item = addresses_item_data.to_dict()

                    addresses.append(addresses_item)

        projects: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            if self.projects is None:
                projects = None
            else:
                projects = []
                for projects_item_data in self.projects:
                    projects_item = projects_item_data.to_dict()

                    projects.append(projects_item)

        intermediator = self.intermediator
        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        size: Union[Unset, None, int] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value if self.size else None

        country_id = self.country_id
        country: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict() if self.country else None

        turn_over = self.turn_over
        turn_over_currency_id = self.turn_over_currency_id
        turn_over_currency: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.turn_over_currency, Unset):
            turn_over_currency = self.turn_over_currency.to_dict() if self.turn_over_currency else None

        email = self.email
        tags: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = []
                for tags_item_data in self.tags:
                    tags_item = tags_item_data.to_dict()

                    tags.append(tags_item)

        managers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.managers, Unset):
            if self.managers is None:
                managers = None
            else:
                managers = []
                for managers_item_data in self.managers:
                    managers_item = managers_item_data.to_dict()

                    managers.append(managers_item)

        id = self.id
        company_id = self.company_id
        name = self.name
        description = self.description
        identification = self.identification
        seo_id = self.seo_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        if phone is not UNSET:
            field_dict["phone"] = phone
        if fax is not UNSET:
            field_dict["fax"] = fax
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if projects is not UNSET:
            field_dict["projects"] = projects
        if intermediator is not UNSET:
            field_dict["intermediator"] = intermediator
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if size is not UNSET:
            field_dict["size"] = size
        if country_id is not UNSET:
            field_dict["countryId"] = country_id
        if country is not UNSET:
            field_dict["country"] = country
        if turn_over is not UNSET:
            field_dict["turnOver"] = turn_over
        if turn_over_currency_id is not UNSET:
            field_dict["turnOverCurrencyId"] = turn_over_currency_id
        if turn_over_currency is not UNSET:
            field_dict["turnOverCurrency"] = turn_over_currency
        if email is not UNSET:
            field_dict["email"] = email
        if tags is not UNSET:
            field_dict["tags"] = tags
        if managers is not UNSET:
            field_dict["managers"] = managers
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if identification is not UNSET:
            field_dict["identification"] = identification
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if status is not UNSET:
            field_dict["status"] = status
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_customer_address_model import CompanyCustomerAddressModel
        from ..models.company_customer_attachment_model import CompanyCustomerAttachmentModel
        from ..models.company_customer_contact_base_model import CompanyCustomerContactBaseModel
        from ..models.company_customer_manager_model import CompanyCustomerManagerModel
        from ..models.company_tag_base_model import CompanyTagBaseModel
        from ..models.country_model import CountryModel
        from ..models.currency_model import CurrencyModel
        from ..models.link import Link
        from ..models.project_base_model import ProjectBaseModel

        d = src_dict.copy()
        phone = d.pop("phone", UNSET)

        fax = d.pop("fax", UNSET)

        homepage = d.pop("homepage", UNSET)

        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        vat_number = d.pop("vatNumber", UNSET)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = CompanyCustomerContactBaseModel.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CompanyCustomerAddressModel.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = ProjectBaseModel.from_dict(projects_item_data)

            projects.append(projects_item)

        intermediator = d.pop("intermediator", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = CompanyCustomerAttachmentModel.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        _size = d.pop("size", UNSET)
        size: Union[Unset, None, CompanySize]
        if _size is None:
            size = None
        elif isinstance(_size, Unset):
            size = UNSET
        else:
            size = CompanySize(_size)

        country_id = d.pop("countryId", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, None, CountryModel]
        if _country is None:
            country = None
        elif isinstance(_country, Unset):
            country = UNSET
        else:
            country = CountryModel.from_dict(_country)

        turn_over = d.pop("turnOver", UNSET)

        turn_over_currency_id = d.pop("turnOverCurrencyId", UNSET)

        _turn_over_currency = d.pop("turnOverCurrency", UNSET)
        turn_over_currency: Union[Unset, None, CurrencyModel]
        if _turn_over_currency is None:
            turn_over_currency = None
        elif isinstance(_turn_over_currency, Unset):
            turn_over_currency = UNSET
        else:
            turn_over_currency = CurrencyModel.from_dict(_turn_over_currency)

        email = d.pop("email", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = CompanyTagBaseModel.from_dict(tags_item_data)

            tags.append(tags_item)

        managers = []
        _managers = d.pop("managers", UNSET)
        for managers_item_data in _managers or []:
            managers_item = CompanyCustomerManagerModel.from_dict(managers_item_data)

            managers.append(managers_item)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        identification = d.pop("identification", UNSET)

        seo_id = d.pop("seoId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status(_status)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_customer_model = cls(
            phone=phone,
            fax=fax,
            homepage=homepage,
            corporate_identity_number=corporate_identity_number,
            vat_number=vat_number,
            contacts=contacts,
            addresses=addresses,
            projects=projects,
            intermediator=intermediator,
            attachments=attachments,
            size=size,
            country_id=country_id,
            country=country,
            turn_over=turn_over,
            turn_over_currency_id=turn_over_currency_id,
            turn_over_currency=turn_over_currency,
            email=email,
            tags=tags,
            managers=managers,
            id=id,
            company_id=company_id,
            name=name,
            description=description,
            identification=identification,
            seo_id=seo_id,
            status=status,
            links=links,
        )

        return company_customer_model
