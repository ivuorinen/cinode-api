from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCandidateAddInviteModel")


@_attrs_define
class CompanyCandidateAddInviteModel:
    """
    Attributes:
        email (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
    """

    email: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        message = d.pop("message", UNSET)

        company_candidate_add_invite_model = cls(
            email=email,
            message=message,
        )

        return company_candidate_add_invite_model
