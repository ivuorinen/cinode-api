import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.save_to_api_option import SaveToApiOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_work_experience_skill_add_model import (
        CompanyUserProfileWorkExperienceSkillAddModel,
    )
    from ..models.location_model import LocationModel


T = TypeVar("T", bound="CompanyUserProfileWorkExperienceAddEditModel")


@_attrs_define
class CompanyUserProfileWorkExperienceAddEditModel:
    """
    Attributes:
        title (str):
        description (str):
        employer (str):
        start_date (datetime.datetime):
        end_date (Union[Unset, None, datetime.datetime]):
        is_current (Union[Unset, None, bool]):
        location (Union[Unset, None, LocationModel]):
        url (Union[Unset, None, str]):
        skills (Union[Unset, None, List['CompanyUserProfileWorkExperienceSkillAddModel']]):
        save_to (Union[Unset, SaveToApiOption]):

            AllResumesOfLanguage = 3

            Profile = 5
    """

    title: str
    description: str
    employer: str
    start_date: datetime.datetime
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    is_current: Union[Unset, None, bool] = UNSET
    location: Union[Unset, None, "LocationModel"] = UNSET
    url: Union[Unset, None, str] = UNSET
    skills: Union[Unset, None, List["CompanyUserProfileWorkExperienceSkillAddModel"]] = UNSET
    save_to: Union[Unset, SaveToApiOption] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        employer = self.employer
        start_date = self.start_date.isoformat()

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        is_current = self.is_current
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        url = self.url
        skills: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skills, Unset):
            if self.skills is None:
                skills = None
            else:
                skills = []
                for skills_item_data in self.skills:
                    skills_item = skills_item_data.to_dict()

                    skills.append(skills_item)

        save_to: Union[Unset, int] = UNSET
        if not isinstance(self.save_to, Unset):
            save_to = self.save_to.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
                "description": description,
                "employer": employer,
                "startDate": start_date,
            }
        )
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current
        if location is not UNSET:
            field_dict["location"] = location
        if url is not UNSET:
            field_dict["url"] = url
        if skills is not UNSET:
            field_dict["skills"] = skills
        if save_to is not UNSET:
            field_dict["saveTo"] = save_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_work_experience_skill_add_model import (
            CompanyUserProfileWorkExperienceSkillAddModel,
        )
        from ..models.location_model import LocationModel

        d = src_dict.copy()
        title = d.pop("title")

        description = d.pop("description")

        employer = d.pop("employer")

        start_date = isoparse(d.pop("startDate"))

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        is_current = d.pop("isCurrent", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, LocationModel]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationModel.from_dict(_location)

        url = d.pop("url", UNSET)

        skills = []
        _skills = d.pop("skills", UNSET)
        for skills_item_data in _skills or []:
            skills_item = CompanyUserProfileWorkExperienceSkillAddModel.from_dict(skills_item_data)

            skills.append(skills_item)

        _save_to = d.pop("saveTo", UNSET)
        save_to: Union[Unset, SaveToApiOption]
        if isinstance(_save_to, Unset):
            save_to = UNSET
        else:
            save_to = SaveToApiOption(_save_to)

        company_user_profile_work_experience_add_edit_model = cls(
            title=title,
            description=description,
            employer=employer,
            start_date=start_date,
            end_date=end_date,
            is_current=is_current,
            location=location,
            url=url,
            skills=skills,
            save_to=save_to,
        )

        return company_user_profile_work_experience_add_edit_model
