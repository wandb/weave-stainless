# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from wand_demo import WeightsAndBiases, AsyncWeightsAndBiases
from tests.utils import assert_matches_type
from wand_demo.types import RefReadBatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRefs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_read_batch(self, client: WeightsAndBiases) -> None:
        ref = client.refs.read_batch(
            refs=["string"],
        )
        assert_matches_type(RefReadBatchResponse, ref, path=["response"])

    @parametrize
    def test_raw_response_read_batch(self, client: WeightsAndBiases) -> None:
        response = client.refs.with_raw_response.read_batch(
            refs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ref = response.parse()
        assert_matches_type(RefReadBatchResponse, ref, path=["response"])

    @parametrize
    def test_streaming_response_read_batch(self, client: WeightsAndBiases) -> None:
        with client.refs.with_streaming_response.read_batch(
            refs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ref = response.parse()
            assert_matches_type(RefReadBatchResponse, ref, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRefs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_read_batch(self, async_client: AsyncWeightsAndBiases) -> None:
        ref = await async_client.refs.read_batch(
            refs=["string"],
        )
        assert_matches_type(RefReadBatchResponse, ref, path=["response"])

    @parametrize
    async def test_raw_response_read_batch(self, async_client: AsyncWeightsAndBiases) -> None:
        response = await async_client.refs.with_raw_response.read_batch(
            refs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ref = await response.parse()
        assert_matches_type(RefReadBatchResponse, ref, path=["response"])

    @parametrize
    async def test_streaming_response_read_batch(self, async_client: AsyncWeightsAndBiases) -> None:
        async with async_client.refs.with_streaming_response.read_batch(
            refs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ref = await response.parse()
            assert_matches_type(RefReadBatchResponse, ref, path=["response"])

        assert cast(Any, response.is_closed) is True
