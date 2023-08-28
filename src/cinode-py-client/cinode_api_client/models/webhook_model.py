from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_configuration_model import WebhookConfigurationModel
    from ..models.webhook_credentials_model import WebhookCredentialsModel


T = TypeVar("T", bound="WebhookModel")


@_attrs_define
class WebhookModel:
    """
    Attributes:
        id (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        endpoint_url (Union[Unset, None, str]):
        configurations (Union[Unset, None, List['WebhookConfigurationModel']]):
        credentials (Union[Unset, None, List['WebhookCredentialsModel']]):
    """

    id: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    endpoint_url: Union[Unset, None, str] = UNSET
    configurations: Union[Unset, None, List["WebhookConfigurationModel"]] = UNSET
    credentials: Union[Unset, None, List["WebhookCredentialsModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_active = self.is_active
        endpoint_url = self.endpoint_url
        configurations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.configurations, Unset):
            if self.configurations is None:
                configurations = None
            else:
                configurations = []
                for configurations_item_data in self.configurations:
                    configurations_item = configurations_item_data.to_dict()

                    configurations.append(configurations_item)

        credentials: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credentials, Unset):
            if self.credentials is None:
                credentials = None
            else:
                credentials = []
                for credentials_item_data in self.credentials:
                    credentials_item = credentials_item_data.to_dict()

                    credentials.append(credentials_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if endpoint_url is not UNSET:
            field_dict["endpointUrl"] = endpoint_url
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_configuration_model import WebhookConfigurationModel
        from ..models.webhook_credentials_model import WebhookCredentialsModel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_active = d.pop("isActive", UNSET)

        endpoint_url = d.pop("endpointUrl", UNSET)

        configurations = []
        _configurations = d.pop("configurations", UNSET)
        for configurations_item_data in _configurations or []:
            configurations_item = WebhookConfigurationModel.from_dict(configurations_item_data)

            configurations.append(configurations_item)

        credentials = []
        _credentials = d.pop("credentials", UNSET)
        for credentials_item_data in _credentials or []:
            credentials_item = WebhookCredentialsModel.from_dict(credentials_item_data)

            credentials.append(credentials_item)

        webhook_model = cls(
            id=id,
            is_active=is_active,
            endpoint_url=endpoint_url,
            configurations=configurations,
            credentials=credentials,
        )

        return webhook_model
