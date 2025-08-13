# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CostQueryParams", "SortBy"]


class CostQueryParams(TypedDict, total=False):
    project_id: Required[str]

    fields: Optional[List[str]]

    limit: Optional[int]

    offset: Optional[int]

    query: Optional["Query"]

    sort_by: Optional[Iterable[SortBy]]


class SortBy(TypedDict, total=False):
    direction: Required[Literal["asc", "desc"]]

    field: Required[str]


from .shared_params.query import Query
