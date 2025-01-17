# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["GteOperation"]


class GteOperation(BaseModel):
    gte: List["Operation"] = FieldInfo(alias="$gte")


from .operation import Operation

if PYDANTIC_V2:
    GteOperation.model_rebuild()
else:
    GteOperation.update_forward_refs()  # type: ignore
