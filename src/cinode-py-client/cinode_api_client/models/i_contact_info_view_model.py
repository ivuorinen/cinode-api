from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_company_address_view_model import ICompanyAddressViewModel


T = TypeVar("T", bound="IContactInfoViewModel")


@_attrs_define
class IContactInfoViewModel:
    """
    Attributes:
        contact_info_id (Union[Unset, int]):
        display_name (Union[Unset, None, str]):
        url (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        address (Union[Unset, None, ICompanyAddressViewModel]):
    """

    contact_info_id: Union[Unset, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    address: Union[Unset, None, "ICompanyAddressViewModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        contact_info_id = self.contact_info_id
        display_name = self.display_name
        url = self.url
        email = self.email
        phone = self.phone
        address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict() if self.address else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if contact_info_id is not UNSET:
            field_dict["contactInfoId"] = contact_info_id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if url is not UNSET:
            field_dict["url"] = url
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.i_company_address_view_model import ICompanyAddressViewModel

        d = src_dict.copy()
        contact_info_id = d.pop("contactInfoId", UNSET)

        display_name = d.pop("displayName", UNSET)

        url = d.pop("url", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, None, ICompanyAddressViewModel]
        if _address is None:
            address = None
        elif isinstance(_address, Unset):
            address = UNSET
        else:
            address = ICompanyAddressViewModel.from_dict(_address)

        i_contact_info_view_model = cls(
            contact_info_id=contact_info_id,
            display_name=display_name,
            url=url,
            email=email,
            phone=phone,
            address=address,
        )

        return i_contact_info_view_model
