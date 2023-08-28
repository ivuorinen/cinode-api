""" Contains all the data models used in inputs/outputs """

from .abscence_period_day_model import AbscencePeriodDayModel
from .absence_add_edit_model import AbsenceAddEditModel
from .absence_period_dto_model import AbsencePeriodDtoModel
from .absence_period_model import AbsencePeriodModel
from .absence_type_dto import AbsenceTypeDto
from .absence_type_model import AbsenceTypeModel
from .access_level import AccessLevel
from .action_type import ActionType
from .add_company_image_multipart_data import AddCompanyImageMultipartData
from .add_company_subcontractor_group_member_model import AddCompanySubcontractorGroupMemberModel
from .address_info_block_view_model import AddressInfoBlockViewModel
from .address_type import AddressType
from .attachment_type import AttachmentType
from .availability_filter_model import AvailabilityFilterModel
from .availability_model import AvailabilityModel
from .calendar_day_model import CalendarDayModel
from .candidate_attachment_multipart_data import CandidateAttachmentMultipartData
from .classic_company_user_resume_model import ClassicCompanyUserResumeModel
from .commitment_block_item_model import CommitmentBlockItemModel
from .commitment_block_model import CommitmentBlockModel
from .company_address_model import CompanyAddressModel
from .company_base_model import CompanyBaseModel
from .company_candidate_add_invite_model import CompanyCandidateAddInviteModel
from .company_candidate_add_model import CompanyCandidateAddModel
from .company_candidate_attachment_model import CompanyCandidateAttachmentModel
from .company_candidate_base_model import CompanyCandidateBaseModel
from .company_candidate_event_base_model import CompanyCandidateEventBaseModel
from .company_candidate_event_meeting_model import CompanyCandidateEventMeetingModel
from .company_candidate_event_model import CompanyCandidateEventModel
from .company_candidate_event_note_model import CompanyCandidateEventNoteModel
from .company_candidate_event_task_model import CompanyCandidateEventTaskModel
from .company_candidate_extended_model import CompanyCandidateExtendedModel
from .company_candidate_file_attachment_list_model import CompanyCandidateFileAttachmentListModel
from .company_candidate_file_attachment_model import CompanyCandidateFileAttachmentModel
from .company_candidate_pipeline_model import CompanyCandidatePipelineModel
from .company_candidate_pipeline_stage_model import CompanyCandidatePipelineStageModel
from .company_candidate_query_sort import CompanyCandidateQuerySort
from .company_candidate_query_sort_page_and_sort_by_model import CompanyCandidateQuerySortPageAndSortByModel
from .company_candidate_skill_add_model import CompanyCandidateSkillAddModel
from .company_candidate_skill_model import CompanyCandidateSkillModel
from .company_candidate_state import CompanyCandidateState
from .company_candidate_uri_attachment_add_model import CompanyCandidateUriAttachmentAddModel
from .company_candidate_uri_attachment_model import CompanyCandidateUriAttachmentModel
from .company_capabilities_model import CompanyCapabilitiesModel
from .company_customer_add_model import CompanyCustomerAddModel
from .company_customer_address_add_edit_model import CompanyCustomerAddressAddEditModel
from .company_customer_address_model import CompanyCustomerAddressModel
from .company_customer_attachment_model import CompanyCustomerAttachmentModel
from .company_customer_base_model import CompanyCustomerBaseModel
from .company_customer_contact_add_edit_model import CompanyCustomerContactAddEditModel
from .company_customer_contact_base_model import CompanyCustomerContactBaseModel
from .company_customer_contact_model import CompanyCustomerContactModel
from .company_customer_contact_query_sort import CompanyCustomerContactQuerySort
from .company_customer_contact_query_sort_page_and_sort_by_model import (
    CompanyCustomerContactQuerySortPageAndSortByModel,
)
from .company_customer_delete_model import CompanyCustomerDeleteModel
from .company_customer_edit_model import CompanyCustomerEditModel
from .company_customer_extended_model import CompanyCustomerExtendedModel
from .company_customer_manager_model import CompanyCustomerManagerModel
from .company_customer_managers_add_edit_model import CompanyCustomerManagersAddEditModel
from .company_customer_model import CompanyCustomerModel
from .company_customer_query_sort import CompanyCustomerQuerySort
from .company_customer_query_sort_page_and_sort_by_model import CompanyCustomerQuerySortPageAndSortByModel
from .company_enabled_module_model import CompanyEnabledModuleModel
from .company_image_model import CompanyImageModel
from .company_model import CompanyModel
from .company_profile_filter_model import CompanyProfileFilterModel
from .company_profile_sort import CompanyProfileSort
from .company_profile_sort_page_and_sort_by_model import CompanyProfileSortPageAndSortByModel
from .company_profiles_model import CompanyProfilesModel
from .company_recruitment_manager_model import CompanyRecruitmentManagerModel
from .company_resume_template_base_model import CompanyResumeTemplateBaseModel
from .company_resume_template_language_model import CompanyResumeTemplateLanguageModel
from .company_size import CompanySize
from .company_subcontractor_group_base_model import CompanySubcontractorGroupBaseModel
from .company_subcontractor_group_model import CompanySubcontractorGroupModel
from .company_tag_base_model import CompanyTagBaseModel
from .company_tag_model import CompanyTagModel
from .company_tag_type_model import CompanyTagTypeModel
from .company_user_add_model import CompanyUserAddModel
from .company_user_base_model import CompanyUserBaseModel
from .company_user_edit_model import CompanyUserEditModel
from .company_user_event_base_model import CompanyUserEventBaseModel
from .company_user_event_meeting_add_edit_model import CompanyUserEventMeetingAddEditModel
from .company_user_event_meeting_model import CompanyUserEventMeetingModel
from .company_user_event_model import CompanyUserEventModel
from .company_user_event_note_add_edit_model import CompanyUserEventNoteAddEditModel
from .company_user_event_note_model import CompanyUserEventNoteModel
from .company_user_event_task_add_edit_model import CompanyUserEventTaskAddEditModel
from .company_user_event_task_model import CompanyUserEventTaskModel
from .company_user_extended_model import CompanyUserExtendedModel
from .company_user_full_model import CompanyUserFullModel
from .company_user_image_model import CompanyUserImageModel
from .company_user_info_block_view_model import CompanyUserInfoBlockViewModel
from .company_user_model import CompanyUserModel
from .company_user_permissions_edit_model import CompanyUserPermissionsEditModel
from .company_user_profile_add_edit_model import CompanyUserProfileAddEditModel
from .company_user_profile_base_model import CompanyUserProfileBaseModel
from .company_user_profile_commitment_add_edit_model import CompanyUserProfileCommitmentAddEditModel
from .company_user_profile_commitment_model import CompanyUserProfileCommitmentModel
from .company_user_profile_commitment_translation_model import CompanyUserProfileCommitmentTranslationModel
from .company_user_profile_education_add_edit_model import CompanyUserProfileEducationAddEditModel
from .company_user_profile_education_model import CompanyUserProfileEducationModel
from .company_user_profile_education_translation_model import CompanyUserProfileEducationTranslationModel
from .company_user_profile_employer_add_edit_model import CompanyUserProfileEmployerAddEditModel
from .company_user_profile_employer_model import CompanyUserProfileEmployerModel
from .company_user_profile_employer_translation_model import CompanyUserProfileEmployerTranslationModel
from .company_user_profile_ext_skill_add_edit_model import CompanyUserProfileExtSkillAddEditModel
from .company_user_profile_ext_skill_model import CompanyUserProfileExtSkillModel
from .company_user_profile_ext_skill_translation_model import CompanyUserProfileExtSkillTranslationModel
from .company_user_profile_full_model import CompanyUserProfileFullModel
from .company_user_profile_language_add_edit_model import CompanyUserProfileLanguageAddEditModel
from .company_user_profile_language_branch_model import CompanyUserProfileLanguageBranchModel
from .company_user_profile_language_model import CompanyUserProfileLanguageModel
from .company_user_profile_presentation_edit_model import CompanyUserProfilePresentationEditModel
from .company_user_profile_presentation_model import CompanyUserProfilePresentationModel
from .company_user_profile_presentation_translation_model import CompanyUserProfilePresentationTranslationModel
from .company_user_profile_reference_add_edit_model import CompanyUserProfileReferenceAddEditModel
from .company_user_profile_reference_model import CompanyUserProfileReferenceModel
from .company_user_profile_reference_translation_model import CompanyUserProfileReferenceTranslationModel
from .company_user_profile_skill_add_model import CompanyUserProfileSkillAddModel
from .company_user_profile_skill_edit_model import CompanyUserProfileSkillEditModel
from .company_user_profile_skill_history_model import CompanyUserProfileSkillHistoryModel
from .company_user_profile_skill_model import CompanyUserProfileSkillModel
from .company_user_profile_skill_translation_model import CompanyUserProfileSkillTranslationModel
from .company_user_profile_training_add_edit_model import CompanyUserProfileTrainingAddEditModel
from .company_user_profile_training_model import CompanyUserProfileTrainingModel
from .company_user_profile_training_translation_model import CompanyUserProfileTrainingTranslationModel
from .company_user_profile_translation_model import CompanyUserProfileTranslationModel
from .company_user_profile_work_experience_add_edit_model import CompanyUserProfileWorkExperienceAddEditModel
from .company_user_profile_work_experience_model import CompanyUserProfileWorkExperienceModel
from .company_user_profile_work_experience_skill_add_model import CompanyUserProfileWorkExperienceSkillAddModel
from .company_user_profile_work_experience_translation_model import CompanyUserProfileWorkExperienceTranslationModel
from .company_user_project_assignment_model import CompanyUserProjectAssignmentModel
from .company_user_query_sort import CompanyUserQuerySort
from .company_user_query_sort_page_and_sort_by_model import CompanyUserQuerySortPageAndSortByModel
from .company_user_resume_base_model import CompanyUserResumeBaseModel
from .company_user_search_skill_model import CompanyUserSearchSkillModel
from .company_user_skill_model import CompanyUserSkillModel
from .company_user_status import CompanyUserStatus
from .company_user_subcontractor_add_edit_model import CompanyUserSubcontractorAddEditModel
from .company_user_subcontractor_attachment_model import CompanyUserSubcontractorAttachmentModel
from .company_user_subcontractor_base_model import CompanyUserSubcontractorBaseModel
from .company_user_subcontractor_file_attachment_list_model import CompanyUserSubcontractorFileAttachmentListModel
from .company_user_subcontractor_file_attachment_model import CompanyUserSubcontractorFileAttachmentModel
from .company_user_subcontractor_model import CompanyUserSubcontractorModel
from .company_user_subcontractor_role_member_model import CompanyUserSubcontractorRoleMemberModel
from .company_user_subcontractor_roles_model import CompanyUserSubcontractorRolesModel
from .company_user_subcontractor_status import CompanyUserSubcontractorStatus
from .company_user_type import CompanyUserType
from .contract_type import ContractType
from .convert_company_user_to_aad_account_model import ConvertCompanyUserToAadAccountModel
from .country_model import CountryModel
from .create_company_user_profile_import_multipart_data import CreateCompanyUserProfileImportMultipartData
from .created_model import CreatedModel
from .currency_model import CurrencyModel
from .customer_event_base_model import CustomerEventBaseModel
from .customer_event_meeting_add_edit_model import CustomerEventMeetingAddEditModel
from .customer_event_meeting_model import CustomerEventMeetingModel
from .customer_event_model import CustomerEventModel
from .customer_event_note_add_edit_model import CustomerEventNoteAddEditModel
from .customer_event_note_model import CustomerEventNoteModel
from .customer_event_task_add_edit_model import CustomerEventTaskAddEditModel
from .customer_event_task_model import CustomerEventTaskModel
from .dynamic_company_user_resume_model import DynamicCompanyUserResumeModel
from .dynamic_template_view_model import DynamicTemplateViewModel
from .dynamic_template_view_model_primary_script_assets import DynamicTemplateViewModelPrimaryScriptAssets
from .dynamic_template_view_model_primary_style_assets import DynamicTemplateViewModelPrimaryStyleAssets
from .education_block_item_model import EducationBlockItemModel
from .education_block_model import EducationBlockModel
from .employer_block_item_model import EmployerBlockItemModel
from .employer_block_model import EmployerBlockModel
from .error_model import ErrorModel
from .event_comment_model import EventCommentModel
from .event_meeting_add_edit_model import EventMeetingAddEditModel
from .event_note_add_edit_model import EventNoteAddEditModel
from .event_note_type import EventNoteType
from .event_status_value import EventStatusValue
from .event_task_add_edit_model import EventTaskAddEditModel
from .event_task_type import EventTaskType
from .event_type import EventType
from .event_visibility import EventVisibility
from .extent_type import ExtentType
from .extra_skill_block_model import ExtraSkillBlockModel
from .extra_skill_item_block_model import ExtraSkillItemBlockModel
from .filter_model import FilterModel
from .highlighted_work_experience_block_item_model import HighlightedWorkExperienceBlockItemModel
from .highlighted_work_experience_block_model import HighlightedWorkExperienceBlockModel
from .i_company_address_view_model import ICompanyAddressViewModel
from .i_company_candidate_patch_document import ICompanyCandidatePatchDocument
from .i_company_user_employee_patch_document import ICompanyUserEmployeePatchDocument
from .i_contact_info_view_model import IContactInfoViewModel
from .i_dynamic_block_view_model import IDynamicBlockViewModel
from .i_template_company import ITemplateCompany
from .i_template_image import ITemplateImage
from .i_template_logotype import ITemplateLogotype
from .i_template_shared_asset_view_model import ITemplateSharedAssetViewModel
from .i_template_style_asset_view_model import ITemplateStyleAssetViewModel
from .i_template_user_info import ITemplateUserInfo
from .image_block_model import ImageBlockModel
from .image_size import ImageSize
from .import_profile_async_operation import ImportProfileAsyncOperation
from .keyword_model import KeywordModel
from .keyword_synonym_model import KeywordSynonymModel
from .keyword_type import KeywordType
from .language_block_model import LanguageBlockModel
from .language_item_block_model import LanguageItemBlockModel
from .language_level import LanguageLevel
from .link import Link
from .location_block_model import LocationBlockModel
from .location_model import LocationModel
from .long_running_status import LongRunningStatus
from .mention_text_model import MentionTextModel
from .module_type import ModuleType
from .operation import Operation
from .operation_value import OperationValue
from .partner_base_model import PartnerBaseModel
from .partner_connection_base_model import PartnerConnectionBaseModel
from .partner_connection_trust_type import PartnerConnectionTrustType
from .partner_recipient_base_model import PartnerRecipientBaseModel
from .partners_filter_model import PartnersFilterModel
from .partners_overview_model import PartnersOverviewModel
from .pdf_engine_type import PdfEngineType
from .pdf_orientation import PdfOrientation
from .presentation_block_model import PresentationBlockModel
from .profile_language_model import ProfileLanguageModel
from .project_add_edit_model import ProjectAddEditModel
from .project_assignment_add_model import ProjectAssignmentAddModel
from .project_assignment_allocation_status import ProjectAssignmentAllocationStatus
from .project_assignment_announce_model import ProjectAssignmentAnnounceModel
from .project_assignment_announcement_base_model import ProjectAssignmentAnnouncementBaseModel
from .project_assignment_base_model import ProjectAssignmentBaseModel
from .project_assignment_edit_model import ProjectAssignmentEditModel
from .project_assignment_extent_type import ProjectAssignmentExtentType
from .project_assignment_filter_model import ProjectAssignmentFilterModel
from .project_assignment_member_allocation_status import ProjectAssignmentMemberAllocationStatus
from .project_assignment_member_employee_add_model import ProjectAssignmentMemberEmployeeAddModel
from .project_assignment_member_employee_edit_model import ProjectAssignmentMemberEmployeeEditModel
from .project_assignment_member_model import ProjectAssignmentMemberModel
from .project_assignment_member_state import ProjectAssignmentMemberState
from .project_assignment_member_state_history_model import ProjectAssignmentMemberStateHistoryModel
from .project_assignment_member_subcontractor_add_model import ProjectAssignmentMemberSubcontractorAddModel
from .project_assignment_member_subcontractor_edit_model import ProjectAssignmentMemberSubcontractorEditModel
from .project_assignment_member_type import ProjectAssignmentMemberType
from .project_assignment_model import ProjectAssignmentModel
from .project_assignment_request_status import ProjectAssignmentRequestStatus
from .project_assignment_skill_add_model import ProjectAssignmentSkillAddModel
from .project_assignment_skill_base_model import ProjectAssignmentSkillBaseModel
from .project_assignment_skill_edit_model import ProjectAssignmentSkillEditModel
from .project_assignment_skill_model import ProjectAssignmentSkillModel
from .project_assignment_status import ProjectAssignmentStatus
from .project_assignment_with_status_model import ProjectAssignmentWithStatusModel
from .project_attachment_model import ProjectAttachmentModel
from .project_base_model import ProjectBaseModel
from .project_event_base_model import ProjectEventBaseModel
from .project_event_meeting_add_edit_model import ProjectEventMeetingAddEditModel
from .project_event_meeting_model import ProjectEventMeetingModel
from .project_event_model import ProjectEventModel
from .project_event_note_add_edit_model import ProjectEventNoteAddEditModel
from .project_event_note_model import ProjectEventNoteModel
from .project_event_task_add_edit_model import ProjectEventTaskAddEditModel
from .project_event_task_model import ProjectEventTaskModel
from .project_model import ProjectModel
from .project_pipeline_model import ProjectPipelineModel
from .project_pipeline_stage_model import ProjectPipelineStageModel
from .project_priority import ProjectPriority
from .project_query_sort import ProjectQuerySort
from .project_query_sort_page_and_sort_by_model import ProjectQuerySortPageAndSortByModel
from .project_reference_model import ProjectReferenceModel
from .project_state import ProjectState
from .project_state_history_model import ProjectStateHistoryModel
from .project_state_reason_model import ProjectStateReasonModel
from .recruitment_source_model import RecruitmentSourceModel
from .reference_block_item_model import ReferenceBlockItemModel
from .reference_block_model import ReferenceBlockModel
from .resume_model import ResumeModel
from .role_model import RoleModel
from .search_company_candidate_query_model import SearchCompanyCandidateQueryModel
from .search_company_candidate_result_model import SearchCompanyCandidateResultModel
from .search_company_customer_contact_query_model import SearchCompanyCustomerContactQueryModel
from .search_company_customer_contact_result_model import SearchCompanyCustomerContactResultModel
from .search_company_customer_query_model import SearchCompanyCustomerQueryModel
from .search_company_customer_result_model import SearchCompanyCustomerResultModel
from .search_company_user_query_model import SearchCompanyUserQueryModel
from .search_company_user_result_model import SearchCompanyUserResultModel
from .search_project_query_model import SearchProjectQueryModel
from .search_projects_result_model import SearchProjectsResultModel
from .search_skill_model import SearchSkillModel
from .search_skill_query_model import SearchSkillQueryModel
from .search_skill_result_model import SearchSkillResultModel
from .skill_block_item_model import SkillBlockItemModel
from .skill_by_category_block_item_model import SkillByCategoryBlockItemModel
from .skill_by_category_block_model import SkillByCategoryBlockModel
from .skill_model_model import SkillModelModel
from .skill_result_model import SkillResultModel
from .skill_search_query_term_model import SkillSearchQueryTermModel
from .sort_order import SortOrder
from .status import Status
from .string_comparison_operator import StringComparisonOperator
from .subcontractor_attachment_multipart_data import SubcontractorAttachmentMultipartData
from .team_add_edit_model import TeamAddEditModel
from .team_base_model import TeamBaseModel
from .team_manager_edit_model import TeamManagerEditModel
from .team_manager_model import TeamManagerModel
from .team_member_add_model import TeamMemberAddModel
from .team_member_edit_model import TeamMemberEditModel
from .team_member_model import TeamMemberModel
from .team_member_move_model import TeamMemberMoveModel
from .team_model import TeamModel
from .template_asset_type import TemplateAssetType
from .text_block_model import TextBlockModel
from .top_skill_block_item_model import TopSkillBlockItemModel
from .top_skill_block_model import TopSkillBlockModel
from .training_block_model import TrainingBlockModel
from .training_item_block_model import TrainingItemBlockModel
from .training_type import TrainingType
from .updated_model import UpdatedModel
from .user_gender import UserGender
from .validation_model import ValidationModel
from .validation_model_errors import ValidationModelErrors
from .webhook_add_model import WebhookAddModel
from .webhook_configuration_add_model import WebhookConfigurationAddModel
from .webhook_configuration_model import WebhookConfigurationModel
from .webhook_credentials_add_model import WebhookCredentialsAddModel
from .webhook_credentials_model import WebhookCredentialsModel
from .webhook_entity_type import WebhookEntityType
from .webhook_model import WebhookModel
from .word_engine_type import WordEngineType
from .work_experience_block_item_model import WorkExperienceBlockItemModel
from .work_experience_block_model import WorkExperienceBlockModel

