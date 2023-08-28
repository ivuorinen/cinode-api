import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_candidate_state import CompanyCandidateState
from ..models.user_gender import UserGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCandidateAddModel")


@_attrs_define
class CompanyCandidateAddModel:
    """
    Attributes:
        first_name (str):
        last_name (str):
        state (CompanyCandidateState):

            Öppen = 0

            Vunnen = 10

            Pausad = 20

            Avböjd av kandidat = 30

            Avböjd av oss = 40
        gender (Union[Unset, UserGender]):

            Ej angiven = 0

            Man = 1

            Kvinna = 2
        birth_year (Union[Unset, None, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        linked_in_url (Union[Unset, None, str]):
        rating (Union[Unset, None, int]):
        available_from_date (Union[Unset, None, datetime.datetime]):
        period_of_notice_days (Union[Unset, None, int]):
        salary_requirement (Union[Unset, None, int]):
        is_mobile (Union[Unset, bool]):
        recruitment_manager_id (Union[Unset, None, int]):
        pipeline_id (Union[Unset, None, int]):
        pipeline_stage_id (Union[Unset, None, int]):
        team_id (Union[Unset, None, int]):
        company_address_id (Union[Unset, None, int]):
        recruitment_source_id (Union[Unset, None, int]):
        current_employer (Union[Unset, None, str]):
        campaign_code (Union[Unset, None, str]):
        currency_id (Union[Unset, None, int]):
        offered_salary (Union[Unset, None, int]):
        notify_recruitment_manager (Union[Unset, bool]):
    """

    first_name: str
    last_name: str
    state: CompanyCandidateState
    gender: Union[Unset, UserGender] = UNSET
    birth_year: Union[Unset, None, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    linked_in_url: Union[Unset, None, str] = UNSET
    rating: Union[Unset, None, int] = UNSET
    available_from_date: Union[Unset, None, datetime.datetime] = UNSET
    period_of_notice_days: Union[Unset, None, int] = UNSET
    salary_requirement: Union[Unset, None, int] = UNSET
    is_mobile: Union[Unset, bool] = UNSET
    recruitment_manager_id: Union[Unset, None, int] = UNSET
    pipeline_id: Union[Unset, None, int] = UNSET
    pipeline_stage_id: Union[Unset, None, int] = UNSET
    team_id: Union[Unset, None, int] = UNSET
    company_address_id: Union[Unset, None, int] = UNSET
    recruitment_source_id: Union[Unset, None, int] = UNSET
    current_employer: Union[Unset, None, str] = UNSET
    campaign_code: Union[Unset, None, str] = UNSET
    currency_id: Union[Unset, None, int] = UNSET
    offered_salary: Union[Unset, None, int] = UNSET
    notify_recruitment_manager: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        state = self.state.value

        gender: Union[Unset, int] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        birth_year = self.birth_year
        title = self.title
        description = self.description
        email = self.email
        phone = self.phone
        linked_in_url = self.linked_in_url
        rating = self.rating
        available_from_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.available_from_date, Unset):
            available_from_date = self.available_from_date.isoformat() if self.available_from_date else None

        period_of_notice_days = self.period_of_notice_days
        salary_requirement = self.salary_requirement
        is_mobile = self.is_mobile
        recruitment_manager_id = self.recruitment_manager_id
        pipeline_id = self.pipeline_id
        pipeline_stage_id = self.pipeline_stage_id
        team_id = self.team_id
        company_address_id = self.company_address_id
        recruitment_source_id = self.recruitment_source_id
        current_employer = self.current_employer
        campaign_code = self.campaign_code
        currency_id = self.currency_id
        offered_salary = self.offered_salary
        notify_recruitment_manager = self.notify_recruitment_manager

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "state": state,
            }
        )
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birth_year is not UNSET:
            field_dict["birthYear"] = birth_year
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if linked_in_url is not UNSET:
            field_dict["linkedInUrl"] = linked_in_url
        if rating is not UNSET:
            field_dict["rating"] = rating
        if available_from_date is not UNSET:
            field_dict["availableFromDate"] = available_from_date
        if period_of_notice_days is not UNSET:
            field_dict["periodOfNoticeDays"] = period_of_notice_days
        if salary_requirement is not UNSET:
            field_dict["salaryRequirement"] = salary_requirement
        if is_mobile is not UNSET:
            field_dict["isMobile"] = is_mobile
        if recruitment_manager_id is not UNSET:
            field_dict["recruitmentManagerId"] = recruitment_manager_id
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if company_address_id is not UNSET:
            field_dict["companyAddressId"] = company_address_id
        if recruitment_source_id is not UNSET:
            field_dict["recruitmentSourceId"] = recruitment_source_id
        if current_employer is not UNSET:
            field_dict["currentEmployer"] = current_employer
        if campaign_code is not UNSET:
            field_dict["campaignCode"] = campaign_code
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if offered_salary is not UNSET:
            field_dict["offeredSalary"] = offered_salary
        if notify_recruitment_manager is not UNSET:
            field_dict["notifyRecruitmentManager"] = notify_recruitment_manager

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        state = CompanyCandidateState(d.pop("state"))

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, UserGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = UserGender(_gender)

        birth_year = d.pop("birthYear", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        linked_in_url = d.pop("linkedInUrl", UNSET)

        rating = d.pop("rating", UNSET)

        _available_from_date = d.pop("availableFromDate", UNSET)
        available_from_date: Union[Unset, None, datetime.datetime]
        if _available_from_date is None:
            available_from_date = None
        elif isinstance(_available_from_date, Unset):
            available_from_date = UNSET
        else:
            available_from_date = isoparse(_available_from_date)

        period_of_notice_days = d.pop("periodOfNoticeDays", UNSET)

        salary_requirement = d.pop("salaryRequirement", UNSET)

        is_mobile = d.pop("isMobile", UNSET)

        recruitment_manager_id = d.pop("recruitmentManagerId", UNSET)

        pipeline_id = d.pop("pipelineId", UNSET)

        pipeline_stage_id = d.pop("pipelineStageId", UNSET)

        team_id = d.pop("teamId", UNSET)

        company_address_id = d.pop("companyAddressId", UNSET)

        recruitment_source_id = d.pop("recruitmentSourceId", UNSET)

        current_employer = d.pop("currentEmployer", UNSET)

        campaign_code = d.pop("campaignCode", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        offered_salary = d.pop("offeredSalary", UNSET)

        notify_recruitment_manager = d.pop("notifyRecruitmentManager", UNSET)

        company_candidate_add_model = cls(
            first_name=first_name,
            last_name=last_name,
            state=state,
            gender=gender,
            birth_year=birth_year,
            title=title,
            description=description,
            email=email,
            phone=phone,
            linked_in_url=linked_in_url,
            rating=rating,
            available_from_date=available_from_date,
            period_of_notice_days=period_of_notice_days,
            salary_requirement=salary_requirement,
            is_mobile=is_mobile,
            recruitment_manager_id=recruitment_manager_id,
            pipeline_id=pipeline_id,
            pipeline_stage_id=pipeline_stage_id,
            team_id=team_id,
            company_address_id=company_address_id,
            recruitment_source_id=recruitment_source_id,
            current_employer=current_employer,
            campaign_code=campaign_code,
            currency_id=currency_id,
            offered_salary=offered_salary,
            notify_recruitment_manager=notify_recruitment_manager,
        )

        return company_candidate_add_model
