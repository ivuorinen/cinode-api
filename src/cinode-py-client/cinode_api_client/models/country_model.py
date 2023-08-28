from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CountryModel")


@_attrs_define
class CountryModel:
    """
    Attributes:
        country_id (Union[Unset, int]):
        code (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
    """

    country_id: Union[Unset, int] = UNSET
    code: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        country_id = self.country_id
        code = self.code
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if country_id is not UNSET:
            field_dict["countryId"] = country_id
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        country_id = d.pop("countryId", UNSET)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        country_model = cls(
            country_id=country_id,
            code=code,
            name=name,
        )

        return country_model
