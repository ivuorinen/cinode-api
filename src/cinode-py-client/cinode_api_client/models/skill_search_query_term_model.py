from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SkillSearchQueryTermModel")


@_attrs_define
class SkillSearchQueryTermModel:
    """
    Attributes:
        term (str):
        min_ (Union[Unset, None, int]):
        max_ (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):
    """

    term: str
    min_: Union[Unset, None, int] = UNSET
    max_: Union[Unset, None, int] = UNSET
    limit: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        min_ = self.min_
        max_ = self.max_
        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "term": term,
            }
        )
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        term = d.pop("term")

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        limit = d.pop("limit", UNSET)

        skill_search_query_term_model = cls(
            term=term,
            min_=min_,
            max_=max_,
            limit=limit,
        )

        return skill_search_query_term_model
