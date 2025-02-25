# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CostPurgeParams", "Query"]


class CostPurgeParams(TypedDict, total=False):
    project_id: Required[str]

    query: Required[Query]


class Query(TypedDict, total=False):
    expr: Required[Annotated["Expr", PropertyInfo(alias="$expr")]]


from .shared_params.expr import Expr
