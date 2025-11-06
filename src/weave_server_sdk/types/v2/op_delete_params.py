# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OpDeleteParams"]


class OpDeleteParams(TypedDict, total=False):
    entity: Required[str]

    project: Required[str]

    body: Optional[SequenceNotStr[str]]
