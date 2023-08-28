from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileSkillEditModel")


@_attrs_define
class CompanyUserProfileSkillEditModel:
    """
    Attributes:
        keyword_synonym_id (Union[Unset, None, int]):
        level (Union[Unset, int]):
    """

    keyword_synonym_id: Union[Unset, None, int] = UNSET
    level: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyword_synonym_id = self.keyword_synonym_id
        level = self.level

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        level = d.pop("level", UNSET)

        company_user_profile_skill_edit_model = cls(
            keyword_synonym_id=keyword_synonym_id,
            level=level,
        )

        return company_user_profile_skill_edit_model
