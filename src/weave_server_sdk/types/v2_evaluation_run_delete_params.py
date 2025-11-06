# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["V2EvaluationRunDeleteParams"]


class V2EvaluationRunDeleteParams(TypedDict, total=False):
    entity: Required[str]

    body: Required[SequenceNotStr[str]]
