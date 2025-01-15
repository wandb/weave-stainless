# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from wand_demo import WeightsAndBiases, AsyncWeightsAndBiases
from tests.utils import assert_matches_type
from wand_demo.types import ObjectReadResponse, ObjectCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeightsAndBiases) -> None:
        object_ = client.objects.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WeightsAndBiases) -> None:
        object_ = client.objects.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
                "builtin_object_class": "builtin_object_class",
                "set_base_object_class": "set_base_object_class",
            },
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeightsAndBiases) -> None:
        response = client.objects.with_raw_response.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeightsAndBiases) -> None:
        with client.objects.with_streaming_response.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectCreateResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read(self, client: WeightsAndBiases) -> None:
        object_ = client.objects.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        )
        assert_matches_type(ObjectReadResponse, object_, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: WeightsAndBiases) -> None:
        response = client.objects.with_raw_response.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectReadResponse, object_, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: WeightsAndBiases) -> None:
        with client.objects.with_streaming_response.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectReadResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncObjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWeightsAndBiases) -> None:
        object_ = await async_client.objects.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWeightsAndBiases) -> None:
        object_ = await async_client.objects.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
                "builtin_object_class": "builtin_object_class",
                "set_base_object_class": "set_base_object_class",
            },
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeightsAndBiases) -> None:
        response = await async_client.objects.with_raw_response.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeightsAndBiases) -> None:
        async with async_client.objects.with_streaming_response.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectCreateResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read(self, async_client: AsyncWeightsAndBiases) -> None:
        object_ = await async_client.objects.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        )
        assert_matches_type(ObjectReadResponse, object_, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncWeightsAndBiases) -> None:
        response = await async_client.objects.with_raw_response.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectReadResponse, object_, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncWeightsAndBiases) -> None:
        async with async_client.objects.with_streaming_response.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectReadResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True
