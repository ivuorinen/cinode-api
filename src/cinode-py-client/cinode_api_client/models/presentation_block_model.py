import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PresentationBlockModel")


@_attrs_define
class PresentationBlockModel:
    """
    Attributes:
        discarded (Union[Unset, None, datetime.datetime]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        personal_description (Union[Unset, None, str]):
        personal_description_heading (Union[Unset, None, str]):
        sub_heading (Union[Unset, None, str]):
        use_advanced_formatting (Union[Unset, bool]):
        editor_settings (Union[Unset, None, str]):
        hide_sub_heading (Union[Unset, bool]):
        personal_presentation_length (Union[Unset, int]):
        show_personal_presentation (Union[Unset, bool]):
        title_length (Union[Unset, int]):
        description_length (Union[Unset, int]):
        employer_length (Union[Unset, int]):
        block_id (Union[Unset, str]):
        updated (Union[Unset, None, datetime.datetime]):
        heading (Union[Unset, None, str]):
    """

    discarded: Union[Unset, None, datetime.datetime] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    personal_description: Union[Unset, None, str] = UNSET
    personal_description_heading: Union[Unset, None, str] = UNSET
    sub_heading: Union[Unset, None, str] = UNSET
    use_advanced_formatting: Union[Unset, bool] = UNSET
    editor_settings: Union[Unset, None, str] = UNSET
    hide_sub_heading: Union[Unset, bool] = UNSET
    personal_presentation_length: Union[Unset, int] = UNSET
    show_personal_presentation: Union[Unset, bool] = UNSET
    title_length: Union[Unset, int] = UNSET
    description_length: Union[Unset, int] = UNSET
    employer_length: Union[Unset, int] = UNSET
    block_id: Union[Unset, str] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    heading: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        discarded: Union[Unset, None, str] = UNSET
        if not isinstance(self.discarded, Unset):
            discarded = self.discarded.isoformat() if self.discarded else None

        title = self.title
        description = self.description
        personal_description = self.personal_description
        personal_description_heading = self.personal_description_heading
        sub_heading = self.sub_heading
        use_advanced_formatting = self.use_advanced_formatting
        editor_settings = self.editor_settings
        hide_sub_heading = self.hide_sub_heading
        personal_presentation_length = self.personal_presentation_length
        show_personal_presentation = self.show_personal_presentation
        title_length = self.title_length
        description_length = self.description_length
        employer_length = self.employer_length
        block_id = self.block_id
        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        heading = self.heading

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if discarded is not UNSET:
            field_dict["discarded"] = discarded
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if personal_description is not UNSET:
            field_dict["personalDescription"] = personal_description
        if personal_description_heading is not UNSET:
            field_dict["personalDescriptionHeading"] = personal_description_heading
        if sub_heading is not UNSET:
            field_dict["subHeading"] = sub_heading
        if use_advanced_formatting is not UNSET:
            field_dict["useAdvancedFormatting"] = use_advanced_formatting
        if editor_settings is not UNSET:
            field_dict["editorSettings"] = editor_settings
        if hide_sub_heading is not UNSET:
            field_dict["hideSubHeading"] = hide_sub_heading
        if personal_presentation_length is not UNSET:
            field_dict["personalPresentationLength"] = personal_presentation_length
        if show_personal_presentation is not UNSET:
            field_dict["showPersonalPresentation"] = show_personal_presentation
        if title_length is not UNSET:
            field_dict["titleLength"] = title_length
        if description_length is not UNSET:
            field_dict["descriptionLength"] = description_length
        if employer_length is not UNSET:
            field_dict["employerLength"] = employer_length
        if block_id is not UNSET:
            field_dict["blockId"] = block_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if heading is not UNSET:
            field_dict["heading"] = heading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _discarded = d.pop("discarded", UNSET)
        discarded: Union[Unset, None, datetime.datetime]
        if _discarded is None:
            discarded = None
        elif isinstance(_discarded, Unset):
            discarded = UNSET
        else:
            discarded = isoparse(_discarded)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        personal_description = d.pop("personalDescription", UNSET)

        personal_description_heading = d.pop("personalDescriptionHeading", UNSET)

        sub_heading = d.pop("subHeading", UNSET)

        use_advanced_formatting = d.pop("useAdvancedFormatting", UNSET)

        editor_settings = d.pop("editorSettings", UNSET)

        hide_sub_heading = d.pop("hideSubHeading", UNSET)

        personal_presentation_length = d.pop("personalPresentationLength", UNSET)

        show_personal_presentation = d.pop("showPersonalPresentation", UNSET)

        title_length = d.pop("titleLength", UNSET)

        description_length = d.pop("descriptionLength", UNSET)

        employer_length = d.pop("employerLength", UNSET)

        block_id = d.pop("blockId", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, datetime.datetime]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        heading = d.pop("heading", UNSET)

        presentation_block_model = cls(
            discarded=discarded,
            title=title,
            description=description,
            personal_description=personal_description,
            personal_description_heading=personal_description_heading,
            sub_heading=sub_heading,
            use_advanced_formatting=use_advanced_formatting,
            editor_settings=editor_settings,
            hide_sub_heading=hide_sub_heading,
            personal_presentation_length=personal_presentation_length,
            show_personal_presentation=show_personal_presentation,
            title_length=title_length,
            description_length=description_length,
            employer_length=employer_length,
            block_id=block_id,
            updated=updated,
            heading=heading,
        )

        return presentation_block_model
