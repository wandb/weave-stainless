# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["ContainsSpec"]


class ContainsSpec(BaseModel):
    input: "Operation"

    substr: "Operation"

    case_insensitive: Optional[bool] = None


from .operation import Operation
