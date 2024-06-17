from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.project_assignment_allocation_status import ProjectAssignmentAllocationStatus
from ..models.project_assignment_member_state import ProjectAssignmentMemberState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentMemberEmployeeEditModel")


@_attrs_define
class ProjectAssignmentMemberEmployeeEditModel:
    """
    Attributes:
        id (int):
        state (ProjectAssignmentMemberState):

            Tillagd = 0

            Offererad = 10

            Intervju bokad = 12

            Intervju utförd = 13

            Avböjd av kund = 20

            Avböjd av oss = 30

            Pausad = 40
        company_user_id (int):
        status (ProjectAssignmentAllocationStatus):

            Ej bokad = 0

            Preliminär = 1

            Tillsatt = 2
        team_id (Union[Unset, None, int]):
    """

    id: int
    state: ProjectAssignmentMemberState
    company_user_id: int
    status: ProjectAssignmentAllocationStatus
    team_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        state = self.state.value

        company_user_id = self.company_user_id
        status = self.status.value

        team_id = self.team_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "state": state,
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
        id = d.pop("id")

        state = ProjectAssignmentMemberState(d.pop("state"))

        company_user_id = d.pop("companyUserId")

        status = ProjectAssignmentAllocationStatus(d.pop("status"))

        team_id = d.pop("teamId", UNSET)

        project_assignment_member_employee_edit_model = cls(
            id=id,
            state=state,
            company_user_id=company_user_id,
            status=status,
            team_id=team_id,
        )

        return project_assignment_member_employee_edit_model
