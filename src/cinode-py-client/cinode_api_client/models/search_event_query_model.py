from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.event_entity_type import EventEntityType
from ..models.event_status_value import EventStatusValue
from ..models.event_type import EventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_time_filter_interval import DateTimeFilterInterval
    from ..models.event_query_sort_page_and_sort_by_model import EventQuerySortPageAndSortByModel


T = TypeVar("T", bound="SearchEventQueryModel")


@_attrs_define
class SearchEventQueryModel:
    """
    Attributes:
        event_statuses (Union[Unset, None, List[EventStatusValue]]):
        entity_types (Union[Unset, None, List[EventEntityType]]):
        event_types (Union[Unset, None, List[EventType]]):
        created_date (Union[Unset, None, DateTimeFilterInterval]):
        event_date (Union[Unset, None, DateTimeFilterInterval]):
        i_am_responsible (Union[Unset, None, bool]):
        no_responsible (Union[Unset, None, bool]):
        responsibles (Union[Unset, None, List[int]]):
        query (Union[Unset, None, str]):
        timezone_id (Union[Unset, None, str]):
        page_and_sort_by (Union[Unset, None, EventQuerySortPageAndSortByModel]):
    """

    event_statuses: Union[Unset, None, List[EventStatusValue]] = UNSET
    entity_types: Union[Unset, None, List[EventEntityType]] = UNSET
    event_types: Union[Unset, None, List[EventType]] = UNSET
    created_date: Union[Unset, None, "DateTimeFilterInterval"] = UNSET
    event_date: Union[Unset, None, "DateTimeFilterInterval"] = UNSET
    i_am_responsible: Union[Unset, None, bool] = UNSET
    no_responsible: Union[Unset, None, bool] = UNSET
    responsibles: Union[Unset, None, List[int]] = UNSET
    query: Union[Unset, None, str] = UNSET
    timezone_id: Union[Unset, None, str] = UNSET
    page_and_sort_by: Union[Unset, None, "EventQuerySortPageAndSortByModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        event_statuses: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.event_statuses, Unset):
            if self.event_statuses is None:
                event_statuses = None
            else:
                event_statuses = []
                for event_statuses_item_data in self.event_statuses:
                    event_statuses_item = event_statuses_item_data.value

                    event_statuses.append(event_statuses_item)

        entity_types: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.entity_types, Unset):
            if self.entity_types is None:
                entity_types = None
            else:
                entity_types = []
                for entity_types_item_data in self.entity_types:
                    entity_types_item = entity_types_item_data.value

                    entity_types.append(entity_types_item)

        event_types: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.event_types, Unset):
            if self.event_types is None:
                event_types = None
            else:
                event_types = []
                for event_types_item_data in self.event_types:
                    event_types_item = event_types_item_data.value

                    event_types.append(event_types_item)

        created_date: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.to_dict() if self.created_date else None

        event_date: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.to_dict() if self.event_date else None

        i_am_responsible = self.i_am_responsible
        no_responsible = self.no_responsible
        responsibles: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.responsibles, Unset):
            if self.responsibles is None:
                responsibles = None
            else:
                responsibles = self.responsibles

        query = self.query
        timezone_id = self.timezone_id
        page_and_sort_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.page_and_sort_by, Unset):
            page_and_sort_by = self.page_and_sort_by.to_dict() if self.page_and_sort_by else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if event_statuses is not UNSET:
            field_dict["eventStatuses"] = event_statuses
        if entity_types is not UNSET:
            field_dict["entityTypes"] = entity_types
        if event_types is not UNSET:
            field_dict["eventTypes"] = event_types
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if i_am_responsible is not UNSET:
            field_dict["iAmResponsible"] = i_am_responsible
        if no_responsible is not UNSET:
            field_dict["noResponsible"] = no_responsible
        if responsibles is not UNSET:
            field_dict["responsibles"] = responsibles
        if query is not UNSET:
            field_dict["query"] = query
        if timezone_id is not UNSET:
            field_dict["timezoneId"] = timezone_id
        if page_and_sort_by is not UNSET:
            field_dict["pageAndSortBy"] = page_and_sort_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_time_filter_interval import DateTimeFilterInterval
        from ..models.event_query_sort_page_and_sort_by_model import EventQuerySortPageAndSortByModel

        d = src_dict.copy()
        event_statuses = []
        _event_statuses = d.pop("eventStatuses", UNSET)
        for event_statuses_item_data in _event_statuses or []:
            event_statuses_item = EventStatusValue(event_statuses_item_data)

            event_statuses.append(event_statuses_item)

        entity_types = []
        _entity_types = d.pop("entityTypes", UNSET)
        for entity_types_item_data in _entity_types or []:
            entity_types_item = EventEntityType(entity_types_item_data)

            entity_types.append(entity_types_item)

        event_types = []
        _event_types = d.pop("eventTypes", UNSET)
        for event_types_item_data in _event_types or []:
            event_types_item = EventType(event_types_item_data)

            event_types.append(event_types_item)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, None, DateTimeFilterInterval]
        if _created_date is None:
            created_date = None
        elif isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = DateTimeFilterInterval.from_dict(_created_date)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, None, DateTimeFilterInterval]
        if _event_date is None:
            event_date = None
        elif isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = DateTimeFilterInterval.from_dict(_event_date)

        i_am_responsible = d.pop("iAmResponsible", UNSET)

        no_responsible = d.pop("noResponsible", UNSET)

        responsibles = cast(List[int], d.pop("responsibles", UNSET))

        query = d.pop("query", UNSET)

        timezone_id = d.pop("timezoneId", UNSET)

        _page_and_sort_by = d.pop("pageAndSortBy", UNSET)
        page_and_sort_by: Union[Unset, None, EventQuerySortPageAndSortByModel]
        if _page_and_sort_by is None:
            page_and_sort_by = None
        elif isinstance(_page_and_sort_by, Unset):
            page_and_sort_by = UNSET
        else:
            page_and_sort_by = EventQuerySortPageAndSortByModel.from_dict(_page_and_sort_by)

        search_event_query_model = cls(
            event_statuses=event_statuses,
            entity_types=entity_types,
            event_types=event_types,
            created_date=created_date,
            event_date=event_date,
            i_am_responsible=i_am_responsible,
            no_responsible=no_responsible,
            responsibles=responsibles,
            query=query,
            timezone_id=timezone_id,
            page_and_sort_by=page_and_sort_by,
        )

        return search_event_query_model
