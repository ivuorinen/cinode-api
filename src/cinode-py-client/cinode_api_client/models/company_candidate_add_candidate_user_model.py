from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyCandidateAddCandidateUserModel")


@_attrs_define
class CompanyCandidateAddCandidateUserModel:
    """
    Attributes:
        email (str):
        first_name (str):
        last_name (str):
        password (str):
        confirm_password (str):
        create_profile (Union[Unset, None, bool]):
        language_id (Union[Unset, None, int]):
    """

    email: str
    first_name: str
    last_name: str
    password: str
    confirm_password: str
    create_profile: Union[Unset, None, bool] = False
    language_id: Union[Unset, None, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        password = self.password
        confirm_password = self.confirm_password
        create_profile = self.create_profile
        language_id = self.language_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "password": password,
                "confirmPassword": confirm_password,
            }
        )
        if create_profile is not UNSET:
            field_dict["createProfile"] = create_profile
        if language_id is not UNSET:
            field_dict["languageId"] = language_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        password = d.pop("password")

        confirm_password = d.pop("confirmPassword")

        create_profile = d.pop("createProfile", UNSET)

        language_id = d.pop("languageId", UNSET)

        company_candidate_add_candidate_user_model = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            confirm_password=confirm_password,
            create_profile=create_profile,
            language_id=language_id,
        )

        return company_candidate_add_candidate_user_model
