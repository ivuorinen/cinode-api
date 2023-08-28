from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_info_block_view_model import AddressInfoBlockViewModel


T = TypeVar("T", bound="CompanyUserInfoBlockViewModel")


@_attrs_define
class CompanyUserInfoBlockViewModel:
    """
    Attributes:
        address (Union[Unset, None, AddressInfoBlockViewModel]):
        email (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
    """

    address: Union[Unset, None, "AddressInfoBlockViewModel"] = UNSET
    email: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict() if self.address else None

        email = self.email
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if email is not UNSET:
            field_dict["email"] = email
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_info_block_view_model import AddressInfoBlockViewModel

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, None, AddressInfoBlockViewModel]
        if _address is None:
            address = None
        elif isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressInfoBlockViewModel.from_dict(_address)

        email = d.pop("email", UNSET)

        title = d.pop("title", UNSET)

        company_user_info_block_view_model = cls(
            address=address,
            email=email,
            title=title,
        )

        return company_user_info_block_view_model
