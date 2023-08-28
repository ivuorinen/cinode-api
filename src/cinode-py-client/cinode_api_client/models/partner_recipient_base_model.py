from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerRecipientBaseModel")


@_attrs_define
class PartnerRecipientBaseModel:
    """
    Attributes:
        partner_id (Union[Unset, int]):
        requested_company_user_anonymous_hash (Union[Unset, None, str]):
        requested_company_user_id (Union[Unset, None, int]):
    """

    partner_id: Union[Unset, int] = UNSET
    requested_company_user_anonymous_hash: Union[Unset, None, str] = UNSET
    requested_company_user_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        partner_id = self.partner_id
        requested_company_user_anonymous_hash = self.requested_company_user_anonymous_hash
        requested_company_user_id = self.requested_company_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if requested_company_user_anonymous_hash is not UNSET:
            field_dict["requestedCompanyUserAnonymousHash"] = requested_company_user_anonymous_hash
        if requested_company_user_id is not UNSET:
            field_dict["requestedCompanyUserId"] = requested_company_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        partner_id = d.pop("partnerId", UNSET)

        requested_company_user_anonymous_hash = d.pop("requestedCompanyUserAnonymousHash", UNSET)

        requested_company_user_id = d.pop("requestedCompanyUserId", UNSET)

        partner_recipient_base_model = cls(
            partner_id=partner_id,
            requested_company_user_anonymous_hash=requested_company_user_anonymous_hash,
            requested_company_user_id=requested_company_user_id,
        )

        return partner_recipient_base_model
