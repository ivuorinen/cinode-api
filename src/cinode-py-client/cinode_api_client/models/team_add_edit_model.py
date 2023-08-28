from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamAddEditModel")


@_attrs_define
class TeamAddEditModel:
    """
    Attributes:
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        internal_identification (Union[Unset, None, str]):
        corporate_identity_number (Union[Unset, None, str]):
        cost_center (Union[Unset, None, str]):
        parent_team_id (Union[Unset, None, int]):
        location_id (Union[Unset, None, int]):
    """

    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    internal_identification: Union[Unset, None, str] = UNSET
    corporate_identity_number: Union[Unset, None, str] = UNSET
    cost_center: Union[Unset, None, str] = UNSET
    parent_team_id: Union[Unset, None, int] = UNSET
    location_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        internal_identification = self.internal_identification
        corporate_identity_number = self.corporate_identity_number
        cost_center = self.cost_center
        parent_team_id = self.parent_team_id
        location_id = self.location_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if internal_identification is not UNSET:
            field_dict["internalIdentification"] = internal_identification
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if parent_team_id is not UNSET:
            field_dict["parentTeamId"] = parent_team_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        internal_identification = d.pop("internalIdentification", UNSET)

        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        parent_team_id = d.pop("parentTeamId", UNSET)

        location_id = d.pop("locationId", UNSET)

        team_add_edit_model = cls(
            name=name,
            description=description,
            internal_identification=internal_identification,
            corporate_identity_number=corporate_identity_number,
            cost_center=cost_center,
            parent_team_id=parent_team_id,
            location_id=location_id,
        )

        return team_add_edit_model
