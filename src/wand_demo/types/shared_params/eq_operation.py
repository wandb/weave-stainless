# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EqOperation"]


class EqOperation(TypedDict, total=False):
    eq: Required[Annotated[Iterable[object], PropertyInfo(alias="$eq")]]
