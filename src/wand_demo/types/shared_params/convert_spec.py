# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .eq_operation import EqOperation
from .gt_operation import GtOperation
from .in_operation import InOperation
from .gte_operation import GteOperation
from .not_operation import NotOperation
from .get_field_operator import GetFieldOperator

__all__ = ["ConvertSpec", "Input"]

Input: TypeAlias = Union[
    "LiteralOperation",
    GetFieldOperator,
    "ConvertOperation",
    "AndOperation",
    "OrOperation",
    NotOperation,
    EqOperation,
    GtOperation,
    GteOperation,
    InOperation,
    "ContainsOperation",
]


class ConvertSpec(TypedDict, total=False):
    input: Required[Input]

    to: Required[Literal["double", "string", "int", "bool", "exists"]]


from .or_operation import OrOperation
from .and_operation import AndOperation
from .convert_operation import ConvertOperation
from .literal_operation import LiteralOperation
from .contains_operation import ContainsOperation
