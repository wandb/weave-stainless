# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_server_sdk import WeaveTrace, AsyncWeaveTrace
from weave_server_sdk.types.v2 import (
    OpListResponse,
    OpReadResponse,
    OpCreateResponse,
    OpDeleteResponse,
)
from weave_server_sdk._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeaveTrace) -> None:
        op = client.v2.ops.create(
            project="project",
            entity="entity",
        )
        assert_matches_type(OpCreateResponse, op, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WeaveTrace) -> None:
        op = client.v2.ops.create(
            project="project",
            entity="entity",
            name="name",
            source_code="source_code",
        )
        assert_matches_type(OpCreateResponse, op, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeaveTrace) -> None:
        response = client.v2.ops.with_raw_response.create(
            project="project",
            entity="entity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        op = response.parse()
        assert_matches_type(OpCreateResponse, op, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeaveTrace) -> None:
        with client.v2.ops.with_streaming_response.create(
            project="project",
            entity="entity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            op = response.parse()
            assert_matches_type(OpCreateResponse, op, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2.ops.with_raw_response.create(
                project="project",
                entity="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2.ops.with_raw_response.create(
                project="",
                entity="entity",
            )

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_method_list(self, client: WeaveTrace) -> None:
        op_stream = client.v2.ops.list(
            project="project",
            entity="entity",
        )
        assert_matches_type(JSONLDecoder[OpListResponse], op_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_method_list_with_all_params(self, client: WeaveTrace) -> None:
        op_stream = client.v2.ops.list(
            project="project",
            entity="entity",
            limit=0,
            offset=0,
        )
        assert_matches_type(JSONLDecoder[OpListResponse], op_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_raw_response_list(self, client: WeaveTrace) -> None:
        response = client.v2.ops.with_raw_response.list(
            project="project",
            entity="entity",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    def test_streaming_response_list(self, client: WeaveTrace) -> None:
        with client.v2.ops.with_streaming_response.list(
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
            client.v2.ops.with_raw_response.list(
                project="project",
                entity="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2.ops.with_raw_response.list(
                project="",
                entity="entity",
            )

    @parametrize
    def test_method_delete(self, client: WeaveTrace) -> None:
        op = client.v2.ops.delete(
            object_id="object_id",
            entity="entity",
            project="project",
        )
        assert_matches_type(OpDeleteResponse, op, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: WeaveTrace) -> None:
        op = client.v2.ops.delete(
            object_id="object_id",
            entity="entity",
            project="project",
            body=["string"],
        )
        assert_matches_type(OpDeleteResponse, op, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: WeaveTrace) -> None:
        response = client.v2.ops.with_raw_response.delete(
            object_id="object_id",
            entity="entity",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        op = response.parse()
        assert_matches_type(OpDeleteResponse, op, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: WeaveTrace) -> None:
        with client.v2.ops.with_streaming_response.delete(
            object_id="object_id",
            entity="entity",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            op = response.parse()
            assert_matches_type(OpDeleteResponse, op, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2.ops.with_raw_response.delete(
                object_id="object_id",
                entity="",
                project="project",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2.ops.with_raw_response.delete(
                object_id="object_id",
                entity="entity",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.v2.ops.with_raw_response.delete(
                object_id="",
                entity="entity",
                project="project",
            )

    @parametrize
    def test_method_read(self, client: WeaveTrace) -> None:
        op = client.v2.ops.read(
            digest="digest",
            entity="entity",
            project="project",
            object_id="object_id",
        )
        assert_matches_type(OpReadResponse, op, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: WeaveTrace) -> None:
        response = client.v2.ops.with_raw_response.read(
            digest="digest",
            entity="entity",
            project="project",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        op = response.parse()
        assert_matches_type(OpReadResponse, op, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: WeaveTrace) -> None:
        with client.v2.ops.with_streaming_response.read(
            digest="digest",
            entity="entity",
            project="project",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            op = response.parse()
            assert_matches_type(OpReadResponse, op, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: WeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            client.v2.ops.with_raw_response.read(
                digest="digest",
                entity="",
                project="project",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            client.v2.ops.with_raw_response.read(
                digest="digest",
                entity="entity",
                project="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.v2.ops.with_raw_response.read(
                digest="digest",
                entity="entity",
                project="project",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `digest` but received ''"):
            client.v2.ops.with_raw_response.read(
                digest="",
                entity="entity",
                project="project",
                object_id="object_id",
            )


class TestAsyncOps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncWeaveTrace) -> None:
        op = await async_client.v2.ops.create(
            project="project",
            entity="entity",
        )
        assert_matches_type(OpCreateResponse, op, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        op = await async_client.v2.ops.create(
            project="project",
            entity="entity",
            name="name",
            source_code="source_code",
        )
        assert_matches_type(OpCreateResponse, op, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2.ops.with_raw_response.create(
            project="project",
            entity="entity",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        op = await response.parse()
        assert_matches_type(OpCreateResponse, op, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2.ops.with_streaming_response.create(
            project="project",
            entity="entity",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            op = await response.parse()
            assert_matches_type(OpCreateResponse, op, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2.ops.with_raw_response.create(
                project="project",
                entity="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2.ops.with_raw_response.create(
                project="",
                entity="entity",
            )

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_method_list(self, async_client: AsyncWeaveTrace) -> None:
        op_stream = await async_client.v2.ops.list(
            project="project",
            entity="entity",
        )
        assert_matches_type(AsyncJSONLDecoder[OpListResponse], op_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        op_stream = await async_client.v2.ops.list(
            project="project",
            entity="entity",
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncJSONLDecoder[OpListResponse], op_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2.ops.with_raw_response.list(
            project="project",
            entity="entity",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support application/jsonl responses")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2.ops.with_streaming_response.list(
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
            await async_client.v2.ops.with_raw_response.list(
                project="project",
                entity="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2.ops.with_raw_response.list(
                project="",
                entity="entity",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncWeaveTrace) -> None:
        op = await async_client.v2.ops.delete(
            object_id="object_id",
            entity="entity",
            project="project",
        )
        assert_matches_type(OpDeleteResponse, op, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        op = await async_client.v2.ops.delete(
            object_id="object_id",
            entity="entity",
            project="project",
            body=["string"],
        )
        assert_matches_type(OpDeleteResponse, op, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2.ops.with_raw_response.delete(
            object_id="object_id",
            entity="entity",
            project="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        op = await response.parse()
        assert_matches_type(OpDeleteResponse, op, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2.ops.with_streaming_response.delete(
            object_id="object_id",
            entity="entity",
            project="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            op = await response.parse()
            assert_matches_type(OpDeleteResponse, op, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2.ops.with_raw_response.delete(
                object_id="object_id",
                entity="",
                project="project",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2.ops.with_raw_response.delete(
                object_id="object_id",
                entity="entity",
                project="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.v2.ops.with_raw_response.delete(
                object_id="",
                entity="entity",
                project="project",
            )

    @parametrize
    async def test_method_read(self, async_client: AsyncWeaveTrace) -> None:
        op = await async_client.v2.ops.read(
            digest="digest",
            entity="entity",
            project="project",
            object_id="object_id",
        )
        assert_matches_type(OpReadResponse, op, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.v2.ops.with_raw_response.read(
            digest="digest",
            entity="entity",
            project="project",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        op = await response.parse()
        assert_matches_type(OpReadResponse, op, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.v2.ops.with_streaming_response.read(
            digest="digest",
            entity="entity",
            project="project",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            op = await response.parse()
            assert_matches_type(OpReadResponse, op, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncWeaveTrace) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity` but received ''"):
            await async_client.v2.ops.with_raw_response.read(
                digest="digest",
                entity="",
                project="project",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project` but received ''"):
            await async_client.v2.ops.with_raw_response.read(
                digest="digest",
                entity="entity",
                project="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.v2.ops.with_raw_response.read(
                digest="digest",
                entity="entity",
                project="project",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `digest` but received ''"):
            await async_client.v2.ops.with_raw_response.read(
                digest="",
                entity="entity",
                project="project",
                object_id="object_id",
            )
