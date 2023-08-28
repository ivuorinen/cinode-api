from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_profile_sort_page_and_sort_by_model import CompanyProfileSortPageAndSortByModel


T = TypeVar("T", bound="CompanyProfileFilterModel")


@_attrs_define
class CompanyProfileFilterModel:
    """
    Attributes:
        created_offset_days (Union[Unset, None, int]): If set to true, the results will include only Profiles created
            within the last X days
        updated_offset_days (Union[Unset, None, int]): If set to true, the results will include only Profiles updated
            within the last X days
        page_and_sort_by (Union[Unset, None, CompanyProfileSortPageAndSortByModel]):
    """

    created_offset_days: Union[Unset, None, int] = UNSET
    updated_offset_days: Union[Unset, None, int] = UNSET
    page_and_sort_by: Union[Unset, None, "CompanyProfileSortPageAndSortByModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        created_offset_days = self.created_offset_days
        updated_offset_days = self.updated_offset_days
        page_and_sort_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.page_and_sort_by, Unset):
            page_and_sort_by = self.page_and_sort_by.to_dict() if self.page_and_sort_by else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if created_offset_days is not UNSET:
            field_dict["createdOffsetDays"] = created_offset_days
        if updated_offset_days is not UNSET:
            field_dict["updatedOffsetDays"] = updated_offset_days
        if page_and_sort_by is not UNSET:
            field_dict["pageAndSortBy"] = page_and_sort_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_profile_sort_page_and_sort_by_model import CompanyProfileSortPageAndSortByModel

        d = src_dict.copy()
        created_offset_days = d.pop("createdOffsetDays", UNSET)

        updated_offset_days = d.pop("updatedOffsetDays", UNSET)

        _page_and_sort_by = d.pop("pageAndSortBy", UNSET)
        page_and_sort_by: Union[Unset, None, CompanyProfileSortPageAndSortByModel]
        if _page_and_sort_by is None:
            page_and_sort_by = None
        elif isinstance(_page_and_sort_by, Unset):
            page_and_sort_by = UNSET
        else:
            page_and_sort_by = CompanyProfileSortPageAndSortByModel.from_dict(_page_and_sort_by)

        company_profile_filter_model = cls(
            created_offset_days=created_offset_days,
            updated_offset_days=updated_offset_days,
            page_and_sort_by=page_and_sort_by,
        )

        return company_profile_filter_model
