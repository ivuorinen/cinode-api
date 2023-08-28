from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.partner_connection_trust_type import PartnerConnectionTrustType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_base_model import CompanyBaseModel


T = TypeVar("T", bound="PartnerConnectionBaseModel")


@_attrs_define
class PartnerConnectionBaseModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        company (Union[Unset, None, CompanyBaseModel]):
        partner_id (Union[Unset, int]):
        connected_partner_connection_id (Union[Unset, None, int]):
        partner_company_id (Union[Unset, int]):
        partner_company (Union[Unset, None, CompanyBaseModel]):
        granted_trusts (Union[Unset, None, List[PartnerConnectionTrustType]]):
        received_trusts (Union[Unset, None, List[PartnerConnectionTrustType]]):
    """

    company_id: Union[Unset, int] = UNSET
    company: Union[Unset, None, "CompanyBaseModel"] = UNSET
    partner_id: Union[Unset, int] = UNSET
    connected_partner_connection_id: Union[Unset, None, int] = UNSET
    partner_company_id: Union[Unset, int] = UNSET
    partner_company: Union[Unset, None, "CompanyBaseModel"] = UNSET
    granted_trusts: Union[Unset, None, List[PartnerConnectionTrustType]] = UNSET
    received_trusts: Union[Unset, None, List[PartnerConnectionTrustType]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        company: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict() if self.company else None

        partner_id = self.partner_id
        connected_partner_connection_id = self.connected_partner_connection_id
        partner_company_id = self.partner_company_id
        partner_company: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.partner_company, Unset):
            partner_company = self.partner_company.to_dict() if self.partner_company else None

        granted_trusts: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.granted_trusts, Unset):
            if self.granted_trusts is None:
                granted_trusts = None
            else:
                granted_trusts = []
                for granted_trusts_item_data in self.granted_trusts:
                    granted_trusts_item = granted_trusts_item_data.value

                    granted_trusts.append(granted_trusts_item)

        received_trusts: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.received_trusts, Unset):
            if self.received_trusts is None:
                received_trusts = None
            else:
                received_trusts = []
                for received_trusts_item_data in self.received_trusts:
                    received_trusts_item = received_trusts_item_data.value

                    received_trusts.append(received_trusts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company is not UNSET:
            field_dict["company"] = company
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if connected_partner_connection_id is not UNSET:
            field_dict["connectedPartnerConnectionId"] = connected_partner_connection_id
        if partner_company_id is not UNSET:
            field_dict["partnerCompanyId"] = partner_company_id
        if partner_company is not UNSET:
            field_dict["partnerCompany"] = partner_company
        if granted_trusts is not UNSET:
            field_dict["grantedTrusts"] = granted_trusts
        if received_trusts is not UNSET:
            field_dict["receivedTrusts"] = received_trusts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_base_model import CompanyBaseModel

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        _company = d.pop("company", UNSET)
        company: Union[Unset, None, CompanyBaseModel]
        if _company is None:
            company = None
        elif isinstance(_company, Unset):
            company = UNSET
        else:
            company = CompanyBaseModel.from_dict(_company)

        partner_id = d.pop("partnerId", UNSET)

        connected_partner_connection_id = d.pop("connectedPartnerConnectionId", UNSET)

        partner_company_id = d.pop("partnerCompanyId", UNSET)

        _partner_company = d.pop("partnerCompany", UNSET)
        partner_company: Union[Unset, None, CompanyBaseModel]
        if _partner_company is None:
            partner_company = None
        elif isinstance(_partner_company, Unset):
            partner_company = UNSET
        else:
            partner_company = CompanyBaseModel.from_dict(_partner_company)

        granted_trusts = []
        _granted_trusts = d.pop("grantedTrusts", UNSET)
        for granted_trusts_item_data in _granted_trusts or []:
            granted_trusts_item = PartnerConnectionTrustType(granted_trusts_item_data)

            granted_trusts.append(granted_trusts_item)

        received_trusts = []
        _received_trusts = d.pop("receivedTrusts", UNSET)
        for received_trusts_item_data in _received_trusts or []:
            received_trusts_item = PartnerConnectionTrustType(received_trusts_item_data)

            received_trusts.append(received_trusts_item)

        partner_connection_base_model = cls(
            company_id=company_id,
            company=company,
            partner_id=partner_id,
            connected_partner_connection_id=connected_partner_connection_id,
            partner_company_id=partner_company_id,
            partner_company=partner_company,
            granted_trusts=granted_trusts,
            received_trusts=received_trusts,
        )

        return partner_connection_base_model
