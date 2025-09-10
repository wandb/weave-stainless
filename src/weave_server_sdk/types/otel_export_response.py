# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OtelExportResponse", "PartialSuccess"]


class PartialSuccess(BaseModel):
    error_message: str

    rejected_spans: int


class OtelExportResponse(BaseModel):
    partial_success: Optional[PartialSuccess] = None
    """The details of a partially successful export request.

    When None or rejected_spans is 0, the request was fully accepted.
    """
