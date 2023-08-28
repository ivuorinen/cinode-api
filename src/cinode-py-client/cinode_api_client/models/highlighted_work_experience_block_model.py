import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.highlighted_work_experience_block_item_model import HighlightedWorkExperienceBlockItemModel


T = TypeVar("T", bound="HighlightedWorkExperienceBlockModel")


@_attrs_define
class HighlightedWorkExperienceBlockModel:
    """
    Attributes:
        number_of_items_in_list (Union[Unset, int]):
        title_length (Union[Unset, int]):
        description_length (Union[Unset, int]):
        employer_length (Union[Unset, int]):
        hide_in_edit (Union[Unset, bool]):
        hide_title (Union[Unset, bool]):
        hide_description (Union[Unset, bool]):
        hide_text (Union[Unset, bool]):
        data (Union[Unset, None, List['HighlightedWorkExperienceBlockItemModel']]):
        block_id (Union[Unset, str]):
        updated (Union[Unset, None, datetime.datetime]):
        heading (Union[Unset, None, str]):
    """

    number_of_items_in_list: Union[Unset, int] = UNSET
    title_length: Union[Unset, int] = UNSET
    description_length: Union[Unset, int] = UNSET
    employer_length: Union[Unset, int] = UNSET
    hide_in_edit: Union[Unset, bool] = UNSET
    hide_title: Union[Unset, bool] = UNSET
    hide_description: Union[Unset, bool] = UNSET
    hide_text: Union[Unset, bool] = UNSET
    data: Union[Unset, None, List["HighlightedWorkExperienceBlockItemModel"]] = UNSET
    block_id: Union[Unset, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    heading: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        number_of_items_in_list = self.number_of_items_in_list
        title_length = self.title_length
        description_length = self.description_length
        employer_length = self.employer_length
        hide_in_edit = self.hide_in_edit
        hide_title = self.hide_title
        hide_description = self.hide_description
        hide_text = self.hide_text
        data: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            if self.data is None:
                data = None
            else:
                data = []
                for data_item_data in self.data:
                    data_item = data_item_data.to_dict()

                    data.append(data_item)

        block_id = self.block_id
        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        heading = self.heading

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if number_of_items_in_list is not UNSET:
            field_dict["numberOfItemsInList"] = number_of_items_in_list
        if title_length is not UNSET:
            field_dict["titleLength"] = title_length
        if description_length is not UNSET:
            field_dict["descriptionLength"] = description_length
        if employer_length is not UNSET:
            field_dict["employerLength"] = employer_length
        if hide_in_edit is not UNSET:
            field_dict["hideInEdit"] = hide_in_edit
        if hide_title is not UNSET:
            field_dict["hideTitle"] = hide_title
        if hide_description is not UNSET:
            field_dict["hideDescription"] = hide_description
        if hide_text is not UNSET:
            field_dict["hideText"] = hide_text
        if data is not UNSET:
            field_dict["data"] = data
        if block_id is not UNSET:
            field_dict["blockId"] = block_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if heading is not UNSET:
            field_dict["heading"] = heading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.highlighted_work_experience_block_item_model import HighlightedWorkExperienceBlockItemModel

        d = src_dict.copy()
        number_of_items_in_list = d.pop("numberOfItemsInList", UNSET)

        title_length = d.pop("titleLength", UNSET)

        description_length = d.pop("descriptionLength", UNSET)

        employer_length = d.pop("employerLength", UNSET)

        hide_in_edit = d.pop("hideInEdit", UNSET)

        hide_title = d.pop("hideTitle", UNSET)

        hide_description = d.pop("hideDescription", UNSET)

        hide_text = d.pop("hideText", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = HighlightedWorkExperienceBlockItemModel.from_dict(data_item_data)

            data.append(data_item)

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

        highlighted_work_experience_block_model = cls(
            number_of_items_in_list=number_of_items_in_list,
            title_length=title_length,
            description_length=description_length,
            employer_length=employer_length,
            hide_in_edit=hide_in_edit,
            hide_title=hide_title,
            hide_description=hide_description,
            hide_text=hide_text,
            data=data,
            block_id=block_id,
            updated=updated,
            heading=heading,
        )

        return highlighted_work_experience_block_model
