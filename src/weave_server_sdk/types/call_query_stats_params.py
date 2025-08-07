# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallQueryStatsParams", "Filter", "Query"]


class CallQueryStatsParams(TypedDict, total=False):
    project_id: Required[str]

    expand_columns: Optional[List[str]]
    """
    Columns with refs to objects or table rows that require expansion during
    filtering or ordering.
    """

    filter: Optional[Filter]

    include_total_storage_size: Optional[bool]

    limit: Optional[int]

    query: Optional[Query]


class Filter(TypedDict, total=False):
    call_ids: Optional[List[str]]

    input_refs: Optional[List[str]]

    op_names: Optional[List[str]]

    output_refs: Optional[List[str]]

    parent_ids: Optional[List[str]]

    thread_ids: Optional[List[str]]

    trace_ids: Optional[List[str]]

    trace_roots_only: Optional[bool]

    turn_ids: Optional[List[str]]

    wb_run_ids: Optional[List[str]]

    wb_user_ids: Optional[List[str]]


class Query(TypedDict, total=False):
    expr: Required[Annotated["Expr", PropertyInfo(alias="$expr")]]
    """Logical AND. All conditions must evaluate to true.

    Example:
    ` { "$and": [ {"$eq": [{"$getField": "op_name"}, {"$literal": "predict"}]}, {"$gt": [{"$getField": "summary.usage.tokens"}, {"$literal": 1000}]} ] } `
    """


from .shared_params.expr import Expr
