import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.project_priority import ProjectPriority
from ..models.project_state import ProjectState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_base_model import CompanyBaseModel
    from ..models.company_customer_base_model import CompanyCustomerBaseModel
    from ..models.company_customer_contact_base_model import CompanyCustomerContactBaseModel
    from ..models.company_tag_base_model import CompanyTagBaseModel
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.currency_model import CurrencyModel
    from ..models.link import Link
    from ..models.project_assignment_base_model import ProjectAssignmentBaseModel
    from ..models.project_attachment_model import ProjectAttachmentModel
    from ..models.project_event_base_model import ProjectEventBaseModel
    from ..models.project_reference_model import ProjectReferenceModel
    from ..models.project_state_history_model import ProjectStateHistoryModel


T = TypeVar("T", bound="ProjectModel")


@_attrs_define
class ProjectModel:
    """
    Attributes:
        company (Union[Unset, None, CompanyBaseModel]):
        customer (Union[Unset, None, CompanyCustomerBaseModel]):
        seo_id (Union[Unset, None, str]):
        location_id (Union[Unset, None, int]):
        google_id (Union[Unset, None, str]):
        probability (Union[Unset, None, int]):
        estimated_value (Union[Unset, None, int]):
        contract_value (Union[Unset, None, int]):
        estimated_close_date (Union[Unset, None, datetime.datetime]):
        managers (Union[Unset, None, List['CompanyUserBaseModel']]):
        sales_manager (Union[Unset, None, CompanyUserBaseModel]):
        sales_managers (Union[Unset, None, List['CompanyUserBaseModel']]):
        intermediator (Union[Unset, None, CompanyCustomerBaseModel]):
        events (Union[Unset, None, List['ProjectEventBaseModel']]):
        customer_contacts (Union[Unset, None, List['CompanyCustomerContactBaseModel']]):
        intermediator_contacts (Union[Unset, None, List['CompanyCustomerContactBaseModel']]):
        assignments (Union[Unset, None, List['ProjectAssignmentBaseModel']]):
        attachments (Union[Unset, None, List['ProjectAttachmentModel']]):
        tags (Union[Unset, None, List['CompanyTagBaseModel']]):
        pipeline_id (Union[Unset, None, int]):
        current_stage_id (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyModel]):
        project_references (Union[Unset, None, List['ProjectReferenceModel']]):
        current_state (Union[Unset, ProjectState]):

            Öppen = 0

            Vunnen = 30

            Förlorad = 40

            Avböjd = 50

            Uppskjuten = 60
        state_history (Union[Unset, None, List['ProjectStateHistoryModel']]):
        created_by (Union[Unset, None, CompanyUserBaseModel]):
        updated_by (Union[Unset, None, CompanyUserBaseModel]):
        created_date_time (Union[Unset, datetime.datetime]):
        updated_date_time (Union[Unset, None, datetime.datetime]):
        team_id (Union[Unset, None, int]):
        state_reason_id (Union[Unset, None, int]):
        sales_manager_ids (Union[Unset, None, List[int]]): List of sales managers employee ids
        project_manager_ids (Union[Unset, None, List[int]]): List of project managers employee ids
        priority (Union[Unset, ProjectPriority]):

            Låg = 3

            Medel = 5

            Hög = 8
        company_id (Union[Unset, int]):
        customer_id (Union[Unset, int]):
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        identifier (Union[Unset, None, str]):
        customer_identifier (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    company: Union[Unset, None, "CompanyBaseModel"] = UNSET
    customer: Union[Unset, None, "CompanyCustomerBaseModel"] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    location_id: Union[Unset, None, int] = UNSET
    google_id: Union[Unset, None, str] = UNSET
    probability: Union[Unset, None, int] = UNSET
    estimated_value: Union[Unset, None, int] = UNSET
    contract_value: Union[Unset, None, int] = UNSET
    estimated_close_date: Union[Unset, None, datetime.datetime] = UNSET
    managers: Union[Unset, None, List["CompanyUserBaseModel"]] = UNSET
    sales_manager: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    sales_managers: Union[Unset, None, List["CompanyUserBaseModel"]] = UNSET
    intermediator: Union[Unset, None, "CompanyCustomerBaseModel"] = UNSET
    events: Union[Unset, None, List["ProjectEventBaseModel"]] = UNSET
    customer_contacts: Union[Unset, None, List["CompanyCustomerContactBaseModel"]] = UNSET
    intermediator_contacts: Union[Unset, None, List["CompanyCustomerContactBaseModel"]] = UNSET
    assignments: Union[Unset, None, List["ProjectAssignmentBaseModel"]] = UNSET
    attachments: Union[Unset, None, List["ProjectAttachmentModel"]] = UNSET
    tags: Union[Unset, None, List["CompanyTagBaseModel"]] = UNSET
    pipeline_id: Union[Unset, None, int] = UNSET
    current_stage_id: Union[Unset, None, int] = UNSET
    currency: Union[Unset, None, "CurrencyModel"] = UNSET
    project_references: Union[Unset, None, List["ProjectReferenceModel"]] = UNSET
    current_state: Union[Unset, ProjectState] = UNSET
    state_history: Union[Unset, None, List["ProjectStateHistoryModel"]] = UNSET
    created_by: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    updated_by: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    updated_date_time: Union[Unset, None, datetime.datetime] = UNSET
    team_id: Union[Unset, None, int] = UNSET
    state_reason_id: Union[Unset, None, int] = UNSET
    sales_manager_ids: Union[Unset, None, List[int]] = UNSET
    project_manager_ids: Union[Unset, None, List[int]] = UNSET
    priority: Union[Unset, ProjectPriority] = UNSET
    company_id: Union[Unset, int] = UNSET
    customer_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    identifier: Union[Unset, None, str] = UNSET
    customer_identifier: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict() if self.company else None

        customer: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict() if self.customer else None

        seo_id = self.seo_id
        location_id = self.location_id
        google_id = self.google_id
        probability = self.probability
        estimated_value = self.estimated_value
        contract_value = self.contract_value
        estimated_close_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.estimated_close_date, Unset):
            estimated_close_date = self.estimated_close_date.isoformat() if self.estimated_close_date else None

        managers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.managers, Unset):
            if self.managers is None:
                managers = None
            else:
                managers = []
                for managers_item_data in self.managers:
                    managers_item = managers_item_data.to_dict()

                    managers.append(managers_item)

        sales_manager: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sales_manager, Unset):
            sales_manager = self.sales_manager.to_dict() if self.sales_manager else None

        sales_managers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_managers, Unset):
            if self.sales_managers is None:
                sales_managers = None
            else:
                sales_managers = []
                for sales_managers_item_data in self.sales_managers:
                    sales_managers_item = sales_managers_item_data.to_dict()

                    sales_managers.append(sales_managers_item)

        intermediator: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.intermediator, Unset):
            intermediator = self.intermediator.to_dict() if self.intermediator else None

        events: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            if self.events is None:
                events = None
            else:
                events = []
                for events_item_data in self.events:
                    events_item = events_item_data.to_dict()

                    events.append(events_item)

        customer_contacts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.customer_contacts, Unset):
            if self.customer_contacts is None:
                customer_contacts = None
            else:
                customer_contacts = []
                for customer_contacts_item_data in self.customer_contacts:
                    customer_contacts_item = customer_contacts_item_data.to_dict()

                    customer_contacts.append(customer_contacts_item)

        intermediator_contacts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.intermediator_contacts, Unset):
            if self.intermediator_contacts is None:
                intermediator_contacts = None
            else:
                intermediator_contacts = []
                for intermediator_contacts_item_data in self.intermediator_contacts:
                    intermediator_contacts_item = intermediator_contacts_item_data.to_dict()

                    intermediator_contacts.append(intermediator_contacts_item)

        assignments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assignments, Unset):
            if self.assignments is None:
                assignments = None
            else:
                assignments = []
                for assignments_item_data in self.assignments:
                    assignments_item = assignments_item_data.to_dict()

                    assignments.append(assignments_item)

        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        tags: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = []
                for tags_item_data in self.tags:
                    tags_item = tags_item_data.to_dict()

                    tags.append(tags_item)

        pipeline_id = self.pipeline_id
        current_stage_id = self.current_stage_id
        currency: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict() if self.currency else None

        project_references: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.project_references, Unset):
            if self.project_references is None:
                project_references = None
            else:
                project_references = []
                for project_references_item_data in self.project_references:
                    project_references_item = project_references_item_data.to_dict()

                    project_references.append(project_references_item)

        current_state: Union[Unset, int] = UNSET
        if not isinstance(self.current_state, Unset):
            current_state = self.current_state.value

        state_history: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.state_history, Unset):
            if self.state_history is None:
                state_history = None
            else:
                state_history = []
                for state_history_item_data in self.state_history:
                    state_history_item = state_history_item_data.to_dict()

                    state_history.append(state_history_item)

        created_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict() if self.created_by else None

        updated_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.updated_by, Unset):
            updated_by = self.updated_by.to_dict() if self.updated_by else None

        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        updated_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_date_time, Unset):
            updated_date_time = self.updated_date_time.isoformat() if self.updated_date_time else None

        team_id = self.team_id
        state_reason_id = self.state_reason_id
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

        priority: Union[Unset, int] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        company_id = self.company_id
        customer_id = self.customer_id
        id = self.id
        title = self.title
        description = self.description
        identifier = self.identifier
        customer_identifier = self.customer_identifier
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if customer is not UNSET:
            field_dict["customer"] = customer
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if probability is not UNSET:
            field_dict["probability"] = probability
        if estimated_value is not UNSET:
            field_dict["estimatedValue"] = estimated_value
        if contract_value is not UNSET:
            field_dict["contractValue"] = contract_value
        if estimated_close_date is not UNSET:
            field_dict["estimatedCloseDate"] = estimated_close_date
        if managers is not UNSET:
            field_dict["managers"] = managers
        if sales_manager is not UNSET:
            field_dict["salesManager"] = sales_manager
        if sales_managers is not UNSET:
            field_dict["salesManagers"] = sales_managers
        if intermediator is not UNSET:
            field_dict["intermediator"] = intermediator
        if events is not UNSET:
            field_dict["events"] = events
        if customer_contacts is not UNSET:
            field_dict["customerContacts"] = customer_contacts
        if intermediator_contacts is not UNSET:
            field_dict["intermediatorContacts"] = intermediator_contacts
        if assignments is not UNSET:
            field_dict["assignments"] = assignments
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if current_stage_id is not UNSET:
            field_dict["currentStageId"] = current_stage_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if project_references is not UNSET:
            field_dict["projectReferences"] = project_references
        if current_state is not UNSET:
            field_dict["currentState"] = current_state
        if state_history is not UNSET:
            field_dict["stateHistory"] = state_history
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if updated_date_time is not UNSET:
            field_dict["updatedDateTime"] = updated_date_time
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if state_reason_id is not UNSET:
            field_dict["stateReasonId"] = state_reason_id
        if sales_manager_ids is not UNSET:
            field_dict["salesManagerIds"] = sales_manager_ids
        if project_manager_ids is not UNSET:
            field_dict["projectManagerIds"] = project_manager_ids
        if priority is not UNSET:
            field_dict["priority"] = priority
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if customer_identifier is not UNSET:
            field_dict["customerIdentifier"] = customer_identifier
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_base_model import CompanyBaseModel
        from ..models.company_customer_base_model import CompanyCustomerBaseModel
        from ..models.company_customer_contact_base_model import CompanyCustomerContactBaseModel
        from ..models.company_tag_base_model import CompanyTagBaseModel
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.currency_model import CurrencyModel
        from ..models.link import Link
        from ..models.project_assignment_base_model import ProjectAssignmentBaseModel
        from ..models.project_attachment_model import ProjectAttachmentModel
        from ..models.project_event_base_model import ProjectEventBaseModel
        from ..models.project_reference_model import ProjectReferenceModel
        from ..models.project_state_history_model import ProjectStateHistoryModel

        d = src_dict.copy()
        _company = d.pop("company", UNSET)
        company: Union[Unset, None, CompanyBaseModel]
        if _company is None:
            company = None
        elif isinstance(_company, Unset):
            company = UNSET
        else:
            company = CompanyBaseModel.from_dict(_company)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, None, CompanyCustomerBaseModel]
        if _customer is None:
            customer = None
        elif isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CompanyCustomerBaseModel.from_dict(_customer)

        seo_id = d.pop("seoId", UNSET)

        location_id = d.pop("locationId", UNSET)

        google_id = d.pop("googleId", UNSET)

        probability = d.pop("probability", UNSET)

        estimated_value = d.pop("estimatedValue", UNSET)

        contract_value = d.pop("contractValue", UNSET)

        _estimated_close_date = d.pop("estimatedCloseDate", UNSET)
        estimated_close_date: Union[Unset, None, datetime.datetime]
        if _estimated_close_date is None:
            estimated_close_date = None
        elif isinstance(_estimated_close_date, Unset):
            estimated_close_date = UNSET
        else:
            estimated_close_date = isoparse(_estimated_close_date)

        managers = []
        _managers = d.pop("managers", UNSET)
        for managers_item_data in _managers or []:
            managers_item = CompanyUserBaseModel.from_dict(managers_item_data)

            managers.append(managers_item)

        _sales_manager = d.pop("salesManager", UNSET)
        sales_manager: Union[Unset, None, CompanyUserBaseModel]
        if _sales_manager is None:
            sales_manager = None
        elif isinstance(_sales_manager, Unset):
            sales_manager = UNSET
        else:
            sales_manager = CompanyUserBaseModel.from_dict(_sales_manager)

        sales_managers = []
        _sales_managers = d.pop("salesManagers", UNSET)
        for sales_managers_item_data in _sales_managers or []:
            sales_managers_item = CompanyUserBaseModel.from_dict(sales_managers_item_data)

            sales_managers.append(sales_managers_item)

        _intermediator = d.pop("intermediator", UNSET)
        intermediator: Union[Unset, None, CompanyCustomerBaseModel]
        if _intermediator is None:
            intermediator = None
        elif isinstance(_intermediator, Unset):
            intermediator = UNSET
        else:
            intermediator = CompanyCustomerBaseModel.from_dict(_intermediator)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = ProjectEventBaseModel.from_dict(events_item_data)

            events.append(events_item)

        customer_contacts = []
        _customer_contacts = d.pop("customerContacts", UNSET)
        for customer_contacts_item_data in _customer_contacts or []:
            customer_contacts_item = CompanyCustomerContactBaseModel.from_dict(customer_contacts_item_data)

            customer_contacts.append(customer_contacts_item)

        intermediator_contacts = []
        _intermediator_contacts = d.pop("intermediatorContacts", UNSET)
        for intermediator_contacts_item_data in _intermediator_contacts or []:
            intermediator_contacts_item = CompanyCustomerContactBaseModel.from_dict(intermediator_contacts_item_data)

            intermediator_contacts.append(intermediator_contacts_item)

        assignments = []
        _assignments = d.pop("assignments", UNSET)
        for assignments_item_data in _assignments or []:
            assignments_item = ProjectAssignmentBaseModel.from_dict(assignments_item_data)

            assignments.append(assignments_item)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = ProjectAttachmentModel.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = CompanyTagBaseModel.from_dict(tags_item_data)

            tags.append(tags_item)

        pipeline_id = d.pop("pipelineId", UNSET)

        current_stage_id = d.pop("currentStageId", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, None, CurrencyModel]
        if _currency is None:
            currency = None
        elif isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = CurrencyModel.from_dict(_currency)

        project_references = []
        _project_references = d.pop("projectReferences", UNSET)
        for project_references_item_data in _project_references or []:
            project_references_item = ProjectReferenceModel.from_dict(project_references_item_data)

            project_references.append(project_references_item)

        _current_state = d.pop("currentState", UNSET)
        current_state: Union[Unset, ProjectState]
        if isinstance(_current_state, Unset):
            current_state = UNSET
        else:
            current_state = ProjectState(_current_state)

        state_history = []
        _state_history = d.pop("stateHistory", UNSET)
        for state_history_item_data in _state_history or []:
            state_history_item = ProjectStateHistoryModel.from_dict(state_history_item_data)

            state_history.append(state_history_item)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, None, CompanyUserBaseModel]
        if _created_by is None:
            created_by = None
        elif isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = CompanyUserBaseModel.from_dict(_created_by)

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: Union[Unset, None, CompanyUserBaseModel]
        if _updated_by is None:
            updated_by = None
        elif isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = CompanyUserBaseModel.from_dict(_updated_by)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _updated_date_time = d.pop("updatedDateTime", UNSET)
        updated_date_time: Union[Unset, None, datetime.datetime]
        if _updated_date_time is None:
            updated_date_time = None
        elif isinstance(_updated_date_time, Unset):
            updated_date_time = UNSET
        else:
            updated_date_time = isoparse(_updated_date_time)

        team_id = d.pop("teamId", UNSET)

        state_reason_id = d.pop("stateReasonId", UNSET)

        sales_manager_ids = cast(List[int], d.pop("salesManagerIds", UNSET))

        project_manager_ids = cast(List[int], d.pop("projectManagerIds", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, ProjectPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ProjectPriority(_priority)

        company_id = d.pop("companyId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        customer_identifier = d.pop("customerIdentifier", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        project_model = cls(
            company=company,
            customer=customer,
            seo_id=seo_id,
            location_id=location_id,
            google_id=google_id,
            probability=probability,
            estimated_value=estimated_value,
            contract_value=contract_value,
            estimated_close_date=estimated_close_date,
            managers=managers,
            sales_manager=sales_manager,
            sales_managers=sales_managers,
            intermediator=intermediator,
            events=events,
            customer_contacts=customer_contacts,
            intermediator_contacts=intermediator_contacts,
            assignments=assignments,
            attachments=attachments,
            tags=tags,
            pipeline_id=pipeline_id,
            current_stage_id=current_stage_id,
            currency=currency,
            project_references=project_references,
            current_state=current_state,
            state_history=state_history,
            created_by=created_by,
            updated_by=updated_by,
            created_date_time=created_date_time,
            updated_date_time=updated_date_time,
            team_id=team_id,
            state_reason_id=state_reason_id,
            sales_manager_ids=sales_manager_ids,
            project_manager_ids=project_manager_ids,
            priority=priority,
            company_id=company_id,
            customer_id=customer_id,
            id=id,
            title=title,
            description=description,
            identifier=identifier,
            customer_identifier=customer_identifier,
            links=links,
        )

        return project_model
