# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from .eq_operation import EqOperation
from .gt_operation import GtOperation
from .in_operation import InOperation
from .gte_operation import GteOperation
from .not_operation import NotOperation
from .get_field_operator import GetFieldOperator

__all__ = ["OrOperation", "Or"]

Or: TypeAlias = Union[
    "LiteralOperation",
    GetFieldOperator,
    ConvertOperation,
    AndOperation,
    OrOperation,
    NotOperation,
    EqOperation,
    GtOperation,
    GteOperation,
    InOperation,
    ContainsOperation,
]


class OrOperation(BaseModel):
    or_: List[Or] = FieldInfo(alias="$or")


from .literal_operation import LiteralOperation

if PYDANTIC_V2:
    OrOperation.model_rebuild()
else:
    OrOperation.update_forward_refs()  # type: ignore
