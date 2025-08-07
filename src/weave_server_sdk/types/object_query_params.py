# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ObjectQueryParams", "Filter", "SortBy"]


class ObjectQueryParams(TypedDict, total=False):
    project_id: Required[str]
    """The ID of the project to query"""

    filter: Optional[Filter]
    """Filter criteria for the query. See `ObjectVersionFilter`"""

    include_storage_size: Optional[bool]
    """If true, the `size_bytes` column is returned."""

    limit: Optional[int]
    """Maximum number of results to return"""

    metadata_only: Optional[bool]
    """
    If true, the `val` column is not read from the database and is empty.All other
    fields are returned.
    """

    offset: Optional[int]
    """Number of results to skip before returning"""

    sort_by: Optional[Iterable[SortBy]]
    """Sorting criteria for the query results.

    Currently only supports 'object_id' and 'created_at'.
    """


class Filter(TypedDict, total=False):
    base_object_classes: Optional[List[str]]
    """Filter objects by their base classes"""

    is_op: Optional[bool]
    """Filter objects based on whether they are weave.ops or not.

    `True` will only return ops, `False` will return non-ops, and `None` will return
    all objects
    """

    latest_only: Optional[bool]
    """If True, return only the latest version of each object.

    `False` and `None` will return all versions
    """

    leaf_object_classes: Optional[List[str]]
    """Filter objects by their leaf classes"""

    object_ids: Optional[List[str]]
    """Filter objects by their IDs"""


class SortBy(TypedDict, total=False):
    direction: Required[Literal["asc", "desc"]]

    field: Required[str]
