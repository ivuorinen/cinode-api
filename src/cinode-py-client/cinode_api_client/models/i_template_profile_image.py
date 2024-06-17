from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_size import ImageSize
from ..types import UNSET, Unset

T = TypeVar("T", bound="ITemplateProfileImage")


@_attrs_define
class ITemplateProfileImage:
    """
    Attributes:
        allow_no_profile_image (Union[Unset, bool]):
        show_image (Union[Unset, bool]):
        use_default_image (Union[Unset, bool]):
        company_user_resume_id (Union[Unset, int]):
        company_user_id (Union[Unset, int]):
        image_id (Union[Unset, int]):
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

    allow_no_profile_image: Union[Unset, bool] = UNSET
    show_image: Union[Unset, bool] = UNSET
    use_default_image: Union[Unset, bool] = UNSET
    company_user_resume_id: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, int] = UNSET
    image_id: Union[Unset, int] = UNSET
    image_url: Union[Unset, None, str] = UNSET
    image_original_url: Union[Unset, None, str] = UNSET
    image_size: Union[Unset, ImageSize] = UNSET
    image_file_name: Union[Unset, str] = UNSET
    extension: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        allow_no_profile_image = self.allow_no_profile_image
        show_image = self.show_image
        use_default_image = self.use_default_image
        company_user_resume_id = self.company_user_resume_id
        company_user_id = self.company_user_id
        image_id = self.image_id
        image_url = self.image_url
        image_original_url = self.image_original_url
        image_size: Union[Unset, int] = UNSET
        if not isinstance(self.image_size, Unset):
            image_size = self.image_size.value

        image_file_name = self.image_file_name
        extension = self.extension

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if allow_no_profile_image is not UNSET:
            field_dict["allowNoProfileImage"] = allow_no_profile_image
        if show_image is not UNSET:
            field_dict["showImage"] = show_image
        if use_default_image is not UNSET:
            field_dict["useDefaultImage"] = use_default_image
        if company_user_resume_id is not UNSET:
            field_dict["companyUserResumeId"] = company_user_resume_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
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
        allow_no_profile_image = d.pop("allowNoProfileImage", UNSET)

        show_image = d.pop("showImage", UNSET)

        use_default_image = d.pop("useDefaultImage", UNSET)

        company_user_resume_id = d.pop("companyUserResumeId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        image_id = d.pop("imageId", UNSET)

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

        i_template_profile_image = cls(
            allow_no_profile_image=allow_no_profile_image,
            show_image=show_image,
            use_default_image=use_default_image,
            company_user_resume_id=company_user_resume_id,
            company_user_id=company_user_id,
            image_id=image_id,
            image_url=image_url,
            image_original_url=image_original_url,
            image_size=image_size,
            image_file_name=image_file_name,
            extension=extension,
        )

        return i_template_profile_image
