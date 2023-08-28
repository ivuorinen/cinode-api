from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.address_type import AddressType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCustomerAddressAddEditModel")


@_attrs_define
class CompanyCustomerAddressAddEditModel:
    """
    Attributes:
        street1 (Union[Unset, None, str]):
        street2 (Union[Unset, None, str]):
        zip_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        comments (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        address_type (Union[Unset, AddressType]):

            Övrig = 0

            Besöksadress = 1

            Faktureringsadress = 2

            Placeringsort = 3
    """

    street1: Union[Unset, None, str] = UNSET
    street2: Union[Unset, None, str] = UNSET
    zip_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    comments: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    address_type: Union[Unset, AddressType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        street1 = self.street1
        street2 = self.street2
        zip_code = self.zip_code
        city = self.city
        email = self.email
        comments = self.comments
        country = self.country
        address_type: Union[Unset, int] = UNSET
        if not isinstance(self.address_type, Unset):
            address_type = self.address_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if street2 is not UNSET:
            field_dict["street2"] = street2
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if city is not UNSET:
            field_dict["city"] = city
        if email is not UNSET:
            field_dict["email"] = email
        if comments is not UNSET:
            field_dict["comments"] = comments
        if country is not UNSET:
            field_dict["country"] = country
        if address_type is not UNSET:
            field_dict["addressType"] = address_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        city = d.pop("city", UNSET)

        email = d.pop("email", UNSET)

        comments = d.pop("comments", UNSET)

        country = d.pop("country", UNSET)

        _address_type = d.pop("addressType", UNSET)
        address_type: Union[Unset, AddressType]
        if isinstance(_address_type, Unset):
            address_type = UNSET
        else:
            address_type = AddressType(_address_type)

        company_customer_address_add_edit_model = cls(
            street1=street1,
            street2=street2,
            zip_code=zip_code,
            city=city,
            email=email,
            comments=comments,
            country=country,
            address_type=address_type,
        )

        return company_customer_address_add_edit_model
