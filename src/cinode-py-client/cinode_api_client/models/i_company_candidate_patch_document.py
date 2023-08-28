import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_candidate_state import CompanyCandidateState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ICompanyCandidatePatchDocument")


@_attrs_define
class ICompanyCandidatePatchDocument:
    """
    Attributes:
        pipeline_id (Union[Unset, None, int]):
        pipeline_stage_id (Union[Unset, None, int]):
        recruitment_manager_id (Union[Unset, None, int]):
        state (Union[Unset, None, CompanyCandidateState]):

            Öppen = 0

            Vunnen = 10

            Pausad = 20

            Avböjd av kandidat = 30

            Avböjd av oss = 40
        available_from_date (Union[Unset, None, datetime.datetime]):
        campaign_code (Union[Unset, None, str]):
    """

    pipeline_id: Union[Unset, None, int] = UNSET
    pipeline_stage_id: Union[Unset, None, int] = UNSET
    recruitment_manager_id: Union[Unset, None, int] = UNSET
    state: Union[Unset, None, CompanyCandidateState] = UNSET
    available_from_date: Union[Unset, None, datetime.datetime] = UNSET
    campaign_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        pipeline_id = self.pipeline_id
        pipeline_stage_id = self.pipeline_stage_id
        recruitment_manager_id = self.recruitment_manager_id
        state: Union[Unset, None, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value if self.state else None

        available_from_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.available_from_date, Unset):
            available_from_date = self.available_from_date.isoformat() if self.available_from_date else None

        campaign_code = self.campaign_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if pipeline_id is not UNSET:
            field_dict["pipelineId"] = pipeline_id
        if pipeline_stage_id is not UNSET:
            field_dict["pipelineStageId"] = pipeline_stage_id
        if recruitment_manager_id is not UNSET:
            field_dict["recruitmentManagerId"] = recruitment_manager_id
        if state is not UNSET:
            field_dict["state"] = state
        if available_from_date is not UNSET:
            field_dict["availableFromDate"] = available_from_date
        if campaign_code is not UNSET:
            field_dict["campaignCode"] = campaign_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pipeline_id = d.pop("pipelineId", UNSET)

        pipeline_stage_id = d.pop("pipelineStageId", UNSET)

        recruitment_manager_id = d.pop("recruitmentManagerId", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, None, CompanyCandidateState]
        if _state is None:
            state = None
        elif isinstance(_state, Unset):
            state = UNSET
        else:
            state = CompanyCandidateState(_state)

        _available_from_date = d.pop("availableFromDate", UNSET)
        available_from_date: Union[Unset, None, datetime.datetime]
        if _available_from_date is None:
            available_from_date = None
        elif isinstance(_available_from_date, Unset):
            available_from_date = UNSET
        else:
            available_from_date = isoparse(_available_from_date)

        campaign_code = d.pop("campaignCode", UNSET)

        i_company_candidate_patch_document = cls(
            pipeline_id=pipeline_id,
            pipeline_stage_id=pipeline_stage_id,
            recruitment_manager_id=recruitment_manager_id,
            state=state,
            available_from_date=available_from_date,
            campaign_code=campaign_code,
        )

        return i_company_candidate_patch_document
