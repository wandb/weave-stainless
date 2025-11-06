# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["V2OpListResponse", "V2OpListResponseItem"]


class V2OpListResponseItem(BaseModel):
    code: str
    """The actual op source code"""

    created_at: datetime
    """When this op was created"""

    digest: str
    """The digest of the op"""

    object_id: str
    """The op ID"""

    version_index: int
    """The version index of this op"""


V2OpListResponse: TypeAlias = List[V2OpListResponseItem]
