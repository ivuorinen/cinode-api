from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCandidatePipelineStageModel")


@_attrs_define
class CompanyCandidatePipelineStageModel:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        order (Union[Unset, int]):
        probability (Union[Unset, None, int]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    order: Union[Unset, int] = UNSET
    probability: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        description = self.description
        order = self.order
        probability = self.probability

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if order is not UNSET:
            field_dict["order"] = order
        if probability is not UNSET:
            field_dict["probability"] = probability

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        order = d.pop("order", UNSET)

        probability = d.pop("probability", UNSET)

        company_candidate_pipeline_stage_model = cls(
            id=id,
            title=title,
            description=description,
            order=order,
            probability=probability,
        )

        return company_candidate_pipeline_stage_model
