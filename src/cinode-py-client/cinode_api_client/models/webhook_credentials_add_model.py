from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookCredentialsAddModel")


@_attrs_define
class WebhookCredentialsAddModel:
    """
    Attributes:
        header_value (Union[Unset, None, str]):
        is_basic_authentication (Union[Unset, None, bool]):
        header_name (Union[Unset, None, str]):
    """

    header_value: Union[Unset, None, str] = UNSET
    is_basic_authentication: Union[Unset, None, bool] = UNSET
    header_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        header_value = self.header_value
        is_basic_authentication = self.is_basic_authentication
        header_name = self.header_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if header_value is not UNSET:
            field_dict["headerValue"] = header_value
        if is_basic_authentication is not UNSET:
            field_dict["isBasicAuthentication"] = is_basic_authentication
        if header_name is not UNSET:
            field_dict["headerName"] = header_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        header_value = d.pop("headerValue", UNSET)

        is_basic_authentication = d.pop("isBasicAuthentication", UNSET)

        header_name = d.pop("headerName", UNSET)

        webhook_credentials_add_model = cls(
            header_value=header_value,
            is_basic_authentication=is_basic_authentication,
            header_name=header_name,
        )

        return webhook_credentials_add_model
