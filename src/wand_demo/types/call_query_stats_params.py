# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallQueryStatsParams", "Filter", "Query", "QueryExpr"]


class CallQueryStatsParams(TypedDict, total=False):
    project_id: Required[str]

    filter: Optional[Filter]

    query: Optional[Query]


class Filter(TypedDict, total=False):
    call_ids: Optional[List[str]]

    input_refs: Optional[List[str]]

    op_names: Optional[List[str]]

    output_refs: Optional[List[str]]

    parent_ids: Optional[List[str]]

    trace_ids: Optional[List[str]]

    trace_roots_only: Optional[bool]

    wb_run_ids: Optional[List[str]]

    wb_user_ids: Optional[List[str]]


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


from .shared_params.eq_operation import EqOperation
from .shared_params.gt_operation import GtOperation
from .shared_params.in_operation import InOperation
from .shared_params.or_operation import OrOperation
from .shared_params.and_operation import AndOperation
from .shared_params.gte_operation import GteOperation
from .shared_params.not_operation import NotOperation
from .shared_params.contains_operation import ContainsOperation
