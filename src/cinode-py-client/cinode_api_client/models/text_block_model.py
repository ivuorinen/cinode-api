import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextBlockModel")


@_attrs_define
class TextBlockModel:
    """
    Attributes:
        description (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        hide_in_edit (Union[Unset, bool]):
        hide_title (Union[Unset, bool]):
        hide_description (Union[Unset, bool]):
        hide_text (Union[Unset, bool]):
        block_id (Union[Unset, str]):
        updated (Union[Unset, None, datetime.datetime]):
        heading (Union[Unset, None, str]):
    """

    description: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    hide_in_edit: Union[Unset, bool] = UNSET
    hide_title: Union[Unset, bool] = UNSET
    hide_description: Union[Unset, bool] = UNSET
    hide_text: Union[Unset, bool] = UNSET
    block_id: Union[Unset, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    heading: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        text = self.text
        hide_in_edit = self.hide_in_edit
        hide_title = self.hide_title
        hide_description = self.hide_description
        hide_text = self.hide_text
        block_id = self.block_id
        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        heading = self.heading

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if text is not UNSET:
            field_dict["text"] = text
        if hide_in_edit is not UNSET:
            field_dict["hideInEdit"] = hide_in_edit
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title
        if hide_description is not UNSET:
            field_dict["hideDescription"] = hide_description
        if hide_text is not UNSET:
            field_dict["hideText"] = hide_text
        if block_id is not UNSET:
            field_dict["blockId"] = block_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if heading is not UNSET:
            field_dict["heading"] = heading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        text = d.pop("text", UNSET)

        hide_in_edit = d.pop("hideInEdit", UNSET)

        hide_title = d.pop("hideTitle", UNSET)

        hide_description = d.pop("hideDescription", UNSET)

        hide_text = d.pop("hideText", UNSET)

        block_id = d.pop("blockId", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, datetime.datetime]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        heading = d.pop("heading", UNSET)

        text_block_model = cls(
            description=description,
            text=text,
            hide_in_edit=hide_in_edit,
            hide_title=hide_title,
            hide_description=hide_description,
            hide_text=hide_text,
            block_id=block_id,
            updated=updated,
            heading=heading,
        )

        return text_block_model
