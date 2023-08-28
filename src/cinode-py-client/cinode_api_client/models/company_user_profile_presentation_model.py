from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_presentation_translation_model import (
        CompanyUserProfilePresentationTranslationModel,
    )
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserProfilePresentationModel")


@_attrs_define
class CompanyUserProfilePresentationModel:
    """
    Attributes:
        translations (Union[Unset, None, List['CompanyUserProfilePresentationTranslationModel']]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        url (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    translations: Union[Unset, None, List["CompanyUserProfilePresentationTranslationModel"]] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
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
        from ..models.company_user_profile_presentation_translation_model import (
            CompanyUserProfilePresentationTranslationModel,
        )
        from ..models.link import Link

        d = src_dict.copy()
        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CompanyUserProfilePresentationTranslationModel.from_dict(translations_item_data)

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

        company_user_profile_presentation_model = cls(
            translations=translations,
            company_id=company_id,
            company_user_id=company_user_id,
            id=id,
            url=url,
            links=links,
        )

        return company_user_profile_presentation_model
