# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PredictionFinishResponse"]


class PredictionFinishResponse(BaseModel):
    success: bool
    """Whether the prediction was finished successfully"""
