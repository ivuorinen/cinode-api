from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MentionTextModel")


@_attrs_define
class MentionTextModel:
    """
    Attributes:
        value (Union[Unset, None, str]):
    """

    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        mention_text_model = cls(
            value=value,
        )

        return mention_text_model
