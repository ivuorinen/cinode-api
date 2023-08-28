from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.access_level import AccessLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserPermissionsEditModel")


@_attrs_define
class CompanyUserPermissionsEditModel:
    """
    Attributes:
        permissions (Union[Unset, None, List[AccessLevel]]):
    """

    permissions: Union[Unset, None, List[AccessLevel]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        permissions: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.permissions, Unset):
            if self.permissions is None:
                permissions = None
            else:
                permissions = []
                for permissions_item_data in self.permissions:
                    permissions_item = permissions_item_data.value

                    permissions.append(permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = AccessLevel(permissions_item_data)

            permissions.append(permissions_item)

        company_user_permissions_edit_model = cls(
            permissions=permissions,
        )

        return company_user_permissions_edit_model
