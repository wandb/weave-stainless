# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GtOperation"]

if TYPE_CHECKING:
    from .operation import Operation


class GtOperation(BaseModel):
    gt: List["Operation"] = FieldInfo(alias="$gt")

    model_config = {"defer_build": True}
