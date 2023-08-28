import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.training_type import TrainingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_training_translation_model import CompanyUserProfileTrainingTranslationModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserProfileTrainingModel")


@_attrs_define
class CompanyUserProfileTrainingModel:
    """
    Attributes:
        profile_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        training_type (Union[Unset, None, TrainingType]):

            Kurs = 0

            Certifiering = 1
        year (Union[Unset, None, int]):
        code (Union[Unset, None, str]):
        translations (Union[Unset, None, List['CompanyUserProfileTrainingTranslationModel']]):
        expire_date (Union[Unset, None, datetime.datetime]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        url (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    profile_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    training_type: Union[Unset, None, TrainingType] = UNSET
    year: Union[Unset, None, int] = UNSET
    code: Union[Unset, None, str] = UNSET
    translations: Union[Unset, None, List["CompanyUserProfileTrainingTranslationModel"]] = UNSET
    expire_date: Union[Unset, None, datetime.datetime] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_id = self.profile_id
        id = self.id
        training_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.training_type, Unset):
            training_type = self.training_type.value if self.training_type else None

        year = self.year
        code = self.code
        translations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            if self.translations is None:
                translations = None
            else:
                translations = []
                for translations_item_data in self.translations:
                    translations_item = translations_item_data.to_dict()

                    translations.append(translations_item)

        expire_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expire_date, Unset):
            expire_date = self.expire_date.isoformat() if self.expire_date else None

        company_id = self.company_id
        company_user_id = self.company_user_id
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
        if id is not UNSET:
            field_dict["id"] = id
        if training_type is not UNSET:
            field_dict["trainingType"] = training_type
        if year is not UNSET:
            field_dict["year"] = year
        if code is not UNSET:
            field_dict["code"] = code
        if translations is not UNSET:
            field_dict["translations"] = translations
        if expire_date is not UNSET:
            field_dict["expireDate"] = expire_date
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if url is not UNSET:
            field_dict["url"] = url
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_training_translation_model import CompanyUserProfileTrainingTranslationModel
        from ..models.link import Link

        d = src_dict.copy()
        profile_id = d.pop("profileId", UNSET)

        id = d.pop("id", UNSET)

        _training_type = d.pop("trainingType", UNSET)
        training_type: Union[Unset, None, TrainingType]
        if _training_type is None:
            training_type = None
        elif isinstance(_training_type, Unset):
            training_type = UNSET
        else:
            training_type = TrainingType(_training_type)

        year = d.pop("year", UNSET)

        code = d.pop("code", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CompanyUserProfileTrainingTranslationModel.from_dict(translations_item_data)

            translations.append(translations_item)

        _expire_date = d.pop("expireDate", UNSET)
        expire_date: Union[Unset, None, datetime.datetime]
        if _expire_date is None:
            expire_date = None
        elif isinstance(_expire_date, Unset):
            expire_date = UNSET
        else:
            expire_date = isoparse(_expire_date)

        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        url = d.pop("url", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_profile_training_model = cls(
            profile_id=profile_id,
            id=id,
            training_type=training_type,
            year=year,
            code=code,
            translations=translations,
            expire_date=expire_date,
            company_id=company_id,
            company_user_id=company_user_id,
            url=url,
            links=links,
        )

        return company_user_profile_training_model
