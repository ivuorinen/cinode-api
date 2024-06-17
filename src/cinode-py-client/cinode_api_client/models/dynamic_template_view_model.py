import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.image_size import ImageSize
from ..models.pdf_engine_type import PdfEngineType
from ..models.pdf_orientation import PdfOrientation
from ..models.template_asset_type import TemplateAssetType
from ..models.word_engine_type import WordEngineType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_info_block_view_model import CompanyUserInfoBlockViewModel
    from ..models.dynamic_template_view_model_primary_script_assets import DynamicTemplateViewModelPrimaryScriptAssets
    from ..models.dynamic_template_view_model_primary_style_assets import DynamicTemplateViewModelPrimaryStyleAssets
    from ..models.i_contact_info_view_model import IContactInfoViewModel
    from ..models.i_dynamic_block_view_model import IDynamicBlockViewModel
    from ..models.i_template_company import ITemplateCompany
    from ..models.i_template_logotype import ITemplateLogotype
    from ..models.i_template_profile_image import ITemplateProfileImage
    from ..models.i_template_shared_asset_view_model import ITemplateSharedAssetViewModel
    from ..models.i_template_style_asset_view_model import ITemplateStyleAssetViewModel
    from ..models.i_template_user_info import ITemplateUserInfo


T = TypeVar("T", bound="DynamicTemplateViewModel")


