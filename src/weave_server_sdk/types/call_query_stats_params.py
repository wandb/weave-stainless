# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CallQueryStatsParams", "Filter"]


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

    query: Optional["Query"]


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


from .shared_params.query import Query
