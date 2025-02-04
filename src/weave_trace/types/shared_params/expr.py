# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

__all__ = ["Expr"]

Expr: TypeAlias = Union[
    "AndOperation",
    "OrOperation",
    "NotOperation",
    "EqOperation",
    "GtOperation",
    "GteOperation",
    "InOperation",
    "ContainsOperation",
]

from .eq_operation import EqOperation
from .gt_operation import GtOperation
from .in_operation import InOperation
from .or_operation import OrOperation
from .and_operation import AndOperation
from .gte_operation import GteOperation
from .not_operation import NotOperation
from .contains_operation import ContainsOperation
