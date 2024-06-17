import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.save_to_api_option import SaveToApiOption
from ..models.training_type import TrainingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyUserProfileTrainingAddEditModel")


@_attrs_define
class CompanyUserProfileTrainingAddEditModel:
    """
    Attributes:
        title (Union[Unset, None, str]):
        year (Union[Unset, int]):
        issuer (Union[Unset, None, str]):
        supplier (Union[Unset, None, str]):
        code (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        training_type (Union[Unset, TrainingType]):

            Kurs = 0

            Certifiering = 1
        url (Union[Unset, None, str]):
        expire_date (Union[Unset, None, datetime.datetime]):
        save_to (Union[Unset, SaveToApiOption]):

            AllResumesOfLanguage = 3

            Profile = 5
    """

    title: Union[Unset, None, str] = UNSET
    year: Union[Unset, int] = UNSET
    issuer: Union[Unset, None, str] = UNSET
    supplier: Union[Unset, None, str] = UNSET
    code: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    training_type: Union[Unset, TrainingType] = UNSET
    url: Union[Unset, None, str] = UNSET
    expire_date: Union[Unset, None, datetime.datetime] = UNSET
    save_to: Union[Unset, SaveToApiOption] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        year = self.year
        issuer = self.issuer
        supplier = self.supplier
        code = self.code
        description = self.description
        training_type: Union[Unset, int] = UNSET
        if not isinstance(self.training_type, Unset):
            training_type = self.training_type.value

        url = self.url
        expire_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.expire_date, Unset):
            expire_date = self.expire_date.isoformat() if self.expire_date else None

        save_to: Union[Unset, int] = UNSET
        if not isinstance(self.save_to, Unset):
            save_to = self.save_to.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if year is not UNSET:
            field_dict["year"] = year
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if training_type is not UNSET:
            field_dict["trainingType"] = training_type
        if url is not UNSET:
            field_dict["url"] = url
        if expire_date is not UNSET:
            field_dict["expireDate"] = expire_date
        if save_to is not UNSET:
            field_dict["saveTo"] = save_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        year = d.pop("year", UNSET)

        issuer = d.pop("issuer", UNSET)

        supplier = d.pop("supplier", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        _training_type = d.pop("trainingType", UNSET)
        training_type: Union[Unset, TrainingType]
        if isinstance(_training_type, Unset):
            training_type = UNSET
        else:
            training_type = TrainingType(_training_type)

        url = d.pop("url", UNSET)

        _expire_date = d.pop("expireDate", UNSET)
        expire_date: Union[Unset, None, datetime.datetime]
        if _expire_date is None:
            expire_date = None
        elif isinstance(_expire_date, Unset):
            expire_date = UNSET
        else:
            expire_date = isoparse(_expire_date)

        _save_to = d.pop("saveTo", UNSET)
        save_to: Union[Unset, SaveToApiOption]
        if isinstance(_save_to, Unset):
            save_to = UNSET
        else:
            save_to = SaveToApiOption(_save_to)

        company_user_profile_training_add_edit_model = cls(
            title=title,
            year=year,
            issuer=issuer,
            supplier=supplier,
            code=code,
            description=description,
            training_type=training_type,
            url=url,
            expire_date=expire_date,
            save_to=save_to,
        )

        return company_user_profile_training_add_edit_model
