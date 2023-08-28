from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_customer_contact_model import CompanyCustomerContactModel
    from ..models.company_customer_contact_query_sort_page_and_sort_by_model import (
        CompanyCustomerContactQuerySortPageAndSortByModel,
    )


T = TypeVar("T", bound="SearchCompanyCustomerContactResultModel")


@_attrs_define
class SearchCompanyCustomerContactResultModel:
    """
    Attributes:
        paged_and_sorted_by (Union[Unset, None, CompanyCustomerContactQuerySortPageAndSortByModel]):
        result (Union[Unset, None, List['CompanyCustomerContactModel']]):
        hits (Union[Unset, int]):
        total_items (Union[Unset, int]):
    """

    paged_and_sorted_by: Union[Unset, None, "CompanyCustomerContactQuerySortPageAndSortByModel"] = UNSET
    result: Union[Unset, None, List["CompanyCustomerContactModel"]] = UNSET
    hits: Union[Unset, int] = UNSET
    total_items: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        paged_and_sorted_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.paged_and_sorted_by, Unset):
            paged_and_sorted_by = self.paged_and_sorted_by.to_dict() if self.paged_and_sorted_by else None

        result: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            if self.result is None:
                result = None
            else:
                result = []
                for result_item_data in self.result:
                    result_item = result_item_data.to_dict()

                    result.append(result_item)

        hits = self.hits
        total_items = self.total_items

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if paged_and_sorted_by is not UNSET:
            field_dict["pagedAndSortedBy"] = paged_and_sorted_by
        if result is not UNSET:
            field_dict["result"] = result
        if hits is not UNSET:
            field_dict["hits"] = hits
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_customer_contact_model import CompanyCustomerContactModel
        from ..models.company_customer_contact_query_sort_page_and_sort_by_model import (
            CompanyCustomerContactQuerySortPageAndSortByModel,
        )

        d = src_dict.copy()
        _paged_and_sorted_by = d.pop("pagedAndSortedBy", UNSET)
        paged_and_sorted_by: Union[Unset, None, CompanyCustomerContactQuerySortPageAndSortByModel]
        if _paged_and_sorted_by is None:
            paged_and_sorted_by = None
        elif isinstance(_paged_and_sorted_by, Unset):
            paged_and_sorted_by = UNSET
        else:
            paged_and_sorted_by = CompanyCustomerContactQuerySortPageAndSortByModel.from_dict(_paged_and_sorted_by)

        result = []
        _result = d.pop("result", UNSET)
        for result_item_data in _result or []:
            result_item = CompanyCustomerContactModel.from_dict(result_item_data)

            result.append(result_item)

        hits = d.pop("hits", UNSET)

        total_items = d.pop("totalItems", UNSET)

        search_company_customer_contact_result_model = cls(
            paged_and_sorted_by=paged_and_sorted_by,
            result=result,
            hits=hits,
            total_items=total_items,
        )

        return search_company_customer_contact_result_model
