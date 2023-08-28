from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel


T = TypeVar("T", bound="CompanyUserProfileTrainingTranslationModel")


@_attrs_define
class CompanyUserProfileTrainingTranslationModel:
    """
    Attributes:
        profile_training_id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        issuer (Union[Unset, None, str]):
        supplier (Union[Unset, None, str]):
        profile_id (Union[Unset, None, int]):
        profile_translation_id (Union[Unset, None, int]):
        profile_translation (Union[Unset, None, CompanyUserProfileTranslationModel]):
    """

    profile_training_id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    issuer: Union[Unset, None, str] = UNSET
    supplier: Union[Unset, None, str] = UNSET
    profile_id: Union[Unset, None, int] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    profile_translation: Union[Unset, None, "CompanyUserProfileTranslationModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_training_id = self.profile_training_id
        title = self.title
        description = self.description
        issuer = self.issuer
        supplier = self.supplier
        profile_id = self.profile_id
        profile_translation_id = self.profile_translation_id
        profile_translation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile_translation, Unset):
            profile_translation = self.profile_translation.to_dict() if self.profile_translation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if profile_training_id is not UNSET:
            field_dict["profileTrainingId"] = profile_training_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
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
        profile_training_id = d.pop("profileTrainingId", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        issuer = d.pop("issuer", UNSET)

        supplier = d.pop("supplier", UNSET)

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

        company_user_profile_training_translation_model = cls(
            profile_training_id=profile_training_id,
            title=title,
            description=description,
            issuer=issuer,
            supplier=supplier,
            profile_id=profile_id,
            profile_translation_id=profile_translation_id,
            profile_translation=profile_translation,
        )

        return company_user_profile_training_translation_model
