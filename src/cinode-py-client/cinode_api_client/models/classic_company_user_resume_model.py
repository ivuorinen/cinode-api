from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_resume_template_base_model import CompanyResumeTemplateBaseModel
    from ..models.company_resume_template_language_model import CompanyResumeTemplateLanguageModel
    from ..models.created_model import CreatedModel
    from ..models.link import Link
    from ..models.resume_model import ResumeModel
    from ..models.updated_model import UpdatedModel


T = TypeVar("T", bound="ClassicCompanyUserResumeModel")


@_attrs_define
class ClassicCompanyUserResumeModel:
    """
    Attributes:
        image_id (Union[Unset, None, int]):
        parent_profile_id (Union[Unset, int]):
        profile_translation_id (Union[Unset, int]):
        parent_company_user_resume_id (Union[Unset, None, int]):
        resume (Union[Unset, None, ResumeModel]):
        id (Union[Unset, None, int]):
        company_user_id (Union[Unset, None, int]):
        company_id (Union[Unset, None, int]):
        created (Union[Unset, None, CreatedModel]):
        updated (Union[Unset, None, UpdatedModel]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        slug (Union[Unset, None, str]):
        language (Union[Unset, None, CompanyResumeTemplateLanguageModel]):
        template (Union[Unset, None, CompanyResumeTemplateBaseModel]):
        is_public (Union[Unset, bool]):
        links (Union[Unset, None, List['Link']]):
    """

    image_id: Union[Unset, None, int] = UNSET
    parent_profile_id: Union[Unset, int] = UNSET
    profile_translation_id: Union[Unset, int] = UNSET
    parent_company_user_resume_id: Union[Unset, None, int] = UNSET
    resume: Union[Unset, None, "ResumeModel"] = UNSET
    id: Union[Unset, None, int] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    created: Union[Unset, None, "CreatedModel"] = UNSET
    updated: Union[Unset, None, "UpdatedModel"] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    slug: Union[Unset, None, str] = UNSET
    language: Union[Unset, None, "CompanyResumeTemplateLanguageModel"] = UNSET
    template: Union[Unset, None, "CompanyResumeTemplateBaseModel"] = UNSET
    is_public: Union[Unset, bool] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        image_id = self.image_id
        parent_profile_id = self.parent_profile_id
        profile_translation_id = self.profile_translation_id
        parent_company_user_resume_id = self.parent_company_user_resume_id
        resume: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.resume, Unset):
            resume = self.resume.to_dict() if self.resume else None

        id = self.id
        company_user_id = self.company_user_id
        company_id = self.company_id
        created: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict() if self.created else None

        updated: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.to_dict() if self.updated else None

        title = self.title
        description = self.description
        slug = self.slug
        language: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict() if self.language else None

        template: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict() if self.template else None

        is_public = self.is_public
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
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if parent_profile_id is not UNSET:
            field_dict["parentProfileId"] = parent_profile_id
        if profile_translation_id is not UNSET:
            field_dict["profileTranslationId"] = profile_translation_id
        if parent_company_user_resume_id is not UNSET:
            field_dict["parentCompanyUserResumeId"] = parent_company_user_resume_id
        if resume is not UNSET:
            field_dict["resume"] = resume
        if id is not UNSET:
            field_dict["id"] = id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if slug is not UNSET:
            field_dict["slug"] = slug
        if language is not UNSET:
            field_dict["language"] = language
        if template is not UNSET:
            field_dict["template"] = template
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_resume_template_base_model import CompanyResumeTemplateBaseModel
        from ..models.company_resume_template_language_model import CompanyResumeTemplateLanguageModel
        from ..models.created_model import CreatedModel
        from ..models.link import Link
        from ..models.resume_model import ResumeModel
        from ..models.updated_model import UpdatedModel

        d = src_dict.copy()
        image_id = d.pop("imageId", UNSET)

        parent_profile_id = d.pop("parentProfileId", UNSET)

        profile_translation_id = d.pop("profileTranslationId", UNSET)

        parent_company_user_resume_id = d.pop("parentCompanyUserResumeId", UNSET)

        _resume = d.pop("resume", UNSET)
        resume: Union[Unset, None, ResumeModel]
        if _resume is None:
            resume = None
        elif isinstance(_resume, Unset):
            resume = UNSET
        else:
            resume = ResumeModel.from_dict(_resume)

        id = d.pop("id", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        company_id = d.pop("companyId", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, CreatedModel]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = CreatedModel.from_dict(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, UpdatedModel]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = UpdatedModel.from_dict(_updated)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        slug = d.pop("slug", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, None, CompanyResumeTemplateLanguageModel]
        if _language is None:
            language = None
        elif isinstance(_language, Unset):
            language = UNSET
        else:
            language = CompanyResumeTemplateLanguageModel.from_dict(_language)

        _template = d.pop("template", UNSET)
        template: Union[Unset, None, CompanyResumeTemplateBaseModel]
        if _template is None:
            template = None
        elif isinstance(_template, Unset):
            template = UNSET
        else:
            template = CompanyResumeTemplateBaseModel.from_dict(_template)

        is_public = d.pop("isPublic", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        classic_company_user_resume_model = cls(
            image_id=image_id,
            parent_profile_id=parent_profile_id,
            profile_translation_id=profile_translation_id,
            parent_company_user_resume_id=parent_company_user_resume_id,
            resume=resume,
            id=id,
            company_user_id=company_user_id,
            company_id=company_id,
            created=created,
            updated=updated,
            title=title,
            description=description,
            slug=slug,
            language=language,
            template=template,
            is_public=is_public,
            links=links,
        )

        return classic_company_user_resume_model
