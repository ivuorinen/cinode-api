import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.skill_by_category_block_item_model import SkillByCategoryBlockItemModel


T = TypeVar("T", bound="SkillByCategoryBlockModel")


@_attrs_define
class SkillByCategoryBlockModel:
    """
    Attributes:
        data (Union[Unset, None, List['SkillByCategoryBlockItemModel']]):
        block_id (Union[Unset, str]):
        updated (Union[Unset, None, datetime.datetime]):
        heading (Union[Unset, None, str]):
    """

    data: Union[Unset, None, List["SkillByCategoryBlockItemModel"]] = UNSET
    block_id: Union[Unset, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    heading: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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
        from ..models.skill_by_category_block_item_model import SkillByCategoryBlockItemModel

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = SkillByCategoryBlockItemModel.from_dict(data_item_data)

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

        skill_by_category_block_model = cls(
            data=data,
            block_id=block_id,
            updated=updated,
            heading=heading,
        )

        return skill_by_category_block_model
