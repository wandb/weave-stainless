# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConvertSpec"]

if TYPE_CHECKING:
    from .operation import Operation


class ConvertSpec(BaseModel):
    input: "Operation"

    to: Literal["double", "string", "int", "bool", "exists"]

    model_config = {"defer_build": True}
