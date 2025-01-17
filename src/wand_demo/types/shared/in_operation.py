# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["InOperation"]


class InOperation(BaseModel):
    in_: List["Operation"] = FieldInfo(alias="$in")


from .operation import Operation

if PYDANTIC_V2:
    InOperation.model_rebuild()
else:
    InOperation.update_forward_refs()  # type: ignore
