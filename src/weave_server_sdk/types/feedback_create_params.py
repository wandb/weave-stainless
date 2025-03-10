# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    feedback_type: Required[str]

    payload: Required[object]

    project_id: Required[str]

    weave_ref: Required[str]

    annotation_ref: Optional[str]

    call_ref: Optional[str]

    creator: Optional[str]

    runnable_ref: Optional[str]

    trigger_ref: Optional[str]

    wb_user_id: Optional[str]
    """Do not set directly. Server will automatically populate this field."""
