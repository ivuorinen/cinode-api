from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SkillResultModel")


@_attrs_define
class SkillResultModel:
    """
    Attributes:
        keyword_id (Union[Unset, None, int]):
        keyword_synonym_id (Union[Unset, None, int]):
        keyword_synonym_name (Union[Unset, None, str]):
        master_synonym_id (Union[Unset, None, int]):
        master_synonym_name (Union[Unset, None, str]):
        level (Union[Unset, None, int]):
    """

    keyword_id: Union[Unset, None, int] = UNSET
    keyword_synonym_id: Union[Unset, None, int] = UNSET
    keyword_synonym_name: Union[Unset, None, str] = UNSET
    master_synonym_id: Union[Unset, None, int] = UNSET
    master_synonym_name: Union[Unset, None, str] = UNSET
    level: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyword_id = self.keyword_id
        keyword_synonym_id = self.keyword_synonym_id
        keyword_synonym_name = self.keyword_synonym_name
        master_synonym_id = self.master_synonym_id
        master_synonym_name = self.master_synonym_name
        level = self.level

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if keyword_synonym_name is not UNSET:
            field_dict["keywordSynonymName"] = keyword_synonym_name
        if master_synonym_id is not UNSET:
            field_dict["masterSynonymId"] = master_synonym_id
        if master_synonym_name is not UNSET:
            field_dict["masterSynonymName"] = master_synonym_name
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyword_id = d.pop("keywordId", UNSET)

        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        keyword_synonym_name = d.pop("keywordSynonymName", UNSET)

        master_synonym_id = d.pop("masterSynonymId", UNSET)

        master_synonym_name = d.pop("masterSynonymName", UNSET)

        level = d.pop("level", UNSET)

        skill_result_model = cls(
            keyword_id=keyword_id,
            keyword_synonym_id=keyword_synonym_id,
            keyword_synonym_name=keyword_synonym_name,
            master_synonym_id=master_synonym_id,
            master_synonym_name=master_synonym_name,
            level=level,
        )

        return skill_result_model
