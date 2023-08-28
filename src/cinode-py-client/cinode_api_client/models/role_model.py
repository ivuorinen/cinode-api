from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.access_level import AccessLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleModel")


@_attrs_define
class RoleModel:
    """
    Attributes:
        id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        level (Union[Unset, None, AccessLevel]):

            NoAccess = 0

            Anonymous = 50

            Read = 100

            Subcontractor = 110

            Candidate = 115

            RestrictedCompanyUser = 150

            CompanyApiUser = 180

            CompanyUser = 200

            PartnerManager = 240

            CompanyRecruiter = 250

            TeamManager = 270

            CompanyManager = 300

            CompanyAdmin = 400

            Owner = 500
    """

    id: Union[Unset, None, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    level: Union[Unset, None, AccessLevel] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        level: Union[Unset, None, int] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value if self.level else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, None, AccessLevel]
        if _level is None:
            level = None
        elif isinstance(_level, Unset):
            level = UNSET
        else:
            level = AccessLevel(_level)

        role_model = cls(
            id=id,
            name=name,
            description=description,
            level=level,
        )

        return role_model
