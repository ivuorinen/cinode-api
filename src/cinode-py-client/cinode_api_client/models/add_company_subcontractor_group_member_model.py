from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddCompanySubcontractorGroupMemberModel")


@_attrs_define
class AddCompanySubcontractorGroupMemberModel:
    """
    Attributes:
        company_user_subcontractor_id (int):
    """

    company_user_subcontractor_id: int

    def to_dict(self) -> Dict[str, Any]:
        company_user_subcontractor_id = self.company_user_subcontractor_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "companyUserSubcontractorId": company_user_subcontractor_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_user_subcontractor_id = d.pop("companyUserSubcontractorId")

        add_company_subcontractor_group_member_model = cls(
            company_user_subcontractor_id=company_user_subcontractor_id,
        )

        return add_company_subcontractor_group_member_model
