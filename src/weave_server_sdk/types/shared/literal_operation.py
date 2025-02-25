# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LiteralOperation"]


class LiteralOperation(BaseModel):
    literal: Union[str, float, bool, Dict[str, "LiteralOperation"], List["LiteralOperation"], None] = FieldInfo(
        alias="$literal", default=None
    )
