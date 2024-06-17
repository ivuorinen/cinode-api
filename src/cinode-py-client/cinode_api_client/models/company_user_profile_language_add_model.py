from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.language_level import LanguageLevel
from ..models.save_to_api_option import SaveToApiOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileLanguageAddModel")


@_attrs_define
class CompanyUserProfileLanguageAddModel:
    """
    Attributes:
        language_id (int):
        save_to (Union[Unset, SaveToApiOption]):

            AllResumesOfLanguage = 3

            Profile = 5
        level (Union[Unset, LanguageLevel]):

            Enstaka ord och fraser = 0

            Grundläggande kunskaper = 1

            Goda kunskaper = 2

            Flytande = 3

            Modersmål = 4
    """

    language_id: int
    save_to: Union[Unset, SaveToApiOption] = UNSET
    level: Union[Unset, LanguageLevel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language_id = self.language_id
        save_to: Union[Unset, int] = UNSET
        if not isinstance(self.save_to, Unset):
            save_to = self.save_to.value

        level: Union[Unset, int] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "languageId": language_id,
            }
        )
        if save_to is not UNSET:
            field_dict["saveTo"] = save_to
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_id = d.pop("languageId")

        _save_to = d.pop("saveTo", UNSET)
        save_to: Union[Unset, SaveToApiOption]
        if isinstance(_save_to, Unset):
            save_to = UNSET
        else:
            save_to = SaveToApiOption(_save_to)

        _level = d.pop("level", UNSET)
        level: Union[Unset, LanguageLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = LanguageLevel(_level)

        company_user_profile_language_add_model = cls(
            language_id=language_id,
            save_to=save_to,
            level=level,
        )

        return company_user_profile_language_add_model
