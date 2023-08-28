import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_block_model import ImageBlockModel
    from ..models.location_block_model import LocationBlockModel
    from ..models.skill_block_item_model import SkillBlockItemModel


T = TypeVar("T", bound="WorkExperienceBlockItemModel")


@_attrs_define
class WorkExperienceBlockItemModel:
    """
    Attributes:
        skills (Union[Unset, None, List['SkillBlockItemModel']]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        employer (Union[Unset, None, str]):
        location (Union[Unset, None, LocationBlockModel]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        url (Union[Unset, None, str]):
        logotype (Union[Unset, None, ImageBlockModel]):
        parent_block_item_id (Union[Unset, None, int]):
        parent_block_item_updated (Union[Unset, None, bool]):
        profile_translation_id (Union[Unset, None, int]):
        updated (Union[Unset, None, datetime.datetime]):
        discarded (Union[Unset, None, datetime.datetime]):
        id (Union[Unset, str]):
        disabled (Union[Unset, bool]):
    """

    skills: Union[Unset, None, List["SkillBlockItemModel"]] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    employer: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, "LocationBlockModel"] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    url: Union[Unset, None, str] = UNSET
    logotype: Union[Unset, None, "ImageBlockModel"] = UNSET
    parent_block_item_id: Union[Unset, None, int] = UNSET
    parent_block_item_updated: Union[Unset, None, bool] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    discarded: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        skills: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skills, Unset):
            if self.skills is None:
                skills = None
            else:
                skills = []
                for skills_item_data in self.skills:
                    skills_item = skills_item_data.to_dict()

                    skills.append(skills_item)

        title = self.title
        description = self.description
        employer = self.employer
        location: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict() if self.location else None

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        url = self.url
        logotype: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.logotype, Unset):
            logotype = self.logotype.to_dict() if self.logotype else None

        parent_block_item_id = self.parent_block_item_id
        parent_block_item_updated = self.parent_block_item_updated
        profile_translation_id = self.profile_translation_id
        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        discarded: Union[Unset, None, str] = UNSET
        if not isinstance(self.discarded, Unset):
            discarded = self.discarded.isoformat() if self.discarded else None

        id = self.id
        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if skills is not UNSET:
            field_dict["skills"] = skills
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if employer is not UNSET:
            field_dict["employer"] = employer
        if location is not UNSET:
            field_dict["location"] = location
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if url is not UNSET:
            field_dict["url"] = url
        if logotype is not UNSET:
            field_dict["logotype"] = logotype
        if parent_block_item_id is not UNSET:
            field_dict["parentBlockItemId"] = parent_block_item_id
        if parent_block_item_updated is not UNSET:
            field_dict["parentBlockItemUpdated"] = parent_block_item_updated
        if profile_translation_id is not UNSET:
            field_dict["profileTranslationId"] = profile_translation_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if discarded is not UNSET:
            field_dict["discarded"] = discarded
        if id is not UNSET:
            field_dict["id"] = id
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_block_model import ImageBlockModel
        from ..models.location_block_model import LocationBlockModel
        from ..models.skill_block_item_model import SkillBlockItemModel

        d = src_dict.copy()
        skills = []
        _skills = d.pop("skills", UNSET)
        for skills_item_data in _skills or []:
            skills_item = SkillBlockItemModel.from_dict(skills_item_data)

            skills.append(skills_item)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        employer = d.pop("employer", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, None, LocationBlockModel]
        if _location is None:
            location = None
        elif isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationBlockModel.from_dict(_location)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        url = d.pop("url", UNSET)

        _logotype = d.pop("logotype", UNSET)
        logotype: Union[Unset, None, ImageBlockModel]
        if _logotype is None:
            logotype = None
        elif isinstance(_logotype, Unset):
            logotype = UNSET
        else:
            logotype = ImageBlockModel.from_dict(_logotype)

        parent_block_item_id = d.pop("parentBlockItemId", UNSET)

        parent_block_item_updated = d.pop("parentBlockItemUpdated", UNSET)

        profile_translation_id = d.pop("profileTranslationId", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, datetime.datetime]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _discarded = d.pop("discarded", UNSET)
        discarded: Union[Unset, None, datetime.datetime]
        if _discarded is None:
            discarded = None
        elif isinstance(_discarded, Unset):
            discarded = UNSET
        else:
            discarded = isoparse(_discarded)

        id = d.pop("id", UNSET)

        disabled = d.pop("disabled", UNSET)

        work_experience_block_item_model = cls(
            skills=skills,
            title=title,
            description=description,
            employer=employer,
            location=location,
            start_date=start_date,
            end_date=end_date,
            url=url,
            logotype=logotype,
            parent_block_item_id=parent_block_item_id,
            parent_block_item_updated=parent_block_item_updated,
            profile_translation_id=profile_translation_id,
            updated=updated,
            discarded=discarded,
            id=id,
            disabled=disabled,
        )

        return work_experience_block_item_model
