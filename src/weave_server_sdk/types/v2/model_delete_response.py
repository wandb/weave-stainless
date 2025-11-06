# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ModelDeleteResponse"]


class ModelDeleteResponse(BaseModel):
    num_deleted: int
    """Number of model versions deleted"""
