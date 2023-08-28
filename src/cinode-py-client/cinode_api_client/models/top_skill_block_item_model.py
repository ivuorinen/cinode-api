import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopSkillBlockItemModel")


@_attrs_define
class TopSkillBlockItemModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        level (Union[Unset, None, int]):
        parent_block_item_id (Union[Unset, None, int]):
        parent_block_item_updated (Union[Unset, None, bool]):
        profile_translation_id (Union[Unset, None, int]):
        updated (Union[Unset, None, datetime.datetime]):
        discarded (Union[Unset, None, datetime.datetime]):
        id (Union[Unset, str]):
        disabled (Union[Unset, bool]):
    """

    name: Union[Unset, None, str] = UNSET
    level: Union[Unset, None, int] = UNSET
    parent_block_item_id: Union[Unset, None, int] = UNSET
    parent_block_item_updated: Union[Unset, None, bool] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    discarded: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        level = self.level
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
        if name is not UNSET:
            field_dict["name"] = name
        if level is not UNSET:
            field_dict["level"] = level
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
        name = d.pop("name", UNSET)

        level = d.pop("level", UNSET)

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

        top_skill_block_item_model = cls(
            name=name,
            level=level,
            parent_block_item_id=parent_block_item_id,
            parent_block_item_updated=parent_block_item_updated,
            profile_translation_id=profile_translation_id,
            updated=updated,
            discarded=discarded,
            id=id,
            disabled=disabled,
        )

        return top_skill_block_item_model
