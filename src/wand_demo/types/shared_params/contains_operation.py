# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContainsOperation"]


class ContainsOperation(TypedDict, total=False):
    contains: Required[Annotated[ContainsSpec, PropertyInfo(alias="$contains")]]


from .contains_spec import ContainsSpec
