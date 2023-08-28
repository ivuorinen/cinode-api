from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        href (Union[Unset, None, str]):
        rel (Union[Unset, None, str]):
        methods (Union[Unset, None, List[str]]):
    """

    href: Union[Unset, None, str] = UNSET
    rel: Union[Unset, None, str] = UNSET
    methods: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        href = self.href
        rel = self.rel
        methods: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.methods, Unset):
            if self.methods is None:
                methods = None
            else:
                methods = self.methods

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if rel is not UNSET:
            field_dict["rel"] = rel
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href", UNSET)

        rel = d.pop("rel", UNSET)

        methods = cast(List[str], d.pop("methods", UNSET))

        link = cls(
            href=href,
            rel=rel,
            methods=methods,
        )

        return link
