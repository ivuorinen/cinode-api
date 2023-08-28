from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.project_assignment_allocation_status import ProjectAssignmentAllocationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentMemberSubcontractorAddModel")


@_attrs_define
class ProjectAssignmentMemberSubcontractorAddModel:
    """
    Attributes:
        company_user_id (int):
        status (ProjectAssignmentAllocationStatus):

            Ej bokad = 0

            Preliminär = 1

            Tillsatt = 2
        group_id (Union[Unset, None, int]):
        currency_id (Union[Unset, None, int]):
        tariff (Union[Unset, None, float]):
    """

    company_user_id: int
    status: ProjectAssignmentAllocationStatus
    group_id: Union[Unset, None, int] = UNSET
    currency_id: Union[Unset, None, int] = UNSET
    tariff: Union[Unset, None, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        status = self.status.value

        group_id = self.group_id
        currency_id = self.currency_id
        tariff = self.tariff

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "companyUserId": company_user_id,
                "status": status,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if tariff is not UNSET:
            field_dict["tariff"] = tariff

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_user_id = d.pop("companyUserId")

        status = ProjectAssignmentAllocationStatus(d.pop("status"))

        group_id = d.pop("groupId", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        tariff = d.pop("tariff", UNSET)

        project_assignment_member_subcontractor_add_model = cls(
            company_user_id=company_user_id,
            status=status,
            group_id=group_id,
            currency_id=currency_id,
            tariff=tariff,
        )

        return project_assignment_member_subcontractor_add_model
