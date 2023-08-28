import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_skill_block_item_model import TopSkillBlockItemModel


T = TypeVar("T", bound="TopSkillBlockModel")


@_attrs_define
class TopSkillBlockModel:
    """
    Attributes:
        use_level (Union[Unset, bool]):
        min_value (Union[Unset, int]):
        max_value (Union[Unset, int]):
        number_of_items_in_list (Union[Unset, int]):
        data (Union[Unset, None, List['TopSkillBlockItemModel']]):
        block_id (Union[Unset, str]):
        updated (Union[Unset, None, datetime.datetime]):
        heading (Union[Unset, None, str]):
    """

    use_level: Union[Unset, bool] = UNSET
    min_value: Union[Unset, int] = UNSET
    max_value: Union[Unset, int] = UNSET
    number_of_items_in_list: Union[Unset, int] = UNSET
    data: Union[Unset, None, List["TopSkillBlockItemModel"]] = UNSET
    block_id: Union[Unset, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    heading: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        use_level = self.use_level
        min_value = self.min_value
        max_value = self.max_value
        number_of_items_in_list = self.number_of_items_in_list
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
        if use_level is not UNSET:
            field_dict["useLevel"] = use_level
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if number_of_items_in_list is not UNSET:
            field_dict["numberOfItemsInList"] = number_of_items_in_list
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
        from ..models.top_skill_block_item_model import TopSkillBlockItemModel

        d = src_dict.copy()
        use_level = d.pop("useLevel", UNSET)

        min_value = d.pop("minValue", UNSET)

        max_value = d.pop("maxValue", UNSET)

        number_of_items_in_list = d.pop("numberOfItemsInList", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = TopSkillBlockItemModel.from_dict(data_item_data)

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

        top_skill_block_model = cls(
            use_level=use_level,
            min_value=min_value,
            max_value=max_value,
            number_of_items_in_list=number_of_items_in_list,
            data=data,
            block_id=block_id,
            updated=updated,
            heading=heading,
        )

        return top_skill_block_model
