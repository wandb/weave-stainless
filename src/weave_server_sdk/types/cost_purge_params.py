# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CostPurgeParams"]


class CostPurgeParams(TypedDict, total=False):
    project_id: Required[str]

    query: Required["Query"]


from .shared_params.query import Query
