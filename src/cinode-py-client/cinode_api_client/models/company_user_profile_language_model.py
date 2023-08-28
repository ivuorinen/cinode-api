from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.profile_language_model import ProfileLanguageModel


T = TypeVar("T", bound="CompanyUserProfileLanguageModel")


@_attrs_define
class CompanyUserProfileLanguageModel:
    """
    Attributes:
        profile_id (Union[Unset, None, int]):
        language (Union[Unset, None, ProfileLanguageModel]):
        level (Union[Unset, None, int]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        url (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    profile_id: Union[Unset, None, int] = UNSET
    language: Union[Unset, None, "ProfileLanguageModel"] = UNSET
    level: Union[Unset, None, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_id = self.profile_id
        language: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict() if self.language else None

        level = self.level
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
        if language is not UNSET:
            field_dict["language"] = language
        if level is not UNSET:
            field_dict["level"] = level
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
        from ..models.link import Link
        from ..models.profile_language_model import ProfileLanguageModel

        d = src_dict.copy()
        profile_id = d.pop("profileId", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, None, ProfileLanguageModel]
        if _language is None:
            language = None
        elif isinstance(_language, Unset):
            language = UNSET
        else:
            language = ProfileLanguageModel.from_dict(_language)

        level = d.pop("level", UNSET)

        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_profile_language_model = cls(
            profile_id=profile_id,
            language=language,
            level=level,
            company_id=company_id,
            company_user_id=company_user_id,
            id=id,
            url=url,
            links=links,
        )

        return company_user_profile_language_model
