# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_server_sdk import WeaveTrace, AsyncWeaveTrace
from weave_server_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream_query(self, client: WeaveTrace) -> None:
        thread = client.threads.stream_query(
            project_id="my_entity/my_project",
        )
        assert_matches_type(object, thread, path=["response"])

    @parametrize
    def test_method_stream_query_with_all_params(self, client: WeaveTrace) -> None:
        thread = client.threads.stream_query(
            project_id="my_entity/my_project",
            filter={
                "after_datetime": parse_datetime("2024-01-01T00:00:00Z"),
                "before_datetime": parse_datetime("2024-12-31T23:59:59Z"),
                "thread_ids": ["thread_1", "thread_2", "my_thread_id"],
            },
            limit=0,
            offset=0,
            sort_by=[
                {
                    "direction": "desc",
                    "field": "last_updated",
                }
            ],
        )
        assert_matches_type(object, thread, path=["response"])

    @parametrize
    def test_raw_response_stream_query(self, client: WeaveTrace) -> None:
        response = client.threads.with_raw_response.stream_query(
            project_id="my_entity/my_project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(object, thread, path=["response"])

    @parametrize
    def test_streaming_response_stream_query(self, client: WeaveTrace) -> None:
        with client.threads.with_streaming_response.stream_query(
            project_id="my_entity/my_project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(object, thread, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_stream_query(self, async_client: AsyncWeaveTrace) -> None:
        thread = await async_client.threads.stream_query(
            project_id="my_entity/my_project",
        )
        assert_matches_type(object, thread, path=["response"])

    @parametrize
    async def test_method_stream_query_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        thread = await async_client.threads.stream_query(
            project_id="my_entity/my_project",
            filter={
                "after_datetime": parse_datetime("2024-01-01T00:00:00Z"),
                "before_datetime": parse_datetime("2024-12-31T23:59:59Z"),
                "thread_ids": ["thread_1", "thread_2", "my_thread_id"],
            },
            limit=0,
            offset=0,
            sort_by=[
                {
                    "direction": "desc",
                    "field": "last_updated",
                }
            ],
        )
        assert_matches_type(object, thread, path=["response"])

    @parametrize
    async def test_raw_response_stream_query(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.threads.with_raw_response.stream_query(
            project_id="my_entity/my_project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = await response.parse()
        assert_matches_type(object, thread, path=["response"])

    @parametrize
    async def test_streaming_response_stream_query(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.threads.with_streaming_response.stream_query(
            project_id="my_entity/my_project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(object, thread, path=["response"])

        assert cast(Any, response.is_closed) is True
