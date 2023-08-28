from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterModel")


@_attrs_define
class FilterModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        values (Union[Unset, None, List[int]]):
    """

    name: Union[Unset, None, str] = UNSET
    values: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        values: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.values, Unset):
            if self.values is None:
                values = None
            else:
                values = self.values

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        values = cast(List[int], d.pop("values", UNSET))

        filter_model = cls(
            name=name,
            values=values,
        )

        return filter_model
