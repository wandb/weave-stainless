# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CallReadParams"]


class CallReadParams(TypedDict, total=False):
    id: Required[str]

    project_id: Required[str]

    include_costs: Optional[bool]
