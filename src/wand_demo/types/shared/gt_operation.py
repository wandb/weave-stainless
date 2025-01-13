# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GtOperation"]


class GtOperation(BaseModel):
    gt: List[object] = FieldInfo(alias="$gt")
