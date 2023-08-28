from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressInfoBlockViewModel")


@_attrs_define
class AddressInfoBlockViewModel:
    """
    Attributes:
        display_name (Union[Unset, None, str]):
        street1 (Union[Unset, None, str]):
        street2 (Union[Unset, None, str]):
        zip_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
    """

    display_name: Union[Unset, None, str] = UNSET
    street1: Union[Unset, None, str] = UNSET
    street2: Union[Unset, None, str] = UNSET
    zip_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        street1 = self.street1
        street2 = self.street2
        zip_code = self.zip_code
        city = self.city
        country = self.country
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        email = d.pop("email", UNSET)

        address_info_block_view_model = cls(
            display_name=display_name,
            street1=street1,
            street2=street2,
            zip_code=zip_code,
            city=city,
            country=country,
            email=email,
        )

        return address_info_block_view_model
