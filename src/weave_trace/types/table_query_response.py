# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["TableQueryResponse", "Row"]


class Row(BaseModel):
    digest: str

    val: object


class TableQueryResponse(BaseModel):
    rows: List[Row]
