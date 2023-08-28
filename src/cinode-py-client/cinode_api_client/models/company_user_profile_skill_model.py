import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_skill_history_model import CompanyUserProfileSkillHistoryModel
    from ..models.company_user_profile_skill_translation_model import CompanyUserProfileSkillTranslationModel
    from ..models.keyword_model import KeywordModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserProfileSkillModel")


@_attrs_define
class CompanyUserProfileSkillModel:
    """
    Attributes:
        profile_id (Union[Unset, None, int]):
        level (Union[Unset, None, int]):
        level_goal (Union[Unset, None, int]):
        level_goal_deadline (Union[Unset, None, datetime.datetime]):
        keyword (Union[Unset, None, KeywordModel]):
        change_history (Union[Unset, None, List['CompanyUserProfileSkillHistoryModel']]):
        translations (Union[Unset, None, List['CompanyUserProfileSkillTranslationModel']]):
        favourite (Union[Unset, bool]):
        number_of_days_work_experience (Union[Unset, int]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        url (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    profile_id: Union[Unset, None, int] = UNSET
    level: Union[Unset, None, int] = UNSET
    level_goal: Union[Unset, None, int] = UNSET
    level_goal_deadline: Union[Unset, None, datetime.datetime] = UNSET
    keyword: Union[Unset, None, "KeywordModel"] = UNSET
    change_history: Union[Unset, None, List["CompanyUserProfileSkillHistoryModel"]] = UNSET
    translations: Union[Unset, None, List["CompanyUserProfileSkillTranslationModel"]] = UNSET
    favourite: Union[Unset, bool] = UNSET
    number_of_days_work_experience: Union[Unset, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_id = self.profile_id
        level = self.level
        level_goal = self.level_goal
        level_goal_deadline: Union[Unset, None, str] = UNSET
        if not isinstance(self.level_goal_deadline, Unset):
            level_goal_deadline = self.level_goal_deadline.isoformat() if self.level_goal_deadline else None

        keyword: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict() if self.keyword else None

        change_history: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.change_history, Unset):
            if self.change_history is None:
                change_history = None
            else:
                change_history = []
                for change_history_item_data in self.change_history:
                    change_history_item = change_history_item_data.to_dict()

                    change_history.append(change_history_item)

        translations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            if self.translations is None:
                translations = None
            else:
                translations = []
                for translations_item_data in self.translations:
                    translations_item = translations_item_data.to_dict()

                    translations.append(translations_item)

        favourite = self.favourite
        number_of_days_work_experience = self.number_of_days_work_experience
        company_id = self.company_id
        company_user_id = self.company_user_id
        id = self.id
        url = self.url
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
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if level is not UNSET:
            field_dict["level"] = level
        if level_goal is not UNSET:
            field_dict["levelGoal"] = level_goal
        if level_goal_deadline is not UNSET:
            field_dict["levelGoalDeadline"] = level_goal_deadline
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if change_history is not UNSET:
            field_dict["changeHistory"] = change_history
        if translations is not UNSET:
            field_dict["translations"] = translations
        if favourite is not UNSET:
            field_dict["favourite"] = favourite
        if number_of_days_work_experience is not UNSET:
            field_dict["numberOfDaysWorkExperience"] = number_of_days_work_experience
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_skill_history_model import CompanyUserProfileSkillHistoryModel
        from ..models.company_user_profile_skill_translation_model import CompanyUserProfileSkillTranslationModel
        from ..models.keyword_model import KeywordModel
        from ..models.link import Link

        d = src_dict.copy()
        profile_id = d.pop("profileId", UNSET)

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

        change_history = []
        _change_history = d.pop("changeHistory", UNSET)
        for change_history_item_data in _change_history or []:
            change_history_item = CompanyUserProfileSkillHistoryModel.from_dict(change_history_item_data)

            change_history.append(change_history_item)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CompanyUserProfileSkillTranslationModel.from_dict(translations_item_data)

            translations.append(translations_item)

        favourite = d.pop("favourite", UNSET)

        number_of_days_work_experience = d.pop("numberOfDaysWorkExperience", UNSET)

        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_profile_skill_model = cls(
            profile_id=profile_id,
            level=level,
            level_goal=level_goal,
            level_goal_deadline=level_goal_deadline,
            keyword=keyword,
            change_history=change_history,
            translations=translations,
            favourite=favourite,
            number_of_days_work_experience=number_of_days_work_experience,
            company_id=company_id,
            company_user_id=company_user_id,
            id=id,
            url=url,
            links=links,
        )

        return company_user_profile_skill_model
