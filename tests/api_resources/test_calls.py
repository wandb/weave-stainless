# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_server_sdk import WeaveTrace, AsyncWeaveTrace
from weave_server_sdk.types import (
    CallReadResponse,
    CallStartResponse,
    CallQueryStatsResponse,
    CallStreamQueryResponse,
    CallUpsertBatchResponse,
)
from weave_server_sdk._utils import parse_datetime
from weave_server_sdk._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: WeaveTrace) -> None:
        call = client.calls.update(
            call_id="call_id",
            project_id="project_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: WeaveTrace) -> None:
        call = client.calls.update(
            call_id="call_id",
            project_id="project_id",
            display_name="display_name",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.update(
            call_id="call_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.update(
            call_id="call_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(object, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: WeaveTrace) -> None:
        call = client.calls.delete(
            call_ids=["string"],
            project_id="project_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: WeaveTrace) -> None:
        call = client.calls.delete(
            call_ids=["string"],
            project_id="project_id",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.delete(
            call_ids=["string"],
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.delete(
            call_ids=["string"],
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(object, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_end(self, client: WeaveTrace) -> None:
        call = client.calls.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {},
            },
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_method_end_with_all_params(self, client: WeaveTrace) -> None:
        call = client.calls.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {
                    "status_counts": {"foo": 0},
                    "usage": {
                        "foo": {
                            "completion_tokens": 0,
                            "input_tokens": 0,
                            "output_tokens": 0,
                            "prompt_tokens": 0,
                            "requests": 0,
                            "total_tokens": 0,
                        }
                    },
                },
                "exception": "exception",
                "output": {},
            },
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_raw_response_end(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(object, call, path=["response"])

    @parametrize
    def test_streaming_response_end(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(object, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_stats(self, client: WeaveTrace) -> None:
        call = client.calls.query_stats(
            project_id="project_id",
        )
        assert_matches_type(CallQueryStatsResponse, call, path=["response"])

    @parametrize
    def test_method_query_stats_with_all_params(self, client: WeaveTrace) -> None:
        call = client.calls.query_stats(
            project_id="project_id",
            expand_columns=["inputs.self.message", "inputs.model.prompt"],
            filter={
                "call_ids": ["string"],
                "input_refs": ["string"],
                "op_names": ["string"],
                "output_refs": ["string"],
                "parent_ids": ["string"],
                "thread_ids": ["string"],
                "trace_ids": ["string"],
                "trace_roots_only": True,
                "turn_ids": ["string"],
                "wb_run_ids": ["string"],
                "wb_user_ids": ["string"],
            },
            include_total_storage_size=True,
            limit=0,
            query={"expr": {"and_": []}},
        )
        assert_matches_type(CallQueryStatsResponse, call, path=["response"])

    @parametrize
    def test_raw_response_query_stats(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.query_stats(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallQueryStatsResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_query_stats(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.query_stats(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallQueryStatsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read(self, client: WeaveTrace) -> None:
        call = client.calls.read(
            id="id",
            project_id="project_id",
        )
        assert_matches_type(CallReadResponse, call, path=["response"])

    @parametrize
    def test_method_read_with_all_params(self, client: WeaveTrace) -> None:
        call = client.calls.read(
            id="id",
            project_id="project_id",
            include_costs=True,
            include_storage_size=True,
            include_total_storage_size=True,
        )
        assert_matches_type(CallReadResponse, call, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.read(
            id="id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallReadResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.read(
            id="id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallReadResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: WeaveTrace) -> None:
        call = client.calls.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(CallStartResponse, call, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: WeaveTrace) -> None:
        call = client.calls.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "id": "id",
                "display_name": "display_name",
                "parent_id": "parent_id",
                "thread_id": "thread_id",
                "trace_id": "trace_id",
                "turn_id": "turn_id",
                "wb_run_id": "wb_run_id",
                "wb_run_step": 0,
                "wb_user_id": "wb_user_id",
            },
        )
        assert_matches_type(CallStartResponse, call, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallStartResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallStartResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="prism")
    @parametrize
    def test_method_stream_query(self, client: WeaveTrace) -> None:
        call_stream = client.calls.stream_query(
            project_id="project_id",
        )
        assert_matches_type(JSONLDecoder[CallStreamQueryResponse], call_stream, path=["response"])

    @pytest.mark.skip(reason="prism")
    @parametrize
    def test_method_stream_query_with_all_params(self, client: WeaveTrace) -> None:
        call_stream = client.calls.stream_query(
            project_id="project_id",
            columns=["string"],
            expand_columns=["inputs.self.message", "inputs.model.prompt"],
            filter={
                "call_ids": ["string"],
                "input_refs": ["string"],
                "op_names": ["string"],
                "output_refs": ["string"],
                "parent_ids": ["string"],
                "thread_ids": ["string"],
                "trace_ids": ["string"],
                "trace_roots_only": True,
                "turn_ids": ["string"],
                "wb_run_ids": ["string"],
                "wb_user_ids": ["string"],
            },
            include_costs=True,
            include_feedback=True,
            include_storage_size=True,
            include_total_storage_size=True,
            limit=0,
            offset=0,
            query={"expr": {"and_": []}},
            return_expanded_column_values=True,
            sort_by=[
                {
                    "direction": "asc",
                    "field": "field",
                }
            ],
            accept="accept",
        )
        assert_matches_type(JSONLDecoder[CallStreamQueryResponse], call_stream, path=["response"])

    @pytest.mark.skip(reason="prism")
    @parametrize
    def test_raw_response_stream_query(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.stream_query(
            project_id="project_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="prism")
    @parametrize
    def test_streaming_response_stream_query(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.stream_query(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upsert_batch(self, client: WeaveTrace) -> None:
        call = client.calls.upsert_batch(
            batch=[
                {
                    "req": {
                        "start": {
                            "attributes": {"foo": "bar"},
                            "inputs": {"foo": "bar"},
                            "op_name": "op_name",
                            "project_id": "project_id",
                            "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    }
                }
            ],
        )
        assert_matches_type(CallUpsertBatchResponse, call, path=["response"])

    @parametrize
    def test_raw_response_upsert_batch(self, client: WeaveTrace) -> None:
        response = client.calls.with_raw_response.upsert_batch(
            batch=[
                {
                    "req": {
                        "start": {
                            "attributes": {"foo": "bar"},
                            "inputs": {"foo": "bar"},
                            "op_name": "op_name",
                            "project_id": "project_id",
                            "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    }
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallUpsertBatchResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_upsert_batch(self, client: WeaveTrace) -> None:
        with client.calls.with_streaming_response.upsert_batch(
            batch=[
                {
                    "req": {
                        "start": {
                            "attributes": {"foo": "bar"},
                            "inputs": {"foo": "bar"},
                            "op_name": "op_name",
                            "project_id": "project_id",
                            "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    }
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallUpsertBatchResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.update(
            call_id="call_id",
            project_id="project_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.update(
            call_id="call_id",
            project_id="project_id",
            display_name="display_name",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.update(
            call_id="call_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.update(
            call_id="call_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(object, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.delete(
            call_ids=["string"],
            project_id="project_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.delete(
            call_ids=["string"],
            project_id="project_id",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.delete(
            call_ids=["string"],
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.delete(
            call_ids=["string"],
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(object, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_end(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {},
            },
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_method_end_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {
                    "status_counts": {"foo": 0},
                    "usage": {
                        "foo": {
                            "completion_tokens": 0,
                            "input_tokens": 0,
                            "output_tokens": 0,
                            "prompt_tokens": 0,
                            "requests": 0,
                            "total_tokens": 0,
                        }
                    },
                },
                "exception": "exception",
                "output": {},
            },
        )
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_raw_response_end(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(object, call, path=["response"])

    @parametrize
    async def test_streaming_response_end(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.end(
            end={
                "id": "id",
                "ended_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "project_id": "project_id",
                "summary": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(object, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_stats(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.query_stats(
            project_id="project_id",
        )
        assert_matches_type(CallQueryStatsResponse, call, path=["response"])

    @parametrize
    async def test_method_query_stats_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.query_stats(
            project_id="project_id",
            expand_columns=["inputs.self.message", "inputs.model.prompt"],
            filter={
                "call_ids": ["string"],
                "input_refs": ["string"],
                "op_names": ["string"],
                "output_refs": ["string"],
                "parent_ids": ["string"],
                "thread_ids": ["string"],
                "trace_ids": ["string"],
                "trace_roots_only": True,
                "turn_ids": ["string"],
                "wb_run_ids": ["string"],
                "wb_user_ids": ["string"],
            },
            include_total_storage_size=True,
            limit=0,
            query={"expr": {"and_": []}},
        )
        assert_matches_type(CallQueryStatsResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_query_stats(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.query_stats(
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallQueryStatsResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_query_stats(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.query_stats(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallQueryStatsResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.read(
            id="id",
            project_id="project_id",
        )
        assert_matches_type(CallReadResponse, call, path=["response"])

    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.read(
            id="id",
            project_id="project_id",
            include_costs=True,
            include_storage_size=True,
            include_total_storage_size=True,
        )
        assert_matches_type(CallReadResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.read(
            id="id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallReadResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.read(
            id="id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallReadResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(CallStartResponse, call, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "id": "id",
                "display_name": "display_name",
                "parent_id": "parent_id",
                "thread_id": "thread_id",
                "trace_id": "trace_id",
                "turn_id": "turn_id",
                "wb_run_id": "wb_run_id",
                "wb_run_step": 0,
                "wb_user_id": "wb_user_id",
            },
        )
        assert_matches_type(CallStartResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallStartResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.start(
            start={
                "attributes": {"foo": "bar"},
                "inputs": {"foo": "bar"},
                "op_name": "op_name",
                "project_id": "project_id",
                "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallStartResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="prism")
    @parametrize
    async def test_method_stream_query(self, async_client: AsyncWeaveTrace) -> None:
        call_stream = await async_client.calls.stream_query(
            project_id="project_id",
        )
        assert_matches_type(AsyncJSONLDecoder[CallStreamQueryResponse], call_stream, path=["response"])

    @pytest.mark.skip(reason="prism")
    @parametrize
    async def test_method_stream_query_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        call_stream = await async_client.calls.stream_query(
            project_id="project_id",
            columns=["string"],
            expand_columns=["inputs.self.message", "inputs.model.prompt"],
            filter={
                "call_ids": ["string"],
                "input_refs": ["string"],
                "op_names": ["string"],
                "output_refs": ["string"],
                "parent_ids": ["string"],
                "thread_ids": ["string"],
                "trace_ids": ["string"],
                "trace_roots_only": True,
                "turn_ids": ["string"],
                "wb_run_ids": ["string"],
                "wb_user_ids": ["string"],
            },
            include_costs=True,
            include_feedback=True,
            include_storage_size=True,
            include_total_storage_size=True,
            limit=0,
            offset=0,
            query={"expr": {"and_": []}},
            return_expanded_column_values=True,
            sort_by=[
                {
                    "direction": "asc",
                    "field": "field",
                }
            ],
            accept="accept",
        )
        assert_matches_type(AsyncJSONLDecoder[CallStreamQueryResponse], call_stream, path=["response"])

    @pytest.mark.skip(reason="prism")
    @parametrize
    async def test_raw_response_stream_query(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.stream_query(
            project_id="project_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="prism")
    @parametrize
    async def test_streaming_response_stream_query(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.stream_query(
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upsert_batch(self, async_client: AsyncWeaveTrace) -> None:
        call = await async_client.calls.upsert_batch(
            batch=[
                {
                    "req": {
                        "start": {
                            "attributes": {"foo": "bar"},
                            "inputs": {"foo": "bar"},
                            "op_name": "op_name",
                            "project_id": "project_id",
                            "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    }
                }
            ],
        )
        assert_matches_type(CallUpsertBatchResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_upsert_batch(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.calls.with_raw_response.upsert_batch(
            batch=[
                {
                    "req": {
                        "start": {
                            "attributes": {"foo": "bar"},
                            "inputs": {"foo": "bar"},
                            "op_name": "op_name",
                            "project_id": "project_id",
                            "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    }
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallUpsertBatchResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_upsert_batch(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.calls.with_streaming_response.upsert_batch(
            batch=[
                {
                    "req": {
                        "start": {
                            "attributes": {"foo": "bar"},
                            "inputs": {"foo": "bar"},
                            "op_name": "op_name",
                            "project_id": "project_id",
                            "started_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        }
                    }
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallUpsertBatchResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True
