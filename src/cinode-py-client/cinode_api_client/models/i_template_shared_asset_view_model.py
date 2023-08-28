from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ITemplateSharedAssetViewModel")


@_attrs_define
class ITemplateSharedAssetViewModel:
    """
    Attributes:
        description (Union[Unset, None, str]):
        order (Union[Unset, int]):
        file_name (Union[Unset, None, str]):
        version (Union[Unset, None, str]):
    """

    description: Union[Unset, None, str] = UNSET
    order: Union[Unset, int] = UNSET
    file_name: Union[Unset, None, str] = UNSET
    version: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        order = self.order
        file_name = self.file_name
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if order is not UNSET:
            field_dict["order"] = order
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        order = d.pop("order", UNSET)

        file_name = d.pop("fileName", UNSET)

        version = d.pop("version", UNSET)

        i_template_shared_asset_view_model = cls(
            description=description,
            order=order,
            file_name=file_name,
            version=version,
        )

        return i_template_shared_asset_view_model
