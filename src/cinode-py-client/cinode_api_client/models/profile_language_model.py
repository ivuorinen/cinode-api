from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileLanguageModel")


@_attrs_define
class ProfileLanguageModel:
    """
    Attributes:
        language_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        culture (Union[Unset, None, str]):
        lang (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
    """

    language_id: Union[Unset, None, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    culture: Union[Unset, None, str] = UNSET
    lang: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language_id = self.language_id
        name = self.name
        culture = self.culture
        lang = self.lang
        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if language_id is not UNSET:
            field_dict["languageId"] = language_id
        if name is not UNSET:
            field_dict["name"] = name
        if culture is not UNSET:
            field_dict["culture"] = culture
        if lang is not UNSET:
            field_dict["lang"] = lang
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_id = d.pop("languageId", UNSET)

        name = d.pop("name", UNSET)

        culture = d.pop("culture", UNSET)

        lang = d.pop("lang", UNSET)

        country = d.pop("country", UNSET)

        profile_language_model = cls(
            language_id=language_id,
            name=name,
            culture=culture,
            lang=lang,
            country=country,
        )

        return profile_language_model
