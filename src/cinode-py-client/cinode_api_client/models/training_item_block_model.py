import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.training_type import TrainingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrainingItemBlockModel")


@_attrs_define
class TrainingItemBlockModel:
    """
    Attributes:
        training_type (Union[Unset, TrainingType]):

            Kurs = 0

            Certifiering = 1
        url (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        issuer (Union[Unset, None, str]):
        year (Union[Unset, int]):
        supplier (Union[Unset, None, str]):
        parent_block_item_id (Union[Unset, None, int]):
        parent_block_item_updated (Union[Unset, None, bool]):
        profile_translation_id (Union[Unset, None, int]):
        updated (Union[Unset, None, datetime.datetime]):
        discarded (Union[Unset, None, datetime.datetime]):
        id (Union[Unset, str]):
        disabled (Union[Unset, bool]):
    """

    training_type: Union[Unset, TrainingType] = UNSET
    url: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    issuer: Union[Unset, None, str] = UNSET
    year: Union[Unset, int] = UNSET
    supplier: Union[Unset, None, str] = UNSET
    parent_block_item_id: Union[Unset, None, int] = UNSET
    parent_block_item_updated: Union[Unset, None, bool] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    discarded: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        training_type: Union[Unset, int] = UNSET
        if not isinstance(self.training_type, Unset):
            training_type = self.training_type.value

        url = self.url
        title = self.title
        description = self.description
        issuer = self.issuer
        year = self.year
        supplier = self.supplier
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
        if training_type is not UNSET:
            field_dict["trainingType"] = training_type
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if year is not UNSET:
            field_dict["year"] = year
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
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
        _training_type = d.pop("trainingType", UNSET)
        training_type: Union[Unset, TrainingType]
        if isinstance(_training_type, Unset):
            training_type = UNSET
        else:
            training_type = TrainingType(_training_type)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        issuer = d.pop("issuer", UNSET)

        year = d.pop("year", UNSET)

        supplier = d.pop("supplier", UNSET)

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

        training_item_block_model = cls(
            training_type=training_type,
            url=url,
            title=title,
            description=description,
            issuer=issuer,
            year=year,
            supplier=supplier,
            parent_block_item_id=parent_block_item_id,
            parent_block_item_updated=parent_block_item_updated,
            profile_translation_id=profile_translation_id,
            updated=updated,
            discarded=discarded,
            id=id,
            disabled=disabled,
        )

        return training_item_block_model
