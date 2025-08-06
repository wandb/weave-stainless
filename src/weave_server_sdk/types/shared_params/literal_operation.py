# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LiteralOperation"]


class LiteralOperation(TypedDict, total=False):
    literal: Required[
        Annotated[
            Union[str, float, bool, Dict[str, "LiteralOperation"], Iterable["LiteralOperation"], None],
            PropertyInfo(alias="$literal"),
        ]
    ]
