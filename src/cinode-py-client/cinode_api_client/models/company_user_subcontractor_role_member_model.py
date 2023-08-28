from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_model import CurrencyModel
    from ..models.project_assignment_base_model import ProjectAssignmentBaseModel
    from ..models.project_assignment_member_state_history_model import ProjectAssignmentMemberStateHistoryModel


T = TypeVar("T", bound="CompanyUserSubcontractorRoleMemberModel")


@_attrs_define
class CompanyUserSubcontractorRoleMemberModel:
    """
    Attributes:
        project_assignment_id (Union[Unset, int]):
        assignment_tariff (Union[Unset, None, int]):
        currency (Union[Unset, None, CurrencyModel]):
        current_state (Union[Unset, None, ProjectAssignmentMemberStateHistoryModel]):
        project_assignment (Union[Unset, None, ProjectAssignmentBaseModel]):
    """

    project_assignment_id: Union[Unset, int] = UNSET
    assignment_tariff: Union[Unset, None, int] = UNSET
    currency: Union[Unset, None, "CurrencyModel"] = UNSET
    current_state: Union[Unset, None, "ProjectAssignmentMemberStateHistoryModel"] = UNSET
    project_assignment: Union[Unset, None, "ProjectAssignmentBaseModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        project_assignment_id = self.project_assignment_id
        assignment_tariff = self.assignment_tariff
        currency: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict() if self.currency else None

        current_state: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.current_state, Unset):
            current_state = self.current_state.to_dict() if self.current_state else None

        project_assignment: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.project_assignment, Unset):
            project_assignment = self.project_assignment.to_dict() if self.project_assignment else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if project_assignment_id is not UNSET:
            field_dict["projectAssignmentId"] = project_assignment_id
        if assignment_tariff is not UNSET:
            field_dict["assignmentTariff"] = assignment_tariff
        if currency is not UNSET:
            field_dict["currency"] = currency
        if current_state is not UNSET:
            field_dict["currentState"] = current_state
        if project_assignment is not UNSET:
            field_dict["projectAssignment"] = project_assignment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency_model import CurrencyModel
        from ..models.project_assignment_base_model import ProjectAssignmentBaseModel
        from ..models.project_assignment_member_state_history_model import ProjectAssignmentMemberStateHistoryModel

        d = src_dict.copy()
        project_assignment_id = d.pop("projectAssignmentId", UNSET)

        assignment_tariff = d.pop("assignmentTariff", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, None, CurrencyModel]
        if _currency is None:
            currency = None
        elif isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = CurrencyModel.from_dict(_currency)

        _current_state = d.pop("currentState", UNSET)
        current_state: Union[Unset, None, ProjectAssignmentMemberStateHistoryModel]
        if _current_state is None:
            current_state = None
        elif isinstance(_current_state, Unset):
            current_state = UNSET
        else:
            current_state = ProjectAssignmentMemberStateHistoryModel.from_dict(_current_state)

        _project_assignment = d.pop("projectAssignment", UNSET)
        project_assignment: Union[Unset, None, ProjectAssignmentBaseModel]
        if _project_assignment is None:
            project_assignment = None
        elif isinstance(_project_assignment, Unset):
            project_assignment = UNSET
        else:
            project_assignment = ProjectAssignmentBaseModel.from_dict(_project_assignment)

        company_user_subcontractor_role_member_model = cls(
            project_assignment_id=project_assignment_id,
            assignment_tariff=assignment_tariff,
            currency=currency,
            current_state=current_state,
            project_assignment=project_assignment,
        )

        return company_user_subcontractor_role_member_model
