from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_model import KeywordModel


T = TypeVar("T", bound="KeywordSynonymModel")


@_attrs_define
class KeywordSynonymModel:
    """
    Attributes:
        keyword_id (Union[Unset, None, int]):
        id (Union[Unset, None, int]):
        keyword (Union[Unset, None, KeywordModel]):
        name (Union[Unset, None, str]):
        seo_id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        language_id (Union[Unset, None, int]):
    """

    keyword_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, None, int] = UNSET
    keyword: Union[Unset, None, "KeywordModel"] = UNSET
    name: Union[Unset, None, str] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    language_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        keyword_id = self.keyword_id
        id = self.id
        keyword: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword, Unset):
            keyword = self.keyword.to_dict() if self.keyword else None

        name = self.name
        seo_id = self.seo_id
        description = self.description
        language_id = self.language_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
        if id is not UNSET:
            field_dict["id"] = id
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if name is not UNSET:
            field_dict["name"] = name
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if description is not UNSET:
            field_dict["description"] = description
        if language_id is not UNSET:
            field_dict["languageId"] = language_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyword_model import KeywordModel

        d = src_dict.copy()
        keyword_id = d.pop("keywordId", UNSET)

        id = d.pop("id", UNSET)

        _keyword = d.pop("keyword", UNSET)
        keyword: Union[Unset, None, KeywordModel]
        if _keyword is None:
            keyword = None
        elif isinstance(_keyword, Unset):
            keyword = UNSET
        else:
            keyword = KeywordModel.from_dict(_keyword)

        name = d.pop("name", UNSET)

        seo_id = d.pop("seoId", UNSET)

        description = d.pop("description", UNSET)

        language_id = d.pop("languageId", UNSET)

        keyword_synonym_model = cls(
            keyword_id=keyword_id,
            id=id,
            keyword=keyword,
            name=name,
            seo_id=seo_id,
            description=description,
            language_id=language_id,
        )

        return keyword_synonym_model
