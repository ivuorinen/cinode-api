from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.project_state import ProjectState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_query_sort_page_and_sort_by_model import ProjectQuerySortPageAndSortByModel


T = TypeVar("T", bound="SearchProjectQueryModel")


@_attrs_define
class SearchProjectQueryModel:
    """
    Attributes:
        title (Union[Unset, None, str]):
        identification (Union[Unset, None, str]):
        customer_identifier (Union[Unset, None, str]):
        corporate_identity_number (Union[Unset, None, str]):
        customer_id (Union[Unset, None, int]):
        page_and_sort_by (Union[Unset, None, ProjectQuerySortPageAndSortByModel]):
        pipelines (Union[Unset, None, List[int]]): Your Project Pipelines can be retrieved from the GET ProjectPipelines
            endpoint
        sales_managers (Union[Unset, None, List[int]]):
        customers (Union[Unset, None, List[int]]):
        intermediators (Union[Unset, None, List[int]]):
        project_states (Union[Unset, None, List[ProjectState]]): Open = 0,
            Won = 30,
            Lost = 40,
            Abandoned = 50,
            Suspended = 60
    """

    title: Union[Unset, None, str] = UNSET
    identification: Union[Unset, None, str] = UNSET
    customer_identifier: Union[Unset, None, str] = UNSET
    corporate_identity_number: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, None, int] = UNSET
    page_and_sort_by: Union[Unset, None, "ProjectQuerySortPageAndSortByModel"] = UNSET
    pipelines: Union[Unset, None, List[int]] = UNSET
    sales_managers: Union[Unset, None, List[int]] = UNSET
    customers: Union[Unset, None, List[int]] = UNSET
    intermediators: Union[Unset, None, List[int]] = UNSET
    project_states: Union[Unset, None, List[ProjectState]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        identification = self.identification
        customer_identifier = self.customer_identifier
        corporate_identity_number = self.corporate_identity_number
        customer_id = self.customer_id
        page_and_sort_by: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.page_and_sort_by, Unset):
            page_and_sort_by = self.page_and_sort_by.to_dict() if self.page_and_sort_by else None

        pipelines: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.pipelines, Unset):
            if self.pipelines is None:
                pipelines = None
            else:
                pipelines = self.pipelines

        sales_managers: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.sales_managers, Unset):
            if self.sales_managers is None:
                sales_managers = None
            else:
                sales_managers = self.sales_managers

        customers: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.customers, Unset):
            if self.customers is None:
                customers = None
            else:
                customers = self.customers

        intermediators: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.intermediators, Unset):
            if self.intermediators is None:
                intermediators = None
            else:
                intermediators = self.intermediators

        project_states: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.project_states, Unset):
            if self.project_states is None:
                project_states = None
            else:
                project_states = []
                for project_states_item_data in self.project_states:
                    project_states_item = project_states_item_data.value

                    project_states.append(project_states_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if identification is not UNSET:
            field_dict["identification"] = identification
        if customer_identifier is not UNSET:
            field_dict["customerIdentifier"] = customer_identifier
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if page_and_sort_by is not UNSET:
            field_dict["pageAndSortBy"] = page_and_sort_by
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines
        if sales_managers is not UNSET:
            field_dict["salesManagers"] = sales_managers
        if customers is not UNSET:
            field_dict["customers"] = customers
        if intermediators is not UNSET:
            field_dict["intermediators"] = intermediators
        if project_states is not UNSET:
            field_dict["projectStates"] = project_states

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_query_sort_page_and_sort_by_model import ProjectQuerySortPageAndSortByModel

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        identification = d.pop("identification", UNSET)

        customer_identifier = d.pop("customerIdentifier", UNSET)

        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        customer_id = d.pop("customerId", UNSET)

        _page_and_sort_by = d.pop("pageAndSortBy", UNSET)
        page_and_sort_by: Union[Unset, None, ProjectQuerySortPageAndSortByModel]
        if _page_and_sort_by is None:
            page_and_sort_by = None
        elif isinstance(_page_and_sort_by, Unset):
            page_and_sort_by = UNSET
        else:
            page_and_sort_by = ProjectQuerySortPageAndSortByModel.from_dict(_page_and_sort_by)

        pipelines = cast(List[int], d.pop("pipelines", UNSET))

        sales_managers = cast(List[int], d.pop("salesManagers", UNSET))

        customers = cast(List[int], d.pop("customers", UNSET))

        intermediators = cast(List[int], d.pop("intermediators", UNSET))

        project_states = []
        _project_states = d.pop("projectStates", UNSET)
        for project_states_item_data in _project_states or []:
            project_states_item = ProjectState(project_states_item_data)

            project_states.append(project_states_item)

        search_project_query_model = cls(
            title=title,
            identification=identification,
            customer_identifier=customer_identifier,
            corporate_identity_number=corporate_identity_number,
            customer_id=customer_id,
            page_and_sort_by=page_and_sort_by,
            pipelines=pipelines,
            sales_managers=sales_managers,
            customers=customers,
            intermediators=intermediators,
            project_states=project_states,
        )

        return search_project_query_model
