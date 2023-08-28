from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ITemplateCompany")


@_attrs_define
class ITemplateCompany:
    """
    Attributes:
        company_id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        seo_id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        corporate_identity_number (Union[Unset, None, str]):
        registration_year (Union[Unset, int]):
        is_tax_registered (Union[Unset, bool]):
        is_using_freemium_resumes (Union[Unset, bool]):
    """

    company_id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    corporate_identity_number: Union[Unset, None, str] = UNSET
    registration_year: Union[Unset, int] = UNSET
    is_tax_registered: Union[Unset, bool] = UNSET
    is_using_freemium_resumes: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        company_id = self.company_id
        name = self.name
        seo_id = self.seo_id
        description = self.description
        corporate_identity_number = self.corporate_identity_number
        registration_year = self.registration_year
        is_tax_registered = self.is_tax_registered
        is_using_freemium_resumes = self.is_using_freemium_resumes

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if description is not UNSET:
            field_dict["description"] = description
        if corporate_identity_number is not UNSET:
            field_dict["corporateIdentityNumber"] = corporate_identity_number
        if registration_year is not UNSET:
            field_dict["registrationYear"] = registration_year
        if is_tax_registered is not UNSET:
            field_dict["isTaxRegistered"] = is_tax_registered
        if is_using_freemium_resumes is not UNSET:
            field_dict["isUsingFreemiumResumes"] = is_using_freemium_resumes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        seo_id = d.pop("seoId", UNSET)

        description = d.pop("description", UNSET)

        corporate_identity_number = d.pop("corporateIdentityNumber", UNSET)

        registration_year = d.pop("registrationYear", UNSET)

        is_tax_registered = d.pop("isTaxRegistered", UNSET)

        is_using_freemium_resumes = d.pop("isUsingFreemiumResumes", UNSET)

        i_template_company = cls(
            company_id=company_id,
            name=name,
            seo_id=seo_id,
            description=description,
            corporate_identity_number=corporate_identity_number,
            registration_year=registration_year,
            is_tax_registered=is_tax_registered,
            is_using_freemium_resumes=is_using_freemium_resumes,
        )

        return i_template_company
