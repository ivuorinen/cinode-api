from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel
    from ..models.keyword_model import KeywordModel
    from ..models.keyword_synonym_model import KeywordSynonymModel


T = TypeVar("T", bound="CompanyUserProfileSkillTranslationModel")


@_attrs_define
class CompanyUserProfileSkillTranslationModel:
    """
    Attributes:
        keyword_id (Union[Unset, None, int]):
        keyword_synonym_id (Union[Unset, None, int]):
        keyword_synonym (Union[Unset, None, KeywordSynonymModel]):
        keyword (Union[Unset, None, KeywordModel]):
        profile_id (Union[Unset, None, int]):
        profile_translation_id (Union[Unset, None, int]):
        profile_translation (Union[Unset, None, CompanyUserProfileTranslationModel]):
    """

    keyword_id: Union[Unset, None, int] = UNSET
    keyword_synonym_id: Union[Unset, None, int] = UNSET
    keyword_synonym: Union[Unset, None, "KeywordSynonymModel"] = UNSET
    keyword: Union[Unset, None, "KeywordModel"] = UNSET
    profile_id: Union[Unset, None, int] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    profile_translation: Union[Unset, None, "CompanyUserProfileTranslationModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyword_id = self.keyword_id
        keyword_synonym_id = self.keyword_synonym_id
        keyword_synonym: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword_synonym, Unset):
            keyword_synonym = self.keyword_synonym.to_dict() if self.keyword_synonym else None

        keyword: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict() if self.keyword else None

        profile_id = self.profile_id
        profile_translation_id = self.profile_translation_id
        profile_translation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile_translation, Unset):
            profile_translation = self.profile_translation.to_dict() if self.profile_translation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if keyword_synonym is not UNSET:
            field_dict["keywordSynonym"] = keyword_synonym
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if profile_translation_id is not UNSET:
            field_dict["profileTranslationId"] = profile_translation_id
        if profile_translation is not UNSET:
            field_dict["profileTranslation"] = profile_translation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel
        from ..models.keyword_model import KeywordModel
        from ..models.keyword_synonym_model import KeywordSynonymModel

        d = src_dict.copy()
        keyword_id = d.pop("keywordId", UNSET)

        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        _keyword_synonym = d.pop("keywordSynonym", UNSET)
        keyword_synonym: Union[Unset, None, KeywordSynonymModel]
        if _keyword_synonym is None:
            keyword_synonym = None
        elif isinstance(_keyword_synonym, Unset):
            keyword_synonym = UNSET
        else:
            keyword_synonym = KeywordSynonymModel.from_dict(_keyword_synonym)

        _keyword = d.pop("keyword", UNSET)
        keyword: Union[Unset, None, KeywordModel]
        if _keyword is None:
            keyword = None
        elif isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = KeywordModel.from_dict(_keyword)

        profile_id = d.pop("profileId", UNSET)

        profile_translation_id = d.pop("profileTranslationId", UNSET)

        _profile_translation = d.pop("profileTranslation", UNSET)
        profile_translation: Union[Unset, None, CompanyUserProfileTranslationModel]
        if _profile_translation is None:
            profile_translation = None
        elif isinstance(_profile_translation, Unset):
            profile_translation = UNSET
        else:
            profile_translation = CompanyUserProfileTranslationModel.from_dict(_profile_translation)

        company_user_profile_skill_translation_model = cls(
            keyword_id=keyword_id,
            keyword_synonym_id=keyword_synonym_id,
            keyword_synonym=keyword_synonym,
            keyword=keyword,
            profile_id=profile_id,
            profile_translation_id=profile_translation_id,
            profile_translation=profile_translation,
        )

        return company_user_profile_skill_translation_model
