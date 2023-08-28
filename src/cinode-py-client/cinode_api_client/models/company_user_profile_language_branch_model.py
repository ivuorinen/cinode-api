from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_language_model import ProfileLanguageModel


T = TypeVar("T", bound="CompanyUserProfileLanguageBranchModel")


@_attrs_define
class CompanyUserProfileLanguageBranchModel:
    """
    Attributes:
        id (Union[Unset, None, int]):
        language_id (Union[Unset, None, int]):
        language (Union[Unset, None, ProfileLanguageModel]):
        enabled (Union[Unset, bool]):
    """

    id: Union[Unset, None, int] = UNSET
    language_id: Union[Unset, None, int] = UNSET
    language: Union[Unset, None, "ProfileLanguageModel"] = UNSET
    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        language_id = self.language_id
        language: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict() if self.language else None

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if language is not UNSET:
            field_dict["language"] = language
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile_language_model import ProfileLanguageModel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        language_id = d.pop("languageId", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, None, ProfileLanguageModel]
        if _language is None:
            language = None
        elif isinstance(_language, Unset):
            language = UNSET
        else:
            language = ProfileLanguageModel.from_dict(_language)

        enabled = d.pop("enabled", UNSET)

        company_user_profile_language_branch_model = cls(
            id=id,
            language_id=language_id,
            language=language,
            enabled=enabled,
        )

        return company_user_profile_language_branch_model
