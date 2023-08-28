from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abscence_period_day_model import AbscencePeriodDayModel


T = TypeVar("T", bound="AbsencePeriodModel")


@_attrs_define
class AbsencePeriodModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        company_user_id (Union[Unset, int]):
        absence_type_id (Union[Unset, int]):
        absence_type_name (Union[Unset, None, str]):
        id (Union[Unset, int]):
        days (Union[Unset, None, List['AbscencePeriodDayModel']]):
        extent_percentage (Union[Unset, int]):
    """

    company_id: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, int] = UNSET
    absence_type_id: Union[Unset, int] = UNSET
    absence_type_name: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    days: Union[Unset, None, List["AbscencePeriodDayModel"]] = UNSET
    extent_percentage: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        company_user_id = self.company_user_id
        absence_type_id = self.absence_type_id
        absence_type_name = self.absence_type_name
        id = self.id
        days: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.days, Unset):
            if self.days is None:
                days = None
            else:
                days = []
                for days_item_data in self.days:
                    days_item = days_item_data.to_dict()

                    days.append(days_item)

        extent_percentage = self.extent_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if absence_type_id is not UNSET:
            field_dict["absenceTypeId"] = absence_type_id
        if absence_type_name is not UNSET:
            field_dict["absenceTypeName"] = absence_type_name
        if id is not UNSET:
            field_dict["id"] = id
        if days is not UNSET:
            field_dict["days"] = days
        if extent_percentage is not UNSET:
            field_dict["extentPercentage"] = extent_percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.abscence_period_day_model import AbscencePeriodDayModel

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        absence_type_id = d.pop("absenceTypeId", UNSET)

        absence_type_name = d.pop("absenceTypeName", UNSET)

        id = d.pop("id", UNSET)

        days = []
        _days = d.pop("days", UNSET)
        for days_item_data in _days or []:
            days_item = AbscencePeriodDayModel.from_dict(days_item_data)

            days.append(days_item)

        extent_percentage = d.pop("extentPercentage", UNSET)

        absence_period_model = cls(
            company_id=company_id,
            company_user_id=company_user_id,
            absence_type_id=absence_type_id,
            absence_type_name=absence_type_name,
            id=id,
            days=days,
            extent_percentage=extent_percentage,
        )

        return absence_period_model
