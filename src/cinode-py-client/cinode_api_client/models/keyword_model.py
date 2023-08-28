from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.keyword_type import KeywordType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeywordModel")


@_attrs_define
class KeywordModel:
    """
    Attributes:
        id (Union[Unset, None, int]):
        type (Union[Unset, KeywordType]):

            Okategoriserad = 0

            Branscher = 1

            Roller = 2

            Verktyg = 3

            Tekniker = 4

            Metoder och processer = 5

            Plattformar = 6

            Produkter och tjänster = 7

            Certifieringar = 10

            Material = 11

            Specifikationer och förordningar = 12

            Hårdvara = 13

            Verksamhet och funktion = 14

            Byggnationer = 15

            Rapporter och utredningar = 16

            Specialiteter - Medicin = 17

            Standarder och regelverk = 18

            Behörigheter = 19

            Mjuka färdigheter = 20

            CustomName = 100
        master_synonym_id (Union[Unset, None, int]):
        master_synonym (Union[Unset, None, str]):
        synonyms (Union[Unset, None, List[str]]):
        universal (Union[Unset, bool]):
        verified (Union[Unset, bool]):
    """

    id: Union[Unset, None, int] = UNSET
    type: Union[Unset, KeywordType] = UNSET
    master_synonym_id: Union[Unset, None, int] = UNSET
    master_synonym: Union[Unset, None, str] = UNSET
    synonyms: Union[Unset, None, List[str]] = UNSET
    universal: Union[Unset, bool] = UNSET
    verified: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        master_synonym_id = self.master_synonym_id
        master_synonym = self.master_synonym
        synonyms: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            if self.synonyms is None:
                synonyms = None
            else:
                synonyms = self.synonyms

        universal = self.universal
        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if master_synonym_id is not UNSET:
            field_dict["masterSynonymId"] = master_synonym_id
        if master_synonym is not UNSET:
            field_dict["masterSynonym"] = master_synonym
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms
        if universal is not UNSET:
            field_dict["universal"] = universal
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, KeywordType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = KeywordType(_type)

        master_synonym_id = d.pop("masterSynonymId", UNSET)

        master_synonym = d.pop("masterSynonym", UNSET)

        synonyms = cast(List[str], d.pop("synonyms", UNSET))

        universal = d.pop("universal", UNSET)

        verified = d.pop("verified", UNSET)

        keyword_model = cls(
            id=id,
            type=type,
            master_synonym_id=master_synonym_id,
            master_synonym=master_synonym,
            synonyms=synonyms,
            universal=universal,
            verified=verified,
        )

        return keyword_model
