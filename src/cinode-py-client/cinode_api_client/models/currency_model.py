from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyModel")


@_attrs_define
class CurrencyModel:
    """
    Attributes:
        id (Union[Unset, int]):
        currency_code (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    currency_code: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        currency_code = self.currency_code
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        description = d.pop("description", UNSET)

        currency_model = cls(
            id=id,
            currency_code=currency_code,
            description=description,
        )

        return currency_model
