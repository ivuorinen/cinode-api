from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.company_customer_contact_query_sort import CompanyCustomerContactQuerySort
from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCustomerContactQuerySortPageAndSortByModel")


@_attrs_define
class CompanyCustomerContactQuerySortPageAndSortByModel:
    """
    Attributes:
        sort_by (Union[Unset, CompanyCustomerContactQuerySort]):

            CreatedDateTime = 0

            FirstName = 1

            LastName = 2

            Email = 3

            UpdatedDateTime = 4

            CustomerId = 5
        sort_order (Union[Unset, SortOrder]): 0 - Ascending,
            1 - Descending
        page (Union[Unset, int]):  Default: 1.
        items_per_page (Union[Unset, int]):  Default: 15.
    """

    sort_by: Union[Unset, CompanyCustomerContactQuerySort] = UNSET
    sort_order: Union[Unset, SortOrder] = UNSET
    page: Union[Unset, int] = 1
    items_per_page: Union[Unset, int] = 15

    def to_dict(self) -> Dict[str, Any]:
        sort_by: Union[Unset, int] = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value

        sort_order: Union[Unset, int] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        page = self.page
        items_per_page = self.items_per_page

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if sort_by is not UNSET:
            field_dict["sortBy"] = sort_by
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if page is not UNSET:
            field_dict["page"] = page
        if items_per_page is not UNSET:
            field_dict["itemsPerPage"] = items_per_page

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sort_by = d.pop("sortBy", UNSET)
        sort_by: Union[Unset, CompanyCustomerContactQuerySort]
        if isinstance(_sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = CompanyCustomerContactQuerySort(_sort_by)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: Union[Unset, SortOrder]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortOrder(_sort_order)

        page = d.pop("page", UNSET)

        items_per_page = d.pop("itemsPerPage", UNSET)

        company_customer_contact_query_sort_page_and_sort_by_model = cls(
            sort_by=sort_by,
            sort_order=sort_order,
            page=page,
            items_per_page=items_per_page,
        )

        return company_customer_contact_query_sort_page_and_sort_by_model
