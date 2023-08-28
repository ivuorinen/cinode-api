from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_query_sort_page_and_sort_by_model import CompanyUserQuerySortPageAndSortByModel


T = TypeVar("T", bound="SearchCompanyUserQueryModel")


@_attrs_define
class SearchCompanyUserQueryModel:
    """
    Attributes:
        term (Union[Unset, None, str]):
        include_disconnected (Union[Unset, bool]):
        page_and_sort_by (Union[Unset, None, CompanyUserQuerySortPageAndSortByModel]):
    """

    term: Union[Unset, None, str] = UNSET
    include_disconnected: Union[Unset, bool] = UNSET
    page_and_sort_by: Union[Unset, None, "CompanyUserQuerySortPageAndSortByModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        include_disconnected = self.include_disconnected
        page_and_sort_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.page_and_sort_by, Unset):
            page_and_sort_by = self.page_and_sort_by.to_dict() if self.page_and_sort_by else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if include_disconnected is not UNSET:
            field_dict["includeDisconnected"] = include_disconnected
        if page_and_sort_by is not UNSET:
            field_dict["pageAndSortBy"] = page_and_sort_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_query_sort_page_and_sort_by_model import CompanyUserQuerySortPageAndSortByModel

        d = src_dict.copy()
        term = d.pop("term", UNSET)

        include_disconnected = d.pop("includeDisconnected", UNSET)

        _page_and_sort_by = d.pop("pageAndSortBy", UNSET)
        page_and_sort_by: Union[Unset, None, CompanyUserQuerySortPageAndSortByModel]
        if _page_and_sort_by is None:
            page_and_sort_by = None
        elif isinstance(_page_and_sort_by, Unset):
            page_and_sort_by = UNSET
        else:
            page_and_sort_by = CompanyUserQuerySortPageAndSortByModel.from_dict(_page_and_sort_by)

        search_company_user_query_model = cls(
            term=term,
            include_disconnected=include_disconnected,
            page_and_sort_by=page_and_sort_by,
        )

        return search_company_user_query_model
