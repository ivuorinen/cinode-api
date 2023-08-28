import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageBlockModel")


@_attrs_define
class ImageBlockModel:
    """
    Attributes:
        image_id (Union[Unset, None, int]):
        company_image_id (Union[Unset, None, int]):
        image_original_url (Union[Unset, None, str]):
        image_file_name (Union[Unset, str]):
        extension (Union[Unset, None, str]):
        block_id (Union[Unset, str]):
        updated (Union[Unset, None, datetime.datetime]):
        heading (Union[Unset, None, str]):
    """

    image_id: Union[Unset, None, int] = UNSET
    company_image_id: Union[Unset, None, int] = UNSET
    image_original_url: Union[Unset, None, str] = UNSET
    image_file_name: Union[Unset, str] = UNSET
    extension: Union[Unset, None, str] = UNSET
    block_id: Union[Unset, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    heading: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image_id = self.image_id
        company_image_id = self.company_image_id
        image_original_url = self.image_original_url
        image_file_name = self.image_file_name
        extension = self.extension
        block_id = self.block_id
        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        heading = self.heading

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if company_image_id is not UNSET:
            field_dict["companyImageId"] = company_image_id
        if image_original_url is not UNSET:
            field_dict["imageOriginalUrl"] = image_original_url
        if image_file_name is not UNSET:
            field_dict["imageFileName"] = image_file_name
        if extension is not UNSET:
            field_dict["extension"] = extension
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
        image_id = d.pop("imageId", UNSET)

        company_image_id = d.pop("companyImageId", UNSET)

        image_original_url = d.pop("imageOriginalUrl", UNSET)

        image_file_name = d.pop("imageFileName", UNSET)

        extension = d.pop("extension", UNSET)

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

        image_block_model = cls(
            image_id=image_id,
            company_image_id=company_image_id,
            image_original_url=image_original_url,
            image_file_name=image_file_name,
            extension=extension,
            block_id=block_id,
            updated=updated,
            heading=heading,
        )

        return image_block_model
