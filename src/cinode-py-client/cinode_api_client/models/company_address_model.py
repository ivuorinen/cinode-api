from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.address_type import AddressType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CompanyAddressModel")


@_attrs_define
class CompanyAddressModel:
    """
    Attributes:
        company_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        street1 (Union[Unset, None, str]):
        street2 (Union[Unset, None, str]):
        zip_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        address_type (Union[Unset, AddressType]):

            Övrig = 0

            Besöksadress = 1

            Faktureringsadress = 2

            Placeringsort = 3
        comments (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    company_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    street1: Union[Unset, None, str] = UNSET
    street2: Union[Unset, None, str] = UNSET
    zip_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    address_type: Union[Unset, AddressType] = UNSET
    comments: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        id = self.id
        street1 = self.street1
        street2 = self.street2
        zip_code = self.zip_code
        city = self.city
        country = self.country
        email = self.email
        address_type: Union[Unset, int] = UNSET
        if not isinstance(self.address_type, Unset):
            address_type = self.address_type.value

        comments = self.comments
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
        if id is not UNSET:
            field_dict["id"] = id
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if email is not UNSET:
            field_dict["email"] = email
        if address_type is not UNSET:
            field_dict["addressType"] = address_type
        if comments is not UNSET:
            field_dict["comments"] = comments
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        id = d.pop("id", UNSET)

        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        email = d.pop("email", UNSET)

        _address_type = d.pop("addressType", UNSET)
        address_type: Union[Unset, AddressType]
        if isinstance(_address_type, Unset):
            address_type = UNSET
        else:
            address_type = AddressType(_address_type)

        comments = d.pop("comments", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_address_model = cls(
            company_id=company_id,
            id=id,
            street1=street1,
            street2=street2,
            zip_code=zip_code,
            city=city,
            country=country,
            email=email,
            address_type=address_type,
            comments=comments,
            links=links,
        )

        return company_address_model
