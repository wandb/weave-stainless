# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContainsOperation"]


class ContainsOperation(BaseModel):
    contains: "ContainsSpec" = FieldInfo(alias="$contains")
    """Specification for the `$contains` operation.

    - `input`: The string to search.
    - `substr`: The substring to search for.
    - `case_insensitive`: If true, match is case-insensitive.
    """


from .contains_spec import ContainsSpec
