from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_language_branch_model import CompanyUserProfileLanguageBranchModel


T = TypeVar("T", bound="CompanyUserProfileTranslationModel")


@_attrs_define
class CompanyUserProfileTranslationModel:
    """
    Attributes:
        profile_translation_id (Union[Unset, None, int]):
        profile_id (Union[Unset, None, int]):
        language_branch_id (Union[Unset, None, int]):
        language_branch (Union[Unset, None, CompanyUserProfileLanguageBranchModel]):
    """

    profile_translation_id: Union[Unset, None, int] = UNSET
    profile_id: Union[Unset, None, int] = UNSET
    language_branch_id: Union[Unset, None, int] = UNSET
    language_branch: Union[Unset, None, "CompanyUserProfileLanguageBranchModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        profile_translation_id = self.profile_translation_id
        profile_id = self.profile_id
        language_branch_id = self.language_branch_id
        language_branch: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.language_branch, Unset):
            language_branch = self.language_branch.to_dict() if self.language_branch else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if profile_translation_id is not UNSET:
            field_dict["profileTranslationId"] = profile_translation_id
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if language_branch_id is not UNSET:
            field_dict["languageBranchId"] = language_branch_id
        if language_branch is not UNSET:
            field_dict["languageBranch"] = language_branch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_language_branch_model import CompanyUserProfileLanguageBranchModel

        d = src_dict.copy()
        profile_translation_id = d.pop("profileTranslationId", UNSET)

        profile_id = d.pop("profileId", UNSET)

        language_branch_id = d.pop("languageBranchId", UNSET)

        _language_branch = d.pop("languageBranch", UNSET)
        language_branch: Union[Unset, None, CompanyUserProfileLanguageBranchModel]
        if _language_branch is None:
            language_branch = None
        elif isinstance(_language_branch, Unset):
            language_branch = UNSET
        else:
            language_branch = CompanyUserProfileLanguageBranchModel.from_dict(_language_branch)

        company_user_profile_translation_model = cls(
            profile_translation_id=profile_translation_id,
            profile_id=profile_id,
            language_branch_id=language_branch_id,
            language_branch=language_branch,
        )

        return company_user_profile_translation_model
