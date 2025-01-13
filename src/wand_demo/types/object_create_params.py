# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ObjectCreateParams", "Obj"]


class ObjectCreateParams(TypedDict, total=False):
    obj: Required[Obj]


class Obj(TypedDict, total=False):
    object_id: Required[str]

    project_id: Required[str]

    val: Required[object]

    builtin_object_class: Optional[str]

    set_base_object_class: Optional[str]
