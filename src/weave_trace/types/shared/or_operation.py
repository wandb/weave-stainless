# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OrOperation"]


class OrOperation(BaseModel):
    or_: List["Operation"] = FieldInfo(alias="$or")


from .operation import Operation
