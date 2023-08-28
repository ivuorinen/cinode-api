import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_user_status import CompanyUserStatus
from ..models.user_gender import UserGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserAddModel")


@_attrs_define
class CompanyUserAddModel:
    """
    Attributes:
        email (str):
        first_name (str):
        last_name (str):
        password (str):
        confirm_password (str):
        gender (UserGender):

            Ej angiven = 0

            Man = 1

            Kvinna = 2
        status (Union[Unset, CompanyUserStatus]):

            Frånkopplad = 0

            Kommande = 2

            Aktiv = 3
        team_id (Union[Unset, None, int]):
        title (Union[Unset, None, str]):
        language_id (Union[Unset, None, int]):
        employment_number (Union[Unset, None, str]):
        employment_start_date (Union[Unset, None, datetime.datetime]):
        add_profile (Union[Unset, bool]):
        location_id (Union[Unset, None, int]):
        default_currency_id (Union[Unset, None, int]):
        display_currency_id (Union[Unset, None, int]):
        must_change_password (Union[Unset, bool]):
    """

    email: str
    first_name: str
    last_name: str
    password: str
    confirm_password: str
    gender: UserGender
    status: Union[Unset, CompanyUserStatus] = UNSET
    team_id: Union[Unset, None, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    language_id: Union[Unset, None, int] = UNSET
    employment_number: Union[Unset, None, str] = UNSET
    employment_start_date: Union[Unset, None, datetime.datetime] = UNSET
    add_profile: Union[Unset, bool] = UNSET
    location_id: Union[Unset, None, int] = UNSET
    default_currency_id: Union[Unset, None, int] = UNSET
    display_currency_id: Union[Unset, None, int] = UNSET
    must_change_password: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        password = self.password
        confirm_password = self.confirm_password
        gender = self.gender.value

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        team_id = self.team_id
        title = self.title
        language_id = self.language_id
        employment_number = self.employment_number
        employment_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.employment_start_date, Unset):
            employment_start_date = self.employment_start_date.isoformat() if self.employment_start_date else None

        add_profile = self.add_profile
        location_id = self.location_id
        default_currency_id = self.default_currency_id
        display_currency_id = self.display_currency_id
        must_change_password = self.must_change_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "password": password,
                "confirmPassword": confirm_password,
                "gender": gender,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if title is not UNSET:
            field_dict["title"] = title
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if employment_number is not UNSET:
            field_dict["employmentNumber"] = employment_number
        if employment_start_date is not UNSET:
            field_dict["employmentStartDate"] = employment_start_date
        if add_profile is not UNSET:
            field_dict["addProfile"] = add_profile
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if default_currency_id is not UNSET:
            field_dict["defaultCurrencyId"] = default_currency_id
        if display_currency_id is not UNSET:
            field_dict["displayCurrencyId"] = display_currency_id
        if must_change_password is not UNSET:
            field_dict["mustChangePassword"] = must_change_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        password = d.pop("password")

        confirm_password = d.pop("confirmPassword")

        gender = UserGender(d.pop("gender"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CompanyUserStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyUserStatus(_status)

        team_id = d.pop("teamId", UNSET)

        title = d.pop("title", UNSET)

        language_id = d.pop("languageId", UNSET)

        employment_number = d.pop("employmentNumber", UNSET)

        _employment_start_date = d.pop("employmentStartDate", UNSET)
        employment_start_date: Union[Unset, None, datetime.datetime]
        if _employment_start_date is None:
            employment_start_date = None
        elif isinstance(_employment_start_date, Unset):
            employment_start_date = UNSET
        else:
            employment_start_date = isoparse(_employment_start_date)

        add_profile = d.pop("addProfile", UNSET)

        location_id = d.pop("locationId", UNSET)

        default_currency_id = d.pop("defaultCurrencyId", UNSET)

        display_currency_id = d.pop("displayCurrencyId", UNSET)

        must_change_password = d.pop("mustChangePassword", UNSET)

        company_user_add_model = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            confirm_password=confirm_password,
            gender=gender,
            status=status,
            team_id=team_id,
            title=title,
            language_id=language_id,
            employment_number=employment_number,
            employment_start_date=employment_start_date,
            add_profile=add_profile,
            location_id=location_id,
            default_currency_id=default_currency_id,
            display_currency_id=display_currency_id,
            must_change_password=must_change_password,
        )

        return company_user_add_model
