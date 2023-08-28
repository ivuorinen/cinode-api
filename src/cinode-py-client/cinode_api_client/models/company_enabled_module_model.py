from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.module_type import ModuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyEnabledModuleModel")


@_attrs_define
class CompanyEnabledModuleModel:
    """
    Attributes:
        module_id (Union[Unset, ModuleType]):

            CompanyUserResume = 1

            Customers = 2

            Assignments = 3

            Partners = 4

            Offers = 5

            Reports = 6

            Recruitment = 8

            Absence = 9

            Api = 10

            ReferenceText = 11

            ProfileCompleteness = 12

            CalendarSync = 13

            AllowWidgetModification = 14

            ConfiguredFilters = 19

            SkillSets = 20

            ProfileUpdateReminders = 21

            OverdueProjectReminders = 22

            EmailSync = 23

            ApplicationRegistration = 30

            ApplicationDirectory = 31

            NextGenResume = 40

            HideLinkToMvcProfilePageInSidebarAndRemoveEditAndCopyCVInoldViewAndTheBetaChips = 41

            ImportCv = 42

            AI = 43

            ExternalAccounts = 50

            ConvertAccount = 51

            UserProvisioning = 52

            Webhooks = 60

            GrowthPlan = 70

            Intercom = 600
    """

    module_id: Union[Unset, ModuleType] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        module_id: Union[Unset, int] = UNSET
        if not isinstance(self.module_id, Unset):
            module_id = self.module_id.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if module_id is not UNSET:
            field_dict["moduleId"] = module_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _module_id = d.pop("moduleId", UNSET)
        module_id: Union[Unset, ModuleType]
        if isinstance(_module_id, Unset):
            module_id = UNSET
        else:
            module_id = ModuleType(_module_id)

        company_enabled_module_model = cls(
            module_id=module_id,
        )

        return company_enabled_module_model
