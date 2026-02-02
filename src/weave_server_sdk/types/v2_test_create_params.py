# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["V2TestCreateParams"]


class V2TestCreateParams(TypedDict, total=False):
    entity: Required[str]

    message: Optional[str]
