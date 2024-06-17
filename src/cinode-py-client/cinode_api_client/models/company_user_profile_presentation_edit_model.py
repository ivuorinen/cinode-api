from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.save_to_api_option import SaveToApiOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfilePresentationEditModel")


@_attrs_define
class CompanyUserProfilePresentationEditModel:
    """
    Attributes:
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        personal_description (Union[Unset, None, str]):
        save_to (Union[Unset, SaveToApiOption]):

            AllResumesOfLanguage = 3

            Profile = 5
    """

    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    personal_description: Union[Unset, None, str] = UNSET
    save_to: Union[Unset, SaveToApiOption] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        personal_description = self.personal_description
        save_to: Union[Unset, int] = UNSET
        if not isinstance(self.save_to, Unset):
            save_to = self.save_to.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if personal_description is not UNSET:
            field_dict["personalDescription"] = personal_description
        if save_to is not UNSET:
            field_dict["saveTo"] = save_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        personal_description = d.pop("personalDescription", UNSET)

        _save_to = d.pop("saveTo", UNSET)
        save_to: Union[Unset, SaveToApiOption]
        if isinstance(_save_to, Unset):
            save_to = UNSET
        else:
            save_to = SaveToApiOption(_save_to)

        company_user_profile_presentation_edit_model = cls(
            title=title,
            description=description,
            personal_description=personal_description,
            save_to=save_to,
        )

        return company_user_profile_presentation_edit_model
