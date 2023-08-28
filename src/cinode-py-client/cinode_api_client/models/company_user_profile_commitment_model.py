import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_commitment_translation_model import CompanyUserProfileCommitmentTranslationModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserProfileCommitmentModel")


@_attrs_define
class CompanyUserProfileCommitmentModel:
    """
    Attributes:
        profile_id (Union[Unset, None, int]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        translations (Union[Unset, None, List['CompanyUserProfileCommitmentTranslationModel']]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        url (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    profile_id: Union[Unset, None, int] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    translations: Union[Unset, None, List["CompanyUserProfileCommitmentTranslationModel"]] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_id = self.profile_id
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

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
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
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
        from ..models.company_user_profile_commitment_translation_model import (
            CompanyUserProfileCommitmentTranslationModel,
        )
        from ..models.link import Link

        d = src_dict.copy()
        profile_id = d.pop("profileId", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CompanyUserProfileCommitmentTranslationModel.from_dict(translations_item_data)

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

        company_user_profile_commitment_model = cls(
            profile_id=profile_id,
            start_date=start_date,
            end_date=end_date,
            translations=translations,
            company_id=company_id,
            company_user_id=company_user_id,
            id=id,
            url=url,
            links=links,
        )

        return company_user_profile_commitment_model
