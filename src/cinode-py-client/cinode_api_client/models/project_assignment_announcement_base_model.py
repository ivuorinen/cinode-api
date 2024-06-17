import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.contract_type import ContractType
from ..models.project_assignment_request_status import ProjectAssignmentRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentAnnouncementBaseModel")


@_attrs_define
class ProjectAssignmentAnnouncementBaseModel:
    """
    Attributes:
        request_id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        project_id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        project_assignment_id (Union[Unset, int]):
        created_date_time (Union[Unset, datetime.datetime]):
        deadline (Union[Unset, datetime.datetime]):
        price (Union[Unset, None, float]):
        contract_type (Union[Unset, ContractType]):

            Timpris = 0

            Fastpris = 1
        description (Union[Unset, None, str]):
        description_html (Union[Unset, None, str]):
        currency_code (Union[Unset, None, str]):
        currency_id (Union[Unset, None, int]):
        status (Union[Unset, ProjectAssignmentRequestStatus]):

            Öppen = 0

            Återkallad = 10

            Stängd = 20
        status_text (Union[Unset, None, str]):
        is_announced_to_partner_network (Union[Unset, None, bool]):
        is_price_negotiable (Union[Unset, bool]):
        is_remote (Union[Unset, None, bool]):
        remote_percentage (Union[Unset, None, int]): 0 indicates that the work is to be done on site. 100 means that the
            position is fully remote.
        is_announced_to_market (Union[Unset, None, bool]):
        is_end_customer_assignment (Union[Unset, None, bool]):
        reference_id (Union[Unset, None, str]):
    """

    request_id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    project_assignment_id: Union[Unset, int] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    deadline: Union[Unset, datetime.datetime] = UNSET
    price: Union[Unset, None, float] = UNSET
    contract_type: Union[Unset, ContractType] = UNSET
    description: Union[Unset, None, str] = UNSET
    description_html: Union[Unset, None, str] = UNSET
    currency_code: Union[Unset, None, str] = UNSET
    currency_id: Union[Unset, None, int] = UNSET
    status: Union[Unset, ProjectAssignmentRequestStatus] = UNSET
    status_text: Union[Unset, None, str] = UNSET
    is_announced_to_partner_network: Union[Unset, None, bool] = UNSET
    is_price_negotiable: Union[Unset, bool] = UNSET
    is_remote: Union[Unset, None, bool] = UNSET
    remote_percentage: Union[Unset, None, int] = UNSET
    is_announced_to_market: Union[Unset, None, bool] = UNSET
    is_end_customer_assignment: Union[Unset, None, bool] = UNSET
    reference_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        request_id = self.request_id
        title = self.title
        project_id = self.project_id
        company_id = self.company_id
        project_assignment_id = self.project_assignment_id
        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        deadline: Union[Unset, str] = UNSET
        if not isinstance(self.deadline, Unset):
            deadline = self.deadline.isoformat()

        price = self.price
        contract_type: Union[Unset, int] = UNSET
        if not isinstance(self.contract_type, Unset):
            contract_type = self.contract_type.value

        description = self.description
        description_html = self.description_html
        currency_code = self.currency_code
        currency_id = self.currency_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_text = self.status_text
        is_announced_to_partner_network = self.is_announced_to_partner_network
        is_price_negotiable = self.is_price_negotiable
        is_remote = self.is_remote
        remote_percentage = self.remote_percentage
        is_announced_to_market = self.is_announced_to_market
        is_end_customer_assignment = self.is_end_customer_assignment
        reference_id = self.reference_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if title is not UNSET:
            field_dict["title"] = title
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if project_assignment_id is not UNSET:
            field_dict["projectAssignmentId"] = project_assignment_id
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if price is not UNSET:
            field_dict["price"] = price
        if contract_type is not UNSET:
            field_dict["contractType"] = contract_type
        if description is not UNSET:
            field_dict["description"] = description
        if description_html is not UNSET:
            field_dict["descriptionHtml"] = description_html
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_text is not UNSET:
            field_dict["statusText"] = status_text
        if is_announced_to_partner_network is not UNSET:
            field_dict["isAnnouncedToPartnerNetwork"] = is_announced_to_partner_network
        if is_price_negotiable is not UNSET:
            field_dict["isPriceNegotiable"] = is_price_negotiable
        if is_remote is not UNSET:
            field_dict["isRemote"] = is_remote
        if remote_percentage is not UNSET:
            field_dict["remotePercentage"] = remote_percentage
        if is_announced_to_market is not UNSET:
            field_dict["isAnnouncedToMarket"] = is_announced_to_market
        if is_end_customer_assignment is not UNSET:
            field_dict["isEndCustomerAssignment"] = is_end_customer_assignment
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        request_id = d.pop("requestId", UNSET)

        title = d.pop("title", UNSET)

        project_id = d.pop("projectId", UNSET)

        company_id = d.pop("companyId", UNSET)

        project_assignment_id = d.pop("projectAssignmentId", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _deadline = d.pop("deadline", UNSET)
        deadline: Union[Unset, datetime.datetime]
        if isinstance(_deadline, Unset):
            deadline = UNSET
        else:
            deadline = isoparse(_deadline)

        price = d.pop("price", UNSET)

        _contract_type = d.pop("contractType", UNSET)
        contract_type: Union[Unset, ContractType]
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = ContractType(_contract_type)

        description = d.pop("description", UNSET)

        description_html = d.pop("descriptionHtml", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProjectAssignmentRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectAssignmentRequestStatus(_status)

        status_text = d.pop("statusText", UNSET)

        is_announced_to_partner_network = d.pop("isAnnouncedToPartnerNetwork", UNSET)

        is_price_negotiable = d.pop("isPriceNegotiable", UNSET)

        is_remote = d.pop("isRemote", UNSET)

        remote_percentage = d.pop("remotePercentage", UNSET)

        is_announced_to_market = d.pop("isAnnouncedToMarket", UNSET)

        is_end_customer_assignment = d.pop("isEndCustomerAssignment", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        project_assignment_announcement_base_model = cls(
            request_id=request_id,
            title=title,
            project_id=project_id,
            company_id=company_id,
            project_assignment_id=project_assignment_id,
            created_date_time=created_date_time,
            deadline=deadline,
            price=price,
            contract_type=contract_type,
            description=description,
            description_html=description_html,
            currency_code=currency_code,
            currency_id=currency_id,
            status=status,
            status_text=status_text,
            is_announced_to_partner_network=is_announced_to_partner_network,
            is_price_negotiable=is_price_negotiable,
            is_remote=is_remote,
            remote_percentage=remote_percentage,
            is_announced_to_market=is_announced_to_market,
            is_end_customer_assignment=is_end_customer_assignment,
            reference_id=reference_id,
        )

        return project_assignment_announcement_base_model
