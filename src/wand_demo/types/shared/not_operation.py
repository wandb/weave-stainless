# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["NotOperation"]


class NotOperation(BaseModel):
    not_: List["Operation"] = FieldInfo(alias="$not")


from .operation import Operation

if PYDANTIC_V2:
    NotOperation.model_rebuild()
else:
    NotOperation.update_forward_refs()  # type: ignore
