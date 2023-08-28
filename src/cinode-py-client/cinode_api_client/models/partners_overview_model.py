from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_base_model import PartnerBaseModel
    from ..models.partners_filter_model import PartnersFilterModel


T = TypeVar("T", bound="PartnersOverviewModel")


@_attrs_define
class PartnersOverviewModel:
    """
    Attributes:
        partners (Union[Unset, None, List['PartnerBaseModel']]):
        total_items (Union[Unset, int]):
        filter_ (Union[Unset, None, PartnersFilterModel]):
    """

    partners: Union[Unset, None, List["PartnerBaseModel"]] = UNSET
    total_items: Union[Unset, int] = UNSET
    filter_: Union[Unset, None, "PartnersFilterModel"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        partners: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.partners, Unset):
            if self.partners is None:
                partners = None
            else:
                partners = []
                for partners_item_data in self.partners:
                    partners_item = partners_item_data.to_dict()

                    partners.append(partners_item)

        total_items = self.total_items
        filter_: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict() if self.filter_ else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if partners is not UNSET:
            field_dict["partners"] = partners
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.partner_base_model import PartnerBaseModel
        from ..models.partners_filter_model import PartnersFilterModel

        d = src_dict.copy()
        partners = []
        _partners = d.pop("partners", UNSET)
        for partners_item_data in _partners or []:
            partners_item = PartnerBaseModel.from_dict(partners_item_data)

            partners.append(partners_item)

        total_items = d.pop("totalItems", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, None, PartnersFilterModel]
        if _filter_ is None:
            filter_ = None
        elif isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = PartnersFilterModel.from_dict(_filter_)

        partners_overview_model = cls(
            partners=partners,
            total_items=total_items,
            filter_=filter_,
        )

        return partners_overview_model
