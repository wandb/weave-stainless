# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContainsOperation"]


class ContainsOperation(BaseModel):
    contains: "ContainsSpec" = FieldInfo(alias="$contains")


from .contains_spec import ContainsSpec
