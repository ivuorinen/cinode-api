from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentSkillEditModel")


@_attrs_define
class ProjectAssignmentSkillEditModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        level (Union[Unset, None, int]):
        is_mandatory (Union[Unset, None, bool]):
    """

    name: Union[Unset, None, str] = UNSET
    level: Union[Unset, None, int] = UNSET
    is_mandatory: Union[Unset, None, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        level = self.level
        is_mandatory = self.is_mandatory

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if level is not UNSET:
            field_dict["level"] = level
        if is_mandatory is not UNSET:
            field_dict["isMandatory"] = is_mandatory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        level = d.pop("level", UNSET)

        is_mandatory = d.pop("isMandatory", UNSET)

        project_assignment_skill_edit_model = cls(
            name=name,
            level=level,
            is_mandatory=is_mandatory,
        )

        return project_assignment_skill_edit_model
