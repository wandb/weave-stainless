# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AndOperation"]


class AndOperation(TypedDict, total=False):
    and_: Required[Annotated[Iterable["Operation"], PropertyInfo(alias="$and")]]


from .operation import Operation
