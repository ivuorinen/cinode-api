from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_model import KeywordModel
    from ..models.keyword_synonym_model import KeywordSynonymModel


T = TypeVar("T", bound="CompanyCandidateSkillModel")


@_attrs_define
class CompanyCandidateSkillModel:
    """
    Attributes:
        company_candidate_id (Union[Unset, int]):
        keyword_id (Union[Unset, int]):
        keyword (Union[Unset, None, KeywordModel]):
        keyword_synonym_id (Union[Unset, int]):
        keyword_synonym (Union[Unset, None, KeywordSynonymModel]):
    """

    company_candidate_id: Union[Unset, int] = UNSET
    keyword_id: Union[Unset, int] = UNSET
    keyword: Union[Unset, None, "KeywordModel"] = UNSET
    keyword_synonym_id: Union[Unset, int] = UNSET
    keyword_synonym: Union[Unset, None, "KeywordSynonymModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_candidate_id = self.company_candidate_id
        keyword_id = self.keyword_id
        keyword: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict() if self.keyword else None

        keyword_synonym_id = self.keyword_synonym_id
        keyword_synonym: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword_synonym, Unset):
            keyword_synonym = self.keyword_synonym.to_dict() if self.keyword_synonym else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_candidate_id is not UNSET:
            field_dict["companyCandidateId"] = company_candidate_id
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if keyword_synonym_id is not UNSET:
            field_dict["keywordSynonymId"] = keyword_synonym_id
        if keyword_synonym is not UNSET:
            field_dict["keywordSynonym"] = keyword_synonym

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyword_model import KeywordModel
        from ..models.keyword_synonym_model import KeywordSynonymModel

        d = src_dict.copy()
        company_candidate_id = d.pop("companyCandidateId", UNSET)

        keyword_id = d.pop("keywordId", UNSET)

        _keyword = d.pop("keyword", UNSET)
        keyword: Union[Unset, None, KeywordModel]
        if _keyword is None:
            keyword = None
        elif isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = KeywordModel.from_dict(_keyword)

        keyword_synonym_id = d.pop("keywordSynonymId", UNSET)

        _keyword_synonym = d.pop("keywordSynonym", UNSET)
        keyword_synonym: Union[Unset, None, KeywordSynonymModel]
        if _keyword_synonym is None:
            keyword_synonym = None
        elif isinstance(_keyword_synonym, Unset):
            keyword_synonym = UNSET
        else:
            keyword_synonym = KeywordSynonymModel.from_dict(_keyword_synonym)

        company_candidate_skill_model = cls(
            company_candidate_id=company_candidate_id,
            keyword_id=keyword_id,
            keyword=keyword,
            keyword_synonym_id=keyword_synonym_id,
            keyword_synonym=keyword_synonym,
        )

        return company_candidate_skill_model
