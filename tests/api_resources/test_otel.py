# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_server_sdk import WeaveTrace, AsyncWeaveTrace
from weave_server_sdk.types import OtelExportResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOtel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_export(self, client: WeaveTrace) -> None:
        otel = client.otel.export(
            project_id="project_id",
            traces={},
        )
        assert_matches_type(OtelExportResponse, otel, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: WeaveTrace) -> None:
        otel = client.otel.export(
            project_id="project_id",
            traces={},
            wb_run_id="wb_run_id",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(OtelExportResponse, otel, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: WeaveTrace) -> None:
        response = client.otel.with_raw_response.export(
            project_id="project_id",
            traces={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        otel = response.parse()
        assert_matches_type(OtelExportResponse, otel, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: WeaveTrace) -> None:
        with client.otel.with_streaming_response.export(
            project_id="project_id",
            traces={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            otel = response.parse()
            assert_matches_type(OtelExportResponse, otel, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOtel:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_export(self, async_client: AsyncWeaveTrace) -> None:
        otel = await async_client.otel.export(
            project_id="project_id",
            traces={},
        )
        assert_matches_type(OtelExportResponse, otel, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        otel = await async_client.otel.export(
            project_id="project_id",
            traces={},
            wb_run_id="wb_run_id",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(OtelExportResponse, otel, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.otel.with_raw_response.export(
            project_id="project_id",
            traces={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        otel = await response.parse()
        assert_matches_type(OtelExportResponse, otel, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.otel.with_streaming_response.export(
            project_id="project_id",
            traces={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            otel = await response.parse()
            assert_matches_type(OtelExportResponse, otel, path=["response"])

        assert cast(Any, response.is_closed) is True
