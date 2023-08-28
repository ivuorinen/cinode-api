import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_user_subcontractor_status import CompanyUserSubcontractorStatus
from ..models.company_user_type import CompanyUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_address_model import CompanyAddressModel
    from ..models.company_subcontractor_group_base_model import CompanySubcontractorGroupBaseModel
    from ..models.company_tag_base_model import CompanyTagBaseModel
    from ..models.company_user_image_model import CompanyUserImageModel
    from ..models.company_user_resume_base_model import CompanyUserResumeBaseModel
    from ..models.company_user_subcontractor_attachment_model import CompanyUserSubcontractorAttachmentModel
    from ..models.currency_model import CurrencyModel
    from ..models.link import Link
    from ..models.location_model import LocationModel


T = TypeVar("T", bound="CompanyUserSubcontractorModel")


@_attrs_define
class CompanyUserSubcontractorModel:
    """
    Attributes:
        resumes (Union[Unset, None, List['CompanyUserResumeBaseModel']]):
        default_currency (Union[Unset, None, CurrencyModel]):
        tariff (Union[Unset, None, int]):
        created_date_time (Union[Unset, datetime.datetime]):
        groups (Union[Unset, None, List['CompanySubcontractorGroupBaseModel']]):
        phone (Union[Unset, None, str]):
        tags (Union[Unset, None, List['CompanyTagBaseModel']]):
        attachments (Union[Unset, None, List['CompanyUserSubcontractorAttachmentModel']]):
        status (Union[Unset, None, CompanyUserSubcontractorStatus]):

            Frånkopplad = 0

            Aktiv = 1
        rating (Union[Unset, None, int]):
        email (Union[Unset, None, str]):
        company_name (Union[Unset, None, str]):
        company_identifier (Union[Unset, None, str]):
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

    resumes: Union[Unset, None, List["CompanyUserResumeBaseModel"]] = UNSET
    default_currency: Union[Unset, None, "CurrencyModel"] = UNSET
    tariff: Union[Unset, None, int] = UNSET
    created_date_time: Union[Unset, datetime.datetime] = UNSET
    groups: Union[Unset, None, List["CompanySubcontractorGroupBaseModel"]] = UNSET
    phone: Union[Unset, None, str] = UNSET
    tags: Union[Unset, None, List["CompanyTagBaseModel"]] = UNSET
    attachments: Union[Unset, None, List["CompanyUserSubcontractorAttachmentModel"]] = UNSET
    status: Union[Unset, None, CompanyUserSubcontractorStatus] = UNSET
    rating: Union[Unset, None, int] = UNSET
    email: Union[Unset, None, str] = UNSET
    company_name: Union[Unset, None, str] = UNSET
    company_identifier: Union[Unset, None, str] = UNSET
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
        resumes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resumes, Unset):
            if self.resumes is None:
                resumes = None
            else:
                resumes = []
                for resumes_item_data in self.resumes:
                    resumes_item = resumes_item_data.to_dict()

                    resumes.append(resumes_item)

        default_currency: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.default_currency, Unset):
            default_currency = self.default_currency.to_dict() if self.default_currency else None

        tariff = self.tariff
        created_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_time, Unset):
            created_date_time = self.created_date_time.isoformat()

        groups: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            if self.groups is None:
                groups = None
            else:
                groups = []
                for groups_item_data in self.groups:
                    groups_item = groups_item_data.to_dict()

                    groups.append(groups_item)

        phone = self.phone
        tags: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = []
                for tags_item_data in self.tags:
                    tags_item = tags_item_data.to_dict()

                    tags.append(tags_item)

        attachments: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            if self.attachments is None:
                attachments = None
            else:
                attachments = []
                for attachments_item_data in self.attachments:
                    attachments_item = attachments_item_data.to_dict()

                    attachments.append(attachments_item)

        status: Union[Unset, None, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        rating = self.rating
        email = self.email
        company_name = self.company_name
        company_identifier = self.company_identifier
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
        if resumes is not UNSET:
            field_dict["resumes"] = resumes
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if tariff is not UNSET:
            field_dict["tariff"] = tariff
        if created_date_time is not UNSET:
            field_dict["createdDateTime"] = created_date_time
        if groups is not UNSET:
            field_dict["groups"] = groups
        if phone is not UNSET:
            field_dict["phone"] = phone
        if tags is not UNSET:
            field_dict["tags"] = tags
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if status is not UNSET:
            field_dict["status"] = status
        if rating is not UNSET:
            field_dict["rating"] = rating
        if email is not UNSET:
            field_dict["email"] = email
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_identifier is not UNSET:
            field_dict["companyIdentifier"] = company_identifier
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
        from ..models.company_subcontractor_group_base_model import CompanySubcontractorGroupBaseModel
        from ..models.company_tag_base_model import CompanyTagBaseModel
        from ..models.company_user_image_model import CompanyUserImageModel
        from ..models.company_user_resume_base_model import CompanyUserResumeBaseModel
        from ..models.company_user_subcontractor_attachment_model import CompanyUserSubcontractorAttachmentModel
        from ..models.currency_model import CurrencyModel
        from ..models.link import Link
        from ..models.location_model import LocationModel

        d = src_dict.copy()
        resumes = []
        _resumes = d.pop("resumes", UNSET)
        for resumes_item_data in _resumes or []:
            resumes_item = CompanyUserResumeBaseModel.from_dict(resumes_item_data)

            resumes.append(resumes_item)

        _default_currency = d.pop("defaultCurrency", UNSET)
        default_currency: Union[Unset, None, CurrencyModel]
        if _default_currency is None:
            default_currency = None
        elif isinstance(_default_currency, Unset):
            default_currency = UNSET
        else:
            default_currency = CurrencyModel.from_dict(_default_currency)

        tariff = d.pop("tariff", UNSET)

        _created_date_time = d.pop("createdDateTime", UNSET)
        created_date_time: Union[Unset, datetime.datetime]
        if isinstance(_created_date_time, Unset):
            created_date_time = UNSET
        else:
            created_date_time = isoparse(_created_date_time)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = CompanySubcontractorGroupBaseModel.from_dict(groups_item_data)

            groups.append(groups_item)

        phone = d.pop("phone", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = CompanyTagBaseModel.from_dict(tags_item_data)

            tags.append(tags_item)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = CompanyUserSubcontractorAttachmentModel.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, CompanyUserSubcontractorStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = CompanyUserSubcontractorStatus(_status)

        rating = d.pop("rating", UNSET)

        email = d.pop("email", UNSET)

        company_name = d.pop("companyName", UNSET)

        company_identifier = d.pop("companyIdentifier", UNSET)

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

        company_user_subcontractor_model = cls(
            resumes=resumes,
            default_currency=default_currency,
            tariff=tariff,
            created_date_time=created_date_time,
            groups=groups,
            phone=phone,
            tags=tags,
            attachments=attachments,
            status=status,
            rating=rating,
            email=email,
            company_name=company_name,
            company_identifier=company_identifier,
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

        return company_user_subcontractor_model
