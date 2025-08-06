# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CallReadResponse", "Call"]


class Call(BaseModel):
    id: str

    attributes: object

    inputs: object

    op_name: str

    project_id: str

    started_at: datetime

    trace_id: str

    deleted_at: Optional[datetime] = None

    display_name: Optional[str] = None

    ended_at: Optional[datetime] = None

    exception: Optional[str] = None

    output: Optional[object] = None

    parent_id: Optional[str] = None

    storage_size_bytes: Optional[int] = None

    summary: Optional[object] = None

    thread_id: Optional[str] = None

    total_storage_size_bytes: Optional[int] = None

    turn_id: Optional[str] = None

    wb_run_id: Optional[str] = None

    wb_run_step: Optional[int] = None

    wb_user_id: Optional[str] = None


class CallReadResponse(BaseModel):
    call: Optional[Call] = None
