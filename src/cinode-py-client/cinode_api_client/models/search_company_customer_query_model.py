from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.string_comparison_operator import StringComparisonOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_customer_query_sort_page_and_sort_by_model import CompanyCustomerQuerySortPageAndSortByModel
    from ..models.date_time_filter_interval import DateTimeFilterInterval


T = TypeVar("T", bound="SearchCompanyCustomerQueryModel")


@_attrs_define
class SearchCompanyCustomerQueryModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        name_operator (Union[Unset, StringComparisonOperator]):

            Contains = 0

            StartsWith = 1

            EndsWith = 2

            Equals = 3
        identification (Union[Unset, None, str]):
        identification_operator (Union[Unset, StringComparisonOperator]):

            Contains = 0

            StartsWith = 1

            EndsWith = 2

            Equals = 3
        corporate_identity_number (Union[Unset, None, str]):
        corporate_identity_number_operator (Union[Unset, StringComparisonOperator]):

            Contains = 0

            StartsWith = 1

            EndsWith = 2

            Equals = 3
        last_touched_at (Union[Unset, None, DateTimeFilterInterval]):
        page_and_sort_by (Union[Unset, None, CompanyCustomerQuerySortPageAndSortByModel]):
    """

    name: Union[Unset, None, str] = UNSET
    name_operator: Union[Unset, StringComparisonOperator] = UNSET
    identification: Union[Unset, None, str] = UNSET
    identification_operator: Union[Unset, StringComparisonOperator] = UNSET
    corporate_identity_number: Union[Unset, None, str] = UNSET
    corporate_identity_number_operator: Union[Unset, StringComparisonOperator] = UNSET
    last_touched_at: Union[Unset, None, "DateTimeFilterInterval"] = UNSET
    page_and_sort_by: Union[Unset, None, "CompanyCustomerQuerySortPageAndSortByModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        name_operator: Union[Unset, int] = UNSET
        if not isinstance(self.name_operator, Unset):
            name_operator = self.name_operator.value

        identification = self.identification
        identification_operator: Union[Unset, int] = UNSET
        if not isinstance(self.identification_operator, Unset):
            identification_operator = self.identification_operator.value

        corporate_identity_number = self.corporate_identity_number
        corporate_identity_number_operator: Union[Unset, int] = UNSET
        if not isinstance(self.corporate_identity_number_operator, Unset):
            corporate_identity_number_operator = self.corporate_identity_number_operator.value

        last_touched_at: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.last_touched_at, Unset):
            last_touched_at = self.last_touched_at.to_dict() if self.last_touched_at else None

        page_and_sort_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.page_and_sort_by, Unset):
            page_and_sort_by = self.page_and_sort_by.to_dict() if self.page_and_sort_by else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if name_operator is not UNSET:
            field_dict["nameOperator"] = name_operator
        if identification is not UNSET:
            field_dict["identification"] = identification
        if identification_operator is not UNSET:
            field_dict["identificationOperator"] = identification_operator
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if corporate_identity_number_operator is not UNSET:
            field_dict["corporateIdentityNumberOperator"] = corporate_identity_number_operator
        if last_touched_at is not UNSET:
            field_dict["lastTouchedAt"] = last_touched_at
        if page_and_sort_by is not UNSET:
            field_dict["pageAndSortBy"] = page_and_sort_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_customer_query_sort_page_and_sort_by_model import (
            CompanyCustomerQuerySortPageAndSortByModel,
        )
        from ..models.date_time_filter_interval import DateTimeFilterInterval

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _name_operator = d.pop("nameOperator", UNSET)
        name_operator: Union[Unset, StringComparisonOperator]
        if isinstance(_name_operator, Unset):
            name_operator = UNSET
        else:
            name_operator = StringComparisonOperator(_name_operator)

        identification = d.pop("identification", UNSET)

        _identification_operator = d.pop("identificationOperator", UNSET)
        identification_operator: Union[Unset, StringComparisonOperator]
        if isinstance(_identification_operator, Unset):
            identification_operator = UNSET
        else:
            identification_operator = StringComparisonOperator(_identification_operator)

        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        _corporate_identity_number_operator = d.pop("corporateIdentityNumberOperator", UNSET)
        corporate_identity_number_operator: Union[Unset, StringComparisonOperator]
        if isinstance(_corporate_identity_number_operator, Unset):
            corporate_identity_number_operator = UNSET
        else:
            corporate_identity_number_operator = StringComparisonOperator(_corporate_identity_number_operator)

        _last_touched_at = d.pop("lastTouchedAt", UNSET)
        last_touched_at: Union[Unset, None, DateTimeFilterInterval]
        if _last_touched_at is None:
            last_touched_at = None
        elif isinstance(_last_touched_at, Unset):
            last_touched_at = UNSET
        else:
            last_touched_at = DateTimeFilterInterval.from_dict(_last_touched_at)

        _page_and_sort_by = d.pop("pageAndSortBy", UNSET)
        page_and_sort_by: Union[Unset, None, CompanyCustomerQuerySortPageAndSortByModel]
        if _page_and_sort_by is None:
            page_and_sort_by = None
        elif isinstance(_page_and_sort_by, Unset):
            page_and_sort_by = UNSET
        else:
            page_and_sort_by = CompanyCustomerQuerySortPageAndSortByModel.from_dict(_page_and_sort_by)

        search_company_customer_query_model = cls(
            name=name,
            name_operator=name_operator,
            identification=identification,
            identification_operator=identification_operator,
            corporate_identity_number=corporate_identity_number,
            corporate_identity_number_operator=corporate_identity_number_operator,
            last_touched_at=last_touched_at,
            page_and_sort_by=page_and_sort_by,
        )

        return search_company_customer_query_model
