from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.action_type import ActionType
from ..models.webhook_entity_type import WebhookEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookConfigurationModel")


@_attrs_define
class WebhookConfigurationModel:
    """
    Attributes:
        entity_type (Union[Unset, WebhookEntityType]):

            All = 1

            CompanyCandidate = 2

            CompanyEmployee = 3

            CompanySubcontractor = 4

            CompanyCustomer = 5

            CompanyProject = 6

            Role = 7

            PublicAnnouncement = 8

            Absence = 9

            CompanyCustomerContact = 10
        action_type (Union[Unset, ActionType]):

            All = 1

            Created = 2

            Updated = 3

            Borttagen = 4
    """

    entity_type: Union[Unset, WebhookEntityType] = UNSET
    action_type: Union[Unset, ActionType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        entity_type: Union[Unset, int] = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        action_type: Union[Unset, int] = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = self.action_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if action_type is not UNSET:
            field_dict["actionType"] = action_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _entity_type = d.pop("entityType", UNSET)
        entity_type: Union[Unset, WebhookEntityType]
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = WebhookEntityType(_entity_type)

        _action_type = d.pop("actionType", UNSET)
        action_type: Union[Unset, ActionType]
        if isinstance(_action_type, Unset):
            action_type = UNSET
        else:
            action_type = ActionType(_action_type)

        webhook_configuration_model = cls(
            entity_type=entity_type,
            action_type=action_type,
        )

        return webhook_configuration_model
