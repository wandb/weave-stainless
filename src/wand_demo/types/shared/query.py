# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Query"]


class Query(BaseModel):
    expr: "Expr" = FieldInfo(alias="$expr")


from .expr import Expr

if PYDANTIC_V2:
    Query.model_rebuild()
else:
    Query.update_forward_refs()  # type: ignore
