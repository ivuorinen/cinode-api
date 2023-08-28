import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_presentation_model import CompanyUserProfilePresentationModel
    from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserProfileBaseModel")


@_attrs_define
class CompanyUserProfileBaseModel:
    """
    Attributes:
        id (Union[Unset, None, int]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        created_when (Union[Unset, None, datetime.datetime]):
        updated_when (Union[Unset, None, datetime.datetime]):
        published_when (Union[Unset, None, datetime.datetime]):
        presentation (Union[Unset, None, CompanyUserProfilePresentationModel]):
        profile_translation_id (Union[Unset, int]):
        profile_translation (Union[Unset, None, CompanyUserProfileTranslationModel]):
        translations (Union[Unset, None, List['CompanyUserProfileTranslationModel']]):
        links (Union[Unset, None, List['Link']]):
    """

    id: Union[Unset, None, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    created_when: Union[Unset, None, datetime.datetime] = UNSET
    updated_when: Union[Unset, None, datetime.datetime] = UNSET
    published_when: Union[Unset, None, datetime.datetime] = UNSET
    presentation: Union[Unset, None, "CompanyUserProfilePresentationModel"] = UNSET
    profile_translation_id: Union[Unset, int] = UNSET
    profile_translation: Union[Unset, None, "CompanyUserProfileTranslationModel"] = UNSET
    translations: Union[Unset, None, List["CompanyUserProfileTranslationModel"]] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_id = self.company_id
        company_user_id = self.company_user_id
        created_when: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_when, Unset):
            created_when = self.created_when.isoformat() if self.created_when else None

        updated_when: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_when, Unset):
            updated_when = self.updated_when.isoformat() if self.updated_when else None

        published_when: Union[Unset, None, str] = UNSET
        if not isinstance(self.published_when, Unset):
            published_when = self.published_when.isoformat() if self.published_when else None

        presentation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.presentation, Unset):
            presentation = self.presentation.to_dict() if self.presentation else None

        profile_translation_id = self.profile_translation_id
        profile_translation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile_translation, Unset):
            profile_translation = self.profile_translation.to_dict() if self.profile_translation else None

        translations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            if self.translations is None:
                translations = None
            else:
                translations = []
                for translations_item_data in self.translations:
                    translations_item = translations_item_data.to_dict()

                    translations.append(translations_item)

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
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if created_when is not UNSET:
            field_dict["createdWhen"] = created_when
        if updated_when is not UNSET:
            field_dict["updatedWhen"] = updated_when
        if published_when is not UNSET:
            field_dict["publishedWhen"] = published_when
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if profile_translation_id is not UNSET:
            field_dict["profileTranslationId"] = profile_translation_id
        if profile_translation is not UNSET:
            field_dict["profileTranslation"] = profile_translation
        if translations is not UNSET:
            field_dict["translations"] = translations
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_presentation_model import CompanyUserProfilePresentationModel
        from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        _created_when = d.pop("createdWhen", UNSET)
        created_when: Union[Unset, None, datetime.datetime]
        if _created_when is None:
            created_when = None
        elif isinstance(_created_when, Unset):
            created_when = UNSET
        else:
            created_when = isoparse(_created_when)

        _updated_when = d.pop("updatedWhen", UNSET)
        updated_when: Union[Unset, None, datetime.datetime]
        if _updated_when is None:
            updated_when = None
        elif isinstance(_updated_when, Unset):
            updated_when = UNSET
        else:
            updated_when = isoparse(_updated_when)

        _published_when = d.pop("publishedWhen", UNSET)
        published_when: Union[Unset, None, datetime.datetime]
        if _published_when is None:
            published_when = None
        elif isinstance(_published_when, Unset):
            published_when = UNSET
        else:
            published_when = isoparse(_published_when)

        _presentation = d.pop("presentation", UNSET)
        presentation: Union[Unset, None, CompanyUserProfilePresentationModel]
        if _presentation is None:
            presentation = None
        elif isinstance(_presentation, Unset):
            presentation = UNSET
        else:
            presentation = CompanyUserProfilePresentationModel.from_dict(_presentation)

        profile_translation_id = d.pop("profileTranslationId", UNSET)

        _profile_translation = d.pop("profileTranslation", UNSET)
        profile_translation: Union[Unset, None, CompanyUserProfileTranslationModel]
        if _profile_translation is None:
            profile_translation = None
        elif isinstance(_profile_translation, Unset):
            profile_translation = UNSET
        else:
            profile_translation = CompanyUserProfileTranslationModel.from_dict(_profile_translation)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CompanyUserProfileTranslationModel.from_dict(translations_item_data)

            translations.append(translations_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_profile_base_model = cls(
            id=id,
            company_id=company_id,
            company_user_id=company_user_id,
            created_when=created_when,
            updated_when=updated_when,
            published_when=published_when,
            presentation=presentation,
            profile_translation_id=profile_translation_id,
            profile_translation=profile_translation,
            translations=translations,
            links=links,
        )

        return company_user_profile_base_model
