from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="ProjectReferenceModel")


@_attrs_define
class ProjectReferenceModel:
    """
    Attributes:
        id (Union[Unset, int]):
        company_id (Union[Unset, int]):
        project_id (Union[Unset, int]):
        title (Union[Unset, None, str]):
        text (Union[Unset, None, str]):
        language (Union[Unset, None, str]):
        links (Union[Unset, None, List['Link']]):
    """

    id: Union[Unset, int] = UNSET
    company_id: Union[Unset, int] = UNSET
    project_id: Union[Unset, int] = UNSET
    title: Union[Unset, None, str] = UNSET
    text: Union[Unset, None, str] = UNSET
    language: Union[Unset, None, str] = UNSET
    links: Union[Unset, None, List["Link"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        company_id = self.company_id
        project_id = self.project_id
        title = self.title
        text = self.text
        language = self.language
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
        if id is not UNSET:
            field_dict["id"] = id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if title is not UNSET:
            field_dict["title"] = title
        if text is not UNSET:
            field_dict["text"] = text
        if language is not UNSET:
            field_dict["language"] = language
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link import Link

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        company_id = d.pop("companyId", UNSET)

        project_id = d.pop("projectId", UNSET)

        title = d.pop("title", UNSET)

        text = d.pop("text", UNSET)

        language = d.pop("language", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        project_reference_model = cls(
            id=id,
            company_id=company_id,
            project_id=project_id,
            title=title,
            text=text,
            language=language,
            links=links,
        )

        return project_reference_model
