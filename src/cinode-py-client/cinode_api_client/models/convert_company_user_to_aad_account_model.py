from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ConvertCompanyUserToAadAccountModel")


@_attrs_define
class ConvertCompanyUserToAadAccountModel:
    """
    Attributes:
        object_identifier (str):
    """

    object_identifier: str

    def to_dict(self) -> Dict[str, Any]:
        object_identifier = self.object_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "objectIdentifier": object_identifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_identifier = d.pop("objectIdentifier")

        convert_company_user_to_aad_account_model = cls(
            object_identifier=object_identifier,
        )

        return convert_company_user_to_aad_account_model
