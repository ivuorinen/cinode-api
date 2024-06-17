from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateCompanyUserProfileImportMultipartData")


@_attrs_define
class CreateCompanyUserProfileImportMultipartData:
    """
    Attributes:
        file (File):
        import_skills (Union[Unset, bool]):
        map_skill_experience_years_to_level (Union[Unset, bool]):
    """

    file: File
    import_skills: Union[Unset, bool] = UNSET
    map_skill_experience_years_to_level: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        import_skills = self.import_skills
        map_skill_experience_years_to_level = self.map_skill_experience_years_to_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "File": file,
            }
        )
        if import_skills is not UNSET:
            field_dict["ImportSkills"] = import_skills
        if map_skill_experience_years_to_level is not UNSET:
            field_dict["MapSkillExperienceYearsToLevel"] = map_skill_experience_years_to_level

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        import_skills = (
            self.import_skills
            if isinstance(self.import_skills, Unset)
            else (None, str(self.import_skills).encode(), "text/plain")
        )
        map_skill_experience_years_to_level = (
            self.map_skill_experience_years_to_level
            if isinstance(self.map_skill_experience_years_to_level, Unset)
            else (None, str(self.map_skill_experience_years_to_level).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "File": file,
            }
        )
        if import_skills is not UNSET:
            field_dict["ImportSkills"] = import_skills
        if map_skill_experience_years_to_level is not UNSET:
            field_dict["MapSkillExperienceYearsToLevel"] = map_skill_experience_years_to_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("File")))

        import_skills = d.pop("ImportSkills", UNSET)

        map_skill_experience_years_to_level = d.pop("MapSkillExperienceYearsToLevel", UNSET)

        create_company_user_profile_import_multipart_data = cls(
            file=file,
            import_skills=import_skills,
            map_skill_experience_years_to_level=map_skill_experience_years_to_level,
        )

        create_company_user_profile_import_multipart_data.additional_properties = d
        return create_company_user_profile_import_multipart_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
