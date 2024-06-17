import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.template_asset_type import TemplateAssetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IDynamicBlockViewModel")


@_attrs_define
class IDynamicBlockViewModel:
    """
    Attributes:
        view_component_name (Union[Unset, None, str]):
        template_asset_types (Union[Unset, None, List[TemplateAssetType]]):
        company_user_resume_id (Union[Unset, int]):
        company_user_id (Union[Unset, int]):
        is_editable (Union[Unset, bool]):
        partial_edit_view_path (Union[Unset, None, str]):
        friendly_block_name (Union[Unset, None, str]):
        has_updates_in_profile (Union[Unset, bool]):
        heading (Union[Unset, None, str]):
        updated (Union[Unset, None, datetime.datetime]):
        block_id (Union[Unset, str]):
    """

    view_component_name: Union[Unset, None, str] = UNSET
    template_asset_types: Union[Unset, None, List[TemplateAssetType]] = UNSET
    company_user_resume_id: Union[Unset, int] = UNSET
    company_user_id: Union[Unset, int] = UNSET
    is_editable: Union[Unset, bool] = UNSET
    partial_edit_view_path: Union[Unset, None, str] = UNSET
    friendly_block_name: Union[Unset, None, str] = UNSET
    has_updates_in_profile: Union[Unset, bool] = UNSET
    heading: Union[Unset, None, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    block_id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        view_component_name = self.view_component_name
        template_asset_types: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.template_asset_types, Unset):
            if self.template_asset_types is None:
                template_asset_types = None
            else:
                template_asset_types = []
                for template_asset_types_item_data in self.template_asset_types:
                    template_asset_types_item = template_asset_types_item_data.value

                    template_asset_types.append(template_asset_types_item)

        company_user_resume_id = self.company_user_resume_id
        company_user_id = self.company_user_id
        is_editable = self.is_editable
        partial_edit_view_path = self.partial_edit_view_path
        friendly_block_name = self.friendly_block_name
        has_updates_in_profile = self.has_updates_in_profile
        heading = self.heading
        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        block_id = self.block_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if view_component_name is not UNSET:
            field_dict["viewComponentName"] = view_component_name
        if template_asset_types is not UNSET:
            field_dict["templateAssetTypes"] = template_asset_types
        if company_user_resume_id is not UNSET:
            field_dict["companyUserResumeId"] = company_user_resume_id
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if partial_edit_view_path is not UNSET:
            field_dict["partialEditViewPath"] = partial_edit_view_path
        if friendly_block_name is not UNSET:
            field_dict["friendlyBlockName"] = friendly_block_name
        if has_updates_in_profile is not UNSET:
            field_dict["hasUpdatesInProfile"] = has_updates_in_profile
        if heading is not UNSET:
            field_dict["heading"] = heading
        if updated is not UNSET:
            field_dict["updated"] = updated
        if block_id is not UNSET:
            field_dict["blockId"] = block_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        view_component_name = d.pop("viewComponentName", UNSET)

        template_asset_types = []
        _template_asset_types = d.pop("templateAssetTypes", UNSET)
        for template_asset_types_item_data in _template_asset_types or []:
            template_asset_types_item = TemplateAssetType(template_asset_types_item_data)

            template_asset_types.append(template_asset_types_item)

        company_user_resume_id = d.pop("companyUserResumeId", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        is_editable = d.pop("isEditable", UNSET)

        partial_edit_view_path = d.pop("partialEditViewPath", UNSET)

        friendly_block_name = d.pop("friendlyBlockName", UNSET)

        has_updates_in_profile = d.pop("hasUpdatesInProfile", UNSET)

        heading = d.pop("heading", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, datetime.datetime]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        block_id = d.pop("blockId", UNSET)

        i_dynamic_block_view_model = cls(
            view_component_name=view_component_name,
            template_asset_types=template_asset_types,
            company_user_resume_id=company_user_resume_id,
            company_user_id=company_user_id,
            is_editable=is_editable,
            partial_edit_view_path=partial_edit_view_path,
            friendly_block_name=friendly_block_name,
            has_updates_in_profile=has_updates_in_profile,
            heading=heading,
            updated=updated,
            block_id=block_id,
        )

        return i_dynamic_block_view_model
