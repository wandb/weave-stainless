# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContainsOperation"]

if TYPE_CHECKING:
    from .contains_spec import ContainsSpec


class ContainsOperation(BaseModel):
    contains: "ContainsSpec" = FieldInfo(alias="$contains")

    model_config = {"defer_build": True}
