# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ObjectCreateResponse"]


class ObjectCreateResponse(BaseModel):
    digest: str

    object_id: str
