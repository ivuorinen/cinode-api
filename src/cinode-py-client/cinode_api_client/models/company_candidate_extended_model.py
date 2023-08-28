import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_candidate_state import CompanyCandidateState
from ..models.user_gender import UserGender
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_candidate_attachment_model import CompanyCandidateAttachmentModel
    from ..models.company_user_base_model import CompanyUserBaseModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyCandidateExtendedModel")


@_attrs_define
class CompanyCandidateExtendedModel:
    """
    Attributes:
        rating (Union[Unset, None, int]):
        available_from_date (Union[Unset, None, datetime.datetime]):
        period_of_notice_days (Union[Unset, None, int]):
        salary_requirement (Union[Unset, None, int]):
        offered_salary (Union[Unset, None, int]):
        state (Union[Unset, None, CompanyCandidateState]):

            Öppen = 0

            Vunnen = 10

            Pausad = 20

            Avböjd av kandidat = 30

            Avböjd av oss = 40
        currency_id (Union[Unset, None, int]):
        is_mobile (Union[Unset, bool]):
        pipeline_id (Union[Unset, None, int]):
        pipeline_stage_id (Union[Unset, None, int]):
        recruitment_manager_id (Union[Unset, None, int]):
        campaign_code (Union[Unset, None, str]):
        gender (Union[Unset, UserGender]):

            Ej angiven = 0

            Man = 1

            Kvinna = 2
        birth_year (Union[Unset, None, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        linked_in_url (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        attachments (Union[Unset, None, List['CompanyCandidateAttachmentModel']]):
        recruitment_manager (Union[Unset, None, CompanyUserBaseModel]):
        current_employer (Union[Unset, None, str]):
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        seo_id (Union[Unset, None, str]):
        firstname (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        lastname (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        created_date_time (Union[Unset, datetime.datetime]):
        last_touch_date_time (Union[Unset, None, datetime.datetime]):
        updated_date_time (Union[Unset, None, datetime.datetime]):
        links (Union[Unset, None, List['Link']]):
    """

    rating: Union[Unset, None, int] = UNSET
    available_from_date: Union[Unset, None, datetime.datetime] = UNSET
    period_of_notice_days: Union[Unset, None, int] = UNSET
    salary_requirement: Union[Unset, None, int] = UNSET
    offered_salary: Union[Unset, None, int] = UNSET
    state: Union[Unset, None, CompanyCandidateState] = UNSET
    currency_id: Union[Unset, None, int] = UNSET
    is_mobile: Union[Unset, bool] = UNSET
    pipeline_id: Union[Unset, None, int] = UNSET
    pipeline_stage_id: Union[Unset, None, int] = UNSET
    recruitment_manager_id: Union[Unset, None, int] = UNSET
    campaign_code: Union[Unset, None, str] = UNSET
    gender: Union[Unset, UserGender] = UNSET
    birth_year: Union[Unset, None, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    linked_in_url: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    attachments: Union[Unset, None, List["CompanyCandidateAttachmentModel"]] = UNSET
    recruitment_manager: Union[Unset, None, "CompanyUserBaseModel"] = UNSET
    current_employer: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    firstname: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    lastname: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    last_touch_date_time: Union[Unset, None, datetime.datetime] = UNSET
    updated_date_time: Union[Unset, None, datetime.datetime] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rating = self.rating
        available_from_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.available_from_date, Unset):
            available_from_date = self.available_from_date.isoformat() if self.available_from_date else None

        period_of_notice_days = self.period_of_notice_days
        salary_requirement = self.salary_requirement
        offered_salary = self.offered_salary
        state: Union[Unset, None, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value if self.state else None

        currency_id = self.currency_id
        is_mobile = self.is_mobile
        pipeline_id = self.pipeline_id
        pipeline_stage_id = self.pipeline_stage_id
        recruitment_manager_id = self.recruitment_manager_id
        campaign_code = self.campaign_code
        gender: Union[Unset, int] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        birth_year = self.birth_year
        title = self.title
        description = self.description
        email = self.email
        linked_in_url = self.linked_in_url
        phone = self.phone
        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        recruitment_manager: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.recruitment_manager, Unset):
            recruitment_manager = self.recruitment_manager.to_dict() if self.recruitment_manager else None

        current_employer = self.current_employer
        id = self.id
        company_id = self.company_id
        seo_id = self.seo_id
        firstname = self.firstname
        first_name = self.first_name
        lastname = self.lastname
        last_name = self.last_name
        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        last_touch_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_touch_date_time, Unset):
            last_touch_date_time = self.last_touch_date_time.isoformat() if self.last_touch_date_time else None

        updated_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_date_time, Unset):
            updated_date_time = self.updated_date_time.isoformat() if self.updated_date_time else None

        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if rating is not UNSET:
            field_dict["rating"] = rating
        if available_from_date is not UNSET:
            field_dict["availableFromDate"] = available_from_date
        if period_of_notice_days is not UNSET:
            field_dict["periodOfNoticeDays"] = period_of_notice_days
        if salary_requirement is not UNSET:
            field_dict["salaryRequirement"] = salary_requirement
        if offered_salary is not UNSET:
            field_dict["offeredSalary"] = offered_salary
        if state is not UNSET:
            field_dict["state"] = state
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if is_mobile is not UNSET:
            field_dict["isMobile"] = is_mobile
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id
        if recruitment_manager_id is not UNSET:
            field_dict["recruitmentManagerId"] = recruitment_manager_id
        if campaign_code is not UNSET:
            field_dict["campaignCode"] = campaign_code
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
        if linked_in_url is not UNSET:
            field_dict["linkedInUrl"] = linked_in_url
        if phone is not UNSET:
            field_dict["phone"] = phone
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if recruitment_manager is not UNSET:
            field_dict["recruitmentManager"] = recruitment_manager
        if current_employer is not UNSET:
            field_dict["currentEmployer"] = current_employer
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if last_touch_date_time is not UNSET:
            field_dict["lastTouchDateTime"] = last_touch_date_time
        if updated_date_time is not UNSET:
            field_dict["updatedDateTime"] = updated_date_time
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_candidate_attachment_model import CompanyCandidateAttachmentModel
        from ..models.company_user_base_model import CompanyUserBaseModel
        from ..models.link import Link

        d = src_dict.copy()
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

        offered_salary = d.pop("offeredSalary", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, None, CompanyCandidateState]
        if _state is None:
            state = None
        elif isinstance(_state, Unset):
            state = UNSET
        else:
            state = CompanyCandidateState(_state)

        currency_id = d.pop("currencyId", UNSET)

        is_mobile = d.pop("isMobile", UNSET)

        pipeline_id = d.pop("pipelineId", UNSET)

        pipeline_stage_id = d.pop("pipelineStageId", UNSET)

        recruitment_manager_id = d.pop("recruitmentManagerId", UNSET)

        campaign_code = d.pop("campaignCode", UNSET)

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

        linked_in_url = d.pop("linkedInUrl", UNSET)

        phone = d.pop("phone", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = CompanyCandidateAttachmentModel.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        _recruitment_manager = d.pop("recruitmentManager", UNSET)
        recruitment_manager: Union[Unset, None, CompanyUserBaseModel]
        if _recruitment_manager is None:
            recruitment_manager = None
        elif isinstance(_recruitment_manager, Unset):
            recruitment_manager = UNSET
        else:
            recruitment_manager = CompanyUserBaseModel.from_dict(_recruitment_manager)

        current_employer = d.pop("currentEmployer", UNSET)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        seo_id = d.pop("seoId", UNSET)

        firstname = d.pop("firstname", UNSET)

        first_name = d.pop("firstName", UNSET)

        lastname = d.pop("lastname", UNSET)

        last_name = d.pop("lastName", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _last_touch_date_time = d.pop("lastTouchDateTime", UNSET)
        last_touch_date_time: Union[Unset, None, datetime.datetime]
        if _last_touch_date_time is None:
            last_touch_date_time = None
        elif isinstance(_last_touch_date_time, Unset):
            last_touch_date_time = UNSET
        else:
            last_touch_date_time = isoparse(_last_touch_date_time)

        _updated_date_time = d.pop("updatedDateTime", UNSET)
        updated_date_time: Union[Unset, None, datetime.datetime]
        if _updated_date_time is None:
            updated_date_time = None
        elif isinstance(_updated_date_time, Unset):
            updated_date_time = UNSET
        else:
            updated_date_time = isoparse(_updated_date_time)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_candidate_extended_model = cls(
            rating=rating,
            available_from_date=available_from_date,
            period_of_notice_days=period_of_notice_days,
            salary_requirement=salary_requirement,
            offered_salary=offered_salary,
            state=state,
            currency_id=currency_id,
            is_mobile=is_mobile,
            pipeline_id=pipeline_id,
            pipeline_stage_id=pipeline_stage_id,
            recruitment_manager_id=recruitment_manager_id,
            campaign_code=campaign_code,
            gender=gender,
            birth_year=birth_year,
            title=title,
            description=description,
            email=email,
            linked_in_url=linked_in_url,
            phone=phone,
            attachments=attachments,
            recruitment_manager=recruitment_manager,
            current_employer=current_employer,
            id=id,
            company_id=company_id,
            seo_id=seo_id,
            firstname=firstname,
            first_name=first_name,
            lastname=lastname,
            last_name=last_name,
            created_date_time=created_date_time,
            last_touch_date_time=last_touch_date_time,
            updated_date_time=updated_date_time,
            links=links,
        )

        return company_candidate_extended_model
