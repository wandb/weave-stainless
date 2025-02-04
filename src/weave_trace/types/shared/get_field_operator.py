# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GetFieldOperator"]


class GetFieldOperator(BaseModel):
    get_field: str = FieldInfo(alias="$getField")
