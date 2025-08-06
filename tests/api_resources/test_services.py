# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_server_sdk import WeaveTrace, AsyncWeaveTrace
from weave_server_sdk.types import ServerInfoRes, ServiceGeolocateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_geolocate(self, client: WeaveTrace) -> None:
        service = client.services.geolocate()
        assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

    @parametrize
    def test_method_geolocate_with_all_params(self, client: WeaveTrace) -> None:
        service = client.services.geolocate(
            ip="1.2.3.4",
        )
        assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

    @parametrize
    def test_raw_response_geolocate(self, client: WeaveTrace) -> None:
        response = client.services.with_raw_response.geolocate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

    @parametrize
    def test_streaming_response_geolocate(self, client: WeaveTrace) -> None:
        with client.services.with_streaming_response.geolocate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_health_check(self, client: WeaveTrace) -> None:
        service = client.services.health_check()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_raw_response_health_check(self, client: WeaveTrace) -> None:
        response = client.services.with_raw_response.health_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_streaming_response_health_check(self, client: WeaveTrace) -> None:
        with client.services.with_streaming_response.health_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_server_info(self, client: WeaveTrace) -> None:
        service = client.services.server_info()
        assert_matches_type(ServerInfoRes, service, path=["response"])

    @parametrize
    def test_raw_response_server_info(self, client: WeaveTrace) -> None:
        response = client.services.with_raw_response.server_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServerInfoRes, service, path=["response"])

    @parametrize
    def test_streaming_response_server_info(self, client: WeaveTrace) -> None:
        with client.services.with_streaming_response.server_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServerInfoRes, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_version(self, client: WeaveTrace) -> None:
        service = client.services.version()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_raw_response_version(self, client: WeaveTrace) -> None:
        response = client.services.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_streaming_response_version(self, client: WeaveTrace) -> None:
        with client.services.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_geolocate(self, async_client: AsyncWeaveTrace) -> None:
        service = await async_client.services.geolocate()
        assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

    @parametrize
    async def test_method_geolocate_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        service = await async_client.services.geolocate(
            ip="1.2.3.4",
        )
        assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

    @parametrize
    async def test_raw_response_geolocate(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.services.with_raw_response.geolocate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

    @parametrize
    async def test_streaming_response_geolocate(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.services.with_streaming_response.geolocate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceGeolocateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_health_check(self, async_client: AsyncWeaveTrace) -> None:
        service = await async_client.services.health_check()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_raw_response_health_check(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.services.with_raw_response.health_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_streaming_response_health_check(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.services.with_streaming_response.health_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_server_info(self, async_client: AsyncWeaveTrace) -> None:
        service = await async_client.services.server_info()
        assert_matches_type(ServerInfoRes, service, path=["response"])

    @parametrize
    async def test_raw_response_server_info(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.services.with_raw_response.server_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServerInfoRes, service, path=["response"])

    @parametrize
    async def test_streaming_response_server_info(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.services.with_streaming_response.server_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServerInfoRes, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_version(self, async_client: AsyncWeaveTrace) -> None:
        service = await async_client.services.version()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_raw_response_version(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.services.with_raw_response.version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_streaming_response_version(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.services.with_streaming_response.version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True
