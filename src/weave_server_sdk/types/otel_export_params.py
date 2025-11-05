# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["OtelExportParams"]


class OtelExportParams(TypedDict, total=False):
    project_id: Required[str]

    traces: Required[object]

    wb_run_id: Optional[str]

    wb_user_id: Optional[str]
    """Do not set directly. Server will automatically populate this field."""
