# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(BaseModel):
    created_at: datetime
    """When the object was created"""

    digest: str
    """The digest of the dataset object"""

    name: str
    """The name of the dataset"""

    object_id: str
    """The dataset ID"""

    rows: str
    """Reference to the dataset rows data"""

    version_index: int
    """The version index of the object"""

    description: Optional[str] = None
    """Description of the dataset"""


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
