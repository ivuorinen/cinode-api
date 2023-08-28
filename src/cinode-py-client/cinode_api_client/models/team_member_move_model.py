from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TeamMemberMoveModel")


@_attrs_define
class TeamMemberMoveModel:
    """
    Attributes:
        to_team_id (int):
    """

    to_team_id: int

    def to_dict(self) -> Dict[str, Any]:
        to_team_id = self.to_team_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "toTeamId": to_team_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        to_team_id = d.pop("toTeamId")

        team_member_move_model = cls(
            to_team_id=to_team_id,
        )

        return team_member_move_model
