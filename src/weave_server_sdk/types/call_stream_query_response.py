# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["CallStreamQueryResponse", "CallStreamQueryResponseItem"]


class CallStreamQueryResponseItem(BaseModel):
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

    summary: Optional[object] = None

    wb_run_id: Optional[str] = None

    wb_user_id: Optional[str] = None


CallStreamQueryResponse: TypeAlias = List[CallStreamQueryResponseItem]
