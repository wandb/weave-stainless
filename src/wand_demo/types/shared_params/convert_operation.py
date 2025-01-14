# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConvertOperation"]


class ConvertOperation(TypedDict, total=False):
    convert: Required[Annotated[ConvertSpec, PropertyInfo(alias="$convert")]]


from .convert_spec import ConvertSpec
