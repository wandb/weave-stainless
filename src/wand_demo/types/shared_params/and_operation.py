# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .get_field_operator import GetFieldOperator

__all__ = ["AndOperation", "And"]

And: TypeAlias = Union[
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


class AndOperation(TypedDict, total=False):
    and_: Required[Annotated[Iterable[And], PropertyInfo(alias="$and")]]


from .eq_operation import EqOperation
from .gt_operation import GtOperation
from .in_operation import InOperation
from .or_operation import OrOperation
from .gte_operation import GteOperation
from .not_operation import NotOperation
from .convert_operation import ConvertOperation
from .literal_operation import LiteralOperation
from .contains_operation import ContainsOperation
