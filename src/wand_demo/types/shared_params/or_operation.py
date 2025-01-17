# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OrOperation"]


class OrOperation(TypedDict, total=False):
    or_: Required[Annotated[Iterable["Operation"], PropertyInfo(alias="$or")]]


from .operation import Operation
