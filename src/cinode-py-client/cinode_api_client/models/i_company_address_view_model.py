from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.address_type import AddressType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ICompanyAddressViewModel")


@_attrs_define
class ICompanyAddressViewModel:
    """
    Attributes:
        address_id (Union[Unset, int]):
        street1 (Union[Unset, None, str]):
        street2 (Union[Unset, None, str]):
        zip_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        address_type (Union[Unset, AddressType]):

            Övrig = 0

            Besöksadress = 1

            Faktureringsadress = 2

            Placeringsort = 3
    """

    address_id: Union[Unset, int] = UNSET
    street1: Union[Unset, None, str] = UNSET
    street2: Union[Unset, None, str] = UNSET
    zip_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    address_type: Union[Unset, AddressType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        address_id = self.address_id
        street1 = self.street1
        street2 = self.street2
        zip_code = self.zip_code
        city = self.city
        country = self.country
        address_type: Union[Unset, int] = UNSET
        if not isinstance(self.address_type, Unset):
            address_type = self.address_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if address_id is not UNSET:
            field_dict["addressId"] = address_id
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
        if address_type is not UNSET:
            field_dict["addressType"] = address_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address_id = d.pop("addressId", UNSET)

        street1 = d.pop("street1", UNSET)

        street2 = d.pop("street2", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        _address_type = d.pop("addressType", UNSET)
        address_type: Union[Unset, AddressType]
        if isinstance(_address_type, Unset):
            address_type = UNSET
        else:
            address_type = AddressType(_address_type)

        i_company_address_view_model = cls(
            address_id=address_id,
            street1=street1,
            street2=street2,
            zip_code=zip_code,
            city=city,
            country=country,
            address_type=address_type,
        )

        return i_company_address_view_model
