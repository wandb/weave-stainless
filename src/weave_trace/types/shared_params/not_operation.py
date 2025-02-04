# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NotOperation"]


class NotOperation(TypedDict, total=False):
    not_: Required[Annotated[Iterable["Operation"], PropertyInfo(alias="$not")]]


from .operation import Operation
