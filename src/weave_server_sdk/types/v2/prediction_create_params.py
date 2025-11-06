# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PredictionCreateParams"]


class PredictionCreateParams(TypedDict, total=False):
    entity: Required[str]

    inputs: Required[Dict[str, object]]
    """The inputs to the prediction"""

    model: Required[str]
    """The model reference (weave:// URI)"""

    output: Required[object]
    """The output of the prediction"""

    evaluation_run_id: Optional[str]
    """Optional evaluation run ID to link this prediction as a child call"""
