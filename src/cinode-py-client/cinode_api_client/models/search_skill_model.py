from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSkillModel")


@_attrs_define
class SearchSkillModel:
    """
    Attributes:
        keyword_id (Union[Unset, None, int]):
        min_ (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
    """

    keyword_id: Union[Unset, None, int] = UNSET
    min_: Union[Unset, None, int] = UNSET
    max_: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyword_id = self.keyword_id
        min_ = self.min_
        max_ = self.max_

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keyword_id = d.pop("keywordId", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        search_skill_model = cls(
            keyword_id=keyword_id,
            min_=min_,
            max_=max_,
        )

        return search_skill_model
