# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    entity: Required[str]

    limit: Optional[int]

    offset: Optional[int]
