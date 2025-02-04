# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallQueryStatsParams", "Filter", "Query"]


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


class Query(TypedDict, total=False):
    expr: Required[Annotated["Expr", PropertyInfo(alias="$expr")]]


from .shared_params.expr import Expr
