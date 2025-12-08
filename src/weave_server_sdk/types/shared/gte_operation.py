# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GteOperation"]


class GteOperation(BaseModel):
    """Greater than or equal comparison.

    Example:
        ```
        {"$gte": [{"$getField": "summary.usage.tokens"}, {"$literal": 100}]}
        ```
    """

    gte: List["Operation"] = FieldInfo(alias="$gte")


from .operation import Operation
