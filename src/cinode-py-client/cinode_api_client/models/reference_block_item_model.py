import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceBlockItemModel")


@_attrs_define
class ReferenceBlockItemModel:
    """
    Attributes:
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        telephone (Union[Unset, None, str]):
        company (Union[Unset, None, str]):
        position (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        work_experience (Union[Unset, None, str]):
        work_experience_id (Union[Unset, None, int]):
        parent_block_item_id (Union[Unset, None, int]):
        parent_block_item_updated (Union[Unset, None, bool]):
        profile_translation_id (Union[Unset, None, int]):
        updated (Union[Unset, None, datetime.datetime]):
        discarded (Union[Unset, None, datetime.datetime]):
        id (Union[Unset, str]):
        disabled (Union[Unset, bool]):
    """

    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    telephone: Union[Unset, None, str] = UNSET
    company: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    work_experience: Union[Unset, None, str] = UNSET
    work_experience_id: Union[Unset, None, int] = UNSET
    parent_block_item_id: Union[Unset, None, int] = UNSET
    parent_block_item_updated: Union[Unset, None, bool] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    discarded: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        telephone = self.telephone
        company = self.company
        position = self.position
        text = self.text
        work_experience = self.work_experience
        work_experience_id = self.work_experience_id
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
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if company is not UNSET:
            field_dict["company"] = company
        if position is not UNSET:
            field_dict["position"] = position
        if text is not UNSET:
            field_dict["text"] = text
        if work_experience is not UNSET:
            field_dict["workExperience"] = work_experience
        if work_experience_id is not UNSET:
            field_dict["workExperienceId"] = work_experience_id
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
        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        telephone = d.pop("telephone", UNSET)

        company = d.pop("company", UNSET)

        position = d.pop("position", UNSET)

        text = d.pop("text", UNSET)

        work_experience = d.pop("workExperience", UNSET)

        work_experience_id = d.pop("workExperienceId", UNSET)

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

        reference_block_item_model = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            company=company,
            position=position,
            text=text,
            work_experience=work_experience,
            work_experience_id=work_experience_id,
            parent_block_item_id=parent_block_item_id,
            parent_block_item_updated=parent_block_item_updated,
            profile_translation_id=profile_translation_id,
            updated=updated,
            discarded=discarded,
            id=id,
            disabled=disabled,
        )

        return reference_block_item_model
