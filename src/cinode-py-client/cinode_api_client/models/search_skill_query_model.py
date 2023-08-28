from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_model import FilterModel
    from ..models.search_skill_model import SearchSkillModel


T = TypeVar("T", bound="SearchSkillQueryModel")


@_attrs_define
class SearchSkillQueryModel:
    """
    Attributes:
        skills (Union[Unset, None, List['SearchSkillModel']]):
        filters (Union[Unset, None, List['FilterModel']]):
    """

    skills: Union[Unset, None, List["SearchSkillModel"]] = UNSET
    filters: Union[Unset, None, List["FilterModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        skills: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skills, Unset):
            if self.skills is None:
                skills = None
            else:
                skills = []
                for skills_item_data in self.skills:
                    skills_item = skills_item_data.to_dict()

                    skills.append(skills_item)

        filters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            if self.filters is None:
                filters = None
            else:
                filters = []
                for filters_item_data in self.filters:
                    filters_item = filters_item_data.to_dict()

                    filters.append(filters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if skills is not UNSET:
            field_dict["skills"] = skills
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_model import FilterModel
        from ..models.search_skill_model import SearchSkillModel

        d = src_dict.copy()
        skills = []
        _skills = d.pop("skills", UNSET)
        for skills_item_data in _skills or []:
            skills_item = SearchSkillModel.from_dict(skills_item_data)

            skills.append(skills_item)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = FilterModel.from_dict(filters_item_data)

            filters.append(filters_item)

        search_skill_query_model = cls(
            skills=skills,
            filters=filters,
        )

        return search_skill_query_model
