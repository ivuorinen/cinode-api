from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnersFilterModel")


@_attrs_define
class PartnersFilterModel:
    """
    Attributes:
        query (Union[Unset, None, str]):
        only_include_connected_partners (Union[Unset, bool]):
    """

    query: Union[Unset, None, str] = UNSET
    only_include_connected_partners: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        query = self.query
        only_include_connected_partners = self.only_include_connected_partners

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if only_include_connected_partners is not UNSET:
            field_dict["onlyIncludeConnectedPartners"] = only_include_connected_partners

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        query = d.pop("query", UNSET)

        only_include_connected_partners = d.pop("onlyIncludeConnectedPartners", UNSET)

        partners_filter_model = cls(
            query=query,
            only_include_connected_partners=only_include_connected_partners,
        )

        return partners_filter_model
