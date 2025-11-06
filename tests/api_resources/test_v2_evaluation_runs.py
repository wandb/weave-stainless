# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_server_sdk import WeaveTrace, AsyncWeaveTrace
from weave_server_sdk.types import (
    V2EvaluationRunListResponse,
    V2EvaluationRunReadResponse,
    V2EvaluationRunCreateResponse,
    V2EvaluationRunDeleteResponse,
    V2EvaluationRunFinishResponse,
)
from weave_server_sdk._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2EvaluationRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeaveTrace) -> None:
        v2_evaluation_run = client.v2_evaluation_runs.create(
            project="project",
            entity="entity",
            evaluation="evaluation",
            model="model",
        )
        assert_matches_type(V2EvaluationRunCreateResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeaveTrace) -> None:
        response = client.v2_evaluation_runs.with_raw_response.create(
            project="project",
            entity="entity",
            evaluation="evaluation",
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = response.parse()
        assert_matches_type(V2EvaluationRunCreateResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeaveTrace) -> None:
        with client.v2_evaluation_runs.with_streaming_response.create(
            project="project",
            entity="entity",
            evaluation="evaluation",
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = response.parse()
            assert_matches_type(V2EvaluationRunCreateResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2_evaluation_runs.with_raw_response.create(
                project="project",
                entity="",
                evaluation="evaluation",
                model="model",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2_evaluation_runs.with_raw_response.create(
                project="",
                entity="entity",
                evaluation="evaluation",
                model="model",
            )

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_method_list(self, client: WeaveTrace) -> None:
        v2_evaluation_run_stream = client.v2_evaluation_runs.list(
            project="project",
            entity="entity",
        )
        assert_matches_type(JSONLDecoder[V2EvaluationRunListResponse], v2_evaluation_run_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_method_list_with_all_params(self, client: WeaveTrace) -> None:
        v2_evaluation_run_stream = client.v2_evaluation_runs.list(
            project="project",
            entity="entity",
            limit=0,
            offset=0,
        )
        assert_matches_type(JSONLDecoder[V2EvaluationRunListResponse], v2_evaluation_run_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_raw_response_list(self, client: WeaveTrace) -> None:
        response = client.v2_evaluation_runs.with_raw_response.list(
            project="project",
            entity="entity",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_streaming_response_list(self, client: WeaveTrace) -> None:
        with client.v2_evaluation_runs.with_streaming_response.list(
            project="project",
            entity="entity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_path_params_list(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2_evaluation_runs.with_raw_response.list(
                project="project",
                entity="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2_evaluation_runs.with_raw_response.list(
                project="",
                entity="entity",
            )

    @parametrize
    def test_method_delete(self, client: WeaveTrace) -> None:
        v2_evaluation_run = client.v2_evaluation_runs.delete(
            project="project",
            entity="entity",
            body=["string"],
        )
        assert_matches_type(V2EvaluationRunDeleteResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: WeaveTrace) -> None:
        response = client.v2_evaluation_runs.with_raw_response.delete(
            project="project",
            entity="entity",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = response.parse()
        assert_matches_type(V2EvaluationRunDeleteResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: WeaveTrace) -> None:
        with client.v2_evaluation_runs.with_streaming_response.delete(
            project="project",
            entity="entity",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = response.parse()
            assert_matches_type(V2EvaluationRunDeleteResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2_evaluation_runs.with_raw_response.delete(
                project="project",
                entity="",
                body=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2_evaluation_runs.with_raw_response.delete(
                project="",
                entity="entity",
                body=["string"],
            )

    @parametrize
    def test_method_finish(self, client: WeaveTrace) -> None:
        v2_evaluation_run = client.v2_evaluation_runs.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )
        assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_method_finish_with_all_params(self, client: WeaveTrace) -> None:
        v2_evaluation_run = client.v2_evaluation_runs.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
            summary={"foo": "bar"},
        )
        assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_raw_response_finish(self, client: WeaveTrace) -> None:
        response = client.v2_evaluation_runs.with_raw_response.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = response.parse()
        assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_streaming_response_finish(self, client: WeaveTrace) -> None:
        with client.v2_evaluation_runs.with_streaming_response.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = response.parse()
            assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_finish(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2_evaluation_runs.with_raw_response.finish(
                evaluation_run_id="evaluation_run_id",
                entity="",
                project="project",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2_evaluation_runs.with_raw_response.finish(
                evaluation_run_id="evaluation_run_id",
                entity="entity",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_id` but received ''"):
            client.v2_evaluation_runs.with_raw_response.finish(
                evaluation_run_id="",
                entity="entity",
                project="project",
            )

    @parametrize
    def test_method_read(self, client: WeaveTrace) -> None:
        v2_evaluation_run = client.v2_evaluation_runs.read(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )
        assert_matches_type(V2EvaluationRunReadResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: WeaveTrace) -> None:
        response = client.v2_evaluation_runs.with_raw_response.read(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = response.parse()
        assert_matches_type(V2EvaluationRunReadResponse, v2_evaluation_run, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: WeaveTrace) -> None:
        with client.v2_evaluation_runs.with_streaming_response.read(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = response.parse()
            assert_matches_type(V2EvaluationRunReadResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2_evaluation_runs.with_raw_response.read(
                evaluation_run_id="evaluation_run_id",
                entity="",
                project="project",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2_evaluation_runs.with_raw_response.read(
                evaluation_run_id="evaluation_run_id",
                entity="entity",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_id` but received ''"):
            client.v2_evaluation_runs.with_raw_response.read(
                evaluation_run_id="",
                entity="entity",
                project="project",
            )


class TestAsyncV2EvaluationRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncWeaveTrace) -> None:
        v2_evaluation_run = await async_client.v2_evaluation_runs.create(
            project="project",
            entity="entity",
            evaluation="evaluation",
            model="model",
        )
        assert_matches_type(V2EvaluationRunCreateResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2_evaluation_runs.with_raw_response.create(
            project="project",
            entity="entity",
            evaluation="evaluation",
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = await response.parse()
        assert_matches_type(V2EvaluationRunCreateResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2_evaluation_runs.with_streaming_response.create(
            project="project",
            entity="entity",
            evaluation="evaluation",
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = await response.parse()
            assert_matches_type(V2EvaluationRunCreateResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.create(
                project="project",
                entity="",
                evaluation="evaluation",
                model="model",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.create(
                project="",
                entity="entity",
                evaluation="evaluation",
                model="model",
            )

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_method_list(self, async_client: AsyncWeaveTrace) -> None:
        v2_evaluation_run_stream = await async_client.v2_evaluation_runs.list(
            project="project",
            entity="entity",
        )
        assert_matches_type(AsyncJSONLDecoder[V2EvaluationRunListResponse], v2_evaluation_run_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        v2_evaluation_run_stream = await async_client.v2_evaluation_runs.list(
            project="project",
            entity="entity",
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJSONLDecoder[V2EvaluationRunListResponse], v2_evaluation_run_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2_evaluation_runs.with_raw_response.list(
            project="project",
            entity="entity",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2_evaluation_runs.with_streaming_response.list(
            project="project",
            entity="entity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.list(
                project="project",
                entity="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.list(
                project="",
                entity="entity",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncWeaveTrace) -> None:
        v2_evaluation_run = await async_client.v2_evaluation_runs.delete(
            project="project",
            entity="entity",
            body=["string"],
        )
        assert_matches_type(V2EvaluationRunDeleteResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2_evaluation_runs.with_raw_response.delete(
            project="project",
            entity="entity",
            body=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = await response.parse()
        assert_matches_type(V2EvaluationRunDeleteResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2_evaluation_runs.with_streaming_response.delete(
            project="project",
            entity="entity",
            body=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = await response.parse()
            assert_matches_type(V2EvaluationRunDeleteResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.delete(
                project="project",
                entity="",
                body=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.delete(
                project="",
                entity="entity",
                body=["string"],
            )

    @parametrize
    async def test_method_finish(self, async_client: AsyncWeaveTrace) -> None:
        v2_evaluation_run = await async_client.v2_evaluation_runs.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )
        assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_method_finish_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        v2_evaluation_run = await async_client.v2_evaluation_runs.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
            summary={"foo": "bar"},
        )
        assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_raw_response_finish(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2_evaluation_runs.with_raw_response.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = await response.parse()
        assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_streaming_response_finish(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2_evaluation_runs.with_streaming_response.finish(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = await response.parse()
            assert_matches_type(V2EvaluationRunFinishResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_finish(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.finish(
                evaluation_run_id="evaluation_run_id",
                entity="",
                project="project",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.finish(
                evaluation_run_id="evaluation_run_id",
                entity="entity",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_id` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.finish(
                evaluation_run_id="",
                entity="entity",
                project="project",
            )

    @parametrize
    async def test_method_read(self, async_client: AsyncWeaveTrace) -> None:
        v2_evaluation_run = await async_client.v2_evaluation_runs.read(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )
        assert_matches_type(V2EvaluationRunReadResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2_evaluation_runs.with_raw_response.read(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2_evaluation_run = await response.parse()
        assert_matches_type(V2EvaluationRunReadResponse, v2_evaluation_run, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2_evaluation_runs.with_streaming_response.read(
            evaluation_run_id="evaluation_run_id",
            entity="entity",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2_evaluation_run = await response.parse()
            assert_matches_type(V2EvaluationRunReadResponse, v2_evaluation_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.read(
                evaluation_run_id="evaluation_run_id",
                entity="",
                project="project",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.read(
                evaluation_run_id="evaluation_run_id",
                entity="entity",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evaluation_run_id` but received ''"):
            await async_client.v2_evaluation_runs.with_raw_response.read(
                evaluation_run_id="",
                entity="entity",
                project="project",
            )
