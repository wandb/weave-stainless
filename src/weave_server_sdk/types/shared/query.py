# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Query"]


class Query(BaseModel):
    expr: "Expr" = FieldInfo(alias="$expr")
    """Logical AND. All conditions must evaluate to true.

    Example:
    ` { "$and": [ {"$eq": [{"$getField": "op_name"}, {"$literal": "predict"}]}, {"$gt": [{"$getField": "summary.usage.tokens"}, {"$literal": 1000}]} ] } `
    """


from .expr import Expr
