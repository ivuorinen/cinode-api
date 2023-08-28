from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_enabled_module_model import CompanyEnabledModuleModel


T = TypeVar("T", bound="CompanyCapabilitiesModel")


@_attrs_define
class CompanyCapabilitiesModel:
    """
    Attributes:
        enabled_modules (Union[Unset, None, List['CompanyEnabledModuleModel']]):
    """

    enabled_modules: Union[Unset, None, List["CompanyEnabledModuleModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        enabled_modules: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enabled_modules, Unset):
            if self.enabled_modules is None:
                enabled_modules = None
            else:
                enabled_modules = []
                for enabled_modules_item_data in self.enabled_modules:
                    enabled_modules_item = enabled_modules_item_data.to_dict()

                    enabled_modules.append(enabled_modules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if enabled_modules is not UNSET:
            field_dict["enabledModules"] = enabled_modules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_enabled_module_model import CompanyEnabledModuleModel

        d = src_dict.copy()
        enabled_modules = []
        _enabled_modules = d.pop("enabledModules", UNSET)
        for enabled_modules_item_data in _enabled_modules or []:
            enabled_modules_item = CompanyEnabledModuleModel.from_dict(enabled_modules_item_data)

            enabled_modules.append(enabled_modules_item)

        company_capabilities_model = cls(
            enabled_modules=enabled_modules,
        )

        return company_capabilities_model
