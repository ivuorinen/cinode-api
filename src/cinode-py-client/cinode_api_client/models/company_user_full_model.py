import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.company_user_status import CompanyUserStatus
from ..models.company_user_type import CompanyUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.absence_period_model import AbsencePeriodModel
    from ..models.company_address_model import CompanyAddressModel
    from ..models.company_customer_manager_model import CompanyCustomerManagerModel
    from ..models.company_tag_model import CompanyTagModel
    from ..models.company_user_image_model import CompanyUserImageModel
    from ..models.company_user_resume_base_model import CompanyUserResumeBaseModel
    from ..models.currency_model import CurrencyModel
    from ..models.link import Link
    from ..models.location_model import LocationModel
    from ..models.role_model import RoleModel
    from ..models.team_manager_model import TeamManagerModel
    from ..models.team_member_model import TeamMemberModel


T = TypeVar("T", bound="CompanyUserFullModel")


@_attrs_define
class CompanyUserFullModel:
    """
    Attributes:
        invoicing_goal (Union[Unset, None, int]):
        tax_table (Union[Unset, None, str]):
        base_salary (Union[Unset, None, int]):
        provision (Union[Unset, None, int]):
        hourly_target_rate (Union[Unset, None, int]):
        self_cost (Union[Unset, None, int]):
        employment_start_date (Union[Unset, None, datetime.datetime]):
        employment_end_date (Union[Unset, None, datetime.datetime]):
        employment_number (Union[Unset, None, str]):
        availability_percent (Union[Unset, None, int]):
        available_from_date (Union[Unset, None, datetime.datetime]):
        mobility (Union[Unset, None, int]):
        location_name (Union[Unset, None, str]):
        resumes (Union[Unset, None, List['CompanyUserResumeBaseModel']]):
        roles (Union[Unset, None, List['RoleModel']]):
        team_managers (Union[Unset, None, List['TeamManagerModel']]):
        team_members (Union[Unset, None, List['TeamMemberModel']]):
        customer_managers (Union[Unset, None, List['CompanyCustomerManagerModel']]):
        periods (Union[Unset, None, List['AbsencePeriodModel']]):
        default_currency (Union[Unset, None, CurrencyModel]):
        phone (Union[Unset, None, str]):
        date_of_birth (Union[Unset, None, datetime.datetime]):
        tags (Union[Unset, None, List['CompanyTagModel']]):
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

    invoicing_goal: Union[Unset, None, int] = UNSET
    tax_table: Union[Unset, None, str] = UNSET
    base_salary: Union[Unset, None, int] = UNSET
    provision: Union[Unset, None, int] = UNSET
    hourly_target_rate: Union[Unset, None, int] = UNSET
    self_cost: Union[Unset, None, int] = UNSET
    employment_start_date: Union[Unset, None, datetime.datetime] = UNSET
    employment_end_date: Union[Unset, None, datetime.datetime] = UNSET
    employment_number: Union[Unset, None, str] = UNSET
    availability_percent: Union[Unset, None, int] = UNSET
    available_from_date: Union[Unset, None, datetime.datetime] = UNSET
    mobility: Union[Unset, None, int] = UNSET
    location_name: Union[Unset, None, str] = UNSET
    resumes: Union[Unset, None, List["CompanyUserResumeBaseModel"]] = UNSET
    roles: Union[Unset, None, List["RoleModel"]] = UNSET
    team_managers: Union[Unset, None, List["TeamManagerModel"]] = UNSET
    team_members: Union[Unset, None, List["TeamMemberModel"]] = UNSET
    customer_managers: Union[Unset, None, List["CompanyCustomerManagerModel"]] = UNSET
    periods: Union[Unset, None, List["AbsencePeriodModel"]] = UNSET
    default_currency: Union[Unset, None, "CurrencyModel"] = UNSET
    phone: Union[Unset, None, str] = UNSET
    date_of_birth: Union[Unset, None, datetime.datetime] = UNSET
    tags: Union[Unset, None, List["CompanyTagModel"]] = UNSET
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
        invoicing_goal = self.invoicing_goal
        tax_table = self.tax_table
        base_salary = self.base_salary
        provision = self.provision
        hourly_target_rate = self.hourly_target_rate
        self_cost = self.self_cost
        employment_start_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.employment_start_date, Unset):
            employment_start_date = self.employment_start_date.isoformat() if self.employment_start_date else None

        employment_end_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.employment_end_date, Unset):
            employment_end_date = self.employment_end_date.isoformat() if self.employment_end_date else None

        employment_number = self.employment_number
        availability_percent = self.availability_percent
        available_from_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.available_from_date, Unset):
            available_from_date = self.available_from_date.isoformat() if self.available_from_date else None

        mobility = self.mobility
        location_name = self.location_name
        resumes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.resumes, Unset):
            if self.resumes is None:
                resumes = None
            else:
                resumes = []
                for resumes_item_data in self.resumes:
                    resumes_item = resumes_item_data.to_dict()

                    resumes.append(resumes_item)

        roles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            if self.roles is None:
                roles = None
            else:
                roles = []
                for roles_item_data in self.roles:
                    roles_item = roles_item_data.to_dict()

                    roles.append(roles_item)

        team_managers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.team_managers, Unset):
            if self.team_managers is None:
                team_managers = None
            else:
                team_managers = []
                for team_managers_item_data in self.team_managers:
                    team_managers_item = team_managers_item_data.to_dict()

                    team_managers.append(team_managers_item)

        team_members: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.team_members, Unset):
            if self.team_members is None:
                team_members = None
            else:
                team_members = []
                for team_members_item_data in self.team_members:
                    team_members_item = team_members_item_data.to_dict()

                    team_members.append(team_members_item)

        customer_managers: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.customer_managers, Unset):
            if self.customer_managers is None:
                customer_managers = None
            else:
                customer_managers = []
                for customer_managers_item_data in self.customer_managers:
                    customer_managers_item = customer_managers_item_data.to_dict()

                    customer_managers.append(customer_managers_item)

        periods: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            if self.periods is None:
                periods = None
            else:
                periods = []
                for periods_item_data in self.periods:
                    periods_item = periods_item_data.to_dict()

                    periods.append(periods_item)

        default_currency: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.default_currency, Unset):
            default_currency = self.default_currency.to_dict() if self.default_currency else None

        phone = self.phone
        date_of_birth: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat() if self.date_of_birth else None

        tags: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            if self.tags is None:
                tags = None
            else:
                tags = []
                for tags_item_data in self.tags:
                    tags_item = tags_item_data.to_dict()

                    tags.append(tags_item)

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
        if invoicing_goal is not UNSET:
            field_dict["invoicingGoal"] = invoicing_goal
        if tax_table is not UNSET:
            field_dict["taxTable"] = tax_table
        if base_salary is not UNSET:
            field_dict["baseSalary"] = base_salary
        if provision is not UNSET:
            field_dict["provision"] = provision
        if hourly_target_rate is not UNSET:
            field_dict["hourlyTargetRate"] = hourly_target_rate
        if self_cost is not UNSET:
            field_dict["selfCost"] = self_cost
        if employment_start_date is not UNSET:
            field_dict["employmentStartDate"] = employment_start_date
        if employment_end_date is not UNSET:
            field_dict["employmentEndDate"] = employment_end_date
        if employment_number is not UNSET:
            field_dict["employmentNumber"] = employment_number
        if availability_percent is not UNSET:
            field_dict["availabilityPercent"] = availability_percent
        if available_from_date is not UNSET:
            field_dict["availableFromDate"] = available_from_date
        if mobility is not UNSET:
            field_dict["mobility"] = mobility
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if resumes is not UNSET:
            field_dict["resumes"] = resumes
        if roles is not UNSET:
            field_dict["roles"] = roles
        if team_managers is not UNSET:
            field_dict["teamManagers"] = team_managers
        if team_members is not UNSET:
            field_dict["teamMembers"] = team_members
        if customer_managers is not UNSET:
            field_dict["customerManagers"] = customer_managers
        if periods is not UNSET:
            field_dict["periods"] = periods
        if default_currency is not UNSET:
            field_dict["defaultCurrency"] = default_currency
        if phone is not UNSET:
            field_dict["phone"] = phone
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if tags is not UNSET:
            field_dict["tags"] = tags
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
        from ..models.absence_period_model import AbsencePeriodModel
        from ..models.company_address_model import CompanyAddressModel
        from ..models.company_customer_manager_model import CompanyCustomerManagerModel
        from ..models.company_tag_model import CompanyTagModel
        from ..models.company_user_image_model import CompanyUserImageModel
        from ..models.company_user_resume_base_model import CompanyUserResumeBaseModel
        from ..models.currency_model import CurrencyModel
        from ..models.link import Link
        from ..models.location_model import LocationModel
        from ..models.role_model import RoleModel
        from ..models.team_manager_model import TeamManagerModel
        from ..models.team_member_model import TeamMemberModel

        d = src_dict.copy()
        invoicing_goal = d.pop("invoicingGoal", UNSET)

        tax_table = d.pop("taxTable", UNSET)

        base_salary = d.pop("baseSalary", UNSET)

        provision = d.pop("provision", UNSET)

        hourly_target_rate = d.pop("hourlyTargetRate", UNSET)

        self_cost = d.pop("selfCost", UNSET)

        _employment_start_date = d.pop("employmentStartDate", UNSET)
        employment_start_date: Union[Unset, None, datetime.datetime]
        if _employment_start_date is None:
            employment_start_date = None
        elif isinstance(_employment_start_date, Unset):
            employment_start_date = UNSET
        else:
            employment_start_date = isoparse(_employment_start_date)

        _employment_end_date = d.pop("employmentEndDate", UNSET)
        employment_end_date: Union[Unset, None, datetime.datetime]
        if _employment_end_date is None:
            employment_end_date = None
        elif isinstance(_employment_end_date, Unset):
            employment_end_date = UNSET
        else:
            employment_end_date = isoparse(_employment_end_date)

        employment_number = d.pop("employmentNumber", UNSET)

        availability_percent = d.pop("availabilityPercent", UNSET)

        _available_from_date = d.pop("availableFromDate", UNSET)
        available_from_date: Union[Unset, None, datetime.datetime]
        if _available_from_date is None:
            available_from_date = None
        elif isinstance(_available_from_date, Unset):
            available_from_date = UNSET
        else:
            available_from_date = isoparse(_available_from_date)

        mobility = d.pop("mobility", UNSET)

        location_name = d.pop("locationName", UNSET)

        resumes = []
        _resumes = d.pop("resumes", UNSET)
        for resumes_item_data in _resumes or []:
            resumes_item = CompanyUserResumeBaseModel.from_dict(resumes_item_data)

            resumes.append(resumes_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = RoleModel.from_dict(roles_item_data)

            roles.append(roles_item)

        team_managers = []
        _team_managers = d.pop("teamManagers", UNSET)
        for team_managers_item_data in _team_managers or []:
            team_managers_item = TeamManagerModel.from_dict(team_managers_item_data)

            team_managers.append(team_managers_item)

        team_members = []
        _team_members = d.pop("teamMembers", UNSET)
        for team_members_item_data in _team_members or []:
            team_members_item = TeamMemberModel.from_dict(team_members_item_data)

            team_members.append(team_members_item)

        customer_managers = []
        _customer_managers = d.pop("customerManagers", UNSET)
        for customer_managers_item_data in _customer_managers or []:
            customer_managers_item = CompanyCustomerManagerModel.from_dict(customer_managers_item_data)

            customer_managers.append(customer_managers_item)

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = AbsencePeriodModel.from_dict(periods_item_data)

            periods.append(periods_item)

        _default_currency = d.pop("defaultCurrency", UNSET)
        default_currency: Union[Unset, None, CurrencyModel]
        if _default_currency is None:
            default_currency = None
        elif isinstance(_default_currency, Unset):
            default_currency = UNSET
        else:
            default_currency = CurrencyModel.from_dict(_default_currency)

        phone = d.pop("phone", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, None, datetime.datetime]
        if _date_of_birth is None:
            date_of_birth = None
        elif isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = CompanyTagModel.from_dict(tags_item_data)

            tags.append(tags_item)

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

        company_user_full_model = cls(
            invoicing_goal=invoicing_goal,
            tax_table=tax_table,
            base_salary=base_salary,
            provision=provision,
            hourly_target_rate=hourly_target_rate,
            self_cost=self_cost,
            employment_start_date=employment_start_date,
            employment_end_date=employment_end_date,
            employment_number=employment_number,
            availability_percent=availability_percent,
            available_from_date=available_from_date,
            mobility=mobility,
            location_name=location_name,
            resumes=resumes,
            roles=roles,
            team_managers=team_managers,
            team_members=team_members,
            customer_managers=customer_managers,
            periods=periods,
            default_currency=default_currency,
            phone=phone,
            date_of_birth=date_of_birth,
            tags=tags,
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

        return company_user_full_model
