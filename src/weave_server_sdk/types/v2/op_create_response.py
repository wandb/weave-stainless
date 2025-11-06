# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["OpCreateResponse"]


class OpCreateResponse(BaseModel):
    digest: str
    """The digest of the created op"""

    object_id: str
    """The ID of the created op"""

    version_index: int
    """The version index of the created op"""
