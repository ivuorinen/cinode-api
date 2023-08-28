from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel


T = TypeVar("T", bound="CompanyUserProfileReferenceTranslationModel")


@_attrs_define
class CompanyUserProfileReferenceTranslationModel:
    """
    Attributes:
        profile_reference_id (Union[Unset, None, int]):
        company (Union[Unset, None, str]):
        position (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        profile_id (Union[Unset, None, int]):
        profile_translation_id (Union[Unset, None, int]):
        profile_translation (Union[Unset, None, CompanyUserProfileTranslationModel]):
    """

    profile_reference_id: Union[Unset, None, int] = UNSET
    company: Union[Unset, None, str] = UNSET
    position: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    profile_id: Union[Unset, None, int] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    profile_translation: Union[Unset, None, "CompanyUserProfileTranslationModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_reference_id = self.profile_reference_id
        company = self.company
        position = self.position
        text = self.text
        profile_id = self.profile_id
        profile_translation_id = self.profile_translation_id
        profile_translation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile_translation, Unset):
            profile_translation = self.profile_translation.to_dict() if self.profile_translation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if profile_reference_id is not UNSET:
            field_dict["profileReferenceId"] = profile_reference_id
        if company is not UNSET:
            field_dict["company"] = company
        if position is not UNSET:
            field_dict["position"] = position
        if text is not UNSET:
            field_dict["text"] = text
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

        d = src_dict.copy()
        profile_reference_id = d.pop("profileReferenceId", UNSET)

        company = d.pop("company", UNSET)

        position = d.pop("position", UNSET)

        text = d.pop("text", UNSET)

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

        company_user_profile_reference_translation_model = cls(
            profile_reference_id=profile_reference_id,
            company=company,
            position=position,
            text=text,
            profile_id=profile_id,
            profile_translation_id=profile_translation_id,
            profile_translation=profile_translation,
        )

        return company_user_profile_reference_translation_model