@_attrs_define
class DynamicTemplateViewModel:
    """
    Attributes:
        title (str):
        blocks (Union[Unset, None, List['IDynamicBlockViewModel']]):
        logotype (Union[Unset, None, ITemplateLogotype]):
        id (Union[Unset, int]):
        resume_template_id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        company_user_id (Union[Unset, int]):
        slug (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        logotype_id (Union[Unset, None, int]):
        word_enabled (Union[Unset, bool]):
        profile_image_size (Union[Unset, ImageSize]):

            Original = 0

            H40W40 = 1

            H100W100 = 2

            H200W200 = 3

            H300W300 = 4

            W100 = 5

            H60 = 6

            H100 = 7

            H40 = 8

            W340 = 9

            W1800 = 10

            H750W1800 = 11

            H250 = 12

            H400W400 = 13

            W150 = 14

            W1200 = 15
        allow_no_profile_image (Union[Unset, bool]):
        hide_profile_image_in_edit (Union[Unset, bool]):
        company_logotype_image_size (Union[Unset, ImageSize]):

            Original = 0

            H40W40 = 1

            H100W100 = 2

            H200W200 = 3

            H300W300 = 4

            W100 = 5

            H60 = 6

            H100 = 7

            H40 = 8

            W340 = 9

            W1800 = 10

            H750W1800 = 11

            H250 = 12

            H400W400 = 13

            W150 = 14

            W1200 = 15
        pdf_engine_type (Union[Unset, PdfEngineType]):

            WkHtmlToPdf = 0

            Puppeteer = 2
        word_engine_type (Union[Unset, WordEngineType]):

            None = 0

            GroupDocs = 1

            Aspose = 2
        pdf_orientation (Union[Unset, PdfOrientation]):

            Portrait = 0

            Landscape = 1
        pdf_margin_top (Union[Unset, int]):
        pdf_margin_right (Union[Unset, int]):
        pdf_margin_bottom (Union[Unset, int]):
        pdf_margin_left (Union[Unset, int]):
        custom_footer_for_wkhtml (Union[Unset, bool]):
        pdf_footer (Union[Unset, bool]):
        show_preview_toggle (Union[Unset, bool]):
        contact_info_id (Union[Unset, None, int]):
        contact_info (Union[Unset, None, IContactInfoViewModel]):
        user_info (Union[Unset, None, ITemplateUserInfo]):
        company_user_info (Union[Unset, None, CompanyUserInfoBlockViewModel]):
        profile_image (Union[Unset, None, ITemplateProfileImage]):
        company (Union[Unset, None, ITemplateCompany]):
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, None, datetime.datetime]):
        language_branch_id (Union[Unset, None, int]):
        is_public (Union[Unset, bool]):
        locked (Union[Unset, bool]):
        current_language (Union[Unset, None, str]):
        style_assets (Union[Unset, None, List['ITemplateStyleAssetViewModel']]):
        customer_managed_style_asset (Union[Unset, None, ITemplateStyleAssetViewModel]):
        shared_style_assets (Union[Unset, None, List['ITemplateSharedAssetViewModel']]):
        shared_script_assets (Union[Unset, None, List['ITemplateSharedAssetViewModel']]):
        shared_font_assets (Union[Unset, None, List['ITemplateSharedAssetViewModel']]):
        primary_style_assets (Union[Unset, None, DynamicTemplateViewModelPrimaryStyleAssets]):
        primary_script_assets (Union[Unset, None, DynamicTemplateViewModelPrimaryScriptAssets]):
        template_asset_types (Union[Unset, None, List[TemplateAssetType]]):
        is_answering_to_request (Union[Unset, bool]):
    """

    title: str
    blocks: Union[Unset, None, List["IDynamicBlockViewModel"]] = UNSET
    logotype: Union[Unset, None, "ITemplateLogotype"] = UNSET
    id: Union[Unset, int] = UNSET
    resume_template_id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, int] = UNSET
    slug: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    logotype_id: Union[Unset, None, int] = UNSET
    word_enabled: Union[Unset, bool] = UNSET
    profile_image_size: Union[Unset, ImageSize] = UNSET
    allow_no_profile_image: Union[Unset, bool] = UNSET
    hide_profile_image_in_edit: Union[Unset, bool] = UNSET
    company_logotype_image_size: Union[Unset, ImageSize] = UNSET
    pdf_engine_type: Union[Unset, PdfEngineType] = UNSET
    word_engine_type: Union[Unset, WordEngineType] = UNSET
    pdf_orientation: Union[Unset, PdfOrientation] = UNSET
    pdf_margin_top: Union[Unset, int] = UNSET
    pdf_margin_right: Union[Unset, int] = UNSET
    pdf_margin_bottom: Union[Unset, int] = UNSET
    pdf_margin_left: Union[Unset, int] = UNSET
    custom_footer_for_wkhtml: Union[Unset, bool] = UNSET
    pdf_footer: Union[Unset, bool] = UNSET
    show_preview_toggle: Union[Unset, bool] = UNSET
    contact_info_id: Union[Unset, None, int] = UNSET
    contact_info: Union[Unset, None, "IContactInfoViewModel"] = UNSET
    user_info: Union[Unset, None, "ITemplateUserInfo"] = UNSET
    company_user_info: Union[Unset, None, "CompanyUserInfoBlockViewModel"] = UNSET
    profile_image: Union[Unset, None, "ITemplateProfileImage"] = UNSET
    company: Union[Unset, None, "ITemplateCompany"] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    language_branch_id: Union[Unset, None, int] = UNSET
    is_public: Union[Unset, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    current_language: Union[Unset, None, str] = UNSET
    style_assets: Union[Unset, None, List["ITemplateStyleAssetViewModel"]] = UNSET
    customer_managed_style_asset: Union[Unset, None, "ITemplateStyleAssetViewModel"] = UNSET
    shared_style_assets: Union[Unset, None, List["ITemplateSharedAssetViewModel"]] = UNSET
    shared_script_assets: Union[Unset, None, List["ITemplateSharedAssetViewModel"]] = UNSET
    shared_font_assets: Union[Unset, None, List["ITemplateSharedAssetViewModel"]] = UNSET
    primary_style_assets: Union[Unset, None, "DynamicTemplateViewModelPrimaryStyleAssets"] = UNSET
    primary_script_assets: Union[Unset, None, "DynamicTemplateViewModelPrimaryScriptAssets"] = UNSET
    template_asset_types: Union[Unset, None, List[TemplateAssetType]] = UNSET
    is_answering_to_request: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        blocks: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.blocks, Unset):
            if self.blocks is None:
                blocks = None
            else:
                blocks = []
                for blocks_item_data in self.blocks:
                    blocks_item = blocks_item_data.to_dict()

                    blocks.append(blocks_item)

        logotype: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.logotype, Unset):
            logotype = self.logotype.to_dict() if self.logotype else None

        id = self.id
        resume_template_id = self.resume_template_id
        company_id = self.company_id
        company_user_id = self.company_user_id
        slug = self.slug
        description = self.description
        logotype_id = self.logotype_id
        word_enabled = self.word_enabled
        profile_image_size: Union[Unset, int] = UNSET
        if not isinstance(self.profile_image_size, Unset):
            profile_image_size = self.profile_image_size.value

        allow_no_profile_image = self.allow_no_profile_image
        hide_profile_image_in_edit = self.hide_profile_image_in_edit
        company_logotype_image_size: Union[Unset, int] = UNSET
        if not isinstance(self.company_logotype_image_size, Unset):
            company_logotype_image_size = self.company_logotype_image_size.value

        pdf_engine_type: Union[Unset, int] = UNSET
        if not isinstance(self.pdf_engine_type, Unset):
            pdf_engine_type = self.pdf_engine_type.value

        word_engine_type: Union[Unset, int] = UNSET
        if not isinstance(self.word_engine_type, Unset):
            word_engine_type = self.word_engine_type.value

        pdf_orientation: Union[Unset, int] = UNSET
        if not isinstance(self.pdf_orientation, Unset):
            pdf_orientation = self.pdf_orientation.value

        pdf_margin_top = self.pdf_margin_top
        pdf_margin_right = self.pdf_margin_right
        pdf_margin_bottom = self.pdf_margin_bottom
        pdf_margin_left = self.pdf_margin_left
        custom_footer_for_wkhtml = self.custom_footer_for_wkhtml
        pdf_footer = self.pdf_footer
        show_preview_toggle = self.show_preview_toggle
        contact_info_id = self.contact_info_id
        contact_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_info, Unset):
            contact_info = self.contact_info.to_dict() if self.contact_info else None

        user_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict() if self.user_info else None

        company_user_info: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company_user_info, Unset):
            company_user_info = self.company_user_info.to_dict() if self.company_user_info else None

        profile_image: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.profile_image, Unset):
            profile_image = self.profile_image.to_dict() if self.profile_image else None

        company: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict() if self.company else None

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        language_branch_id = self.language_branch_id
        is_public = self.is_public
        locked = self.locked
        current_language = self.current_language
        style_assets: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.style_assets, Unset):
            if self.style_assets is None:
                style_assets = None
            else:
                style_assets = []
                for style_assets_item_data in self.style_assets:
                    style_assets_item = style_assets_item_data.to_dict()

                    style_assets.append(style_assets_item)

        customer_managed_style_asset: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.customer_managed_style_asset, Unset):
            customer_managed_style_asset = (
                self.customer_managed_style_asset.to_dict() if self.customer_managed_style_asset else None
            )

        shared_style_assets: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shared_style_assets, Unset):
            if self.shared_style_assets is None:
                shared_style_assets = None
            else:
                shared_style_assets = []
                for shared_style_assets_item_data in self.shared_style_assets:
                    shared_style_assets_item = shared_style_assets_item_data.to_dict()

                    shared_style_assets.append(shared_style_assets_item)

        shared_script_assets: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shared_script_assets, Unset):
            if self.shared_script_assets is None:
                shared_script_assets = None
            else:
                shared_script_assets = []
                for shared_script_assets_item_data in self.shared_script_assets:
                    shared_script_assets_item = shared_script_assets_item_data.to_dict()

                    shared_script_assets.append(shared_script_assets_item)

        shared_font_assets: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shared_font_assets, Unset):
            if self.shared_font_assets is None:
                shared_font_assets = None
            else:
                shared_font_assets = []
                for shared_font_assets_item_data in self.shared_font_assets:
                    shared_font_assets_item = shared_font_assets_item_data.to_dict()

                    shared_font_assets.append(shared_font_assets_item)

        primary_style_assets: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.primary_style_assets, Unset):
            primary_style_assets = self.primary_style_assets.to_dict() if self.primary_style_assets else None

        primary_script_assets: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.primary_script_assets, Unset):
            primary_script_assets = self.primary_script_assets.to_dict() if self.primary_script_assets else None

        template_asset_types: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.template_asset_types, Unset):
            if self.template_asset_types is None:
                template_asset_types = None
            else:
                template_asset_types = []
                for template_asset_types_item_data in self.template_asset_types:
                    template_asset_types_item = template_asset_types_item_data.value

                    template_asset_types.append(template_asset_types_item)

        is_answering_to_request = self.is_answering_to_request

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
            }
        )
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if logotype is not UNSET:
            field_dict["logotype"] = logotype
        if id is not UNSET:
            field_dict["id"] = id
        if resume_template_id is not UNSET:
            field_dict["resumeTemplateId"] = resume_template_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if logotype_id is not UNSET:
            field_dict["logotypeId"] = logotype_id
        if word_enabled is not UNSET:
            field_dict["wordEnabled"] = word_enabled
        if profile_image_size is not UNSET:
            field_dict["profileImageSize"] = profile_image_size
        if allow_no_profile_image is not UNSET:
            field_dict["allowNoProfileImage"] = allow_no_profile_image
        if hide_profile_image_in_edit is not UNSET:
            field_dict["hideProfileImageInEdit"] = hide_profile_image_in_edit
        if company_logotype_image_size is not UNSET:
            field_dict["companyLogotypeImageSize"] = company_logotype_image_size
        if pdf_engine_type is not UNSET:
            field_dict["pdfEngineType"] = pdf_engine_type
        if word_engine_type is not UNSET:
            field_dict["wordEngineType"] = word_engine_type
        if pdf_orientation is not UNSET:
            field_dict["pdfOrientation"] = pdf_orientation
        if pdf_margin_top is not UNSET:
            field_dict["pdfMarginTop"] = pdf_margin_top
        if pdf_margin_right is not UNSET:
            field_dict["pdfMarginRight"] = pdf_margin_right
        if pdf_margin_bottom is not UNSET:
            field_dict["pdfMarginBottom"] = pdf_margin_bottom
        if pdf_margin_left is not UNSET:
            field_dict["pdfMarginLeft"] = pdf_margin_left
        if custom_footer_for_wkhtml is not UNSET:
            field_dict["customFooterForWkhtml"] = custom_footer_for_wkhtml
        if pdf_footer is not UNSET:
            field_dict["pdfFooter"] = pdf_footer
        if show_preview_toggle is not UNSET:
            field_dict["showPreviewToggle"] = show_preview_toggle
        if contact_info_id is not UNSET:
            field_dict["contactInfoId"] = contact_info_id
        if contact_info is not UNSET:
            field_dict["contactInfo"] = contact_info
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info
        if company_user_info is not UNSET:
            field_dict["companyUserInfo"] = company_user_info
        if profile_image is not UNSET:
            field_dict["profileImage"] = profile_image
        if company is not UNSET:
            field_dict["company"] = company
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if language_branch_id is not UNSET:
            field_dict["languageBranchId"] = language_branch_id
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if locked is not UNSET:
            field_dict["locked"] = locked
        if current_language is not UNSET:
            field_dict["currentLanguage"] = current_language
        if style_assets is not UNSET:
            field_dict["styleAssets"] = style_assets
        if customer_managed_style_asset is not UNSET:
            field_dict["customerManagedStyleAsset"] = customer_managed_style_asset
        if shared_style_assets is not UNSET:
            field_dict["sharedStyleAssets"] = shared_style_assets
        if shared_script_assets is not UNSET:
            field_dict["sharedScriptAssets"] = shared_script_assets
        if shared_font_assets is not UNSET:
            field_dict["sharedFontAssets"] = shared_font_assets
        if primary_style_assets is not UNSET:
            field_dict["primaryStyleAssets"] = primary_style_assets
        if primary_script_assets is not UNSET:
            field_dict["primaryScriptAssets"] = primary_script_assets
        if template_asset_types is not UNSET:
            field_dict["templateAssetTypes"] = template_asset_types
        if is_answering_to_request is not UNSET:
            field_dict["isAnsweringToRequest"] = is_answering_to_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_info_block_view_model import CompanyUserInfoBlockViewModel
        from ..models.dynamic_template_view_model_primary_script_assets import (
            DynamicTemplateViewModelPrimaryScriptAssets,
        )
        from ..models.dynamic_template_view_model_primary_style_assets import DynamicTemplateViewModelPrimaryStyleAssets
        from ..models.i_contact_info_view_model import IContactInfoViewModel
        from ..models.i_dynamic_block_view_model import IDynamicBlockViewModel
        from ..models.i_template_company import ITemplateCompany
        from ..models.i_template_logotype import ITemplateLogotype
        from ..models.i_template_profile_image import ITemplateProfileImage
        from ..models.i_template_shared_asset_view_model import ITemplateSharedAssetViewModel
        from ..models.i_template_style_asset_view_model import ITemplateStyleAssetViewModel
        from ..models.i_template_user_info import ITemplateUserInfo

        d = src_dict.copy()
        title = d.pop("title")

        blocks = []
        _blocks = d.pop("blocks", UNSET)
        for blocks_item_data in _blocks or []:
            blocks_item = IDynamicBlockViewModel.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        _logotype = d.pop("logotype", UNSET)
        logotype: Union[Unset, None, ITemplateLogotype]
        if _logotype is None:
            logotype = None
        elif isinstance(_logotype, Unset):
            logotype = UNSET
        else:
            logotype = ITemplateLogotype.from_dict(_logotype)

        id = d.pop("id", UNSET)

        resume_template_id = d.pop("resumeTemplateId", UNSET)

        company_id = d.pop("companyId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        logotype_id = d.pop("logotypeId", UNSET)

        word_enabled = d.pop("wordEnabled", UNSET)

        _profile_image_size = d.pop("profileImageSize", UNSET)
        profile_image_size: Union[Unset, ImageSize]
        if isinstance(_profile_image_size, Unset):
            profile_image_size = UNSET
        else:
            profile_image_size = ImageSize(_profile_image_size)

        allow_no_profile_image = d.pop("allowNoProfileImage", UNSET)

        hide_profile_image_in_edit = d.pop("hideProfileImageInEdit", UNSET)

        _company_logotype_image_size = d.pop("companyLogotypeImageSize", UNSET)
        company_logotype_image_size: Union[Unset, ImageSize]
        if isinstance(_company_logotype_image_size, Unset):
            company_logotype_image_size = UNSET
        else:
            company_logotype_image_size = ImageSize(_company_logotype_image_size)

        _pdf_engine_type = d.pop("pdfEngineType", UNSET)
        pdf_engine_type: Union[Unset, PdfEngineType]
        if isinstance(_pdf_engine_type, Unset):
            pdf_engine_type = UNSET
        else:
            pdf_engine_type = PdfEngineType(_pdf_engine_type)

        _word_engine_type = d.pop("wordEngineType", UNSET)
        word_engine_type: Union[Unset, WordEngineType]
        if isinstance(_word_engine_type, Unset):
            word_engine_type = UNSET
        else:
            word_engine_type = WordEngineType(_word_engine_type)

        _pdf_orientation = d.pop("pdfOrientation", UNSET)
        pdf_orientation: Union[Unset, PdfOrientation]
        if isinstance(_pdf_orientation, Unset):
            pdf_orientation = UNSET
        else:
            pdf_orientation = PdfOrientation(_pdf_orientation)

        pdf_margin_top = d.pop("pdfMarginTop", UNSET)

        pdf_margin_right = d.pop("pdfMarginRight", UNSET)

        pdf_margin_bottom = d.pop("pdfMarginBottom", UNSET)

        pdf_margin_left = d.pop("pdfMarginLeft", UNSET)

        custom_footer_for_wkhtml = d.pop("customFooterForWkhtml", UNSET)

        pdf_footer = d.pop("pdfFooter", UNSET)

        show_preview_toggle = d.pop("showPreviewToggle", UNSET)

        contact_info_id = d.pop("contactInfoId", UNSET)

        _contact_info = d.pop("contactInfo", UNSET)
        contact_info: Union[Unset, None, IContactInfoViewModel]
        if _contact_info is None:
            contact_info = None
        elif isinstance(_contact_info, Unset):
            contact_info = UNSET
        else:
            contact_info = IContactInfoViewModel.from_dict(_contact_info)

        _user_info = d.pop("userInfo", UNSET)
        user_info: Union[Unset, None, ITemplateUserInfo]
        if _user_info is None:
            user_info = None
        elif isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = ITemplateUserInfo.from_dict(_user_info)

        _company_user_info = d.pop("companyUserInfo", UNSET)
        company_user_info: Union[Unset, None, CompanyUserInfoBlockViewModel]
        if _company_user_info is None:
            company_user_info = None
        elif isinstance(_company_user_info, Unset):
            company_user_info = UNSET
        else:
            company_user_info = CompanyUserInfoBlockViewModel.from_dict(_company_user_info)

        _profile_image = d.pop("profileImage", UNSET)
        profile_image: Union[Unset, None, ITemplateProfileImage]
        if _profile_image is None:
            profile_image = None
        elif isinstance(_profile_image, Unset):
            profile_image = UNSET
        else:
            profile_image = ITemplateProfileImage.from_dict(_profile_image)

        _company = d.pop("company", UNSET)
        company: Union[Unset, None, ITemplateCompany]
        if _company is None:
            company = None
        elif isinstance(_company, Unset):
            company = UNSET
        else:
            company = ITemplateCompany.from_dict(_company)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, datetime.datetime]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        language_branch_id = d.pop("languageBranchId", UNSET)

        is_public = d.pop("isPublic", UNSET)

        locked = d.pop("locked", UNSET)

        current_language = d.pop("currentLanguage", UNSET)

        style_assets = []
        _style_assets = d.pop("styleAssets", UNSET)
        for style_assets_item_data in _style_assets or []:
            style_assets_item = ITemplateStyleAssetViewModel.from_dict(style_assets_item_data)

            style_assets.append(style_assets_item)

        _customer_managed_style_asset = d.pop("customerManagedStyleAsset", UNSET)
        customer_managed_style_asset: Union[Unset, None, ITemplateStyleAssetViewModel]
        if _customer_managed_style_asset is None:
            customer_managed_style_asset = None
        elif isinstance(_customer_managed_style_asset, Unset):
            customer_managed_style_asset = UNSET
        else:
            customer_managed_style_asset = ITemplateStyleAssetViewModel.from_dict(_customer_managed_style_asset)

        shared_style_assets = []
        _shared_style_assets = d.pop("sharedStyleAssets", UNSET)
        for shared_style_assets_item_data in _shared_style_assets or []:
            shared_style_assets_item = ITemplateSharedAssetViewModel.from_dict(shared_style_assets_item_data)

            shared_style_assets.append(shared_style_assets_item)

        shared_script_assets = []
        _shared_script_assets = d.pop("sharedScriptAssets", UNSET)
        for shared_script_assets_item_data in _shared_script_assets or []:
            shared_script_assets_item = ITemplateSharedAssetViewModel.from_dict(shared_script_assets_item_data)

            shared_script_assets.append(shared_script_assets_item)

        shared_font_assets = []
        _shared_font_assets = d.pop("sharedFontAssets", UNSET)
        for shared_font_assets_item_data in _shared_font_assets or []:
            shared_font_assets_item = ITemplateSharedAssetViewModel.from_dict(shared_font_assets_item_data)

            shared_font_assets.append(shared_font_assets_item)

        _primary_style_assets = d.pop("primaryStyleAssets", UNSET)
        primary_style_assets: Union[Unset, None, DynamicTemplateViewModelPrimaryStyleAssets]
        if _primary_style_assets is None:
            primary_style_assets = None
        elif isinstance(_primary_style_assets, Unset):
            primary_style_assets = UNSET
        else:
            primary_style_assets = DynamicTemplateViewModelPrimaryStyleAssets.from_dict(_primary_style_assets)

        _primary_script_assets = d.pop("primaryScriptAssets", UNSET)
        primary_script_assets: Union[Unset, None, DynamicTemplateViewModelPrimaryScriptAssets]
        if _primary_script_assets is None:
            primary_script_assets = None
        elif isinstance(_primary_script_assets, Unset):
            primary_script_assets = UNSET
        else:
            primary_script_assets = DynamicTemplateViewModelPrimaryScriptAssets.from_dict(_primary_script_assets)

        template_asset_types = []
        _template_asset_types = d.pop("templateAssetTypes", UNSET)
        for template_asset_types_item_data in _template_asset_types or []:
            template_asset_types_item = TemplateAssetType(template_asset_types_item_data)

            template_asset_types.append(template_asset_types_item)

        is_answering_to_request = d.pop("isAnsweringToRequest", UNSET)

        dynamic_template_view_model = cls(
            title=title,
            blocks=blocks,
            logotype=logotype,
            id=id,
            resume_template_id=resume_template_id,
            company_id=company_id,
            company_user_id=company_user_id,
            slug=slug,
            description=description,
            logotype_id=logotype_id,
            word_enabled=word_enabled,
            profile_image_size=profile_image_size,
            allow_no_profile_image=allow_no_profile_image,
            hide_profile_image_in_edit=hide_profile_image_in_edit,
            company_logotype_image_size=company_logotype_image_size,
            pdf_engine_type=pdf_engine_type,
            word_engine_type=word_engine_type,
            pdf_orientation=pdf_orientation,
            pdf_margin_top=pdf_margin_top,
            pdf_margin_right=pdf_margin_right,
            pdf_margin_bottom=pdf_margin_bottom,
            pdf_margin_left=pdf_margin_left,
            custom_footer_for_wkhtml=custom_footer_for_wkhtml,
            pdf_footer=pdf_footer,
            show_preview_toggle=show_preview_toggle,
            contact_info_id=contact_info_id,
            contact_info=contact_info,
            user_info=user_info,
            company_user_info=company_user_info,
            profile_image=profile_image,
            company=company,
            created=created,
            updated=updated,
            language_branch_id=language_branch_id,
            is_public=is_public,
            locked=locked,
            current_language=current_language,
            style_assets=style_assets,
            customer_managed_style_asset=customer_managed_style_asset,
            shared_style_assets=shared_style_assets,
            shared_script_assets=shared_script_assets,
            shared_font_assets=shared_font_assets,
            primary_style_assets=primary_style_assets,
            primary_script_assets=primary_script_assets,
            template_asset_types=template_asset_types,
            is_answering_to_request=is_answering_to_request,
        )

        return dynamic_template_view_model
