from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_user_search_skill_model import CompanyUserSearchSkillModel
    from ..models.search_skill_query_model import SearchSkillQueryModel


T = TypeVar("T", bound="SearchSkillResultModel")


@_attrs_define
class SearchSkillResultModel:
    """
    Attributes:
        query (Union[Unset, None, SearchSkillQueryModel]):
        hits (Union[Unset, None, List['CompanyUserSearchSkillModel']]):
    """

    query: Union[Unset, None, "SearchSkillQueryModel"] = UNSET
    hits: Union[Unset, None, List["CompanyUserSearchSkillModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        query: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict() if self.query else None

        hits: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hits, Unset):
            if self.hits is None:
                hits = None
            else:
                hits = []
                for hits_item_data in self.hits:
                    hits_item = hits_item_data.to_dict()

                    hits.append(hits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if hits is not UNSET:
            field_dict["hits"] = hits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_user_search_skill_model import CompanyUserSearchSkillModel
        from ..models.search_skill_query_model import SearchSkillQueryModel

        d = src_dict.copy()
        _query = d.pop("query", UNSET)
        query: Union[Unset, None, SearchSkillQueryModel]
        if _query is None:
            query = None
        elif isinstance(_query, Unset):
            query = UNSET
        else:
            query = SearchSkillQueryModel.from_dict(_query)

        hits = []
        _hits = d.pop("hits", UNSET)
        for hits_item_data in _hits or []:
            hits_item = CompanyUserSearchSkillModel.from_dict(hits_item_data)

            hits.append(hits_item)

        search_skill_result_model = cls(
            query=query,
            hits=hits,
        )

        return search_skill_result_model
