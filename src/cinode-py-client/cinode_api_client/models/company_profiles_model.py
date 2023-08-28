from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_base_model import CompanyUserProfileBaseModel


T = TypeVar("T", bound="CompanyProfilesModel")


@_attrs_define
class CompanyProfilesModel:
    """
    Attributes:
        total_items (Union[Unset, int]):
        profiles (Union[Unset, None, List['CompanyUserProfileBaseModel']]):
    """

    total_items: Union[Unset, int] = UNSET
    profiles: Union[Unset, None, List["CompanyUserProfileBaseModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        total_items = self.total_items
        profiles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.profiles, Unset):
            if self.profiles is None:
                profiles = None
            else:
                profiles = []
                for profiles_item_data in self.profiles:
                    profiles_item = profiles_item_data.to_dict()

                    profiles.append(profiles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if profiles is not UNSET:
            field_dict["profiles"] = profiles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_base_model import CompanyUserProfileBaseModel

        d = src_dict.copy()
        total_items = d.pop("totalItems", UNSET)

        profiles = []
        _profiles = d.pop("profiles", UNSET)
        for profiles_item_data in _profiles or []:
            profiles_item = CompanyUserProfileBaseModel.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        company_profiles_model = cls(
            total_items=total_items,
            profiles=profiles,
        )

        return company_profiles_model
