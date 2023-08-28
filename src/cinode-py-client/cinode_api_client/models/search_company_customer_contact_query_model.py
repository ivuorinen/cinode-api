from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_customer_contact_query_sort_page_and_sort_by_model import (
        CompanyCustomerContactQuerySortPageAndSortByModel,
    )


T = TypeVar("T", bound="SearchCompanyCustomerContactQueryModel")


@_attrs_define
class SearchCompanyCustomerContactQueryModel:
    """
    Attributes:
        term (Union[Unset, None, str]):
        managers (Union[Unset, None, List[int]]):
        customers (Union[Unset, None, List[int]]):
        tags (Union[Unset, None, List[int]]):
        page_and_sort_by (Union[Unset, None, CompanyCustomerContactQuerySortPageAndSortByModel]):
    """

    term: Union[Unset, None, str] = UNSET
    managers: Union[Unset, None, List[int]] = UNSET
    customers: Union[Unset, None, List[int]] = UNSET
    tags: Union[Unset, None, List[int]] = UNSET
    page_and_sort_by: Union[Unset, None, "CompanyCustomerContactQuerySortPageAndSortByModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        managers: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.managers, Unset):
            if self.managers is None:
                managers = None
            else:
                managers = self.managers

        customers: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.customers, Unset):
            if self.customers is None:
                customers = None
            else:
                customers = self.customers

        tags: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = self.tags

        page_and_sort_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.page_and_sort_by, Unset):
            page_and_sort_by = self.page_and_sort_by.to_dict() if self.page_and_sort_by else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if managers is not UNSET:
            field_dict["managers"] = managers
        if customers is not UNSET:
            field_dict["customers"] = customers
        if tags is not UNSET:
            field_dict["tags"] = tags
        if page_and_sort_by is not UNSET:
            field_dict["pageAndSortBy"] = page_and_sort_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_customer_contact_query_sort_page_and_sort_by_model import (
            CompanyCustomerContactQuerySortPageAndSortByModel,
        )

        d = src_dict.copy()
        term = d.pop("term", UNSET)

        managers = cast(List[int], d.pop("managers", UNSET))

        customers = cast(List[int], d.pop("customers", UNSET))

        tags = cast(List[int], d.pop("tags", UNSET))

        _page_and_sort_by = d.pop("pageAndSortBy", UNSET)
        page_and_sort_by: Union[Unset, None, CompanyCustomerContactQuerySortPageAndSortByModel]
        if _page_and_sort_by is None:
            page_and_sort_by = None
        elif isinstance(_page_and_sort_by, Unset):
            page_and_sort_by = UNSET
        else:
            page_and_sort_by = CompanyCustomerContactQuerySortPageAndSortByModel.from_dict(_page_and_sort_by)

        search_company_customer_contact_query_model = cls(
            term=term,
            managers=managers,
            customers=customers,
            tags=tags,
            page_and_sort_by=page_and_sort_by,
        )

        return search_company_customer_contact_query_model
