import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.project_priority import ProjectPriority
from ..models.project_state import ProjectState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_model import LocationModel


T = TypeVar("T", bound="ProjectAddEditModel")


@_attrs_define
class ProjectAddEditModel:
    """
    Attributes:
        title (str):
        customer_id (int):
        description (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        customer_identifier (Union[Unset, None, str]):
        intermediator_id (Union[Unset, None, int]):
        estimated_close_date (Union[Unset, None, datetime.datetime]):
        estimated_value (Union[Unset, None, int]):
        contract_value (Union[Unset, None, int]):
        probability (Union[Unset, None, int]):
        pipeline_id (Union[Unset, None, int]):
        pipeline_stage_id (Union[Unset, None, int]):
        currency_id (Union[Unset, None, int]):
        project_state (Union[Unset, ProjectState]):

            Öppen = 0

            Vunnen = 30

            Förlorad = 40

            Avböjd = 50

            Uppskjuten = 60
        location (Union[Unset, None, LocationModel]):
        team_id (Union[Unset, None, int]):
        state_reason_id (Union[Unset, None, int]):
        priority (Union[Unset, ProjectPriority]):

            Låg = 3

            Medel = 5

            Hög = 8 Default: ProjectPriority.VALUE_5.
        sales_manager_ids (Union[Unset, None, List[int]]): List of sales managers employee ids
        project_manager_ids (Union[Unset, None, List[int]]): List of project managers employee ids
    """

    title: str
    customer_id: int
    description: Union[Unset, None, str] = UNSET
    identifier: Union[Unset, None, str] = UNSET
    customer_identifier: Union[Unset, None, str] = UNSET
    intermediator_id: Union[Unset, None, int] = UNSET
    estimated_close_date: Union[Unset, None, datetime.datetime] = UNSET
    estimated_value: Union[Unset, None, int] = UNSET
    contract_value: Union[Unset, None, int] = UNSET
    probability: Union[Unset, None, int] = UNSET
    pipeline_id: Union[Unset, None, int] = UNSET
    pipeline_stage_id: Union[Unset, None, int] = UNSET
    currency_id: Union[Unset, None, int] = UNSET
    project_state: Union[Unset, ProjectState] = UNSET
    location: Union[Unset, None, "LocationModel"] = UNSET
    team_id: Union[Unset, None, int] = UNSET
    state_reason_id: Union[Unset, None, int] = UNSET
    priority: Union[Unset, ProjectPriority] = ProjectPriority.VALUE_5
    sales_manager_ids: Union[Unset, None, List[int]] = UNSET
    project_manager_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        customer_id = self.customer_id
        description = self.description
        identifier = self.identifier
        customer_identifier = self.customer_identifier
        intermediator_id = self.intermediator_id
        estimated_close_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.estimated_close_date, Unset):
            estimated_close_date = self.estimated_close_date.isoformat() if self.estimated_close_date else None

        estimated_value = self.estimated_value
        contract_value = self.contract_value
        probability = self.probability
        pipeline_id = self.pipeline_id
        pipeline_stage_id = self.pipeline_stage_id
        currency_id = self.currency_id
        project_state: Union[Unset, int] = UNSET
        if not isinstance(self.project_state, Unset):
            project_state = self.project_state.value

        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        team_id = self.team_id
        state_reason_id = self.state_reason_id
        priority: Union[Unset, int] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        sales_manager_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.sales_manager_ids, Unset):
            if self.sales_manager_ids is None:
                sales_manager_ids = None
            else:
                sales_manager_ids = self.sales_manager_ids

        project_manager_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.project_manager_ids, Unset):
            if self.project_manager_ids is None:
                project_manager_ids = None
            else:
                project_manager_ids = self.project_manager_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
                "customerId": customer_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if customer_identifier is not UNSET:
            field_dict["customerIdentifier"] = customer_identifier
        if intermediator_id is not UNSET:
            field_dict["intermediatorId"] = intermediator_id
        if estimated_close_date is not UNSET:
            field_dict["estimatedCloseDate"] = estimated_close_date
        if estimated_value is not UNSET:
            field_dict["estimatedValue"] = estimated_value
        if contract_value is not UNSET:
            field_dict["contractValue"] = contract_value
        if probability is not UNSET:
            field_dict["probability"] = probability
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if project_state is not UNSET:
            field_dict["projectState"] = project_state
        if location is not UNSET:
            field_dict["location"] = location
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if state_reason_id is not UNSET:
            field_dict["stateReasonId"] = state_reason_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if sales_manager_ids is not UNSET:
            field_dict["salesManagerIds"] = sales_manager_ids
        if project_manager_ids is not UNSET:
            field_dict["projectManagerIds"] = project_manager_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_model import LocationModel

        d = src_dict.copy()
        title = d.pop("title")

        customer_id = d.pop("customerId")

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        customer_identifier = d.pop("customerIdentifier", UNSET)

        intermediator_id = d.pop("intermediatorId", UNSET)

        _estimated_close_date = d.pop("estimatedCloseDate", UNSET)
        estimated_close_date: Union[Unset, None, datetime.datetime]
        if _estimated_close_date is None:
            estimated_close_date = None
        elif isinstance(_estimated_close_date, Unset):
            estimated_close_date = UNSET
        else:
            estimated_close_date = isoparse(_estimated_close_date)

        estimated_value = d.pop("estimatedValue", UNSET)

        contract_value = d.pop("contractValue", UNSET)

        probability = d.pop("probability", UNSET)

        pipeline_id = d.pop("pipelineId", UNSET)

        pipeline_stage_id = d.pop("pipelineStageId", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        _project_state = d.pop("projectState", UNSET)
        project_state: Union[Unset, ProjectState]
        if isinstance(_project_state, Unset):
            project_state = UNSET
        else:
            project_state = ProjectState(_project_state)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, LocationModel]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationModel.from_dict(_location)

        team_id = d.pop("teamId", UNSET)

        state_reason_id = d.pop("stateReasonId", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, ProjectPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ProjectPriority(_priority)

        sales_manager_ids = cast(List[int], d.pop("salesManagerIds", UNSET))

        project_manager_ids = cast(List[int], d.pop("projectManagerIds", UNSET))

        project_add_edit_model = cls(
            title=title,
            customer_id=customer_id,
            description=description,
            identifier=identifier,
            customer_identifier=customer_identifier,
            intermediator_id=intermediator_id,
            estimated_close_date=estimated_close_date,
            estimated_value=estimated_value,
            contract_value=contract_value,
            probability=probability,
            pipeline_id=pipeline_id,
            pipeline_stage_id=pipeline_stage_id,
            currency_id=currency_id,
            project_state=project_state,
            location=location,
            team_id=team_id,
            state_reason_id=state_reason_id,
            priority=priority,
            sales_manager_ids=sales_manager_ids,
            project_manager_ids=project_manager_ids,
        )

        return project_add_edit_model
