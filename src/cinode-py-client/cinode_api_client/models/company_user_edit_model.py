import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_user_status import CompanyUserStatus
from ..models.user_gender import UserGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserEditModel")


@_attrs_define
class CompanyUserEditModel:
    """
    Attributes:
        status (Union[Unset, CompanyUserStatus]):

            Frånkopplad = 0

            Kommande = 2

            Aktiv = 3
        employment_start_date (Union[Unset, None, datetime.datetime]):
        employment_end_date (Union[Unset, None, datetime.datetime]):
        employment_number (Union[Unset, None, str]):
        invoicing_goal (Union[Unset, None, int]):
        mobility (Union[Unset, None, int]):
        availability_percent (Union[Unset, None, int]):
        available_from_date (Union[Unset, None, datetime.datetime]):
        title (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        tax_table (Union[Unset, None, str]):
        base_salary (Union[Unset, None, int]):
        provision (Union[Unset, None, int]):
        hourly_target_rate (Union[Unset, None, int]):
        self_cost (Union[Unset, None, int]):
        location_id (Union[Unset, None, int]):
        default_currency_id (Union[Unset, None, int]):
        display_currency_id (Union[Unset, None, int]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        date_of_birth (Union[Unset, None, datetime.datetime]):
        gender (Union[Unset, UserGender]):

            Ej angiven = 0

            Man = 1

            Kvinna = 2
        company_calendar_id (Union[Unset, None, int]):
        timezone_id (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
    """

    status: Union[Unset, CompanyUserStatus] = UNSET
    employment_start_date: Union[Unset, None, datetime.datetime] = UNSET
    employment_end_date: Union[Unset, None, datetime.datetime] = UNSET
    employment_number: Union[Unset, None, str] = UNSET
    invoicing_goal: Union[Unset, None, int] = UNSET
    mobility: Union[Unset, None, int] = UNSET
    availability_percent: Union[Unset, None, int] = UNSET
    available_from_date: Union[Unset, None, datetime.datetime] = UNSET
    title: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    tax_table: Union[Unset, None, str] = UNSET
    base_salary: Union[Unset, None, int] = UNSET
    provision: Union[Unset, None, int] = UNSET
    hourly_target_rate: Union[Unset, None, int] = UNSET
    self_cost: Union[Unset, None, int] = UNSET
    location_id: Union[Unset, None, int] = UNSET
    default_currency_id: Union[Unset, None, int] = UNSET
    display_currency_id: Union[Unset, None, int] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    date_of_birth: Union[Unset, None, datetime.datetime] = UNSET
    gender: Union[Unset, UserGender] = UNSET
    company_calendar_id: Union[Unset, None, int] = UNSET
    timezone_id: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        employment_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.employment_start_date, Unset):
            employment_start_date = self.employment_start_date.isoformat() if self.employment_start_date else None

        employment_end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.employment_end_date, Unset):
            employment_end_date = self.employment_end_date.isoformat() if self.employment_end_date else None

        employment_number = self.employment_number
        invoicing_goal = self.invoicing_goal
        mobility = self.mobility
        availability_percent = self.availability_percent
        available_from_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.available_from_date, Unset):
            available_from_date = self.available_from_date.isoformat() if self.available_from_date else None

        title = self.title
        email = self.email
        tax_table = self.tax_table
        base_salary = self.base_salary
        provision = self.provision
        hourly_target_rate = self.hourly_target_rate
        self_cost = self.self_cost
        location_id = self.location_id
        default_currency_id = self.default_currency_id
        display_currency_id = self.display_currency_id
        first_name = self.first_name
        last_name = self.last_name
        date_of_birth: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat() if self.date_of_birth else None

        gender: Union[Unset, int] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        company_calendar_id = self.company_calendar_id
        timezone_id = self.timezone_id
        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if employment_start_date is not UNSET:
            field_dict["employmentStartDate"] = employment_start_date
        if employment_end_date is not UNSET:
            field_dict["employmentEndDate"] = employment_end_date
        if employment_number is not UNSET:
            field_dict["employmentNumber"] = employment_number
        if invoicing_goal is not UNSET:
            field_dict["invoicingGoal"] = invoicing_goal
        if mobility is not UNSET:
            field_dict["mobility"] = mobility
        if availability_percent is not UNSET:
            field_dict["availabilityPercent"] = availability_percent
        if available_from_date is not UNSET:
            field_dict["availableFromDate"] = available_from_date
        if title is not UNSET:
            field_dict["title"] = title
        if email is not UNSET:
            field_dict["email"] = email
        if tax_table is not UNSET:
            field_dict["taxTable"] = tax_table
        if base_salary is not UNSET:
            field_dict["baseSalary"] = base_salary
        if provision is not UNSET:
            field_dict["provision"] = provision
        if hourly_target_rate is not UNSET:
            field_dict["hourlyTargetRate"] = hourly_target_rate
        if self_cost is not UNSET:
            field_dict["selfCost"] = self_cost
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if default_currency_id is not UNSET:
            field_dict["defaultCurrencyId"] = default_currency_id
        if display_currency_id is not UNSET:
            field_dict["displayCurrencyId"] = display_currency_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if gender is not UNSET:
            field_dict["gender"] = gender
        if company_calendar_id is not UNSET:
            field_dict["companyCalendarId"] = company_calendar_id
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, CompanyUserStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyUserStatus(_status)

        _employment_start_date = d.pop("employmentStartDate", UNSET)
        employment_start_date: Union[Unset, None, datetime.datetime]
        if _employment_start_date is None:
            employment_start_date = None
        elif isinstance(_employment_start_date, Unset):
            employment_start_date = UNSET
        else:
            employment_start_date = isoparse(_employment_start_date)

        _employment_end_date = d.pop("employmentEndDate", UNSET)
        employment_end_date: Union[Unset, None, datetime.datetime]
        if _employment_end_date is None:
            employment_end_date = None
        elif isinstance(_employment_end_date, Unset):
            employment_end_date = UNSET
        else:
            employment_end_date = isoparse(_employment_end_date)

        employment_number = d.pop("employmentNumber", UNSET)

        invoicing_goal = d.pop("invoicingGoal", UNSET)

        mobility = d.pop("mobility", UNSET)

        availability_percent = d.pop("availabilityPercent", UNSET)

        _available_from_date = d.pop("availableFromDate", UNSET)
        available_from_date: Union[Unset, None, datetime.datetime]
        if _available_from_date is None:
            available_from_date = None
        elif isinstance(_available_from_date, Unset):
            available_from_date = UNSET
        else:
            available_from_date = isoparse(_available_from_date)

        title = d.pop("title", UNSET)

        email = d.pop("email", UNSET)

        tax_table = d.pop("taxTable", UNSET)

        base_salary = d.pop("baseSalary", UNSET)

        provision = d.pop("provision", UNSET)

        hourly_target_rate = d.pop("hourlyTargetRate", UNSET)

        self_cost = d.pop("selfCost", UNSET)

        location_id = d.pop("locationId", UNSET)

        default_currency_id = d.pop("defaultCurrencyId", UNSET)

        display_currency_id = d.pop("displayCurrencyId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, None, datetime.datetime]
        if _date_of_birth is None:
            date_of_birth = None
        elif isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, UserGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = UserGender(_gender)

        company_calendar_id = d.pop("companyCalendarId", UNSET)

        timezone_id = d.pop("timezoneId", UNSET)

        phone = d.pop("phone", UNSET)

        company_user_edit_model = cls(
            status=status,
            employment_start_date=employment_start_date,
            employment_end_date=employment_end_date,
            employment_number=employment_number,
            invoicing_goal=invoicing_goal,
            mobility=mobility,
            availability_percent=availability_percent,
            available_from_date=available_from_date,
            title=title,
            email=email,
            tax_table=tax_table,
            base_salary=base_salary,
            provision=provision,
            hourly_target_rate=hourly_target_rate,
            self_cost=self_cost,
            location_id=location_id,
            default_currency_id=default_currency_id,
            display_currency_id=display_currency_id,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            company_calendar_id=company_calendar_id,
            timezone_id=timezone_id,
            phone=phone,
        )

        return company_user_edit_model
