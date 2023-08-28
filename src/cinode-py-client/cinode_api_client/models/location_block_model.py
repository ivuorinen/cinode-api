from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationBlockModel")


@_attrs_define
class LocationBlockModel:
    """
    Attributes:
        location_id (Union[Unset, int]):
        google_id (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        street (Union[Unset, None, str]):
        street_number (Union[Unset, None, str]):
        zip_code (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        country (Union[Unset, None, str]):
        country_code (Union[Unset, None, str]):
        formatted_address (Union[Unset, None, str]):
        phone_number (Union[Unset, None, str]):
        latitude (Union[Unset, None, str]):
        longitude (Union[Unset, None, str]):
        web_site_url (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
    """

    location_id: Union[Unset, int] = UNSET
    google_id: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    street: Union[Unset, None, str] = UNSET
    street_number: Union[Unset, None, str] = UNSET
    zip_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    country: Union[Unset, None, str] = UNSET
    country_code: Union[Unset, None, str] = UNSET
    formatted_address: Union[Unset, None, str] = UNSET
    phone_number: Union[Unset, None, str] = UNSET
    latitude: Union[Unset, None, str] = UNSET
    longitude: Union[Unset, None, str] = UNSET
    web_site_url: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        location_id = self.location_id
        google_id = self.google_id
        name = self.name
        street = self.street
        street_number = self.street_number
        zip_code = self.zip_code
        city = self.city
        country = self.country
        country_code = self.country_code
        formatted_address = self.formatted_address
        phone_number = self.phone_number
        latitude = self.latitude
        longitude = self.longitude
        web_site_url = self.web_site_url
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if name is not UNSET:
            field_dict["name"] = name
        if street is not UNSET:
            field_dict["street"] = street
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if formatted_address is not UNSET:
            field_dict["formattedAddress"] = formatted_address
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if web_site_url is not UNSET:
            field_dict["webSiteUrl"] = web_site_url
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location_id = d.pop("locationId", UNSET)

        google_id = d.pop("googleId", UNSET)

        name = d.pop("name", UNSET)

        street = d.pop("street", UNSET)

        street_number = d.pop("streetNumber", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("countryCode", UNSET)

        formatted_address = d.pop("formattedAddress", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        web_site_url = d.pop("webSiteUrl", UNSET)

        display_name = d.pop("displayName", UNSET)

        location_block_model = cls(
            location_id=location_id,
            google_id=google_id,
            name=name,
            street=street,
            street_number=street_number,
            zip_code=zip_code,
            city=city,
            country=country,
            country_code=country_code,
            formatted_address=formatted_address,
            phone_number=phone_number,
            latitude=latitude,
            longitude=longitude,
            web_site_url=web_site_url,
            display_name=display_name,
        )

        return location_block_model
