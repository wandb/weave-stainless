# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ObjectDeleteParams"]


class ObjectDeleteParams(TypedDict, total=False):
    object_id: Required[str]

    project_id: Required[str]

    digests: Optional[List[str]]
    """List of digests to delete.

    If not provided, all digests for the object will be deleted.
    """
