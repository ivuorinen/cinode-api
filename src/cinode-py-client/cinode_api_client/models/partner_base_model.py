from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.partner_connection_base_model import PartnerConnectionBaseModel


T = TypeVar("T", bound="PartnerBaseModel")


@_attrs_define
class PartnerBaseModel:
    """
    Attributes:
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        partner_connection (Union[Unset, None, PartnerConnectionBaseModel]):
        company_user_manager (Union[Unset, None, CompanyUserBaseModel]):
        has_trusts (Union[Unset, bool]):
        is_enabled (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    partner_connection: Union[Unset, None, "PartnerConnectionBaseModel"] = UNSET
    company_user_manager: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    has_trusts: Union[Unset, bool] = UNSET
    is_enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_id = self.company_id
        name = self.name
        description = self.description
        partner_connection: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.partner_connection, Unset):
            partner_connection = self.partner_connection.to_dict() if self.partner_connection else None

        company_user_manager: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company_user_manager, Unset):
            company_user_manager = self.company_user_manager.to_dict() if self.company_user_manager else None

        has_trusts = self.has_trusts
        is_enabled = self.is_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if partner_connection is not UNSET:
            field_dict["partnerConnection"] = partner_connection
        if company_user_manager is not UNSET:
            field_dict["companyUserManager"] = company_user_manager
        if has_trusts is not UNSET:
            field_dict["hasTrusts"] = has_trusts
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.partner_connection_base_model import PartnerConnectionBaseModel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _partner_connection = d.pop("partnerConnection", UNSET)
        partner_connection: Union[Unset, None, PartnerConnectionBaseModel]
        if _partner_connection is None:
            partner_connection = None
        elif isinstance(_partner_connection, Unset):
            partner_connection = UNSET
        else:
            partner_connection = PartnerConnectionBaseModel.from_dict(_partner_connection)

        _company_user_manager = d.pop("companyUserManager", UNSET)
        company_user_manager: Union[Unset, None, CompanyUserBaseModel]
        if _company_user_manager is None:
            company_user_manager = None
        elif isinstance(_company_user_manager, Unset):
            company_user_manager = UNSET
        else:
            company_user_manager = CompanyUserBaseModel.from_dict(_company_user_manager)

        has_trusts = d.pop("hasTrusts", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        partner_base_model = cls(
            id=id,
            company_id=company_id,
            name=name,
            description=description,
            partner_connection=partner_connection,
            company_user_manager=company_user_manager,
            has_trusts=has_trusts,
            is_enabled=is_enabled,
        )

        return partner_base_model
