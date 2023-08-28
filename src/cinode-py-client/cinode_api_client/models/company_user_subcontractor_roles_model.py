from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_subcontractor_role_member_model import CompanyUserSubcontractorRoleMemberModel


T = TypeVar("T", bound="CompanyUserSubcontractorRolesModel")


@_attrs_define
class CompanyUserSubcontractorRolesModel:
    """
    Attributes:
        assigned (Union[Unset, None, List['CompanyUserSubcontractorRoleMemberModel']]):
        prospect (Union[Unset, None, List['CompanyUserSubcontractorRoleMemberModel']]):
    """

    assigned: Union[Unset, None, List["CompanyUserSubcontractorRoleMemberModel"]] = UNSET
    prospect: Union[Unset, None, List["CompanyUserSubcontractorRoleMemberModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        assigned: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assigned, Unset):
            if self.assigned is None:
                assigned = None
            else:
                assigned = []
                for assigned_item_data in self.assigned:
                    assigned_item = assigned_item_data.to_dict()

                    assigned.append(assigned_item)

        prospect: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prospect, Unset):
            if self.prospect is None:
                prospect = None
            else:
                prospect = []
                for prospect_item_data in self.prospect:
                    prospect_item = prospect_item_data.to_dict()

                    prospect.append(prospect_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if prospect is not UNSET:
            field_dict["prospect"] = prospect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_subcontractor_role_member_model import CompanyUserSubcontractorRoleMemberModel

        d = src_dict.copy()
        assigned = []
        _assigned = d.pop("assigned", UNSET)
        for assigned_item_data in _assigned or []:
            assigned_item = CompanyUserSubcontractorRoleMemberModel.from_dict(assigned_item_data)

            assigned.append(assigned_item)

        prospect = []
        _prospect = d.pop("prospect", UNSET)
        for prospect_item_data in _prospect or []:
            prospect_item = CompanyUserSubcontractorRoleMemberModel.from_dict(prospect_item_data)

            prospect.append(prospect_item)

        company_user_subcontractor_roles_model = cls(
            assigned=assigned,
            prospect=prospect,
        )

        return company_user_subcontractor_roles_model
