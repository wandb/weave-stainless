# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GtOperation"]


class GtOperation(TypedDict, total=False):
    gt: Required[Annotated[Iterable["Operation"], PropertyInfo(alias="$gt")]]


from .operation import Operation
