# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["CallStreamQueryResponse", "CallStreamQueryResponseItem"]


class CallStreamQueryResponseItem(BaseModel):
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

    storage_size_bytes: Optional[int] = None

    summary: Optional[Dict[str, object]] = None

    thread_id: Optional[str] = None

    total_storage_size_bytes: Optional[int] = None

    turn_id: Optional[str] = None

    wb_run_id: Optional[str] = None

    wb_run_step: Optional[int] = None

    wb_user_id: Optional[str] = None


CallStreamQueryResponse: TypeAlias = List[CallStreamQueryResponseItem]
