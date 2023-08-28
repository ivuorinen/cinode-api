import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_profile_commitment_model import CompanyUserProfileCommitmentModel
    from ..models.company_user_profile_education_model import CompanyUserProfileEducationModel
    from ..models.company_user_profile_employer_model import CompanyUserProfileEmployerModel
    from ..models.company_user_profile_ext_skill_model import CompanyUserProfileExtSkillModel
    from ..models.company_user_profile_language_model import CompanyUserProfileLanguageModel
    from ..models.company_user_profile_presentation_model import CompanyUserProfilePresentationModel
    from ..models.company_user_profile_reference_model import CompanyUserProfileReferenceModel
    from ..models.company_user_profile_skill_model import CompanyUserProfileSkillModel
    from ..models.company_user_profile_training_model import CompanyUserProfileTrainingModel
    from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel
    from ..models.company_user_profile_work_experience_model import CompanyUserProfileWorkExperienceModel
    from ..models.link import Link


T = TypeVar("T", bound="CompanyUserProfileFullModel")


@_attrs_define
class CompanyUserProfileFullModel:
    """
    Attributes:
        employers (Union[Unset, None, List['CompanyUserProfileEmployerModel']]):
        work_experience (Union[Unset, None, List['CompanyUserProfileWorkExperienceModel']]):
        education (Union[Unset, None, List['CompanyUserProfileEducationModel']]):
        training (Union[Unset, None, List['CompanyUserProfileTrainingModel']]):
        references (Union[Unset, None, List['CompanyUserProfileReferenceModel']]):
        skills (Union[Unset, None, List['CompanyUserProfileSkillModel']]):
        ext_skills (Union[Unset, None, List['CompanyUserProfileExtSkillModel']]):
        commitments (Union[Unset, None, List['CompanyUserProfileCommitmentModel']]):
        languages (Union[Unset, None, List['CompanyUserProfileLanguageModel']]):
        user_id (Union[Unset, None, str]):
        id (Union[Unset, None, int]):
        company_id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        created_when (Union[Unset, None, datetime.datetime]):
        updated_when (Union[Unset, None, datetime.datetime]):
        published_when (Union[Unset, None, datetime.datetime]):
        presentation (Union[Unset, None, CompanyUserProfilePresentationModel]):
        profile_translation_id (Union[Unset, int]):
        profile_translation (Union[Unset, None, CompanyUserProfileTranslationModel]):
        translations (Union[Unset, None, List['CompanyUserProfileTranslationModel']]):
        links (Union[Unset, None, List['Link']]):
    """

    employers: Union[Unset, None, List["CompanyUserProfileEmployerModel"]] = UNSET
    work_experience: Union[Unset, None, List["CompanyUserProfileWorkExperienceModel"]] = UNSET
    education: Union[Unset, None, List["CompanyUserProfileEducationModel"]] = UNSET
    training: Union[Unset, None, List["CompanyUserProfileTrainingModel"]] = UNSET
    references: Union[Unset, None, List["CompanyUserProfileReferenceModel"]] = UNSET
    skills: Union[Unset, None, List["CompanyUserProfileSkillModel"]] = UNSET
    ext_skills: Union[Unset, None, List["CompanyUserProfileExtSkillModel"]] = UNSET
    commitments: Union[Unset, None, List["CompanyUserProfileCommitmentModel"]] = UNSET
    languages: Union[Unset, None, List["CompanyUserProfileLanguageModel"]] = UNSET
    user_id: Union[Unset, None, str] = UNSET
    id: Union[Unset, None, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    created_when: Union[Unset, None, datetime.datetime] = UNSET
    updated_when: Union[Unset, None, datetime.datetime] = UNSET
    published_when: Union[Unset, None, datetime.datetime] = UNSET
    presentation: Union[Unset, None, "CompanyUserProfilePresentationModel"] = UNSET
    profile_translation_id: Union[Unset, int] = UNSET
    profile_translation: Union[Unset, None, "CompanyUserProfileTranslationModel"] = UNSET
    translations: Union[Unset, None, List["CompanyUserProfileTranslationModel"]] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        employers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.employers, Unset):
            if self.employers is None:
                employers = None
            else:
                employers = []
                for employers_item_data in self.employers:
                    employers_item = employers_item_data.to_dict()

                    employers.append(employers_item)

        work_experience: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.work_experience, Unset):
            if self.work_experience is None:
                work_experience = None
            else:
                work_experience = []
                for work_experience_item_data in self.work_experience:
                    work_experience_item = work_experience_item_data.to_dict()

                    work_experience.append(work_experience_item)

        education: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.education, Unset):
            if self.education is None:
                education = None
            else:
                education = []
                for education_item_data in self.education:
                    education_item = education_item_data.to_dict()

                    education.append(education_item)

        training: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.training, Unset):
            if self.training is None:
                training = None
            else:
                training = []
                for training_item_data in self.training:
                    training_item = training_item_data.to_dict()

                    training.append(training_item)

        references: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            if self.references is None:
                references = None
            else:
                references = []
                for references_item_data in self.references:
                    references_item = references_item_data.to_dict()

                    references.append(references_item)

        skills: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skills, Unset):
            if self.skills is None:
                skills = None
            else:
                skills = []
                for skills_item_data in self.skills:
                    skills_item = skills_item_data.to_dict()

                    skills.append(skills_item)

        ext_skills: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ext_skills, Unset):
            if self.ext_skills is None:
                ext_skills = None
            else:
                ext_skills = []
                for ext_skills_item_data in self.ext_skills:
                    ext_skills_item = ext_skills_item_data.to_dict()

                    ext_skills.append(ext_skills_item)

        commitments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.commitments, Unset):
            if self.commitments is None:
                commitments = None
            else:
                commitments = []
                for commitments_item_data in self.commitments:
                    commitments_item = commitments_item_data.to_dict()

                    commitments.append(commitments_item)

        languages: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.languages, Unset):
            if self.languages is None:
                languages = None
            else:
                languages = []
                for languages_item_data in self.languages:
                    languages_item = languages_item_data.to_dict()

                    languages.append(languages_item)

        user_id = self.user_id
        id = self.id
        company_id = self.company_id
        company_user_id = self.company_user_id
        created_when: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_when, Unset):
            created_when = self.created_when.isoformat() if self.created_when else None

        updated_when: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_when, Unset):
            updated_when = self.updated_when.isoformat() if self.updated_when else None

        published_when: Union[Unset, None, str] = UNSET
        if not isinstance(self.published_when, Unset):
            published_when = self.published_when.isoformat() if self.published_when else None

        presentation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.presentation, Unset):
            presentation = self.presentation.to_dict() if self.presentation else None

        profile_translation_id = self.profile_translation_id
        profile_translation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile_translation, Unset):
            profile_translation = self.profile_translation.to_dict() if self.profile_translation else None

        translations: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            if self.translations is None:
                translations = None
            else:
                translations = []
                for translations_item_data in self.translations:
                    translations_item = translations_item_data.to_dict()

                    translations.append(translations_item)

        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if employers is not UNSET:
            field_dict["employers"] = employers
        if work_experience is not UNSET:
            field_dict["workExperience"] = work_experience
        if education is not UNSET:
            field_dict["education"] = education
        if training is not UNSET:
            field_dict["training"] = training
        if references is not UNSET:
            field_dict["references"] = references
        if skills is not UNSET:
            field_dict["skills"] = skills
        if ext_skills is not UNSET:
            field_dict["extSkills"] = ext_skills
        if commitments is not UNSET:
            field_dict["commitments"] = commitments
        if languages is not UNSET:
            field_dict["languages"] = languages
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if created_when is not UNSET:
            field_dict["createdWhen"] = created_when
        if updated_when is not UNSET:
            field_dict["updatedWhen"] = updated_when
        if published_when is not UNSET:
            field_dict["publishedWhen"] = published_when
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if profile_translation_id is not UNSET:
            field_dict["profileTranslationId"] = profile_translation_id
        if profile_translation is not UNSET:
            field_dict["profileTranslation"] = profile_translation
        if translations is not UNSET:
            field_dict["translations"] = translations
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_profile_commitment_model import CompanyUserProfileCommitmentModel
        from ..models.company_user_profile_education_model import CompanyUserProfileEducationModel
        from ..models.company_user_profile_employer_model import CompanyUserProfileEmployerModel
        from ..models.company_user_profile_ext_skill_model import CompanyUserProfileExtSkillModel
        from ..models.company_user_profile_language_model import CompanyUserProfileLanguageModel
        from ..models.company_user_profile_presentation_model import CompanyUserProfilePresentationModel
        from ..models.company_user_profile_reference_model import CompanyUserProfileReferenceModel
        from ..models.company_user_profile_skill_model import CompanyUserProfileSkillModel
        from ..models.company_user_profile_training_model import CompanyUserProfileTrainingModel
        from ..models.company_user_profile_translation_model import CompanyUserProfileTranslationModel
        from ..models.company_user_profile_work_experience_model import CompanyUserProfileWorkExperienceModel
        from ..models.link import Link

        d = src_dict.copy()
        employers = []
        _employers = d.pop("employers", UNSET)
        for employers_item_data in _employers or []:
            employers_item = CompanyUserProfileEmployerModel.from_dict(employers_item_data)

            employers.append(employers_item)

        work_experience = []
        _work_experience = d.pop("workExperience", UNSET)
        for work_experience_item_data in _work_experience or []:
            work_experience_item = CompanyUserProfileWorkExperienceModel.from_dict(work_experience_item_data)

            work_experience.append(work_experience_item)

        education = []
        _education = d.pop("education", UNSET)
        for education_item_data in _education or []:
            education_item = CompanyUserProfileEducationModel.from_dict(education_item_data)

            education.append(education_item)

        training = []
        _training = d.pop("training", UNSET)
        for training_item_data in _training or []:
            training_item = CompanyUserProfileTrainingModel.from_dict(training_item_data)

            training.append(training_item)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = CompanyUserProfileReferenceModel.from_dict(references_item_data)

            references.append(references_item)

        skills = []
        _skills = d.pop("skills", UNSET)
        for skills_item_data in _skills or []:
            skills_item = CompanyUserProfileSkillModel.from_dict(skills_item_data)

            skills.append(skills_item)

        ext_skills = []
        _ext_skills = d.pop("extSkills", UNSET)
        for ext_skills_item_data in _ext_skills or []:
            ext_skills_item = CompanyUserProfileExtSkillModel.from_dict(ext_skills_item_data)

            ext_skills.append(ext_skills_item)

        commitments = []
        _commitments = d.pop("commitments", UNSET)
        for commitments_item_data in _commitments or []:
            commitments_item = CompanyUserProfileCommitmentModel.from_dict(commitments_item_data)

            commitments.append(commitments_item)

        languages = []
        _languages = d.pop("languages", UNSET)
        for languages_item_data in _languages or []:
            languages_item = CompanyUserProfileLanguageModel.from_dict(languages_item_data)

            languages.append(languages_item)

        user_id = d.pop("userId", UNSET)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        _created_when = d.pop("createdWhen", UNSET)
        created_when: Union[Unset, None, datetime.datetime]
        if _created_when is None:
            created_when = None
        elif isinstance(_created_when, Unset):
            created_when = UNSET
        else:
            created_when = isoparse(_created_when)

        _updated_when = d.pop("updatedWhen", UNSET)
        updated_when: Union[Unset, None, datetime.datetime]
        if _updated_when is None:
            updated_when = None
        elif isinstance(_updated_when, Unset):
            updated_when = UNSET
        else:
            updated_when = isoparse(_updated_when)

        _published_when = d.pop("publishedWhen", UNSET)
        published_when: Union[Unset, None, datetime.datetime]
        if _published_when is None:
            published_when = None
        elif isinstance(_published_when, Unset):
            published_when = UNSET
        else:
            published_when = isoparse(_published_when)

        _presentation = d.pop("presentation", UNSET)
        presentation: Union[Unset, None, CompanyUserProfilePresentationModel]
        if _presentation is None:
            presentation = None
        elif isinstance(_presentation, Unset):
            presentation = UNSET
        else:
            presentation = CompanyUserProfilePresentationModel.from_dict(_presentation)

        profile_translation_id = d.pop("profileTranslationId", UNSET)

        _profile_translation = d.pop("profileTranslation", UNSET)
        profile_translation: Union[Unset, None, CompanyUserProfileTranslationModel]
        if _profile_translation is None:
            profile_translation = None
        elif isinstance(_profile_translation, Unset):
            profile_translation = UNSET
        else:
            profile_translation = CompanyUserProfileTranslationModel.from_dict(_profile_translation)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = CompanyUserProfileTranslationModel.from_dict(translations_item_data)

            translations.append(translations_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_profile_full_model = cls(
            employers=employers,
            work_experience=work_experience,
            education=education,
            training=training,
            references=references,
            skills=skills,
            ext_skills=ext_skills,
            commitments=commitments,
            languages=languages,
            user_id=user_id,
            id=id,
            company_id=company_id,
            company_user_id=company_user_id,
            created_when=created_when,
            updated_when=updated_when,
            published_when=published_when,
            presentation=presentation,
            profile_translation_id=profile_translation_id,
            profile_translation=profile_translation,
            translations=translations,
            links=links,
        )

        return company_user_profile_full_model
