from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectStateReasonModel")


@_attrs_define
class ProjectStateReasonModel:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        project_state_reason_model = cls(
            id=id,
            title=title,
            description=description,
        )

        return project_state_reason_model
