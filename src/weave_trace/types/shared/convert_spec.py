# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConvertSpec"]


class ConvertSpec(BaseModel):
    input: "Operation"

    to: Literal["double", "string", "int", "bool", "exists"]


from .operation import Operation
