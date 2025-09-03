# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from ..._compat import PYDANTIC_V1
from .get_field_operator import GetFieldOperator

__all__ = ["Operation"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Operation = TypeAliasType(
        "Operation",
        Union[
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
        ],
    )
else:
    Operation: TypeAlias = Union[
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
