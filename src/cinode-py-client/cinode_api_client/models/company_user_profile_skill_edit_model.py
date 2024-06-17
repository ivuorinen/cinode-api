from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.save_to_api_option import SaveToApiOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileSkillEditModel")


@_attrs_define
class CompanyUserProfileSkillEditModel:
    """
    Attributes:
        keyword_synonym_id (Union[Unset, None, int]):
        level (Union[Unset, int]):
        save_to (Union[Unset, SaveToApiOption]):

            AllResumesOfLanguage = 3

            Profile = 5
    """

    keyword_synonym_id: Union[Unset, None, int] = UNSET
    level: Union[Unset, int] = UNSET
    save_to: Union[Unset, SaveToApiOption] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyword_synonym_id = self.keyword_synonym_id
        level = self.level
        save_to: Union[Unset, int] = UNSET
        if not isinstance(self.save_to, Unset):
            save_to = self.save_to.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if level is not UNSET:
            field_dict["level"] = level
        if save_to is not UNSET:
            field_dict["saveTo"] = save_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        level = d.pop("level", UNSET)

        _save_to = d.pop("saveTo", UNSET)
        save_to: Union[Unset, SaveToApiOption]
        if isinstance(_save_to, Unset):
            save_to = UNSET
        else:
            save_to = SaveToApiOption(_save_to)

        company_user_profile_skill_edit_model = cls(
            keyword_synonym_id=keyword_synonym_id,
            level=level,
            save_to=save_to,
        )

        return company_user_profile_skill_edit_model
