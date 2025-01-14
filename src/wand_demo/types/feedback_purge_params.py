# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.eq_operation import EqOperation
from .shared_params.gt_operation import GtOperation
from .shared_params.in_operation import InOperation
from .shared_params.gte_operation import GteOperation
from .shared_params.not_operation import NotOperation

__all__ = ["FeedbackPurgeParams", "Query", "QueryExpr"]


class FeedbackPurgeParams(TypedDict, total=False):
    project_id: Required[str]

    query: Required[Query]


QueryExpr: TypeAlias = Union[
    "AndOperation",
    "OrOperation",
    NotOperation,
    EqOperation,
    GtOperation,
    GteOperation,
    InOperation,
    "ContainsOperation",
]


class Query(TypedDict, total=False):
    expr: Required[Annotated[QueryExpr, PropertyInfo(alias="$expr")]]


from .shared_params.or_operation import OrOperation
from .shared_params.and_operation import AndOperation
from .shared_params.contains_operation import ContainsOperation
