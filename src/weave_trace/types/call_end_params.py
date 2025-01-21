# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallEndParams", "End", "EndSummary", "EndSummaryUsage"]


class CallEndParams(TypedDict, total=False):
    end: Required[End]


class EndSummaryUsage(TypedDict, total=False):
    completion_tokens: Optional[int]

    input_tokens: Optional[int]

    output_tokens: Optional[int]

    prompt_tokens: Optional[int]

    requests: Optional[int]

    total_tokens: Optional[int]


class EndSummaryTyped(TypedDict, total=False):
    usage: Dict[str, EndSummaryUsage]


EndSummary: TypeAlias = Union[EndSummaryTyped, Dict[str, object]]


class End(TypedDict, total=False):
    id: Required[str]

    ended_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    project_id: Required[str]

    summary: Required[EndSummary]

    exception: Optional[str]

    output: object
