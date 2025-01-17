# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .get_field_operator import GetFieldOperator

__all__ = ["ContainsSpec", "Substr"]

Substr: TypeAlias = Union[
    "LiteralOperation",
    GetFieldOperator,
    "ConvertOperation",
    "AndOperation",
    "OrOperation",
    "NotOperation",
    "EqOperation",
    "GtOperation",
    "GteOperation",
    "InOperation",
    "ContainsOperation",
]


class ContainsSpec(TypedDict, total=False):
    input: Required["Operation"]

    substr: Required[Substr]

    case_insensitive: Optional[bool]


from .operation import Operation
from .eq_operation import EqOperation
from .gt_operation import GtOperation
from .in_operation import InOperation
from .or_operation import OrOperation
from .and_operation import AndOperation
from .gte_operation import GteOperation
from .not_operation import NotOperation
from .convert_operation import ConvertOperation
from .literal_operation import LiteralOperation
from .contains_operation import ContainsOperation
