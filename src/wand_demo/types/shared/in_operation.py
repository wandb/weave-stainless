# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InOperation"]


class InOperation(BaseModel):
    in_: List[object] = FieldInfo(alias="$in")
