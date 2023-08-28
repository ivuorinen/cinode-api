from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCustomerDeleteModel")


@_attrs_define
class CompanyCustomerDeleteModel:
    """
    Attributes:
        customer_verification_name (Union[Unset, None, str]):
    """

    customer_verification_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        customer_verification_name = self.customer_verification_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if customer_verification_name is not UNSET:
            field_dict["customerVerificationName"] = customer_verification_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        customer_verification_name = d.pop("customerVerificationName", UNSET)

        company_customer_delete_model = cls(
            customer_verification_name=customer_verification_name,
        )

        return company_customer_delete_model
