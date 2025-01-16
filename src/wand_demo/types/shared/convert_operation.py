# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["ConvertOperation"]


class ConvertOperation(BaseModel):
    # convert: "ConvertSpec" = FieldInfo(alias="$convert")
    convert: object = FieldInfo(alias="$convert")


# from .convert_spec import ConvertSpec

if PYDANTIC_V2:
    ConvertOperation.model_rebuild()
else:
    ConvertOperation.update_forward_refs()  # type: ignore
