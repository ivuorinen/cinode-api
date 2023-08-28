from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileAddEditModel")


@_attrs_define
class CompanyUserProfileAddEditModel:
    """
    Attributes:
        language_id (Union[Unset, None, int]):
    """

    language_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language_id = self.language_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if language_id is not UNSET:
            field_dict["languageId"] = language_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_id = d.pop("languageId", UNSET)

        company_user_profile_add_edit_model = cls(
            language_id=language_id,
        )

        return company_user_profile_add_edit_model