__all__ = (
    "AbscencePeriodDayModel",
    "AbsenceAddEditModel",
    "AbsencePeriodDtoModel",
    "AbsencePeriodModel",
    "AbsenceTypeDto",
    "AbsenceTypeModel",
    "AccessLevel",
    "ActionType",
    "AddCompanyImageMultipartData",
    "AddCompanySubcontractorGroupMemberModel",
    "AddressInfoBlockViewModel",
    "AddressType",
    "AttachmentType",
    "AvailabilityFilterModel",
    "AvailabilityModel",
    "CalendarDayModel",
    "CandidateAttachmentMultipartData",
    "ClassicCompanyUserResumeModel",
    "CommitmentBlockItemModel",
    "CommitmentBlockModel",
    "CompanyAddressModel",
    "CompanyBaseModel",
    "CompanyCandidateAddInviteModel",
    "CompanyCandidateAddModel",
    "CompanyCandidateAttachmentModel",
    "CompanyCandidateBaseModel",
    "CompanyCandidateEventBaseModel",
    "CompanyCandidateEventMeetingModel",
    "CompanyCandidateEventModel",
    "CompanyCandidateEventNoteModel",
    "CompanyCandidateEventTaskModel",
    "CompanyCandidateExtendedModel",
    "CompanyCandidateFileAttachmentListModel",
    "CompanyCandidateFileAttachmentModel",
    "CompanyCandidatePipelineModel",
    "CompanyCandidatePipelineStageModel",
    "CompanyCandidateQuerySort",
    "CompanyCandidateQuerySortPageAndSortByModel",
    "CompanyCandidateSkillAddModel",
    "CompanyCandidateSkillModel",
    "CompanyCandidateState",
    "CompanyCandidateUriAttachmentAddModel",
    "CompanyCandidateUriAttachmentModel",
    "CompanyCapabilitiesModel",
    "CompanyCustomerAddModel",
    "CompanyCustomerAddressAddEditModel",
    "CompanyCustomerAddressModel",
    "CompanyCustomerAttachmentModel",
    "CompanyCustomerBaseModel",
    "CompanyCustomerContactAddEditModel",
    "CompanyCustomerContactBaseModel",
    "CompanyCustomerContactModel",
    "CompanyCustomerContactQuerySort",
    "CompanyCustomerContactQuerySortPageAndSortByModel",
    "CompanyCustomerDeleteModel",
    "CompanyCustomerEditModel",
    "CompanyCustomerExtendedModel",
    "CompanyCustomerManagerModel",
    "CompanyCustomerManagersAddEditModel",
    "CompanyCustomerModel",
    "CompanyCustomerQuerySort",
    "CompanyCustomerQuerySortPageAndSortByModel",
    "CompanyEnabledModuleModel",
    "CompanyImageModel",
    "CompanyModel",
    "CompanyProfileFilterModel",
    "CompanyProfilesModel",
    "CompanyProfileSort",
    "CompanyProfileSortPageAndSortByModel",
    "CompanyRecruitmentManagerModel",
    "CompanyResumeTemplateBaseModel",
    "CompanyResumeTemplateLanguageModel",
    "CompanySize",
    "CompanySubcontractorGroupBaseModel",
    "CompanySubcontractorGroupModel",
    "CompanyTagBaseModel",
    "CompanyTagModel",
    "CompanyTagTypeModel",
    "CompanyUserAddModel",
    "CompanyUserBaseModel",
    "CompanyUserEditModel",
    "CompanyUserEventBaseModel",
    "CompanyUserEventMeetingAddEditModel",
    "CompanyUserEventMeetingModel",
    "CompanyUserEventModel",
    "CompanyUserEventNoteAddEditModel",
    "CompanyUserEventNoteModel",
    "CompanyUserEventTaskAddEditModel",
    "CompanyUserEventTaskModel",
    "CompanyUserExtendedModel",
    "CompanyUserFullModel",
    "CompanyUserImageModel",
    "CompanyUserInfoBlockViewModel",
    "CompanyUserModel",
    "CompanyUserPermissionsEditModel",
    "CompanyUserProfileAddEditModel",
    "CompanyUserProfileBaseModel",
    "CompanyUserProfileCommitmentAddEditModel",
    "CompanyUserProfileCommitmentModel",
    "CompanyUserProfileCommitmentTranslationModel",
    "CompanyUserProfileEducationAddEditModel",
    "CompanyUserProfileEducationModel",
    "CompanyUserProfileEducationTranslationModel",
    "CompanyUserProfileEmployerAddEditModel",
    "CompanyUserProfileEmployerModel",
    "CompanyUserProfileEmployerTranslationModel",
    "CompanyUserProfileExtSkillAddEditModel",
    "CompanyUserProfileExtSkillModel",
    "CompanyUserProfileExtSkillTranslationModel",
    "CompanyUserProfileFullModel",
    "CompanyUserProfileLanguageAddEditModel",
    "CompanyUserProfileLanguageBranchModel",
    "CompanyUserProfileLanguageModel",
    "CompanyUserProfilePresentationEditModel",
    "CompanyUserProfilePresentationModel",
    "CompanyUserProfilePresentationTranslationModel",
    "CompanyUserProfileReferenceAddEditModel",
    "CompanyUserProfileReferenceModel",
    "CompanyUserProfileReferenceTranslationModel",
    "CompanyUserProfileSkillAddModel",
    "CompanyUserProfileSkillEditModel",
    "CompanyUserProfileSkillHistoryModel",
    "CompanyUserProfileSkillModel",
    "CompanyUserProfileSkillTranslationModel",
    "CompanyUserProfileTrainingAddEditModel",
    "CompanyUserProfileTrainingModel",
    "CompanyUserProfileTrainingTranslationModel",
    "CompanyUserProfileTranslationModel",
    "CompanyUserProfileWorkExperienceAddEditModel",
    "CompanyUserProfileWorkExperienceModel",
    "CompanyUserProfileWorkExperienceSkillAddModel",
    "CompanyUserProfileWorkExperienceTranslationModel",
    "CompanyUserProjectAssignmentModel",
    "CompanyUserQuerySort",
    "CompanyUserQuerySortPageAndSortByModel",
    "CompanyUserResumeBaseModel",
    "CompanyUserSearchSkillModel",
    "CompanyUserSkillModel",
    "CompanyUserStatus",
    "CompanyUserSubcontractorAddEditModel",
    "CompanyUserSubcontractorAttachmentModel",
    "CompanyUserSubcontractorBaseModel",
    "CompanyUserSubcontractorFileAttachmentListModel",
    "CompanyUserSubcontractorFileAttachmentModel",
    "CompanyUserSubcontractorModel",
    "CompanyUserSubcontractorRoleMemberModel",
    "CompanyUserSubcontractorRolesModel",
    "CompanyUserSubcontractorStatus",
    "CompanyUserType",
    "ContractType",
    "ConvertCompanyUserToAadAccountModel",
    "CountryModel",
    "CreateCompanyUserProfileImportMultipartData",
    "CreatedModel",
    "CurrencyModel",
    "CustomerEventBaseModel",
    "CustomerEventMeetingAddEditModel",
    "CustomerEventMeetingModel",
    "CustomerEventModel",
    "CustomerEventNoteAddEditModel",
    "CustomerEventNoteModel",
    "CustomerEventTaskAddEditModel",
    "CustomerEventTaskModel",
    "DynamicCompanyUserResumeModel",
    "DynamicTemplateViewModel",
    "DynamicTemplateViewModelPrimaryScriptAssets",
    "DynamicTemplateViewModelPrimaryStyleAssets",
    "EducationBlockItemModel",
    "EducationBlockModel",
    "EmployerBlockItemModel",
    "EmployerBlockModel",
    "ErrorModel",
    "EventCommentModel",
    "EventMeetingAddEditModel",
    "EventNoteAddEditModel",
    "EventNoteType",
    "EventStatusValue",
    "EventTaskAddEditModel",
    "EventTaskType",
    "EventType",
    "EventVisibility",
    "ExtentType",
    "ExtraSkillBlockModel",
    "ExtraSkillItemBlockModel",
    "FilterModel",
    "HighlightedWorkExperienceBlockItemModel",
    "HighlightedWorkExperienceBlockModel",
    "ICompanyAddressViewModel",
    "ICompanyCandidatePatchDocument",
    "ICompanyUserEmployeePatchDocument",
    "IContactInfoViewModel",
    "IDynamicBlockViewModel",
    "ImageBlockModel",
    "ImageSize",
    "ImportProfileAsyncOperation",
    "ITemplateCompany",
    "ITemplateImage",
    "ITemplateLogotype",
    "ITemplateSharedAssetViewModel",
    "ITemplateStyleAssetViewModel",
    "ITemplateUserInfo",
    "KeywordModel",
    "KeywordSynonymModel",
    "KeywordType",
    "LanguageBlockModel",
    "LanguageItemBlockModel",
    "LanguageLevel",
    "Link",
    "LocationBlockModel",
    "LocationModel",
    "LongRunningStatus",
    "MentionTextModel",
    "ModuleType",
    "Operation",
    "OperationValue",
    "PartnerBaseModel",
    "PartnerConnectionBaseModel",
    "PartnerConnectionTrustType",
    "PartnerRecipientBaseModel",
    "PartnersFilterModel",
    "PartnersOverviewModel",
    "PdfEngineType",
    "PdfOrientation",
    "PresentationBlockModel",
    "ProfileLanguageModel",
    "ProjectAddEditModel",
    "ProjectAssignmentAddModel",
    "ProjectAssignmentAllocationStatus",
    "ProjectAssignmentAnnouncementBaseModel",
    "ProjectAssignmentAnnounceModel",
    "ProjectAssignmentBaseModel",
    "ProjectAssignmentEditModel",
    "ProjectAssignmentExtentType",
    "ProjectAssignmentFilterModel",
    "ProjectAssignmentMemberAllocationStatus",
    "ProjectAssignmentMemberEmployeeAddModel",
    "ProjectAssignmentMemberEmployeeEditModel",
    "ProjectAssignmentMemberModel",
    "ProjectAssignmentMemberState",
    "ProjectAssignmentMemberStateHistoryModel",
    "ProjectAssignmentMemberSubcontractorAddModel",
    "ProjectAssignmentMemberSubcontractorEditModel",
    "ProjectAssignmentMemberType",
    "ProjectAssignmentModel",
    "ProjectAssignmentRequestStatus",
    "ProjectAssignmentSkillAddModel",
    "ProjectAssignmentSkillBaseModel",
    "ProjectAssignmentSkillEditModel",
    "ProjectAssignmentSkillModel",
    "ProjectAssignmentStatus",
    "ProjectAssignmentWithStatusModel",
    "ProjectAttachmentModel",
    "ProjectBaseModel",
    "ProjectEventBaseModel",
    "ProjectEventMeetingAddEditModel",
    "ProjectEventMeetingModel",
    "ProjectEventModel",
    "ProjectEventNoteAddEditModel",
    "ProjectEventNoteModel",
    "ProjectEventTaskAddEditModel",
    "ProjectEventTaskModel",
    "ProjectModel",
    "ProjectPipelineModel",
    "ProjectPipelineStageModel",
    "ProjectPriority",
    "ProjectQuerySort",
    "ProjectQuerySortPageAndSortByModel",
    "ProjectReferenceModel",
    "ProjectState",
    "ProjectStateHistoryModel",
    "ProjectStateReasonModel",
    "RecruitmentSourceModel",
    "ReferenceBlockItemModel",
    "ReferenceBlockModel",
    "ResumeModel",
    "RoleModel",
    "SearchCompanyCandidateQueryModel",
    "SearchCompanyCandidateResultModel",
    "SearchCompanyCustomerContactQueryModel",
    "SearchCompanyCustomerContactResultModel",
    "SearchCompanyCustomerQueryModel",
    "SearchCompanyCustomerResultModel",
    "SearchCompanyUserQueryModel",
    "SearchCompanyUserResultModel",
    "SearchProjectQueryModel",
    "SearchProjectsResultModel",
    "SearchSkillModel",
    "SearchSkillQueryModel",
    "SearchSkillResultModel",
    "SkillBlockItemModel",
    "SkillByCategoryBlockItemModel",
    "SkillByCategoryBlockModel",
    "SkillModelModel",
    "SkillResultModel",
    "SkillSearchQueryTermModel",
    "SortOrder",
    "Status",
    "StringComparisonOperator",
    "SubcontractorAttachmentMultipartData",
    "TeamAddEditModel",
    "TeamBaseModel",
    "TeamManagerEditModel",
    "TeamManagerModel",
    "TeamMemberAddModel",
    "TeamMemberEditModel",
    "TeamMemberModel",
    "TeamMemberMoveModel",
    "TeamModel",
    "TemplateAssetType",
    "TextBlockModel",
    "TopSkillBlockItemModel",
    "TopSkillBlockModel",
    "TrainingBlockModel",
    "TrainingItemBlockModel",
    "TrainingType",
    "UpdatedModel",
    "UserGender",
    "ValidationModel",
    "ValidationModelErrors",
    "WebhookAddModel",
    "WebhookConfigurationAddModel",
    "WebhookConfigurationModel",
    "WebhookCredentialsAddModel",
    "WebhookCredentialsModel",
    "WebhookEntityType",
    "WebhookModel",
    "WordEngineType",
    "WorkExperienceBlockItemModel",
    "WorkExperienceBlockModel",
)
