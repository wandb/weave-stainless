# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContainsSpec"]


class ContainsSpec(TypedDict, total=False):
    input: Required["Operation"]

    substr: Required["Operation"]

    case_insensitive: Optional[bool]


from .operation import Operation
