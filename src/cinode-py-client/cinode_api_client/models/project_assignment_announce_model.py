import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_recipient_base_model import PartnerRecipientBaseModel


T = TypeVar("T", bound="ProjectAssignmentAnnounceModel")


@_attrs_define
class ProjectAssignmentAnnounceModel:
    """
    Attributes:
        title (str):
        deadline (datetime.datetime):
        manager_company_user_id (int):
        description (Union[Unset, None, str]):
        price (Union[Unset, None, float]):
        is_price_negotiable (Union[Unset, bool]):
        currency_id (Union[Unset, None, int]):
        attachment_ids (Union[Unset, None, List[str]]):
        partner_recipients (Union[Unset, None, List['PartnerRecipientBaseModel']]):
        subcontractor_ids (Union[Unset, None, List[int]]):
        announce_to_partner_network (Union[Unset, None, bool]):
        announce_to_market (Union[Unset, None, bool]):
        is_remote (Union[Unset, None, bool]):
        remote_percentage (Union[Unset, None, int]): Accepts values between 0 and 100. 0 indicates that the work is to
            be done on site. 100 means that the position is fully remote.
        is_end_customer_assignment (Union[Unset, None, bool]):
        publish_for_real (Union[Unset, bool]): Set to true if you actually want to publish the announcement to your
            recipients, if you are developing/testing the endpoint it should be false, then no persist will take place.
        reference_id (Union[Unset, None, str]):
    """

    title: str
    deadline: datetime.datetime
    manager_company_user_id: int
    description: Union[Unset, None, str] = UNSET
    price: Union[Unset, None, float] = UNSET
    is_price_negotiable: Union[Unset, bool] = UNSET
    currency_id: Union[Unset, None, int] = UNSET
    attachment_ids: Union[Unset, None, List[str]] = UNSET
    partner_recipients: Union[Unset, None, List["PartnerRecipientBaseModel"]] = UNSET
    subcontractor_ids: Union[Unset, None, List[int]] = UNSET
    announce_to_partner_network: Union[Unset, None, bool] = UNSET
    announce_to_market: Union[Unset, None, bool] = UNSET
    is_remote: Union[Unset, None, bool] = UNSET
    remote_percentage: Union[Unset, None, int] = UNSET
    is_end_customer_assignment: Union[Unset, None, bool] = UNSET
    publish_for_real: Union[Unset, bool] = UNSET
    reference_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        deadline = self.deadline.isoformat()

        manager_company_user_id = self.manager_company_user_id
        description = self.description
        price = self.price
        is_price_negotiable = self.is_price_negotiable
        currency_id = self.currency_id
        attachment_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.attachment_ids, Unset):
            if self.attachment_ids is None:
                attachment_ids = None
            else:
                attachment_ids = self.attachment_ids

        partner_recipients: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partner_recipients, Unset):
            if self.partner_recipients is None:
                partner_recipients = None
            else:
                partner_recipients = []
                for partner_recipients_item_data in self.partner_recipients:
                    partner_recipients_item = partner_recipients_item_data.to_dict()

                    partner_recipients.append(partner_recipients_item)

        subcontractor_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.subcontractor_ids, Unset):
            if self.subcontractor_ids is None:
                subcontractor_ids = None
            else:
                subcontractor_ids = self.subcontractor_ids

        announce_to_partner_network = self.announce_to_partner_network
        announce_to_market = self.announce_to_market
        is_remote = self.is_remote
        remote_percentage = self.remote_percentage
        is_end_customer_assignment = self.is_end_customer_assignment
        publish_for_real = self.publish_for_real
        reference_id = self.reference_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
                "deadline": deadline,
                "managerCompanyUserId": manager_company_user_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if price is not UNSET:
            field_dict["price"] = price
        if is_price_negotiable is not UNSET:
            field_dict["isPriceNegotiable"] = is_price_negotiable
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if attachment_ids is not UNSET:
            field_dict["attachmentIds"] = attachment_ids
        if partner_recipients is not UNSET:
            field_dict["partnerRecipients"] = partner_recipients
        if subcontractor_ids is not UNSET:
            field_dict["subcontractorIds"] = subcontractor_ids
        if announce_to_partner_network is not UNSET:
            field_dict["announceToPartnerNetwork"] = announce_to_partner_network
        if announce_to_market is not UNSET:
            field_dict["announceToMarket"] = announce_to_market
        if is_remote is not UNSET:
            field_dict["isRemote"] = is_remote
        if remote_percentage is not UNSET:
            field_dict["remotePercentage"] = remote_percentage
        if is_end_customer_assignment is not UNSET:
            field_dict["isEndCustomerAssignment"] = is_end_customer_assignment
        if publish_for_real is not UNSET:
            field_dict["publishForReal"] = publish_for_real
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.partner_recipient_base_model import PartnerRecipientBaseModel

        d = src_dict.copy()
        title = d.pop("title")

        deadline = isoparse(d.pop("deadline"))

        manager_company_user_id = d.pop("managerCompanyUserId")

        description = d.pop("description", UNSET)

        price = d.pop("price", UNSET)

        is_price_negotiable = d.pop("isPriceNegotiable", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        attachment_ids = cast(List[str], d.pop("attachmentIds", UNSET))

        partner_recipients = []
        _partner_recipients = d.pop("partnerRecipients", UNSET)
        for partner_recipients_item_data in _partner_recipients or []:
            partner_recipients_item = PartnerRecipientBaseModel.from_dict(partner_recipients_item_data)

            partner_recipients.append(partner_recipients_item)

        subcontractor_ids = cast(List[int], d.pop("subcontractorIds", UNSET))

        announce_to_partner_network = d.pop("announceToPartnerNetwork", UNSET)

        announce_to_market = d.pop("announceToMarket", UNSET)

        is_remote = d.pop("isRemote", UNSET)

        remote_percentage = d.pop("remotePercentage", UNSET)

        is_end_customer_assignment = d.pop("isEndCustomerAssignment", UNSET)

        publish_for_real = d.pop("publishForReal", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        project_assignment_announce_model = cls(
            title=title,
            deadline=deadline,
            manager_company_user_id=manager_company_user_id,
            description=description,
            price=price,
            is_price_negotiable=is_price_negotiable,
            currency_id=currency_id,
            attachment_ids=attachment_ids,
            partner_recipients=partner_recipients,
            subcontractor_ids=subcontractor_ids,
            announce_to_partner_network=announce_to_partner_network,
            announce_to_market=announce_to_market,
            is_remote=is_remote,
            remote_percentage=remote_percentage,
            is_end_customer_assignment=is_end_customer_assignment,
            publish_for_real=publish_for_real,
            reference_id=reference_id,
        )

        return project_assignment_announce_model
