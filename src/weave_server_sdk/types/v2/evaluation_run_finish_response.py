# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EvaluationRunFinishResponse"]


class EvaluationRunFinishResponse(BaseModel):
    success: bool
    """Whether the evaluation run was finished successfully"""
