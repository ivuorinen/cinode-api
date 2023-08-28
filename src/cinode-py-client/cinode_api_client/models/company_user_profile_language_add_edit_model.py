from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.language_level import LanguageLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileLanguageAddEditModel")


@_attrs_define
class CompanyUserProfileLanguageAddEditModel:
    """
    Attributes:
        language_id (int):
        level (Union[Unset, LanguageLevel]):

            Enstaka ord och fraser = 0

            Grundläggande kunskaper = 1

            Goda kunskaper = 2

            Flytande = 3

            Modersmål = 4
    """

    language_id: int
    level: Union[Unset, LanguageLevel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language_id = self.language_id
        level: Union[Unset, int] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "languageId": language_id,
            }
        )
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_id = d.pop("languageId")

        _level = d.pop("level", UNSET)
        level: Union[Unset, LanguageLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = LanguageLevel(_level)

        company_user_profile_language_add_edit_model = cls(
            language_id=language_id,
            level=level,
        )

        return company_user_profile_language_add_edit_model
