# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CallReadResponse", "Call"]


class Call(BaseModel):
    id: str

    attributes: Dict[str, object]

    inputs: Dict[str, object]

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

    summary: Optional[object] = None

    wb_run_id: Optional[str] = None

    wb_user_id: Optional[str] = None


class CallReadResponse(BaseModel):
    call: Optional[Call] = None
