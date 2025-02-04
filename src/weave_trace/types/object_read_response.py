# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ObjectReadResponse", "Obj"]


class Obj(BaseModel):
    base_object_class: Optional[str] = None

    created_at: datetime

    digest: str

    is_latest: int

    kind: str

    object_id: str

    project_id: str

    val: object

    version_index: int

    deleted_at: Optional[datetime] = None


class ObjectReadResponse(BaseModel):
    obj: Obj
