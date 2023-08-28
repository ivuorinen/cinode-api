from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_configuration_add_model import WebhookConfigurationAddModel
    from ..models.webhook_credentials_add_model import WebhookCredentialsAddModel


T = TypeVar("T", bound="WebhookAddModel")


@_attrs_define
class WebhookAddModel:
    """
    Attributes:
        company_id (Union[Unset, None, int]):
        is_active (Union[Unset, bool]):
        endpoint_url (Union[Unset, None, str]):
        configurations (Union[Unset, None, List['WebhookConfigurationAddModel']]):
        credentials (Union[Unset, None, List['WebhookCredentialsAddModel']]):
    """

    company_id: Union[Unset, None, int] = UNSET
    is_active: Union[Unset, bool] = UNSET
    endpoint_url: Union[Unset, None, str] = UNSET
    configurations: Union[Unset, None, List["WebhookConfigurationAddModel"]] = UNSET
    credentials: Union[Unset, None, List["WebhookCredentialsAddModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
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
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
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
        from ..models.webhook_configuration_add_model import WebhookConfigurationAddModel
        from ..models.webhook_credentials_add_model import WebhookCredentialsAddModel

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        is_active = d.pop("isActive", UNSET)

        endpoint_url = d.pop("endpointUrl", UNSET)

        configurations = []
        _configurations = d.pop("configurations", UNSET)
        for configurations_item_data in _configurations or []:
            configurations_item = WebhookConfigurationAddModel.from_dict(configurations_item_data)

            configurations.append(configurations_item)

        credentials = []
        _credentials = d.pop("credentials", UNSET)
        for credentials_item_data in _credentials or []:
            credentials_item = WebhookCredentialsAddModel.from_dict(credentials_item_data)

            credentials.append(credentials_item)

        webhook_add_model = cls(
            company_id=company_id,
            is_active=is_active,
            endpoint_url=endpoint_url,
            configurations=configurations,
            credentials=credentials,
        )

        return webhook_add_model
