from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.user_gender import UserGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserSubcontractorAddEditModel")


@_attrs_define
class CompanyUserSubcontractorAddEditModel:
    """
    Attributes:
        first_name (str):
        last_name (str):
        email (str):
        password (str):
        password_confirm (str):
        gender (UserGender):

            Ej angiven = 0

            Man = 1

            Kvinna = 2
        language_id (int):
        title (Union[Unset, None, str]):
        profile_language_id (Union[Unset, None, int]):
        create_profile (Union[Unset, bool]):
        tariff (Union[Unset, None, int]):
        phone (Union[Unset, None, str]):
        currency_id (Union[Unset, None, int]):
        company_calendar_id (Union[Unset, None, int]):
        company_address_id (Union[Unset, None, int]):
        company_name (Union[Unset, None, str]):
        company_identifier (Union[Unset, None, str]):
        internal_identifier (Union[Unset, None, str]):
        linked_in (Union[Unset, None, str]):
        rating (Union[Unset, None, int]):
    """

    first_name: str
    last_name: str
    email: str
    password: str
    password_confirm: str
    gender: UserGender
    language_id: int
    title: Union[Unset, None, str] = UNSET
    profile_language_id: Union[Unset, None, int] = UNSET
    create_profile: Union[Unset, bool] = UNSET
    tariff: Union[Unset, None, int] = UNSET
    phone: Union[Unset, None, str] = UNSET
    currency_id: Union[Unset, None, int] = UNSET
    company_calendar_id: Union[Unset, None, int] = UNSET
    company_address_id: Union[Unset, None, int] = UNSET
    company_name: Union[Unset, None, str] = UNSET
    company_identifier: Union[Unset, None, str] = UNSET
    internal_identifier: Union[Unset, None, str] = UNSET
    linked_in: Union[Unset, None, str] = UNSET
    rating: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        password = self.password
        password_confirm = self.password_confirm
        gender = self.gender.value

        language_id = self.language_id
        title = self.title
        profile_language_id = self.profile_language_id
        create_profile = self.create_profile
        tariff = self.tariff
        phone = self.phone
        currency_id = self.currency_id
        company_calendar_id = self.company_calendar_id
        company_address_id = self.company_address_id
        company_name = self.company_name
        company_identifier = self.company_identifier
        internal_identifier = self.internal_identifier
        linked_in = self.linked_in
        rating = self.rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "password": password,
                "passwordConfirm": password_confirm,
                "gender": gender,
                "languageId": language_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if profile_language_id is not UNSET:
            field_dict["profileLanguageId"] = profile_language_id
        if create_profile is not UNSET:
            field_dict["createProfile"] = create_profile
        if tariff is not UNSET:
            field_dict["tariff"] = tariff
        if phone is not UNSET:
            field_dict["phone"] = phone
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if company_calendar_id is not UNSET:
            field_dict["companyCalendarId"] = company_calendar_id
        if company_address_id is not UNSET:
            field_dict["companyAddressId"] = company_address_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_identifier is not UNSET:
            field_dict["companyIdentifier"] = company_identifier
        if internal_identifier is not UNSET:
            field_dict["internalIdentifier"] = internal_identifier
        if linked_in is not UNSET:
            field_dict["linkedIn"] = linked_in
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email")

        password = d.pop("password")

        password_confirm = d.pop("passwordConfirm")

        gender = UserGender(d.pop("gender"))

        language_id = d.pop("languageId")

        title = d.pop("title", UNSET)

        profile_language_id = d.pop("profileLanguageId", UNSET)

        create_profile = d.pop("createProfile", UNSET)

        tariff = d.pop("tariff", UNSET)

        phone = d.pop("phone", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        company_calendar_id = d.pop("companyCalendarId", UNSET)

        company_address_id = d.pop("companyAddressId", UNSET)

        company_name = d.pop("companyName", UNSET)

        company_identifier = d.pop("companyIdentifier", UNSET)

        internal_identifier = d.pop("internalIdentifier", UNSET)

        linked_in = d.pop("linkedIn", UNSET)

        rating = d.pop("rating", UNSET)

        company_user_subcontractor_add_edit_model = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            password_confirm=password_confirm,
            gender=gender,
            language_id=language_id,
            title=title,
            profile_language_id=profile_language_id,
            create_profile=create_profile,
            tariff=tariff,
            phone=phone,
            currency_id=currency_id,
            company_calendar_id=company_calendar_id,
            company_address_id=company_address_id,
            company_name=company_name,
            company_identifier=company_identifier,
            internal_identifier=internal_identifier,
            linked_in=linked_in,
            rating=rating,
        )

        return company_user_subcontractor_add_edit_model
