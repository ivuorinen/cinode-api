from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_reference_translation_model import CompanyUserProfileReferenceTranslationModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserProfileReferenceModel")


@_attrs_define
class CompanyUserProfileReferenceModel:
    """
    Attributes:
        profile_id (Union[Unset, None, int]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        telephone (Union[Unset, None, str]):
        profile_work_experience_id (Union[Unset, None, int]):
        translations (Union[Unset, None, List['CompanyUserProfileReferenceTranslationModel']]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        url (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    profile_id: Union[Unset, None, int] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    telephone: Union[Unset, None, str] = UNSET
    profile_work_experience_id: Union[Unset, None, int] = UNSET
    translations: Union[Unset, None, List["CompanyUserProfileReferenceTranslationModel"]] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_id = self.profile_id
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        telephone = self.telephone
        profile_work_experience_id = self.profile_work_experience_id
        translations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            if self.translations is None:
                translations = None
            else:
                translations = []
                for translations_item_data in self.translations:
                    translations_item = translations_item_data.to_dict()

                    translations.append(translations_item)

        company_id = self.company_id
        company_user_id = self.company_user_id
        id = self.id
        url = self.url
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if profile_work_experience_id is not UNSET:
            field_dict["profileWorkExperienceId"] = profile_work_experience_id
        if translations is not UNSET:
            field_dict["translations"] = translations
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_reference_translation_model import (
            CompanyUserProfileReferenceTranslationModel,
        )
        from ..models.link import Link

        d = src_dict.copy()
        profile_id = d.pop("profileId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        telephone = d.pop("telephone", UNSET)

        profile_work_experience_id = d.pop("profileWorkExperienceId", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CompanyUserProfileReferenceTranslationModel.from_dict(translations_item_data)

            translations.append(translations_item)

        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_profile_reference_model = cls(
            profile_id=profile_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            profile_work_experience_id=profile_work_experience_id,
            translations=translations,
            company_id=company_id,
            company_user_id=company_user_id,
            id=id,
            url=url,
            links=links,
        )

        return company_user_profile_reference_model
