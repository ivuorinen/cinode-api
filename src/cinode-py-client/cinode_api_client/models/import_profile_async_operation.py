from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.long_running_status import LongRunningStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_base_model import CompanyUserProfileBaseModel


T = TypeVar("T", bound="ImportProfileAsyncOperation")


@_attrs_define
class ImportProfileAsyncOperation:
    """
    Attributes:
        profile (Union[Unset, None, CompanyUserProfileBaseModel]):
        operation_id (Union[Unset, int]):
        status (Union[Unset, LongRunningStatus]):

            InProgress = 0

            Completed = 1

            Failed = 2
        errors (Union[Unset, None, List[str]]):
    """

    profile: Union[Unset, None, "CompanyUserProfileBaseModel"] = UNSET
    operation_id: Union[Unset, int] = UNSET
    status: Union[Unset, LongRunningStatus] = UNSET
    errors: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict() if self.profile else None

        operation_id = self.operation_id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        errors: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            if self.errors is None:
                errors = None
            else:
                errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if profile is not UNSET:
            field_dict["profile"] = profile
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if status is not UNSET:
            field_dict["status"] = status
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_base_model import CompanyUserProfileBaseModel

        d = src_dict.copy()
        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, None, CompanyUserProfileBaseModel]
        if _profile is None:
            profile = None
        elif isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = CompanyUserProfileBaseModel.from_dict(_profile)

        operation_id = d.pop("operationId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, LongRunningStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LongRunningStatus(_status)

        errors = cast(List[str], d.pop("errors", UNSET))

        import_profile_async_operation = cls(
            profile=profile,
            operation_id=operation_id,
            status=status,
            errors=errors,
        )

        return import_profile_async_operation
