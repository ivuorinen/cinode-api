import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_user_status import CompanyUserStatus
from ..models.company_user_type import CompanyUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_address_model import CompanyAddressModel
    from ..models.company_user_image_model import CompanyUserImageModel
    from ..models.link import Link
    from ..models.location_model import LocationModel


T = TypeVar("T", bound="CompanyUserExtendedModel")


@_attrs_define
class CompanyUserExtendedModel:
    """
    Attributes:
        status (Union[Unset, None, CompanyUserStatus]):

            Frånkopplad = 0

            Kommande = 2

            Aktiv = 3
        title (Union[Unset, None, str]):
        company_user_email (Union[Unset, None, str]):
        created_date_time (Union[Unset, None, datetime.datetime]):
        updated_date_time (Union[Unset, None, datetime.datetime]):
        company_address (Union[Unset, None, CompanyAddressModel]):
        home_address (Union[Unset, None, LocationModel]):
        image (Union[Unset, None, CompanyUserImageModel]):
        desired_assignment (Union[Unset, None, str]):
        internal_identifier (Union[Unset, None, str]):
        twitter (Union[Unset, None, str]):
        linked_in (Union[Unset, None, str]):
        homepage (Union[Unset, None, str]):
        blog (Union[Unset, None, str]):
        git_hub (Union[Unset, None, str]):
        company_user_id (Union[Unset, None, int]):
        company_id (Union[Unset, None, int]):
        seo_id (Union[Unset, None, str]):
        first_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        company_user_type (Union[Unset, None, CompanyUserType]):

            Medarbetare = 0

            Kandidat = 10

            Underkonsult = 20

            Api = 30

            Bot = 40
        id (Union[Unset, None, int]):
        links (Union[Unset, None, List['Link']]):
    """

    status: Union[Unset, None, CompanyUserStatus] = UNSET
    title: Union[Unset, None, str] = UNSET
    company_user_email: Union[Unset, None, str] = UNSET
    created_date_time: Union[Unset, None, datetime.datetime] = UNSET
    updated_date_time: Union[Unset, None, datetime.datetime] = UNSET
    company_address: Union[Unset, None, "CompanyAddressModel"] = UNSET
    home_address: Union[Unset, None, "LocationModel"] = UNSET
    image: Union[Unset, None, "CompanyUserImageModel"] = UNSET
    desired_assignment: Union[Unset, None, str] = UNSET
    internal_identifier: Union[Unset, None, str] = UNSET
    twitter: Union[Unset, None, str] = UNSET
    linked_in: Union[Unset, None, str] = UNSET
    homepage: Union[Unset, None, str] = UNSET
    blog: Union[Unset, None, str] = UNSET
    git_hub: Union[Unset, None, str] = UNSET
    company_user_id: Union[Unset, None, int] = UNSET
    company_id: Union[Unset, None, int] = UNSET
    seo_id: Union[Unset, None, str] = UNSET
    first_name: Union[Unset, None, str] = UNSET
    last_name: Union[Unset, None, str] = UNSET
    company_user_type: Union[Unset, None, CompanyUserType] = UNSET
    id: Union[Unset, None, int] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, None, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        title = self.title
        company_user_email = self.company_user_email
        created_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat() if self.created_date_time else None

        updated_date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.updated_date_time, Unset):
            updated_date_time = self.updated_date_time.isoformat() if self.updated_date_time else None

        company_address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.company_address, Unset):
            company_address = self.company_address.to_dict() if self.company_address else None

        home_address: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.home_address, Unset):
            home_address = self.home_address.to_dict() if self.home_address else None

        image: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict() if self.image else None

        desired_assignment = self.desired_assignment
        internal_identifier = self.internal_identifier
        twitter = self.twitter
        linked_in = self.linked_in
        homepage = self.homepage
        blog = self.blog
        git_hub = self.git_hub
        company_user_id = self.company_user_id
        company_id = self.company_id
        seo_id = self.seo_id
        first_name = self.first_name
        last_name = self.last_name
        company_user_type: Union[Unset, None, int] = UNSET
        if not isinstance(self.company_user_type, Unset):
            company_user_type = self.company_user_type.value if self.company_user_type else None

        id = self.id
        links: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            if self.links is None:
                links = None
            else:
                links = []
                for links_item_data in self.links:
                    links_item = links_item_data.to_dict()

                    links.append(links_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if company_user_email is not UNSET:
            field_dict["companyUserEmail"] = company_user_email
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if updated_date_time is not UNSET:
            field_dict["updatedDateTime"] = updated_date_time
        if company_address is not UNSET:
            field_dict["companyAddress"] = company_address
        if home_address is not UNSET:
            field_dict["homeAddress"] = home_address
        if image is not UNSET:
            field_dict["image"] = image
        if desired_assignment is not UNSET:
            field_dict["desiredAssignment"] = desired_assignment
        if internal_identifier is not UNSET:
            field_dict["internalIdentifier"] = internal_identifier
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if linked_in is not UNSET:
            field_dict["linkedIn"] = linked_in
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if blog is not UNSET:
            field_dict["blog"] = blog
        if git_hub is not UNSET:
            field_dict["gitHub"] = git_hub
        if company_user_id is not UNSET:
            field_dict["companyUserId"] = company_user_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if seo_id is not UNSET:
            field_dict["seoId"] = seo_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company_user_type is not UNSET:
            field_dict["companyUserType"] = company_user_type
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.company_address_model import CompanyAddressModel
        from ..models.company_user_image_model import CompanyUserImageModel
        from ..models.link import Link
        from ..models.location_model import LocationModel

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, None, CompanyUserStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyUserStatus(_status)

        title = d.pop("title", UNSET)

        company_user_email = d.pop("companyUserEmail", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, None, datetime.datetime]
        if _created_date_time is None:
            created_date_time = None
        elif isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        _updated_date_time = d.pop("updatedDateTime", UNSET)
        updated_date_time: Union[Unset, None, datetime.datetime]
        if _updated_date_time is None:
            updated_date_time = None
        elif isinstance(_updated_date_time, Unset):
            updated_date_time = UNSET
        else:
            updated_date_time = isoparse(_updated_date_time)

        _company_address = d.pop("companyAddress", UNSET)
        company_address: Union[Unset, None, CompanyAddressModel]
        if _company_address is None:
            company_address = None
        elif isinstance(_company_address, Unset):
            company_address = UNSET
        else:
            company_address = CompanyAddressModel.from_dict(_company_address)

        _home_address = d.pop("homeAddress", UNSET)
        home_address: Union[Unset, None, LocationModel]
        if _home_address is None:
            home_address = None
        elif isinstance(_home_address, Unset):
            home_address = UNSET
        else:
            home_address = LocationModel.from_dict(_home_address)

        _image = d.pop("image", UNSET)
        image: Union[Unset, None, CompanyUserImageModel]
        if _image is None:
            image = None
        elif isinstance(_image, Unset):
            image = UNSET
        else:
            image = CompanyUserImageModel.from_dict(_image)

        desired_assignment = d.pop("desiredAssignment", UNSET)

        internal_identifier = d.pop("internalIdentifier", UNSET)

        twitter = d.pop("twitter", UNSET)

        linked_in = d.pop("linkedIn", UNSET)

        homepage = d.pop("homepage", UNSET)

        blog = d.pop("blog", UNSET)

        git_hub = d.pop("gitHub", UNSET)

        company_user_id = d.pop("companyUserId", UNSET)

        company_id = d.pop("companyId", UNSET)

        seo_id = d.pop("seoId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _company_user_type = d.pop("companyUserType", UNSET)
        company_user_type: Union[Unset, None, CompanyUserType]
        if _company_user_type is None:
            company_user_type = None
        elif isinstance(_company_user_type, Unset):
            company_user_type = UNSET
        else:
            company_user_type = CompanyUserType(_company_user_type)

        id = d.pop("id", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        company_user_extended_model = cls(
            status=status,
            title=title,
            company_user_email=company_user_email,
            created_date_time=created_date_time,
            updated_date_time=updated_date_time,
            company_address=company_address,
            home_address=home_address,
            image=image,
            desired_assignment=desired_assignment,
            internal_identifier=internal_identifier,
            twitter=twitter,
            linked_in=linked_in,
            homepage=homepage,
            blog=blog,
            git_hub=git_hub,
            company_user_id=company_user_id,
            company_id=company_id,
            seo_id=seo_id,
            first_name=first_name,
            last_name=last_name,
            company_user_type=company_user_type,
            id=id,
            links=links,
        )

        return company_user_extended_model
