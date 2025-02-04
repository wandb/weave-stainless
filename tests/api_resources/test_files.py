# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_trace import WeaveTrace, AsyncWeaveTrace
from weave_trace.types import FileCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeaveTrace) -> None:
        file = client.files.create(
            file=b"raw file contents",
            project_id="project_id",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeaveTrace) -> None:
        response = client.files.with_raw_response.create(
            file=b"raw file contents",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeaveTrace) -> None:
        with client.files.with_streaming_response.create(
            file=b"raw file contents",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_content(self, client: WeaveTrace) -> None:
        file = client.files.content(
            digest="digest",
            project_id="project_id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_raw_response_content(self, client: WeaveTrace) -> None:
        response = client.files.with_raw_response.content(
            digest="digest",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_streaming_response_content(self, client: WeaveTrace) -> None:
        with client.files.with_streaming_response.content(
            digest="digest",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWeaveTrace) -> None:
        file = await async_client.files.create(
            file=b"raw file contents",
            project_id="project_id",
        )
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.files.with_raw_response.create(
            file=b"raw file contents",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCreateResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.files.with_streaming_response.create(
            file=b"raw file contents",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCreateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_content(self, async_client: AsyncWeaveTrace) -> None:
        file = await async_client.files.content(
            digest="digest",
            project_id="project_id",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_raw_response_content(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.files.with_raw_response.content(
            digest="digest",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_streaming_response_content(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.files.with_streaming_response.content(
            digest="digest",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True
