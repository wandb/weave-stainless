# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CallDeleteParams"]


class CallDeleteParams(TypedDict, total=False):
    call_ids: Required[List[str]]

    project_id: Required[str]

    wb_user_id: Optional[str]
    """Do not set directly. Server will automatically populate this field."""
