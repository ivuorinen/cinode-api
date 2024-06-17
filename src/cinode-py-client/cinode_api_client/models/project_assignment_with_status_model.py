import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.project_assignment_extent_type import ProjectAssignmentExtentType
from ..models.project_assignment_member_allocation_status import ProjectAssignmentMemberAllocationStatus
from ..models.project_assignment_member_type import ProjectAssignmentMemberType
from ..models.project_state import ProjectState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_assignment_member_model import ProjectAssignmentMemberModel


T = TypeVar("T", bound="ProjectAssignmentWithStatusModel")


@_attrs_define
class ProjectAssignmentWithStatusModel:
    """
    Attributes:
        pipeline_id (Union[Unset, None, int]):
        project_pipeline_stage_title (Union[Unset, None, str]):
        customer_id (Union[Unset, int]):
        project_id (Union[Unset, int]):
        project_state (Union[Unset, ProjectState]):

            Öppen = 0

            Vunnen = 30

            Förlorad = 40

            Avböjd = 50

            Uppskjuten = 60
        probability (Union[Unset, int]):
        project_assignment_id (Union[Unset, int]): Unspecified = 0,
            Coming = 1,
            Ongoing = 2,
            Ended = 3
        project_assignment_allocation_status (Union[Unset, ProjectAssignmentMemberAllocationStatus]):

            None = 0

            Preliminär = 1

            Tillsatt = 2

            Offererad = 3
        project_assignment_member_type (Union[Unset, ProjectAssignmentMemberType]):

            Unspecified = 0

            Medarbetare = 1

            Partnerkonsult = 2

            Underkonsult = 3
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        option_to_date (Union[Unset, None, datetime.datetime]):
        oral_agreement_to_date (Union[Unset, None, datetime.datetime]):
        project_assignment_extent (Union[Unset, int]):
        project_assignment_extent_type (Union[Unset, ProjectAssignmentExtentType]):

            Procent = 0

            Timmar = 1
        rate (Union[Unset, None, int]):
        estimated_close_date (Union[Unset, None, datetime.datetime]):
        estimated_value (Union[Unset, None, int]):
        assigned (Union[Unset, None, ProjectAssignmentMemberModel]):
        prospects (Union[Unset, None, List['ProjectAssignmentMemberModel']]):
        project_commitment_booking_id (Union[Unset, None, str]): A value in this field indicates that the role is part
            of advanced planning and can't be updated through the API
    """

    pipeline_id: Union[Unset, None, int] = UNSET
    project_pipeline_stage_title: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    project_state: Union[Unset, ProjectState] = UNSET
    probability: Union[Unset, int] = UNSET
    project_assignment_id: Union[Unset, int] = UNSET
    project_assignment_allocation_status: Union[Unset, ProjectAssignmentMemberAllocationStatus] = UNSET
    project_assignment_member_type: Union[Unset, ProjectAssignmentMemberType] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    option_to_date: Union[Unset, None, datetime.datetime] = UNSET
    oral_agreement_to_date: Union[Unset, None, datetime.datetime] = UNSET
    project_assignment_extent: Union[Unset, int] = UNSET
    project_assignment_extent_type: Union[Unset, ProjectAssignmentExtentType] = UNSET
    rate: Union[Unset, None, int] = UNSET
    estimated_close_date: Union[Unset, None, datetime.datetime] = UNSET
    estimated_value: Union[Unset, None, int] = UNSET
    assigned: Union[Unset, None, "ProjectAssignmentMemberModel"] = UNSET
    prospects: Union[Unset, None, List["ProjectAssignmentMemberModel"]] = UNSET
    project_commitment_booking_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        pipeline_id = self.pipeline_id
        project_pipeline_stage_title = self.project_pipeline_stage_title
        customer_id = self.customer_id
        project_id = self.project_id
        project_state: Union[Unset, int] = UNSET
        if not isinstance(self.project_state, Unset):
            project_state = self.project_state.value

        probability = self.probability
        project_assignment_id = self.project_assignment_id
        project_assignment_allocation_status: Union[Unset, int] = UNSET
        if not isinstance(self.project_assignment_allocation_status, Unset):
            project_assignment_allocation_status = self.project_assignment_allocation_status.value

        project_assignment_member_type: Union[Unset, int] = UNSET
        if not isinstance(self.project_assignment_member_type, Unset):
            project_assignment_member_type = self.project_assignment_member_type.value

        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        option_to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.option_to_date, Unset):
            option_to_date = self.option_to_date.isoformat() if self.option_to_date else None

        oral_agreement_to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.oral_agreement_to_date, Unset):
            oral_agreement_to_date = self.oral_agreement_to_date.isoformat() if self.oral_agreement_to_date else None

        project_assignment_extent = self.project_assignment_extent
        project_assignment_extent_type: Union[Unset, int] = UNSET
        if not isinstance(self.project_assignment_extent_type, Unset):
            project_assignment_extent_type = self.project_assignment_extent_type.value

        rate = self.rate
        estimated_close_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.estimated_close_date, Unset):
            estimated_close_date = self.estimated_close_date.isoformat() if self.estimated_close_date else None

        estimated_value = self.estimated_value
        assigned: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned, Unset):
            assigned = self.assigned.to_dict() if self.assigned else None

        prospects: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.prospects, Unset):
            if self.prospects is None:
                prospects = None
            else:
                prospects = []
                for prospects_item_data in self.prospects:
                    prospects_item = prospects_item_data.to_dict()

                    prospects.append(prospects_item)

        project_commitment_booking_id = self.project_commitment_booking_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if project_pipeline_stage_title is not UNSET:
            field_dict["projectPipelineStageTitle"] = project_pipeline_stage_title
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_state is not UNSET:
            field_dict["projectState"] = project_state
        if probability is not UNSET:
            field_dict["probability"] = probability
        if project_assignment_id is not UNSET:
            field_dict["projectAssignmentId"] = project_assignment_id
        if project_assignment_allocation_status is not UNSET:
            field_dict["projectAssignmentAllocationStatus"] = project_assignment_allocation_status
        if project_assignment_member_type is not UNSET:
            field_dict["projectAssignmentMemberType"] = project_assignment_member_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if option_to_date is not UNSET:
            field_dict["optionToDate"] = option_to_date
        if oral_agreement_to_date is not UNSET:
            field_dict["oralAgreementToDate"] = oral_agreement_to_date
        if project_assignment_extent is not UNSET:
            field_dict["projectAssignmentExtent"] = project_assignment_extent
        if project_assignment_extent_type is not UNSET:
            field_dict["projectAssignmentExtentType"] = project_assignment_extent_type
        if rate is not UNSET:
            field_dict["rate"] = rate
        if estimated_close_date is not UNSET:
            field_dict["estimatedCloseDate"] = estimated_close_date
        if estimated_value is not UNSET:
            field_dict["estimatedValue"] = estimated_value
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if prospects is not UNSET:
            field_dict["prospects"] = prospects
        if project_commitment_booking_id is not UNSET:
            field_dict["projectCommitmentBookingId"] = project_commitment_booking_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_assignment_member_model import ProjectAssignmentMemberModel

        d = src_dict.copy()
        pipeline_id = d.pop("pipelineId", UNSET)

        project_pipeline_stage_title = d.pop("projectPipelineStageTitle", UNSET)

        customer_id = d.pop("customerId", UNSET)

        project_id = d.pop("projectId", UNSET)

        _project_state = d.pop("projectState", UNSET)
        project_state: Union[Unset, ProjectState]
        if isinstance(_project_state, Unset):
            project_state = UNSET
        else:
            project_state = ProjectState(_project_state)

        probability = d.pop("probability", UNSET)

        project_assignment_id = d.pop("projectAssignmentId", UNSET)

        _project_assignment_allocation_status = d.pop("projectAssignmentAllocationStatus", UNSET)
        project_assignment_allocation_status: Union[Unset, ProjectAssignmentMemberAllocationStatus]
        if isinstance(_project_assignment_allocation_status, Unset):
            project_assignment_allocation_status = UNSET
        else:
            project_assignment_allocation_status = ProjectAssignmentMemberAllocationStatus(
                _project_assignment_allocation_status
            )

        _project_assignment_member_type = d.pop("projectAssignmentMemberType", UNSET)
        project_assignment_member_type: Union[Unset, ProjectAssignmentMemberType]
        if isinstance(_project_assignment_member_type, Unset):
            project_assignment_member_type = UNSET
        else:
            project_assignment_member_type = ProjectAssignmentMemberType(_project_assignment_member_type)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _option_to_date = d.pop("optionToDate", UNSET)
        option_to_date: Union[Unset, None, datetime.datetime]
        if _option_to_date is None:
            option_to_date = None
        elif isinstance(_option_to_date, Unset):
            option_to_date = UNSET
        else:
            option_to_date = isoparse(_option_to_date)

        _oral_agreement_to_date = d.pop("oralAgreementToDate", UNSET)
        oral_agreement_to_date: Union[Unset, None, datetime.datetime]
        if _oral_agreement_to_date is None:
            oral_agreement_to_date = None
        elif isinstance(_oral_agreement_to_date, Unset):
            oral_agreement_to_date = UNSET
        else:
            oral_agreement_to_date = isoparse(_oral_agreement_to_date)

        project_assignment_extent = d.pop("projectAssignmentExtent", UNSET)

        _project_assignment_extent_type = d.pop("projectAssignmentExtentType", UNSET)
        project_assignment_extent_type: Union[Unset, ProjectAssignmentExtentType]
        if isinstance(_project_assignment_extent_type, Unset):
            project_assignment_extent_type = UNSET
        else:
            project_assignment_extent_type = ProjectAssignmentExtentType(_project_assignment_extent_type)

        rate = d.pop("rate", UNSET)

        _estimated_close_date = d.pop("estimatedCloseDate", UNSET)
        estimated_close_date: Union[Unset, None, datetime.datetime]
        if _estimated_close_date is None:
            estimated_close_date = None
        elif isinstance(_estimated_close_date, Unset):
            estimated_close_date = UNSET
        else:
            estimated_close_date = isoparse(_estimated_close_date)

        estimated_value = d.pop("estimatedValue", UNSET)

        _assigned = d.pop("assigned", UNSET)
        assigned: Union[Unset, None, ProjectAssignmentMemberModel]
        if _assigned is None:
            assigned = None
        elif isinstance(_assigned, Unset):
            assigned = UNSET
        else:
            assigned = ProjectAssignmentMemberModel.from_dict(_assigned)

        prospects = []
        _prospects = d.pop("prospects", UNSET)
        for prospects_item_data in _prospects or []:
            prospects_item = ProjectAssignmentMemberModel.from_dict(prospects_item_data)

            prospects.append(prospects_item)

        project_commitment_booking_id = d.pop("projectCommitmentBookingId", UNSET)

        project_assignment_with_status_model = cls(
            pipeline_id=pipeline_id,
            project_pipeline_stage_title=project_pipeline_stage_title,
            customer_id=customer_id,
            project_id=project_id,
            project_state=project_state,
            probability=probability,
            project_assignment_id=project_assignment_id,
            project_assignment_allocation_status=project_assignment_allocation_status,
            project_assignment_member_type=project_assignment_member_type,
            start_date=start_date,
            end_date=end_date,
            option_to_date=option_to_date,
            oral_agreement_to_date=oral_agreement_to_date,
            project_assignment_extent=project_assignment_extent,
            project_assignment_extent_type=project_assignment_extent_type,
            rate=rate,
            estimated_close_date=estimated_close_date,
            estimated_value=estimated_value,
            assigned=assigned,
            prospects=prospects,
            project_commitment_booking_id=project_commitment_booking_id,
        )

        return project_assignment_with_status_model
