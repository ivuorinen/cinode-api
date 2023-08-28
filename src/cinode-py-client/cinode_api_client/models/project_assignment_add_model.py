import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.contract_type import ContractType
from ..models.extent_type import ExtentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssignmentAddModel")


@_attrs_define
class ProjectAssignmentAddModel:
    """
    Attributes:
        title (str):
        description (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        rate (Union[Unset, None, int]):
        extent (Union[Unset, None, int]):
        oral_agreement_to_date (Union[Unset, None, datetime.datetime]):
        option_to_date (Union[Unset, None, datetime.datetime]):
        contract_type (Union[Unset, ContractType]):

            Timpris = 0

            Fastpris = 1
        extent_type (Union[Unset, ExtentType]):

            Procent = 0

            Timmar = 1
        currency_id (Union[Unset, None, int]):
    """

    title: str
    description: Union[Unset, None, str] = UNSET
    start_date: Union[Unset, None, datetime.datetime] = UNSET
    end_date: Union[Unset, None, datetime.datetime] = UNSET
    rate: Union[Unset, None, int] = UNSET
    extent: Union[Unset, None, int] = UNSET
    oral_agreement_to_date: Union[Unset, None, datetime.datetime] = UNSET
    option_to_date: Union[Unset, None, datetime.datetime] = UNSET
    contract_type: Union[Unset, ContractType] = UNSET
    extent_type: Union[Unset, ExtentType] = UNSET
    currency_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat() if self.start_date else None

        end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat() if self.end_date else None

        rate = self.rate
        extent = self.extent
        oral_agreement_to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.oral_agreement_to_date, Unset):
            oral_agreement_to_date = self.oral_agreement_to_date.isoformat() if self.oral_agreement_to_date else None

        option_to_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.option_to_date, Unset):
            option_to_date = self.option_to_date.isoformat() if self.option_to_date else None

        contract_type: Union[Unset, int] = UNSET
        if not isinstance(self.contract_type, Unset):
            contract_type = self.contract_type.value

        extent_type: Union[Unset, int] = UNSET
        if not isinstance(self.extent_type, Unset):
            extent_type = self.extent_type.value

        currency_id = self.currency_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if rate is not UNSET:
            field_dict["rate"] = rate
        if extent is not UNSET:
            field_dict["extent"] = extent
        if oral_agreement_to_date is not UNSET:
            field_dict["oralAgreementToDate"] = oral_agreement_to_date
        if option_to_date is not UNSET:
            field_dict["optionToDate"] = option_to_date
        if contract_type is not UNSET:
            field_dict["contractType"] = contract_type
        if extent_type is not UNSET:
            field_dict["extentType"] = extent_type
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        description = d.pop("description", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, None, datetime.datetime]
        if _start_date is None:
            start_date = None
        elif isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, None, datetime.datetime]
        if _end_date is None:
            end_date = None
        elif isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        rate = d.pop("rate", UNSET)

        extent = d.pop("extent", UNSET)

        _oral_agreement_to_date = d.pop("oralAgreementToDate", UNSET)
        oral_agreement_to_date: Union[Unset, None, datetime.datetime]
        if _oral_agreement_to_date is None:
            oral_agreement_to_date = None
        elif isinstance(_oral_agreement_to_date, Unset):
            oral_agreement_to_date = UNSET
        else:
            oral_agreement_to_date = isoparse(_oral_agreement_to_date)

        _option_to_date = d.pop("optionToDate", UNSET)
        option_to_date: Union[Unset, None, datetime.datetime]
        if _option_to_date is None:
            option_to_date = None
        elif isinstance(_option_to_date, Unset):
            option_to_date = UNSET
        else:
            option_to_date = isoparse(_option_to_date)

        _contract_type = d.pop("contractType", UNSET)
        contract_type: Union[Unset, ContractType]
        if isinstance(_contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = ContractType(_contract_type)

        _extent_type = d.pop("extentType", UNSET)
        extent_type: Union[Unset, ExtentType]
        if isinstance(_extent_type, Unset):
            extent_type = UNSET
        else:
            extent_type = ExtentType(_extent_type)

        currency_id = d.pop("currencyId", UNSET)

        project_assignment_add_model = cls(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            rate=rate,
            extent=extent,
            oral_agreement_to_date=oral_agreement_to_date,
            option_to_date=option_to_date,
            contract_type=contract_type,
            extent_type=extent_type,
            currency_id=currency_id,
        )

        return project_assignment_add_model
