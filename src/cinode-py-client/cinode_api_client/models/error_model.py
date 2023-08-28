from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorModel")


@_attrs_define
class ErrorModel:
    """
    Attributes:
        correlation_id (Union[Unset, None, str]): CorrelationId
        status (Union[Unset, None, str]): Severity of error
        description (Union[Unset, None, str]): Error description in plain text
        code (Union[Unset, None, int]): Cinode specific error code
        more_info (Union[Unset, None, str]): Url to help page containing more information
    """

    correlation_id: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    code: Union[Unset, None, int] = UNSET
    more_info: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        correlation_id = self.correlation_id
        status = self.status
        description = self.description
        code = self.code
        more_info = self.more_info

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if code is not UNSET:
            field_dict["code"] = code
        if more_info is not UNSET:
            field_dict["moreInfo"] = more_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        correlation_id = d.pop("correlationId", UNSET)

        status = d.pop("status", UNSET)

        description = d.pop("description", UNSET)

        code = d.pop("code", UNSET)

        more_info = d.pop("moreInfo", UNSET)

        error_model = cls(
            correlation_id=correlation_id,
            status=status,
            description=description,
            code=code,
            more_info=more_info,
        )

        return error_model
