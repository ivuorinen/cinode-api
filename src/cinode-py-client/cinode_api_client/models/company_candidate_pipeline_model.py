from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_candidate_pipeline_stage_model import CompanyCandidatePipelineStageModel


T = TypeVar("T", bound="CompanyCandidatePipelineModel")


@_attrs_define
class CompanyCandidatePipelineModel:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        stages (Union[Unset, None, List['CompanyCandidatePipelineStageModel']]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    stages: Union[Unset, None, List["CompanyCandidatePipelineStageModel"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        description = self.description
        stages: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stages, Unset):
            if self.stages is None:
                stages = None
            else:
                stages = []
                for stages_item_data in self.stages:
                    stages_item = stages_item_data.to_dict()

                    stages.append(stages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_candidate_pipeline_stage_model import CompanyCandidatePipelineStageModel

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = CompanyCandidatePipelineStageModel.from_dict(stages_item_data)

            stages.append(stages_item)

        company_candidate_pipeline_model = cls(
            id=id,
            title=title,
            description=description,
            stages=stages,
        )

        return company_candidate_pipeline_model
