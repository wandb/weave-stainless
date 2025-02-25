# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RefReadBatchParams"]


class RefReadBatchParams(TypedDict, total=False):
    refs: Required[List[str]]
