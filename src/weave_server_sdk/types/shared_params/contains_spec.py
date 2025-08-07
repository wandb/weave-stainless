# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ContainsSpec"]


class ContainsSpec(TypedDict, total=False):
    input: Required["Operation"]
    """Represents a constant value in the query language.

    This can be any standard JSON-serializable value.

    Example: ` {"$literal": "predict"} `
    """

    substr: Required["Operation"]
    """Represents a constant value in the query language.

    This can be any standard JSON-serializable value.

    Example: ` {"$literal": "predict"} `
    """

    case_insensitive: Optional[bool]


from .operation import Operation
