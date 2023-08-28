import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_block_item_model import ReferenceBlockItemModel


T = TypeVar("T", bound="ReferenceBlockModel")


@_attrs_define
class ReferenceBlockModel:
    """
    Attributes:
        hide_description (Union[Unset, bool]):
        hide_in_edit (Union[Unset, bool]):
        data (Union[Unset, None, List['ReferenceBlockItemModel']]):
        block_id (Union[Unset, str]):
        updated (Union[Unset, None, datetime.datetime]):
        heading (Union[Unset, None, str]):
    """

    hide_description: Union[Unset, bool] = UNSET
    hide_in_edit: Union[Unset, bool] = UNSET
    data: Union[Unset, None, List["ReferenceBlockItemModel"]] = UNSET
    block_id: Union[Unset, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    heading: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        hide_description = self.hide_description
        hide_in_edit = self.hide_in_edit
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
        if hide_description is not UNSET:
            field_dict["hideDescription"] = hide_description
        if hide_in_edit is not UNSET:
            field_dict["hideInEdit"] = hide_in_edit
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
        from ..models.reference_block_item_model import ReferenceBlockItemModel

        d = src_dict.copy()
        hide_description = d.pop("hideDescription", UNSET)

        hide_in_edit = d.pop("hideInEdit", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ReferenceBlockItemModel.from_dict(data_item_data)

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

        reference_block_model = cls(
            hide_description=hide_description,
            hide_in_edit=hide_in_edit,
            data=data,
            block_id=block_id,
            updated=updated,
            heading=heading,
        )

        return reference_block_model
