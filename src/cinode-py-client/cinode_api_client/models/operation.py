from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_value import OperationValue


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """
    Attributes:
        op (Union[Unset, str]):
        value (Union[Unset, None, OperationValue]):
        path (Union[Unset, str]):
    """

    op: Union[Unset, str] = UNSET
    value: Union[Unset, None, "OperationValue"] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        op = self.op
        value: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict() if self.value else None

        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if op is not UNSET:
            field_dict["op"] = op
        if value is not UNSET:
            field_dict["value"] = value
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.operation_value import OperationValue

        d = src_dict.copy()
        op = d.pop("op", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, None, OperationValue]
        if _value is None:
            value = None
        elif isinstance(_value, Unset):
            value = UNSET
        else:
            value = OperationValue.from_dict(_value)

        path = d.pop("path", UNSET)

        operation = cls(
            op=op,
            value=value,
            path=path,
        )

        operation.additional_properties = d
        return operation

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
