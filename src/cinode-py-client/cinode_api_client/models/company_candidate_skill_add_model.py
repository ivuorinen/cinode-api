from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCandidateSkillAddModel")


@_attrs_define
class CompanyCandidateSkillAddModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        company_candidate_id (Union[Unset, int]):
        keyword_synonym_id (Union[Unset, None, int]):
        language_id (Union[Unset, None, int]):
    """

    name: Union[Unset, None, str] = UNSET
    company_candidate_id: Union[Unset, int] = UNSET
    keyword_synonym_id: Union[Unset, None, int] = UNSET
    language_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        company_candidate_id = self.company_candidate_id
        keyword_synonym_id = self.keyword_synonym_id
        language_id = self.language_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if company_candidate_id is not UNSET:
            field_dict["companyCandidateId"] = company_candidate_id
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if language_id is not UNSET:
            field_dict["languageId"] = language_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        company_candidate_id = d.pop("companyCandidateId", UNSET)

        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        language_id = d.pop("languageId", UNSET)

        company_candidate_skill_add_model = cls(
            name=name,
            company_candidate_id=company_candidate_id,
            keyword_synonym_id=keyword_synonym_id,
            language_id=language_id,
        )

        return company_candidate_skill_add_model
