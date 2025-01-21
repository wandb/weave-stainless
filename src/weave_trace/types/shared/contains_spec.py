# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

__all__ = ["ContainsSpec"]

if TYPE_CHECKING:
    from .operation import Operation


class ContainsSpec(BaseModel):
    input: "Operation"

    substr: "Operation"

    case_insensitive: Optional[bool] = None

    model_config = {"defer_build": True}
