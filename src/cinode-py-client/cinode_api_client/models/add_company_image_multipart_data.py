from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="AddCompanyImageMultipartData")


@_attrs_define
class AddCompanyImageMultipartData:
    """
    Attributes:
        file (File):
        set_as_primary (Union[Unset, bool]):
    """

    file: File
    set_as_primary: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        set_as_primary = self.set_as_primary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "File": file,
            }
        )
        if set_as_primary is not UNSET:
            field_dict["SetAsPrimary"] = set_as_primary

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        file = self.file.to_tuple()

        set_as_primary = (
            self.set_as_primary
            if isinstance(self.set_as_primary, Unset)
            else (None, str(self.set_as_primary).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "File": file,
            }
        )
        if set_as_primary is not UNSET:
            field_dict["SetAsPrimary"] = set_as_primary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("File")))

        set_as_primary = d.pop("SetAsPrimary", UNSET)

        add_company_image_multipart_data = cls(
            file=file,
            set_as_primary=set_as_primary,
        )

        add_company_image_multipart_data.additional_properties = d
        return add_company_image_multipart_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
