# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NotOperation"]


class NotOperation(BaseModel):
    not_: List["Operation"] = FieldInfo(alias="$not")


from .operation import Operation
