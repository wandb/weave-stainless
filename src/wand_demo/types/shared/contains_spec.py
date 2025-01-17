# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["ContainsSpec"]


class ContainsSpec(BaseModel):
    input: "Operation"

    substr: "Operation"

    case_insensitive: Optional[bool] = None


from .operation import Operation

if PYDANTIC_V2:
    ContainsSpec.model_rebuild()
else:
    ContainsSpec.update_forward_refs()  # type: ignore
