# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from .eq_operation import EqOperation
from .gt_operation import GtOperation
from .in_operation import InOperation
from .gte_operation import GteOperation
from .not_operation import NotOperation
from .get_field_operator import GetFieldOperator

__all__ = ["AndOperation", "And", "AndConvertOperation", "AndConvertOperationConvert"]


class AndConvertOperationConvert(BaseModel):
    input: object

    to: Literal["double", "string", "int", "bool", "exists"]


class AndConvertOperation(BaseModel):
    convert: AndConvertOperationConvert = FieldInfo(alias="$convert")


And: TypeAlias = Union[
    "LiteralOperation",
    GetFieldOperator,
    AndConvertOperation,
    AndOperation,
    OrOperation,
    NotOperation,
    EqOperation,
    GtOperation,
    GteOperation,
    InOperation,
    object,
]


class AndOperation(BaseModel):
    and_: List[And] = FieldInfo(alias="$and")


from .literal_operation import LiteralOperation

if PYDANTIC_V2:
    AndOperation.model_rebuild()
    AndConvertOperation.model_rebuild()
    AndConvertOperationConvert.model_rebuild()
else:
    AndOperation.update_forward_refs()  # type: ignore
    AndConvertOperation.update_forward_refs()  # type: ignore
    AndConvertOperationConvert.update_forward_refs()  # type: ignore
