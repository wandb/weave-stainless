# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["ConvertSpec"]


class ConvertSpec(BaseModel):
    input: "Operation"

    to: Literal["double", "string", "int", "bool", "exists"]


from .operation import Operation

if PYDANTIC_V2:
    ConvertSpec.model_rebuild()
else:
    ConvertSpec.update_forward_refs()  # type: ignore
