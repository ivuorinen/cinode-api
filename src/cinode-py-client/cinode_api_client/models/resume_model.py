from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commitment_block_model import CommitmentBlockModel
    from ..models.education_block_model import EducationBlockModel
    from ..models.employer_block_model import EmployerBlockModel
    from ..models.extra_skill_block_model import ExtraSkillBlockModel
    from ..models.highlighted_work_experience_block_model import HighlightedWorkExperienceBlockModel
    from ..models.language_block_model import LanguageBlockModel
    from ..models.presentation_block_model import PresentationBlockModel
    from ..models.reference_block_model import ReferenceBlockModel
    from ..models.skill_by_category_block_model import SkillByCategoryBlockModel
    from ..models.skill_model_model import SkillModelModel
    from ..models.text_block_model import TextBlockModel
    from ..models.top_skill_block_model import TopSkillBlockModel
    from ..models.training_block_model import TrainingBlockModel
    from ..models.work_experience_block_model import WorkExperienceBlockModel


T = TypeVar("T", bound="ResumeModel")


@_attrs_define
class ResumeModel:
    """
    Attributes:
        presentation (Union[Unset, None, PresentationBlockModel]):
        highlighted_work_experience (Union[Unset, None, HighlightedWorkExperienceBlockModel]):
        skills_by_category (Union[Unset, None, SkillByCategoryBlockModel]):
        top_skills (Union[Unset, None, TopSkillBlockModel]):
        work_experience (Union[Unset, None, WorkExperienceBlockModel]):
        skills (Union[Unset, None, SkillModelModel]):
        employer (Union[Unset, None, EmployerBlockModel]):
        training (Union[Unset, None, TrainingBlockModel]):
        education (Union[Unset, None, EducationBlockModel]):
        language (Union[Unset, None, LanguageBlockModel]):
        commitment (Union[Unset, None, CommitmentBlockModel]):
        extra_skills (Union[Unset, None, ExtraSkillBlockModel]):
        reference (Union[Unset, None, ReferenceBlockModel]):
        text (Union[Unset, None, TextBlockModel]):
        id (Union[Unset, int]):
    """

    presentation: Union[Unset, None, "PresentationBlockModel"] = UNSET
    highlighted_work_experience: Union[Unset, None, "HighlightedWorkExperienceBlockModel"] = UNSET
    skills_by_category: Union[Unset, None, "SkillByCategoryBlockModel"] = UNSET
    top_skills: Union[Unset, None, "TopSkillBlockModel"] = UNSET
    work_experience: Union[Unset, None, "WorkExperienceBlockModel"] = UNSET
    skills: Union[Unset, None, "SkillModelModel"] = UNSET
    employer: Union[Unset, None, "EmployerBlockModel"] = UNSET
    training: Union[Unset, None, "TrainingBlockModel"] = UNSET
    education: Union[Unset, None, "EducationBlockModel"] = UNSET
    language: Union[Unset, None, "LanguageBlockModel"] = UNSET
    commitment: Union[Unset, None, "CommitmentBlockModel"] = UNSET
    extra_skills: Union[Unset, None, "ExtraSkillBlockModel"] = UNSET
    reference: Union[Unset, None, "ReferenceBlockModel"] = UNSET
    text: Union[Unset, None, "TextBlockModel"] = UNSET
    id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        presentation: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.presentation, Unset):
            presentation = self.presentation.to_dict() if self.presentation else None

        highlighted_work_experience: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.highlighted_work_experience, Unset):
            highlighted_work_experience = (
                self.highlighted_work_experience.to_dict() if self.highlighted_work_experience else None
            )

        skills_by_category: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.skills_by_category, Unset):
            skills_by_category = self.skills_by_category.to_dict() if self.skills_by_category else None

        top_skills: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.top_skills, Unset):
            top_skills = self.top_skills.to_dict() if self.top_skills else None

        work_experience: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.work_experience, Unset):
            work_experience = self.work_experience.to_dict() if self.work_experience else None

        skills: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.skills, Unset):
            skills = self.skills.to_dict() if self.skills else None

        employer: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.employer, Unset):
            employer = self.employer.to_dict() if self.employer else None

        training: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.training, Unset):
            training = self.training.to_dict() if self.training else None

        education: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.education, Unset):
            education = self.education.to_dict() if self.education else None

        language: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict() if self.language else None

        commitment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.commitment, Unset):
            commitment = self.commitment.to_dict() if self.commitment else None

        extra_skills: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_skills, Unset):
            extra_skills = self.extra_skills.to_dict() if self.extra_skills else None

        reference: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.reference, Unset):
            reference = self.reference.to_dict() if self.reference else None

        text: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict() if self.text else None

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if highlighted_work_experience is not UNSET:
            field_dict["highlightedWorkExperience"] = highlighted_work_experience
        if skills_by_category is not UNSET:
            field_dict["skillsByCategory"] = skills_by_category
        if top_skills is not UNSET:
            field_dict["topSkills"] = top_skills
        if work_experience is not UNSET:
            field_dict["workExperience"] = work_experience
        if skills is not UNSET:
            field_dict["skills"] = skills
        if employer is not UNSET:
            field_dict["employer"] = employer
        if training is not UNSET:
            field_dict["training"] = training
        if education is not UNSET:
            field_dict["education"] = education
        if language is not UNSET:
            field_dict["language"] = language
        if commitment is not UNSET:
            field_dict["commitment"] = commitment
        if extra_skills is not UNSET:
            field_dict["extraSkills"] = extra_skills
        if reference is not UNSET:
            field_dict["reference"] = reference
        if text is not UNSET:
            field_dict["text"] = text
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commitment_block_model import CommitmentBlockModel
        from ..models.education_block_model import EducationBlockModel
        from ..models.employer_block_model import EmployerBlockModel
        from ..models.extra_skill_block_model import ExtraSkillBlockModel
        from ..models.highlighted_work_experience_block_model import HighlightedWorkExperienceBlockModel
        from ..models.language_block_model import LanguageBlockModel
        from ..models.presentation_block_model import PresentationBlockModel
        from ..models.reference_block_model import ReferenceBlockModel
        from ..models.skill_by_category_block_model import SkillByCategoryBlockModel
        from ..models.skill_model_model import SkillModelModel
        from ..models.text_block_model import TextBlockModel
        from ..models.top_skill_block_model import TopSkillBlockModel
        from ..models.training_block_model import TrainingBlockModel
        from ..models.work_experience_block_model import WorkExperienceBlockModel

        d = src_dict.copy()
        _presentation = d.pop("presentation", UNSET)
        presentation: Union[Unset, None, PresentationBlockModel]
        if _presentation is None:
            presentation = None
        elif isinstance(_presentation, Unset):
            presentation = UNSET
        else:
            presentation = PresentationBlockModel.from_dict(_presentation)

        _highlighted_work_experience = d.pop("highlightedWorkExperience", UNSET)
        highlighted_work_experience: Union[Unset, None, HighlightedWorkExperienceBlockModel]
        if _highlighted_work_experience is None:
            highlighted_work_experience = None
        elif isinstance(_highlighted_work_experience, Unset):
            highlighted_work_experience = UNSET
        else:
            highlighted_work_experience = HighlightedWorkExperienceBlockModel.from_dict(_highlighted_work_experience)

        _skills_by_category = d.pop("skillsByCategory", UNSET)
        skills_by_category: Union[Unset, None, SkillByCategoryBlockModel]
        if _skills_by_category is None:
            skills_by_category = None
        elif isinstance(_skills_by_category, Unset):
            skills_by_category = UNSET
        else:
            skills_by_category = SkillByCategoryBlockModel.from_dict(_skills_by_category)

        _top_skills = d.pop("topSkills", UNSET)
        top_skills: Union[Unset, None, TopSkillBlockModel]
        if _top_skills is None:
            top_skills = None
        elif isinstance(_top_skills, Unset):
            top_skills = UNSET
        else:
            top_skills = TopSkillBlockModel.from_dict(_top_skills)

        _work_experience = d.pop("workExperience", UNSET)
        work_experience: Union[Unset, None, WorkExperienceBlockModel]
        if _work_experience is None:
            work_experience = None
        elif isinstance(_work_experience, Unset):
            work_experience = UNSET
        else:
            work_experience = WorkExperienceBlockModel.from_dict(_work_experience)

        _skills = d.pop("skills", UNSET)
        skills: Union[Unset, None, SkillModelModel]
        if _skills is None:
            skills = None
        elif isinstance(_skills, Unset):
            skills = UNSET
        else:
            skills = SkillModelModel.from_dict(_skills)

        _employer = d.pop("employer", UNSET)
        employer: Union[Unset, None, EmployerBlockModel]
        if _employer is None:
            employer = None
        elif isinstance(_employer, Unset):
            employer = UNSET
        else:
            employer = EmployerBlockModel.from_dict(_employer)

        _training = d.pop("training", UNSET)
        training: Union[Unset, None, TrainingBlockModel]
        if _training is None:
            training = None
        elif isinstance(_training, Unset):
            training = UNSET
        else:
            training = TrainingBlockModel.from_dict(_training)

        _education = d.pop("education", UNSET)
        education: Union[Unset, None, EducationBlockModel]
        if _education is None:
            education = None
        elif isinstance(_education, Unset):
            education = UNSET
        else:
            education = EducationBlockModel.from_dict(_education)

        _language = d.pop("language", UNSET)
        language: Union[Unset, None, LanguageBlockModel]
        if _language is None:
            language = None
        elif isinstance(_language, Unset):
            language = UNSET
        else:
            language = LanguageBlockModel.from_dict(_language)

        _commitment = d.pop("commitment", UNSET)
        commitment: Union[Unset, None, CommitmentBlockModel]
        if _commitment is None:
            commitment = None
        elif isinstance(_commitment, Unset):
            commitment = UNSET
        else:
            commitment = CommitmentBlockModel.from_dict(_commitment)

        _extra_skills = d.pop("extraSkills", UNSET)
        extra_skills: Union[Unset, None, ExtraSkillBlockModel]
        if _extra_skills is None:
            extra_skills = None
        elif isinstance(_extra_skills, Unset):
            extra_skills = UNSET
        else:
            extra_skills = ExtraSkillBlockModel.from_dict(_extra_skills)

        _reference = d.pop("reference", UNSET)
        reference: Union[Unset, None, ReferenceBlockModel]
        if _reference is None:
            reference = None
        elif isinstance(_reference, Unset):
            reference = UNSET
        else:
            reference = ReferenceBlockModel.from_dict(_reference)

        _text = d.pop("text", UNSET)
        text: Union[Unset, None, TextBlockModel]
        if _text is None:
            text = None
        elif isinstance(_text, Unset):
            text = UNSET
        else:
            text = TextBlockModel.from_dict(_text)

        id = d.pop("id", UNSET)

        resume_model = cls(
            presentation=presentation,
            highlighted_work_experience=highlighted_work_experience,
            skills_by_category=skills_by_category,
            top_skills=top_skills,
            work_experience=work_experience,
            skills=skills,
            employer=employer,
            training=training,
            education=education,
            language=language,
            commitment=commitment,
            extra_skills=extra_skills,
            reference=reference,
            text=text,
            id=id,
        )

        return resume_model
