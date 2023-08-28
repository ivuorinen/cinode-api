from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyUserProfileWorkExperienceSkillAddModel")


@_attrs_define
class CompanyUserProfileWorkExperienceSkillAddModel:
    """
    Attributes:
        keyword_synonym_id (int):
        name (str):
    """

    keyword_synonym_id: int
    name: str

    def to_dict(self) -> Dict[str, Any]:
        keyword_synonym_id = self.keyword_synonym_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "keywordSynonymId": keyword_synonym_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyword_synonym_id = d.pop("keywordSynonymId")

        name = d.pop("name")

        company_user_profile_work_experience_skill_add_model = cls(
            keyword_synonym_id=keyword_synonym_id,
            name=name,
        )

        return company_user_profile_work_experience_skill_add_model
