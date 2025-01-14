# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .eq_operation import EqOperation
from .gt_operation import GtOperation
from .in_operation import InOperation
from .gte_operation import GteOperation
from .not_operation import NotOperation
from .get_field_operator import GetFieldOperator

__all__ = ["ContainsSpec", "Input", "Substr"]

Input: TypeAlias = Union[
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

Substr: TypeAlias = Union[
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


class ContainsSpec(TypedDict, total=False):
    input: Required[Input]

    substr: Required[Substr]

    case_insensitive: Optional[bool]


from .literal_operation import LiteralOperation
