from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_size import ImageSize
from ..types import UNSET, Unset

T = TypeVar("T", bound="ITemplateLogotype")


@_attrs_define
class ITemplateLogotype:
    """
    Attributes:
        image_url (Union[Unset, None, str]):
        image_original_url (Union[Unset, None, str]):
        image_size (Union[Unset, ImageSize]):

            Original = 0

            H40W40 = 1

            H100W100 = 2

            H200W200 = 3

            H300W300 = 4

            W100 = 5

            H60 = 6

            H100 = 7

            H40 = 8

            W340 = 9

            W1800 = 10

            H750W1800 = 11

            H250 = 12

            H400W400 = 13

            W150 = 14

            W1200 = 15
        image_file_name (Union[Unset, str]):
        extension (Union[Unset, None, str]):
    """

    image_url: Union[Unset, None, str] = UNSET
    image_original_url: Union[Unset, None, str] = UNSET
    image_size: Union[Unset, ImageSize] = UNSET
    image_file_name: Union[Unset, str] = UNSET
    extension: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image_url = self.image_url
        image_original_url = self.image_original_url
        image_size: Union[Unset, int] = UNSET
        if not isinstance(self.image_size, Unset):
            image_size = self.image_size.value

        image_file_name = self.image_file_name
        extension = self.extension

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if image_original_url is not UNSET:
            field_dict["imageOriginalUrl"] = image_original_url
        if image_size is not UNSET:
            field_dict["imageSize"] = image_size
        if image_file_name is not UNSET:
            field_dict["imageFileName"] = image_file_name
        if extension is not UNSET:
            field_dict["extension"] = extension

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_url = d.pop("imageUrl", UNSET)

        image_original_url = d.pop("imageOriginalUrl", UNSET)

        _image_size = d.pop("imageSize", UNSET)
        image_size: Union[Unset, ImageSize]
        if isinstance(_image_size, Unset):
            image_size = UNSET
        else:
            image_size = ImageSize(_image_size)

        image_file_name = d.pop("imageFileName", UNSET)

        extension = d.pop("extension", UNSET)

        i_template_logotype = cls(
            image_url=image_url,
            image_original_url=image_original_url,
            image_size=image_size,
            image_file_name=image_file_name,
            extension=extension,
        )

        return i_template_logotype
