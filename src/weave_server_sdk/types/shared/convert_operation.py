# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConvertOperation"]


class ConvertOperation(BaseModel):
    convert: "ConvertSpec" = FieldInfo(alias="$convert")
    """Specifies conversion details for `$convert`.

    - `input`: The operand to convert.
    - `to`: The type to convert to.
    """


from .convert_spec import ConvertSpec
