from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.company_candidate_state import CompanyCandidateState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_candidate_query_sort_page_and_sort_by_model import CompanyCandidateQuerySortPageAndSortByModel


T = TypeVar("T", bound="SearchCompanyCandidateQueryModel")


@_attrs_define
class SearchCompanyCandidateQueryModel:
    """
    Attributes:
        term (Union[Unset, None, str]):
        rating (Union[Unset, None, int]):
        states (Union[Unset, None, List[CompanyCandidateState]]):
        pipeline (Union[Unset, None, int]):
        no_recruiter (Union[Unset, bool]):
        recruiters (Union[Unset, None, List[int]]):
        teams (Union[Unset, None, List[int]]):
        sources (Union[Unset, None, List[int]]):
        page_and_sort_by (Union[Unset, None, CompanyCandidateQuerySortPageAndSortByModel]):
    """

    term: Union[Unset, None, str] = UNSET
    rating: Union[Unset, None, int] = UNSET
    states: Union[Unset, None, List[CompanyCandidateState]] = UNSET
    pipeline: Union[Unset, None, int] = UNSET
    no_recruiter: Union[Unset, bool] = UNSET
    recruiters: Union[Unset, None, List[int]] = UNSET
    teams: Union[Unset, None, List[int]] = UNSET
    sources: Union[Unset, None, List[int]] = UNSET
    page_and_sort_by: Union[Unset, None, "CompanyCandidateQuerySortPageAndSortByModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        term = self.term
        rating = self.rating
        states: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.states, Unset):
            if self.states is None:
                states = None
            else:
                states = []
                for states_item_data in self.states:
                    states_item = states_item_data.value

                    states.append(states_item)

        pipeline = self.pipeline
        no_recruiter = self.no_recruiter
        recruiters: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.recruiters, Unset):
            if self.recruiters is None:
                recruiters = None
            else:
                recruiters = self.recruiters

        teams: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.teams, Unset):
            if self.teams is None:
                teams = None
            else:
                teams = self.teams

        sources: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.sources, Unset):
            if self.sources is None:
                sources = None
            else:
                sources = self.sources

        page_and_sort_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.page_and_sort_by, Unset):
            page_and_sort_by = self.page_and_sort_by.to_dict() if self.page_and_sort_by else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if rating is not UNSET:
            field_dict["rating"] = rating
        if states is not UNSET:
            field_dict["states"] = states
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if no_recruiter is not UNSET:
            field_dict["noRecruiter"] = no_recruiter
        if recruiters is not UNSET:
            field_dict["recruiters"] = recruiters
        if teams is not UNSET:
            field_dict["teams"] = teams
        if sources is not UNSET:
            field_dict["sources"] = sources
        if page_and_sort_by is not UNSET:
            field_dict["pageAndSortBy"] = page_and_sort_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_candidate_query_sort_page_and_sort_by_model import (
            CompanyCandidateQuerySortPageAndSortByModel,
        )

        d = src_dict.copy()
        term = d.pop("term", UNSET)

        rating = d.pop("rating", UNSET)

        states = []
        _states = d.pop("states", UNSET)
        for states_item_data in _states or []:
            states_item = CompanyCandidateState(states_item_data)

            states.append(states_item)

        pipeline = d.pop("pipeline", UNSET)

        no_recruiter = d.pop("noRecruiter", UNSET)

        recruiters = cast(List[int], d.pop("recruiters", UNSET))

        teams = cast(List[int], d.pop("teams", UNSET))

        sources = cast(List[int], d.pop("sources", UNSET))

        _page_and_sort_by = d.pop("pageAndSortBy", UNSET)
        page_and_sort_by: Union[Unset, None, CompanyCandidateQuerySortPageAndSortByModel]
        if _page_and_sort_by is None:
            page_and_sort_by = None
        elif isinstance(_page_and_sort_by, Unset):
            page_and_sort_by = UNSET
        else:
            page_and_sort_by = CompanyCandidateQuerySortPageAndSortByModel.from_dict(_page_and_sort_by)

        search_company_candidate_query_model = cls(
            term=term,
            rating=rating,
            states=states,
            pipeline=pipeline,
            no_recruiter=no_recruiter,
            recruiters=recruiters,
            teams=teams,
            sources=sources,
            page_and_sort_by=page_and_sort_by,
        )

        return search_company_candidate_query_model
