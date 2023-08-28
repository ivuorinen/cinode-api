from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_address_model import CompanyAddressModel
    from ..models.company_tag_base_model import CompanyTagBaseModel
    from ..models.currency_model import CurrencyModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyModel")


@_attrs_define
class CompanyModel:
    """
    Attributes:
        corporate_identity_number (Union[Unset, None, str]): External identifier
        vat_number (Union[Unset, None, str]):
        registration_year (Union[Unset, None, int]):
        is_tax_registered (Union[Unset, None, bool]):
        addresses (Union[Unset, None, List['CompanyAddressModel']]):
        tags (Union[Unset, None, List['CompanyTagBaseModel']]):
        country_id (Union[Unset, None, int]):
        default_currency (Union[Unset, None, CurrencyModel]):
        currencies (Union[Unset, None, List['CurrencyModel']]):
        id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        seo_id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    corporate_identity_number: Union[Unset, None, str] = UNSET
    vat_number: Union[Unset, None, str] = UNSET
    registration_year: Union[Unset, None, int] = UNSET
    is_tax_registered: Union[Unset, None, bool] = UNSET
    addresses: Union[Unset, None, List["CompanyAddressModel"]] = UNSET
    tags: Union[Unset, None, List["CompanyTagBaseModel"]] = UNSET
    country_id: Union[Unset, None, int] = UNSET
    default_currency: Union[Unset, None, "CurrencyModel"] = UNSET
    currencies: Union[Unset, None, List["CurrencyModel"]] = UNSET
    id: Union[Unset, None, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        corporate_identity_number = self.corporate_identity_number
        vat_number = self.vat_number
        registration_year = self.registration_year
        is_tax_registered = self.is_tax_registered
        addresses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            if self.addresses is None:
                addresses = None
            else:
                addresses = []
                for addresses_item_data in self.addresses:
                    addresses_item = addresses_item_data.to_dict()

                    addresses.append(addresses_item)

        tags: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = []
                for tags_item_data in self.tags:
                    tags_item = tags_item_data.to_dict()

                    tags.append(tags_item)

        country_id = self.country_id
        default_currency: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.default_currency, Unset):
            default_currency = self.default_currency.to_dict() if self.default_currency else None

        currencies: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.currencies, Unset):
            if self.currencies is None:
                currencies = None
            else:
                currencies = []
                for currencies_item_data in self.currencies:
                    currencies_item = currencies_item_data.to_dict()

                    currencies.append(currencies_item)

        id = self.id
        name = self.name
        seo_id = self.seo_id
        description = self.description
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
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number
        if registration_year is not UNSET:
            field_dict["registrationYear"] = registration_year
        if is_tax_registered is not UNSET:
            field_dict["isTaxRegistered"] = is_tax_registered
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if tags is not UNSET:
            field_dict["tags"] = tags
        if country_id is not UNSET:
            field_dict["countryId"] = country_id
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if currencies is not UNSET:
            field_dict["currencies"] = currencies
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if description is not UNSET:
            field_dict["description"] = description
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_address_model import CompanyAddressModel
        from ..models.company_tag_base_model import CompanyTagBaseModel
        from ..models.currency_model import CurrencyModel
        from ..models.link import Link

        d = src_dict.copy()
        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        vat_number = d.pop("vatNumber", UNSET)

        registration_year = d.pop("registrationYear", UNSET)

        is_tax_registered = d.pop("isTaxRegistered", UNSET)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = CompanyAddressModel.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = CompanyTagBaseModel.from_dict(tags_item_data)

            tags.append(tags_item)

        country_id = d.pop("countryId", UNSET)

        _default_currency = d.pop("defaultCurrency", UNSET)
        default_currency: Union[Unset, None, CurrencyModel]
        if _default_currency is None:
            default_currency = None
        elif isinstance(_default_currency, Unset):
            default_currency = UNSET
        else:
            default_currency = CurrencyModel.from_dict(_default_currency)

        currencies = []
        _currencies = d.pop("currencies", UNSET)
        for currencies_item_data in _currencies or []:
            currencies_item = CurrencyModel.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        seo_id = d.pop("seoId", UNSET)

        description = d.pop("description", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_model = cls(
            corporate_identity_number=corporate_identity_number,
            vat_number=vat_number,
            registration_year=registration_year,
            is_tax_registered=is_tax_registered,
            addresses=addresses,
            tags=tags,
            country_id=country_id,
            default_currency=default_currency,
            currencies=currencies,
            id=id,
            name=name,
            seo_id=seo_id,
            description=description,
            links=links,
        )

        return company_model
