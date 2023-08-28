from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel


T = TypeVar("T", bound="CompanyUserProfileEducationTranslationModel")


@_attrs_define
class CompanyUserProfileEducationTranslationModel:
    """
    Attributes:
        profile_education_id (Union[Unset, None, int]):
        school_name (Union[Unset, None, str]):
        program_name (Union[Unset, None, str]):
        degree (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        profile_id (Union[Unset, None, int]):
        profile_translation_id (Union[Unset, None, int]):
        profile_translation (Union[Unset, None, CompanyUserProfileTranslationModel]):
    """

    profile_education_id: Union[Unset, None, int] = UNSET
    school_name: Union[Unset, None, str] = UNSET
    program_name: Union[Unset, None, str] = UNSET
    degree: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    profile_id: Union[Unset, None, int] = UNSET
    profile_translation_id: Union[Unset, None, int] = UNSET
    profile_translation: Union[Unset, None, "CompanyUserProfileTranslationModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_education_id = self.profile_education_id
        school_name = self.school_name
        program_name = self.program_name
        degree = self.degree
        description = self.description
        profile_id = self.profile_id
        profile_translation_id = self.profile_translation_id
        profile_translation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile_translation, Unset):
            profile_translation = self.profile_translation.to_dict() if self.profile_translation else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if profile_education_id is not UNSET:
            field_dict["profileEducationId"] = profile_education_id
        if school_name is not UNSET:
            field_dict["schoolName"] = school_name
        if program_name is not UNSET:
            field_dict["programName"] = program_name
        if degree is not UNSET:
            field_dict["degree"] = degree
        if description is not UNSET:
            field_dict["description"] = description
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
        profile_education_id = d.pop("profileEducationId", UNSET)

        school_name = d.pop("schoolName", UNSET)

        program_name = d.pop("programName", UNSET)

        degree = d.pop("degree", UNSET)

        description = d.pop("description", UNSET)

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

        company_user_profile_education_translation_model = cls(
            profile_education_id=profile_education_id,
            school_name=school_name,
            program_name=program_name,
            degree=degree,
            description=description,
            profile_id=profile_id,
            profile_translation_id=profile_translation_id,
            profile_translation=profile_translation,
        )

        return company_user_profile_education_translation_model
