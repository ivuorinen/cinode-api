from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.company_size import CompanySize
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCustomerAddModel")


@_attrs_define
class CompanyCustomerAddModel:
    """
    Attributes:
        name (str):
        status (Union[Unset, bool]):
        description (Union[Unset, None, str]):
        corporate_identity_number (Union[Unset, None, str]):
        vat_number (Union[Unset, None, str]):
        identification (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        homepage (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        fax (Union[Unset, None, str]):
        intermediator (Union[Unset, bool]):
        size (Union[Unset, None, CompanySize]):

            Egenföretagare = 0

            2-10 = 1

            11-50 = 2

            51-200 = 3

            201-500 = 4

            501-1 000 = 5

            1 001-5 000 = 6

            5 001-10 000 = 7

            10 001+ = 8
        country_id (Union[Unset, None, int]):
        turn_over (Union[Unset, None, int]):
        turn_over_currency_id (Union[Unset, None, int]):
    """

    name: str
    status: Union[Unset, bool] = UNSET
    description: Union[Unset, None, str] = UNSET
    corporate_identity_number: Union[Unset, None, str] = UNSET
    vat_number: Union[Unset, None, str] = UNSET
    identification: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    homepage: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    fax: Union[Unset, None, str] = UNSET
    intermediator: Union[Unset, bool] = UNSET
    size: Union[Unset, None, CompanySize] = UNSET
    country_id: Union[Unset, None, int] = UNSET
    turn_over: Union[Unset, None, int] = UNSET
    turn_over_currency_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        status = self.status
        description = self.description
        corporate_identity_number = self.corporate_identity_number
        vat_number = self.vat_number
        identification = self.identification
        email = self.email
        homepage = self.homepage
        phone = self.phone
        fax = self.fax
        intermediator = self.intermediator
        size: Union[Unset, None, int] = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.value if self.size else None

        country_id = self.country_id
        turn_over = self.turn_over
        turn_over_currency_id = self.turn_over_currency_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if vat_number is not UNSET:
            field_dict["vatNumber"] = vat_number
        if identification is not UNSET:
            field_dict["identification"] = identification
        if email is not UNSET:
            field_dict["email"] = email
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if phone is not UNSET:
            field_dict["phone"] = phone
        if fax is not UNSET:
            field_dict["fax"] = fax
        if intermediator is not UNSET:
            field_dict["intermediator"] = intermediator
        if size is not UNSET:
            field_dict["size"] = size
        if country_id is not UNSET:
            field_dict["countryId"] = country_id
        if turn_over is not UNSET:
            field_dict["turnOver"] = turn_over
        if turn_over_currency_id is not UNSET:
            field_dict["turnOverCurrencyId"] = turn_over_currency_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        status = d.pop("status", UNSET)

        description = d.pop("description", UNSET)

        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        vat_number = d.pop("vatNumber", UNSET)

        identification = d.pop("identification", UNSET)

        email = d.pop("email", UNSET)

        homepage = d.pop("homepage", UNSET)

        phone = d.pop("phone", UNSET)

        fax = d.pop("fax", UNSET)

        intermediator = d.pop("intermediator", UNSET)

        _size = d.pop("size", UNSET)
        size: Union[Unset, None, CompanySize]
        if _size is None:
            size = None
        elif isinstance(_size, Unset):
            size = UNSET
        else:
            size = CompanySize(_size)

        country_id = d.pop("countryId", UNSET)

        turn_over = d.pop("turnOver", UNSET)

        turn_over_currency_id = d.pop("turnOverCurrencyId", UNSET)

        company_customer_add_model = cls(
            name=name,
            status=status,
            description=description,
            corporate_identity_number=corporate_identity_number,
            vat_number=vat_number,
            identification=identification,
            email=email,
            homepage=homepage,
            phone=phone,
            fax=fax,
            intermediator=intermediator,
            size=size,
            country_id=country_id,
            turn_over=turn_over,
            turn_over_currency_id=turn_over_currency_id,
        )

        return company_customer_add_model
