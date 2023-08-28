from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentSkillAddModel")


@_attrs_define
class ProjectAssignmentSkillAddModel:
    """
    Attributes:
        name (str):
        keyword_synonym_id (Union[Unset, None, int]):
        level (Union[Unset, None, int]):
        is_mandatory (Union[Unset, None, bool]):
    """

    name: str
    keyword_synonym_id: Union[Unset, None, int] = UNSET
    level: Union[Unset, None, int] = UNSET
    is_mandatory: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        keyword_synonym_id = self.keyword_synonym_id
        level = self.level
        is_mandatory = self.is_mandatory

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if level is not UNSET:
            field_dict["level"] = level
        if is_mandatory is not UNSET:
            field_dict["isMandatory"] = is_mandatory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        level = d.pop("level", UNSET)

        is_mandatory = d.pop("isMandatory", UNSET)

        project_assignment_skill_add_model = cls(
            name=name,
            keyword_synonym_id=keyword_synonym_id,
            level=level,
            is_mandatory=is_mandatory,
        )

        return project_assignment_skill_add_model
