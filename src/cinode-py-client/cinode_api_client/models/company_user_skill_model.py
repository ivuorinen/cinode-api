import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_model import KeywordModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserSkillModel")


@_attrs_define
class CompanyUserSkillModel:
    """
    Attributes:
        company_id (Union[Unset, int]):
        company_user_id (Union[Unset, int]):
        number_of_days_work_experience (Union[Unset, int]):
        profile_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        level (Union[Unset, None, int]):
        level_goal (Union[Unset, None, int]):
        level_goal_deadline (Union[Unset, None, datetime.datetime]):
        keyword (Union[Unset, None, KeywordModel]):
        favourite (Union[Unset, bool]):
        links (Union[Unset, None, List['Link']]):
    """

    company_id: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, int] = UNSET
    number_of_days_work_experience: Union[Unset, int] = UNSET
    profile_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    level: Union[Unset, None, int] = UNSET
    level_goal: Union[Unset, None, int] = UNSET
    level_goal_deadline: Union[Unset, None, datetime.datetime] = UNSET
    keyword: Union[Unset, None, "KeywordModel"] = UNSET
    favourite: Union[Unset, bool] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        company_user_id = self.company_user_id
        number_of_days_work_experience = self.number_of_days_work_experience
        profile_id = self.profile_id
        id = self.id
        level = self.level
        level_goal = self.level_goal
        level_goal_deadline: Union[Unset, None, str] = UNSET
        if not isinstance(self.level_goal_deadline, Unset):
            level_goal_deadline = self.level_goal_deadline.isoformat() if self.level_goal_deadline else None

        keyword: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict() if self.keyword else None

        favourite = self.favourite
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
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if number_of_days_work_experience is not UNSET:
            field_dict["numberOfDaysWorkExperience"] = number_of_days_work_experience
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if id is not UNSET:
            field_dict["id"] = id
        if level is not UNSET:
            field_dict["level"] = level
        if level_goal is not UNSET:
            field_dict["levelGoal"] = level_goal
        if level_goal_deadline is not UNSET:
            field_dict["levelGoalDeadline"] = level_goal_deadline
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if favourite is not UNSET:
            field_dict["favourite"] = favourite
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyword_model import KeywordModel
        from ..models.link import Link

        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        number_of_days_work_experience = d.pop("numberOfDaysWorkExperience", UNSET)

        profile_id = d.pop("profileId", UNSET)

        id = d.pop("id", UNSET)

        level = d.pop("level", UNSET)

        level_goal = d.pop("levelGoal", UNSET)

        _level_goal_deadline = d.pop("levelGoalDeadline", UNSET)
        level_goal_deadline: Union[Unset, None, datetime.datetime]
        if _level_goal_deadline is None:
            level_goal_deadline = None
        elif isinstance(_level_goal_deadline, Unset):
            level_goal_deadline = UNSET
        else:
            level_goal_deadline = isoparse(_level_goal_deadline)

        _keyword = d.pop("keyword", UNSET)
        keyword: Union[Unset, None, KeywordModel]
        if _keyword is None:
            keyword = None
        elif isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = KeywordModel.from_dict(_keyword)

        favourite = d.pop("favourite", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_skill_model = cls(
            company_id=company_id,
            company_user_id=company_user_id,
            number_of_days_work_experience=number_of_days_work_experience,
            profile_id=profile_id,
            id=id,
            level=level,
            level_goal=level_goal,
            level_goal_deadline=level_goal_deadline,
            keyword=keyword,
            favourite=favourite,
            links=links,
        )

        return company_user_skill_model
