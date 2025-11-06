# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EvaluationRunCreateResponse"]


class EvaluationRunCreateResponse(BaseModel):
    evaluation_run_id: str
    """The ID of the created evaluation run"""
