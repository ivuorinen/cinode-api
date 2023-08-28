import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="TeamModel")


@_attrs_define
class TeamModel:
    """
    Attributes:
        internal_identification (Union[Unset, None, str]):
        corporate_identity_number (Union[Unset, None, str]):
        cost_center (Union[Unset, None, str]):
        location (Union[Unset, None, str]):
        parent_team_id (Union[Unset, None, int]):
        created (Union[Unset, None, datetime.datetime]):
        updated (Union[Unset, None, datetime.datetime]):
        location_id (Union[Unset, None, int]):
        id (Union[Unset, int]):
        company_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    internal_identification: Union[Unset, None, str] = UNSET
    corporate_identity_number: Union[Unset, None, str] = UNSET
    cost_center: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    parent_team_id: Union[Unset, None, int] = UNSET
    created: Union[Unset, None, datetime.datetime] = UNSET
    updated: Union[Unset, None, datetime.datetime] = UNSET
    location_id: Union[Unset, None, int] = UNSET
    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        internal_identification = self.internal_identification
        corporate_identity_number = self.corporate_identity_number
        cost_center = self.cost_center
        location = self.location
        parent_team_id = self.parent_team_id
        created: Union[Unset, None, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat() if self.created else None

        updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat() if self.updated else None

        location_id = self.location_id
        id = self.id
        company_id = self.company_id
        name = self.name
        description = self.description
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if internal_identification is not UNSET:
            field_dict["internalIdentification"] = internal_identification
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if location is not UNSET:
            field_dict["location"] = location
        if parent_team_id is not UNSET:
            field_dict["parentTeamId"] = parent_team_id
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        internal_identification = d.pop("internalIdentification", UNSET)

        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        location = d.pop("location", UNSET)

        parent_team_id = d.pop("parentTeamId", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, None, datetime.datetime]
        if _created is None:
            created = None
        elif isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, None, datetime.datetime]
        if _updated is None:
            updated = None
        elif isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        location_id = d.pop("locationId", UNSET)

        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        team_model = cls(
            internal_identification=internal_identification,
            corporate_identity_number=corporate_identity_number,
            cost_center=cost_center,
            location=location,
            parent_team_id=parent_team_id,
            created=created,
            updated=updated,
            location_id=location_id,
            id=id,
            company_id=company_id,
            name=name,
            description=description,
            links=links,
        )

        return team_model
