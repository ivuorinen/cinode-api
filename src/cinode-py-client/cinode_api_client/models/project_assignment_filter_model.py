from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.project_assignment_allocation_status import ProjectAssignmentAllocationStatus
from ..models.project_assignment_member_type import ProjectAssignmentMemberType
from ..models.project_assignment_status import ProjectAssignmentStatus
from ..models.project_state import ProjectState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentFilterModel")


@_attrs_define
class ProjectAssignmentFilterModel:
    """
    Attributes:
        pipelines (Union[Unset, None, List[int]]): Pipeline Ids can be retrieved from the Project Pipelines endpoint
        project_assignment_member_types (Union[Unset, None, List[ProjectAssignmentMemberType]]): 0 - Employee
            1 - Partner consultant
            2- Subcontractor
        project_assignment_statuses (Union[Unset, None, List[ProjectAssignmentStatus]]): 1 - Upcoming
            2 - Ongoing
        teams (Union[Unset, None, List[int]]): Team Id of Employee assigned to Role
        project_states (Union[Unset, None, List[ProjectState]]): 0 - Open
            30 - Won
            40 - Lost
            50 - Abandoned
            60 - Suspended
        project_assignment_allocation_statuses (Union[Unset, None, List[ProjectAssignmentAllocationStatus]]):
    """

    pipelines: Union[Unset, None, List[int]] = UNSET
    project_assignment_member_types: Union[Unset, None, List[ProjectAssignmentMemberType]] = UNSET
    project_assignment_statuses: Union[Unset, None, List[ProjectAssignmentStatus]] = UNSET
    teams: Union[Unset, None, List[int]] = UNSET
    project_states: Union[Unset, None, List[ProjectState]] = UNSET
    project_assignment_allocation_statuses: Union[Unset, None, List[ProjectAssignmentAllocationStatus]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        pipelines: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.pipelines, Unset):
            if self.pipelines is None:
                pipelines = None
            else:
                pipelines = self.pipelines

        project_assignment_member_types: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.project_assignment_member_types, Unset):
            if self.project_assignment_member_types is None:
                project_assignment_member_types = None
            else:
                project_assignment_member_types = []
                for project_assignment_member_types_item_data in self.project_assignment_member_types:
                    project_assignment_member_types_item = project_assignment_member_types_item_data.value

                    project_assignment_member_types.append(project_assignment_member_types_item)

        project_assignment_statuses: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.project_assignment_statuses, Unset):
            if self.project_assignment_statuses is None:
                project_assignment_statuses = None
            else:
                project_assignment_statuses = []
                for project_assignment_statuses_item_data in self.project_assignment_statuses:
                    project_assignment_statuses_item = project_assignment_statuses_item_data.value

                    project_assignment_statuses.append(project_assignment_statuses_item)

        teams: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.teams, Unset):
            if self.teams is None:
                teams = None
            else:
                teams = self.teams

        project_states: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.project_states, Unset):
            if self.project_states is None:
                project_states = None
            else:
                project_states = []
                for project_states_item_data in self.project_states:
                    project_states_item = project_states_item_data.value

                    project_states.append(project_states_item)

        project_assignment_allocation_statuses: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.project_assignment_allocation_statuses, Unset):
            if self.project_assignment_allocation_statuses is None:
                project_assignment_allocation_statuses = None
            else:
                project_assignment_allocation_statuses = []
                for project_assignment_allocation_statuses_item_data in self.project_assignment_allocation_statuses:
                    project_assignment_allocation_statuses_item = project_assignment_allocation_statuses_item_data.value

                    project_assignment_allocation_statuses.append(project_assignment_allocation_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines
        if project_assignment_member_types is not UNSET:
            field_dict["projectAssignmentMemberTypes"] = project_assignment_member_types
        if project_assignment_statuses is not UNSET:
            field_dict["projectAssignmentStatuses"] = project_assignment_statuses
        if teams is not UNSET:
            field_dict["teams"] = teams
        if project_states is not UNSET:
            field_dict["projectStates"] = project_states
        if project_assignment_allocation_statuses is not UNSET:
            field_dict["projectAssignmentAllocationStatuses"] = project_assignment_allocation_statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pipelines = cast(List[int], d.pop("pipelines", UNSET))

        project_assignment_member_types = []
        _project_assignment_member_types = d.pop("projectAssignmentMemberTypes", UNSET)
        for project_assignment_member_types_item_data in _project_assignment_member_types or []:
            project_assignment_member_types_item = ProjectAssignmentMemberType(
                project_assignment_member_types_item_data
            )

            project_assignment_member_types.append(project_assignment_member_types_item)

        project_assignment_statuses = []
        _project_assignment_statuses = d.pop("projectAssignmentStatuses", UNSET)
        for project_assignment_statuses_item_data in _project_assignment_statuses or []:
            project_assignment_statuses_item = ProjectAssignmentStatus(project_assignment_statuses_item_data)

            project_assignment_statuses.append(project_assignment_statuses_item)

        teams = cast(List[int], d.pop("teams", UNSET))

        project_states = []
        _project_states = d.pop("projectStates", UNSET)
        for project_states_item_data in _project_states or []:
            project_states_item = ProjectState(project_states_item_data)

            project_states.append(project_states_item)

        project_assignment_allocation_statuses = []
        _project_assignment_allocation_statuses = d.pop("projectAssignmentAllocationStatuses", UNSET)
        for project_assignment_allocation_statuses_item_data in _project_assignment_allocation_statuses or []:
            project_assignment_allocation_statuses_item = ProjectAssignmentAllocationStatus(
                project_assignment_allocation_statuses_item_data
            )

            project_assignment_allocation_statuses.append(project_assignment_allocation_statuses_item)

        project_assignment_filter_model = cls(
            pipelines=pipelines,
            project_assignment_member_types=project_assignment_member_types,
            project_assignment_statuses=project_assignment_statuses,
            teams=teams,
            project_states=project_states,
            project_assignment_allocation_statuses=project_assignment_allocation_statuses,
        )

        return project_assignment_filter_model
