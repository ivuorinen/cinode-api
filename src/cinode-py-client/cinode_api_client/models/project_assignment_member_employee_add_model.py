from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.project_assignment_allocation_status import ProjectAssignmentAllocationStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentMemberEmployeeAddModel")


@_attrs_define
class ProjectAssignmentMemberEmployeeAddModel:
    """
    Attributes:
        company_user_id (int):
        status (ProjectAssignmentAllocationStatus):

            Ej bokad = 0

            Preliminär = 1

            Tillsatt = 2
        team_id (Union[Unset, None, int]):
    """

    company_user_id: int
    status: ProjectAssignmentAllocationStatus
    team_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_id = self.company_user_id
        status = self.status.value

        team_id = self.team_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "companyUserId": company_user_id,
                "status": status,
            }
        )
        if team_id is not UNSET:
            field_dict["teamId"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_user_id = d.pop("companyUserId")

        status = ProjectAssignmentAllocationStatus(d.pop("status"))

        team_id = d.pop("teamId", UNSET)

        project_assignment_member_employee_add_model = cls(
            company_user_id=company_user_id,
            status=status,
            team_id=team_id,
        )

        return project_assignment_member_employee_add_model
