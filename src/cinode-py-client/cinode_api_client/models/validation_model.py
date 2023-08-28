from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_model_errors import ValidationModelErrors


T = TypeVar("T", bound="ValidationModel")


@_attrs_define
class ValidationModel:
    """
    Attributes:
        errors (Union[Unset, None, ValidationModelErrors]): Collection of validation errors
    """

    errors: Union[Unset, None, "ValidationModelErrors"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict() if self.errors else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation_model_errors import ValidationModelErrors

        d = src_dict.copy()
        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, None, ValidationModelErrors]
        if _errors is None:
            errors = None
        elif isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ValidationModelErrors.from_dict(_errors)

        validation_model = cls(
            errors=errors,
        )

        return validation_model
