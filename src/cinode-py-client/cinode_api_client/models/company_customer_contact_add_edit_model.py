from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCustomerContactAddEditModel")


@_attrs_define
class CompanyCustomerContactAddEditModel:
    """
    Attributes:
        first_name (str):
        last_name (str):
        email (Union[Unset, None, str]):
        phone1 (Union[Unset, None, str]):
        phone2 (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        comments (Union[Unset, None, str]):
        pronouns (Union[Unset, None, str]):
    """

    first_name: str
    last_name: str
    email: Union[Unset, None, str] = UNSET
    phone1: Union[Unset, None, str] = UNSET
    phone2: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    comments: Union[Unset, None, str] = UNSET
    pronouns: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        phone1 = self.phone1
        phone2 = self.phone2
        title = self.title
        comments = self.comments
        pronouns = self.pronouns

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if phone1 is not UNSET:
            field_dict["phone1"] = phone1
        if phone2 is not UNSET:
            field_dict["phone2"] = phone2
        if title is not UNSET:
            field_dict["title"] = title
        if comments is not UNSET:
            field_dict["comments"] = comments
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email", UNSET)

        phone1 = d.pop("phone1", UNSET)

        phone2 = d.pop("phone2", UNSET)

        title = d.pop("title", UNSET)

        comments = d.pop("comments", UNSET)

        pronouns = d.pop("pronouns", UNSET)

        company_customer_contact_add_edit_model = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone1=phone1,
            phone2=phone2,
            title=title,
            comments=comments,
            pronouns=pronouns,
        )

        return company_customer_contact_add_edit_model
