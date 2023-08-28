from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileReferenceAddEditModel")


@_attrs_define
class CompanyUserProfileReferenceAddEditModel:
    """
    Attributes:
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        telephone (Union[Unset, None, str]):
        company (Union[Unset, None, str]):
        position (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        profile_work_experience_id (Union[Unset, None, int]):
    """

    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    telephone: Union[Unset, None, str] = UNSET
    company: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    profile_work_experience_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        telephone = self.telephone
        company = self.company
        position = self.position
        text = self.text
        profile_work_experience_id = self.profile_work_experience_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if company is not UNSET:
            field_dict["company"] = company
        if position is not UNSET:
            field_dict["position"] = position
        if text is not UNSET:
            field_dict["text"] = text
        if profile_work_experience_id is not UNSET:
            field_dict["profileWorkExperienceId"] = profile_work_experience_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        telephone = d.pop("telephone", UNSET)

        company = d.pop("company", UNSET)

        position = d.pop("position", UNSET)

        text = d.pop("text", UNSET)

        profile_work_experience_id = d.pop("profileWorkExperienceId", UNSET)

        company_user_profile_reference_add_edit_model = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            company=company,
            position=position,
            text=text,
            profile_work_experience_id=profile_work_experience_id,
        )

        return company_user_profile_reference_add_edit_model
