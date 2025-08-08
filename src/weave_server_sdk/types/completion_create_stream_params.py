# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompletionCreateStreamParams", "Inputs"]


class CompletionCreateStreamParams(TypedDict, total=False):
    inputs: Required[Inputs]

    project_id: Required[str]

    track_llm_call: Optional[bool]
    """Whether to track this LLM call in the trace server"""

    wb_user_id: Optional[str]
    """Do not set directly. Server will automatically populate this field."""


class Inputs(TypedDict, total=False):
    model: Required[str]

    api_version: Optional[str]

    extra_headers: Optional[Dict[str, object]]

    frequency_penalty: Optional[float]

    function_call: Optional[str]

    functions: Optional[Iterable[object]]

    logit_bias: Optional[Dict[str, object]]

    logprobs: Optional[bool]

    max_completion_tokens: Optional[int]

    max_tokens: Optional[int]

    messages: Iterable[object]

    modalities: Optional[Iterable[object]]

    n: Optional[int]

    parallel_tool_calls: Optional[bool]

    presence_penalty: Optional[float]

    response_format: Union[Dict[str, object], object, None]

    seed: Optional[int]

    stop: Union[str, Iterable[object], None]

    stream: Optional[bool]

    temperature: Optional[float]

    timeout: Union[float, str, None]

    tool_choice: Union[str, Dict[str, object], None]

    tools: Optional[Iterable[object]]

    top_logprobs: Optional[int]

    top_p: Optional[float]

    user: Optional[str]
