# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConvertOperation"]

if TYPE_CHECKING:
    from .convert_spec import ConvertSpec


class ConvertOperation(BaseModel):
    convert: "ConvertSpec" = FieldInfo(alias="$convert")

    model_config = {"defer_build": True}
