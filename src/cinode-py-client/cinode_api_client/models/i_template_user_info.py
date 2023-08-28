import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ITemplateUserInfo")


@_attrs_define
class ITemplateUserInfo:
    """
    Attributes:
        firstname (Union[Unset, None, str]):
        lastname (Union[Unset, None, str]):
        fullname (Union[Unset, None, str]):
        phone (Union[Unset, None, str]):
        date_of_birth (Union[Unset, None, datetime.datetime]):
        email (Union[Unset, None, str]):
        twitter_user_name (Union[Unset, None, str]):
        linked_in_user_name (Union[Unset, None, str]):
        homepage_url (Union[Unset, None, str]):
        blogg_url (Union[Unset, None, str]):
        git_hub_user_name (Union[Unset, None, str]):
        location (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        internal_identifier (Union[Unset, None, str]):
    """

    firstname: Union[Unset, None, str] = UNSET
    lastname: Union[Unset, None, str] = UNSET
    fullname: Union[Unset, None, str] = UNSET
    phone: Union[Unset, None, str] = UNSET
    date_of_birth: Union[Unset, None, datetime.datetime] = UNSET
    email: Union[Unset, None, str] = UNSET
    twitter_user_name: Union[Unset, None, str] = UNSET
    linked_in_user_name: Union[Unset, None, str] = UNSET
    homepage_url: Union[Unset, None, str] = UNSET
    blogg_url: Union[Unset, None, str] = UNSET
    git_hub_user_name: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    internal_identifier: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        firstname = self.firstname
        lastname = self.lastname
        fullname = self.fullname
        phone = self.phone
        date_of_birth: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat() if self.date_of_birth else None

        email = self.email
        twitter_user_name = self.twitter_user_name
        linked_in_user_name = self.linked_in_user_name
        homepage_url = self.homepage_url
        blogg_url = self.blogg_url
        git_hub_user_name = self.git_hub_user_name
        location = self.location
        country = self.country
        internal_identifier = self.internal_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if fullname is not UNSET:
            field_dict["fullname"] = fullname
        if phone is not UNSET:
            field_dict["phone"] = phone
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if email is not UNSET:
            field_dict["email"] = email
        if twitter_user_name is not UNSET:
            field_dict["twitterUserName"] = twitter_user_name
        if linked_in_user_name is not UNSET:
            field_dict["linkedInUserName"] = linked_in_user_name
        if homepage_url is not UNSET:
            field_dict["homepageUrl"] = homepage_url
        if blogg_url is not UNSET:
            field_dict["bloggUrl"] = blogg_url
        if git_hub_user_name is not UNSET:
            field_dict["gitHubUserName"] = git_hub_user_name
        if location is not UNSET:
            field_dict["location"] = location
        if country is not UNSET:
            field_dict["country"] = country
        if internal_identifier is not UNSET:
            field_dict["internalIdentifier"] = internal_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        fullname = d.pop("fullname", UNSET)

        phone = d.pop("phone", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, None, datetime.datetime]
        if _date_of_birth is None:
            date_of_birth = None
        elif isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        email = d.pop("email", UNSET)

        twitter_user_name = d.pop("twitterUserName", UNSET)

        linked_in_user_name = d.pop("linkedInUserName", UNSET)

        homepage_url = d.pop("homepageUrl", UNSET)

        blogg_url = d.pop("bloggUrl", UNSET)

        git_hub_user_name = d.pop("gitHubUserName", UNSET)

        location = d.pop("location", UNSET)

        country = d.pop("country", UNSET)

        internal_identifier = d.pop("internalIdentifier", UNSET)

        i_template_user_info = cls(
            firstname=firstname,
            lastname=lastname,
            fullname=fullname,
            phone=phone,
            date_of_birth=date_of_birth,
            email=email,
            twitter_user_name=twitter_user_name,
            linked_in_user_name=linked_in_user_name,
            homepage_url=homepage_url,
            blogg_url=blogg_url,
            git_hub_user_name=git_hub_user_name,
            location=location,
            country=country,
            internal_identifier=internal_identifier,
        )

        return i_template_user_info
