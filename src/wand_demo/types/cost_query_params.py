# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["CostQueryParams", "Query", "QueryExpr", "SortBy"]


class CostQueryParams(TypedDict, total=False):
    project_id: Required[str]

    fields: Optional[List[str]]

    limit: Optional[int]

    offset: Optional[int]

    query: Optional[Query]

    sort_by: Optional[Iterable[SortBy]]


QueryExpr: TypeAlias = Union[
    "AndOperation",
    "OrOperation",
    "NotOperation",
    "EqOperation",
    "GtOperation",
    "GteOperation",
    "InOperation",
    "ContainsOperation",
]


class Query(TypedDict, total=False):
    expr: Required[Annotated[QueryExpr, PropertyInfo(alias="$expr")]]


class SortBy(TypedDict, total=False):
    direction: Required[Literal["asc", "desc"]]

    field: Required[str]


from .shared_params.eq_operation import EqOperation
from .shared_params.gt_operation import GtOperation
from .shared_params.in_operation import InOperation
from .shared_params.or_operation import OrOperation
from .shared_params.and_operation import AndOperation
from .shared_params.gte_operation import GteOperation
from .shared_params.not_operation import NotOperation
from .shared_params.contains_operation import ContainsOperation
