# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["EvaluationRunListResponse", "EvaluationRunListResponseItem"]


class EvaluationRunListResponseItem(BaseModel):
    evaluation: str
    """Reference to the evaluation (weave:// URI)"""

    evaluation_run_id: str
    """The evaluation run ID"""

    model: str
    """Reference to the model (weave:// URI)"""

    finished_at: Optional[datetime] = None
    """When the evaluation run finished"""

    started_at: Optional[datetime] = None
    """When the evaluation run started"""

    status: Optional[str] = None
    """Status of the evaluation run"""

    summary: Optional[Dict[str, object]] = None
    """Summary data for the evaluation run"""


EvaluationRunListResponse: TypeAlias = List[EvaluationRunListResponseItem]
