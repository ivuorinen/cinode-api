from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_template_shared_asset_view_model import ITemplateSharedAssetViewModel


T = TypeVar("T", bound="DynamicTemplateViewModelPrimaryStyleAssets")


@_attrs_define
class DynamicTemplateViewModelPrimaryStyleAssets:
    """
    Attributes:
        none (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        primary (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        classic (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        dynamic (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        page_flow (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        block_work_experience (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        block_skills_by_level (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        cinode_premium_3_page_flow (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        cinode_premium_2_page_flow (Union[Unset, List['ITemplateSharedAssetViewModel']]):
        template_type (Union[Unset, List['ITemplateSharedAssetViewModel']]):
    """

    none: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    primary: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    classic: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    dynamic: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    page_flow: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    block_work_experience: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    block_skills_by_level: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    cinode_premium_3_page_flow: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    cinode_premium_2_page_flow: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET
    template_type: Union[Unset, List["ITemplateSharedAssetViewModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        none: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.none, Unset):
            none = []
            for none_item_data in self.none:
                none_item = none_item_data.to_dict()

                none.append(none_item)

        primary: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.primary, Unset):
            primary = []
            for primary_item_data in self.primary:
                primary_item = primary_item_data.to_dict()

                primary.append(primary_item)

        classic: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classic, Unset):
            classic = []
            for classic_item_data in self.classic:
                classic_item = classic_item_data.to_dict()

                classic.append(classic_item)

        dynamic: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dynamic, Unset):
            dynamic = []
            for dynamic_item_data in self.dynamic:
                dynamic_item = dynamic_item_data.to_dict()

                dynamic.append(dynamic_item)

        page_flow: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.page_flow, Unset):
            page_flow = []
            for page_flow_item_data in self.page_flow:
                page_flow_item = page_flow_item_data.to_dict()

                page_flow.append(page_flow_item)

        block_work_experience: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.block_work_experience, Unset):
            block_work_experience = []
            for block_work_experience_item_data in self.block_work_experience:
                block_work_experience_item = block_work_experience_item_data.to_dict()

                block_work_experience.append(block_work_experience_item)

        block_skills_by_level: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.block_skills_by_level, Unset):
            block_skills_by_level = []
            for block_skills_by_level_item_data in self.block_skills_by_level:
                block_skills_by_level_item = block_skills_by_level_item_data.to_dict()

                block_skills_by_level.append(block_skills_by_level_item)

        cinode_premium_3_page_flow: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cinode_premium_3_page_flow, Unset):
            cinode_premium_3_page_flow = []
            for cinode_premium_3_page_flow_item_data in self.cinode_premium_3_page_flow:
                cinode_premium_3_page_flow_item = cinode_premium_3_page_flow_item_data.to_dict()

                cinode_premium_3_page_flow.append(cinode_premium_3_page_flow_item)

        cinode_premium_2_page_flow: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cinode_premium_2_page_flow, Unset):
            cinode_premium_2_page_flow = []
            for cinode_premium_2_page_flow_item_data in self.cinode_premium_2_page_flow:
                cinode_premium_2_page_flow_item = cinode_premium_2_page_flow_item_data.to_dict()

                cinode_premium_2_page_flow.append(cinode_premium_2_page_flow_item)

        template_type: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.template_type, Unset):
            template_type = []
            for template_type_item_data in self.template_type:
                template_type_item = template_type_item_data.to_dict()

                template_type.append(template_type_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if none is not UNSET:
            field_dict["None"] = none
        if primary is not UNSET:
            field_dict["Primary"] = primary
        if classic is not UNSET:
            field_dict["Classic"] = classic
        if dynamic is not UNSET:
            field_dict["Dynamic"] = dynamic
        if page_flow is not UNSET:
            field_dict["PageFlow"] = page_flow
        if block_work_experience is not UNSET:
            field_dict["BlockWorkExperience"] = block_work_experience
        if block_skills_by_level is not UNSET:
            field_dict["BlockSkillsByLevel"] = block_skills_by_level
        if cinode_premium_3_page_flow is not UNSET:
            field_dict["CinodePremium3PageFlow"] = cinode_premium_3_page_flow
        if cinode_premium_2_page_flow is not UNSET:
            field_dict["CinodePremium2PageFlow"] = cinode_premium_2_page_flow
        if template_type is not UNSET:
            field_dict["TemplateType"] = template_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.i_template_shared_asset_view_model import ITemplateSharedAssetViewModel

        d = src_dict.copy()
        none = []
        _none = d.pop("None", UNSET)
        for none_item_data in _none or []:
            none_item = ITemplateSharedAssetViewModel.from_dict(none_item_data)

            none.append(none_item)

        primary = []
        _primary = d.pop("Primary", UNSET)
        for primary_item_data in _primary or []:
            primary_item = ITemplateSharedAssetViewModel.from_dict(primary_item_data)

            primary.append(primary_item)

        classic = []
        _classic = d.pop("Classic", UNSET)
        for classic_item_data in _classic or []:
            classic_item = ITemplateSharedAssetViewModel.from_dict(classic_item_data)

            classic.append(classic_item)

        dynamic = []
        _dynamic = d.pop("Dynamic", UNSET)
        for dynamic_item_data in _dynamic or []:
            dynamic_item = ITemplateSharedAssetViewModel.from_dict(dynamic_item_data)

            dynamic.append(dynamic_item)

        page_flow = []
        _page_flow = d.pop("PageFlow", UNSET)
        for page_flow_item_data in _page_flow or []:
            page_flow_item = ITemplateSharedAssetViewModel.from_dict(page_flow_item_data)

            page_flow.append(page_flow_item)

        block_work_experience = []
        _block_work_experience = d.pop("BlockWorkExperience", UNSET)
        for block_work_experience_item_data in _block_work_experience or []:
            block_work_experience_item = ITemplateSharedAssetViewModel.from_dict(block_work_experience_item_data)

            block_work_experience.append(block_work_experience_item)

        block_skills_by_level = []
        _block_skills_by_level = d.pop("BlockSkillsByLevel", UNSET)
        for block_skills_by_level_item_data in _block_skills_by_level or []:
            block_skills_by_level_item = ITemplateSharedAssetViewModel.from_dict(block_skills_by_level_item_data)

            block_skills_by_level.append(block_skills_by_level_item)

        cinode_premium_3_page_flow = []
        _cinode_premium_3_page_flow = d.pop("CinodePremium3PageFlow", UNSET)
        for cinode_premium_3_page_flow_item_data in _cinode_premium_3_page_flow or []:
            cinode_premium_3_page_flow_item = ITemplateSharedAssetViewModel.from_dict(
                cinode_premium_3_page_flow_item_data
            )

            cinode_premium_3_page_flow.append(cinode_premium_3_page_flow_item)

        cinode_premium_2_page_flow = []
        _cinode_premium_2_page_flow = d.pop("CinodePremium2PageFlow", UNSET)
        for cinode_premium_2_page_flow_item_data in _cinode_premium_2_page_flow or []:
            cinode_premium_2_page_flow_item = ITemplateSharedAssetViewModel.from_dict(
                cinode_premium_2_page_flow_item_data
            )

            cinode_premium_2_page_flow.append(cinode_premium_2_page_flow_item)

        template_type = []
        _template_type = d.pop("TemplateType", UNSET)
        for template_type_item_data in _template_type or []:
            template_type_item = ITemplateSharedAssetViewModel.from_dict(template_type_item_data)

            template_type.append(template_type_item)

        dynamic_template_view_model_primary_style_assets = cls(
            none=none,
            primary=primary,
            classic=classic,
            dynamic=dynamic,
            page_flow=page_flow,
            block_work_experience=block_work_experience,
            block_skills_by_level=block_skills_by_level,
            cinode_premium_3_page_flow=cinode_premium_3_page_flow,
            cinode_premium_2_page_flow=cinode_premium_2_page_flow,
            template_type=template_type,
        )

        return dynamic_template_view_model_primary_style_assets
