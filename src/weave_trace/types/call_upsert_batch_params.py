# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "CallUpsertBatchParams",
    "Batch",
    "BatchCallBatchStartMode",
    "BatchCallBatchStartModeReq",
    "BatchCallBatchStartModeReqStart",
    "BatchCallBatchEndMode",
    "BatchCallBatchEndModeReq",
    "BatchCallBatchEndModeReqEnd",
    "BatchCallBatchEndModeReqEndSummary",
    "BatchCallBatchEndModeReqEndSummaryUsage",
]


class CallUpsertBatchParams(TypedDict, total=False):
    batch: Required[Iterable[Batch]]


class BatchCallBatchStartModeReqStart(TypedDict, total=False):
    attributes: Required[object]

    inputs: Required[object]

    op_name: Required[str]

    project_id: Required[str]

    started_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    id: Optional[str]

    display_name: Optional[str]

    parent_id: Optional[str]

    trace_id: Optional[str]

    wb_run_id: Optional[str]

    wb_user_id: Optional[str]
    """Do not set directly. Server will automatically populate this field."""


class BatchCallBatchStartModeReq(TypedDict, total=False):
    start: Required[BatchCallBatchStartModeReqStart]


class BatchCallBatchStartMode(TypedDict, total=False):
    req: Required[BatchCallBatchStartModeReq]

    mode: str


class BatchCallBatchEndModeReqEndSummaryUsage(TypedDict, total=False):
    completion_tokens: Optional[int]

    input_tokens: Optional[int]

    output_tokens: Optional[int]

    prompt_tokens: Optional[int]

    requests: Optional[int]

    total_tokens: Optional[int]


class BatchCallBatchEndModeReqEndSummaryTyped(TypedDict, total=False):
    usage: Dict[str, BatchCallBatchEndModeReqEndSummaryUsage]


BatchCallBatchEndModeReqEndSummary: TypeAlias = Union[BatchCallBatchEndModeReqEndSummaryTyped, Dict[str, object]]


class BatchCallBatchEndModeReqEnd(TypedDict, total=False):
    id: Required[str]

    ended_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    project_id: Required[str]

    summary: Required[BatchCallBatchEndModeReqEndSummary]

    exception: Optional[str]

    output: object


class BatchCallBatchEndModeReq(TypedDict, total=False):
    end: Required[BatchCallBatchEndModeReqEnd]


class BatchCallBatchEndMode(TypedDict, total=False):
    req: Required[BatchCallBatchEndModeReq]

    mode: str


Batch: TypeAlias = Union[BatchCallBatchStartMode, BatchCallBatchEndMode]
