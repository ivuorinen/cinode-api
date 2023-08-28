from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCustomerManagersAddEditModel")


@_attrs_define
class CompanyCustomerManagersAddEditModel:
    """
    Attributes:
        company_user_ids (Union[Unset, None, List[int]]):
    """

    company_user_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_user_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.company_user_ids, Unset):
            if self.company_user_ids is None:
                company_user_ids = None
            else:
                company_user_ids = self.company_user_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_user_ids is not UNSET:
            field_dict["companyUserIds"] = company_user_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_user_ids = cast(List[int], d.pop("companyUserIds", UNSET))

        company_customer_managers_add_edit_model = cls(
            company_user_ids=company_user_ids,
        )

        return company_customer_managers_add_edit_model
