# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_trace import WeaveTrace, AsyncWeaveTrace
from weave_trace.types import (
    TableQueryResponse,
    TableCreateResponse,
    TableUpdateResponse,
    TableQueryStatsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeaveTrace) -> None:
        table = client.tables.create(
            table={
                "project_id": "project_id",
                "rows": [{}],
            },
        )
        assert_matches_type(TableCreateResponse, table, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeaveTrace) -> None:
        response = client.tables.with_raw_response.create(
            table={
                "project_id": "project_id",
                "rows": [{}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableCreateResponse, table, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeaveTrace) -> None:
        with client.tables.with_streaming_response.create(
            table={
                "project_id": "project_id",
                "rows": [{}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableCreateResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: WeaveTrace) -> None:
        table = client.tables.update(
            base_digest="base_digest",
            project_id="project_id",
            updates=[{"append": {"row": {"foo": "bar"}}}],
        )
        assert_matches_type(TableUpdateResponse, table, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: WeaveTrace) -> None:
        response = client.tables.with_raw_response.update(
            base_digest="base_digest",
            project_id="project_id",
            updates=[{"append": {"row": {"foo": "bar"}}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableUpdateResponse, table, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: WeaveTrace) -> None:
        with client.tables.with_streaming_response.update(
            base_digest="base_digest",
            project_id="project_id",
            updates=[{"append": {"row": {"foo": "bar"}}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableUpdateResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: WeaveTrace) -> None:
        table = client.tables.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )
        assert_matches_type(TableQueryResponse, table, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: WeaveTrace) -> None:
        table = client.tables.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
            filter={
                "row_digests": [
                    "aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
                    "aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
                ]
            },
            limit=100,
            offset=10,
            sort_by=[
                {
                    "direction": "asc",
                    "field": "col_a.prop_b",
                }
            ],
        )
        assert_matches_type(TableQueryResponse, table, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: WeaveTrace) -> None:
        response = client.tables.with_raw_response.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableQueryResponse, table, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: WeaveTrace) -> None:
        with client.tables.with_streaming_response.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableQueryResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_stats(self, client: WeaveTrace) -> None:
        table = client.tables.query_stats(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )
        assert_matches_type(TableQueryStatsResponse, table, path=["response"])

    @parametrize
    def test_raw_response_query_stats(self, client: WeaveTrace) -> None:
        response = client.tables.with_raw_response.query_stats(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(TableQueryStatsResponse, table, path=["response"])

    @parametrize
    def test_streaming_response_query_stats(self, client: WeaveTrace) -> None:
        with client.tables.with_streaming_response.query_stats(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(TableQueryStatsResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTables:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncWeaveTrace) -> None:
        table = await async_client.tables.create(
            table={
                "project_id": "project_id",
                "rows": [{}],
            },
        )
        assert_matches_type(TableCreateResponse, table, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.tables.with_raw_response.create(
            table={
                "project_id": "project_id",
                "rows": [{}],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableCreateResponse, table, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.tables.with_streaming_response.create(
            table={
                "project_id": "project_id",
                "rows": [{}],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableCreateResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncWeaveTrace) -> None:
        table = await async_client.tables.update(
            base_digest="base_digest",
            project_id="project_id",
            updates=[{"append": {"row": {"foo": "bar"}}}],
        )
        assert_matches_type(TableUpdateResponse, table, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.tables.with_raw_response.update(
            base_digest="base_digest",
            project_id="project_id",
            updates=[{"append": {"row": {"foo": "bar"}}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableUpdateResponse, table, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.tables.with_streaming_response.update(
            base_digest="base_digest",
            project_id="project_id",
            updates=[{"append": {"row": {"foo": "bar"}}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableUpdateResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncWeaveTrace) -> None:
        table = await async_client.tables.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )
        assert_matches_type(TableQueryResponse, table, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        table = await async_client.tables.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
            filter={
                "row_digests": [
                    "aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
                    "aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
                ]
            },
            limit=100,
            offset=10,
            sort_by=[
                {
                    "direction": "asc",
                    "field": "col_a.prop_b",
                }
            ],
        )
        assert_matches_type(TableQueryResponse, table, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.tables.with_raw_response.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableQueryResponse, table, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.tables.with_streaming_response.query(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableQueryResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_stats(self, async_client: AsyncWeaveTrace) -> None:
        table = await async_client.tables.query_stats(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )
        assert_matches_type(TableQueryStatsResponse, table, path=["response"])

    @parametrize
    async def test_raw_response_query_stats(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.tables.with_raw_response.query_stats(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(TableQueryStatsResponse, table, path=["response"])

    @parametrize
    async def test_streaming_response_query_stats(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.tables.with_streaming_response.query_stats(
            digest="aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims",
            project_id="my_entity/my_project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(TableQueryStatsResponse, table, path=["response"])

        assert cast(Any, response.is_closed) is True
