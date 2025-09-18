# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_server_sdk import WeaveTrace, AsyncWeaveTrace
from weave_server_sdk.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeaveTrace) -> None:
        completion = client.completions.create(
            inputs={"model": "model"},
            project_id="project_id",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WeaveTrace) -> None:
        completion = client.completions.create(
            inputs={
                "model": "model",
                "api_version": "api_version",
                "extra_headers": {"foo": "bar"},
                "frequency_penalty": 0,
                "function_call": "function_call",
                "functions": [{}],
                "logit_bias": {"foo": "bar"},
                "logprobs": True,
                "max_completion_tokens": 0,
                "max_tokens": 0,
                "messages": [{}],
                "modalities": [{}],
                "n": 0,
                "parallel_tool_calls": True,
                "presence_penalty": 0,
                "response_format": {"foo": "bar"},
                "seed": 0,
                "stop": "string",
                "stream": True,
                "temperature": 0,
                "timeout": 0,
                "tool_choice": "string",
                "tools": [{}],
                "top_logprobs": 0,
                "top_p": 0,
                "user": "user",
            },
            project_id="project_id",
            track_llm_call=True,
            wb_user_id="wb_user_id",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeaveTrace) -> None:
        response = client.completions.with_raw_response.create(
            inputs={"model": "model"},
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeaveTrace) -> None:
        with client.completions.with_streaming_response.create(
            inputs={"model": "model"},
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncWeaveTrace) -> None:
        completion = await async_client.completions.create(
            inputs={"model": "model"},
            project_id="project_id",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        completion = await async_client.completions.create(
            inputs={
                "model": "model",
                "api_version": "api_version",
                "extra_headers": {"foo": "bar"},
                "frequency_penalty": 0,
                "function_call": "function_call",
                "functions": [{}],
                "logit_bias": {"foo": "bar"},
                "logprobs": True,
                "max_completion_tokens": 0,
                "max_tokens": 0,
                "messages": [{}],
                "modalities": [{}],
                "n": 0,
                "parallel_tool_calls": True,
                "presence_penalty": 0,
                "response_format": {"foo": "bar"},
                "seed": 0,
                "stop": "string",
                "stream": True,
                "temperature": 0,
                "timeout": 0,
                "tool_choice": "string",
                "tools": [{}],
                "top_logprobs": 0,
                "top_p": 0,
                "user": "user",
            },
            project_id="project_id",
            track_llm_call=True,
            wb_user_id="wb_user_id",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.completions.with_raw_response.create(
            inputs={"model": "model"},
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.completions.with_streaming_response.create(
            inputs={"model": "model"},
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
