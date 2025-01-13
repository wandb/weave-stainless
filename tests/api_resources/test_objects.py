# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from wand_demo import WandDemo, AsyncWandDemo
from tests.utils import assert_matches_type
from wand_demo.types import (
    ObjectReadResponse,
    ObjectQueryResponse,
    ObjectCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WandDemo) -> None:
        object_ = client.objects.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WandDemo) -> None:
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
    def test_raw_response_create(self, client: WandDemo) -> None:
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
    def test_streaming_response_create(self, client: WandDemo) -> None:
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
    def test_method_query(self, client: WandDemo) -> None:
        object_ = client.objects.query(
            project_id="user/project",
        )
        assert_matches_type(ObjectQueryResponse, object_, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: WandDemo) -> None:
        object_ = client.objects.query(
            project_id="user/project",
            filter={
                "base_object_classes": ["Model"],
                "is_op": True,
                "latest_only": True,
                "object_ids": ["my_favorite_model"],
            },
            limit=100,
            metadata_only=True,
            offset=0,
            sort_by=[
                {
                    "direction": "asc",
                    "field": "created_at",
                }
            ],
        )
        assert_matches_type(ObjectQueryResponse, object_, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: WandDemo) -> None:
        response = client.objects.with_raw_response.query(
            project_id="user/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectQueryResponse, object_, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: WandDemo) -> None:
        with client.objects.with_streaming_response.query(
            project_id="user/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectQueryResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_read(self, client: WandDemo) -> None:
        object_ = client.objects.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        )
        assert_matches_type(ObjectReadResponse, object_, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: WandDemo) -> None:
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
    def test_streaming_response_read(self, client: WandDemo) -> None:
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
    async def test_method_create(self, async_client: AsyncWandDemo) -> None:
        object_ = await async_client.objects.create(
            obj={
                "object_id": "object_id",
                "project_id": "project_id",
                "val": {},
            },
        )
        assert_matches_type(ObjectCreateResponse, object_, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWandDemo) -> None:
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
    async def test_raw_response_create(self, async_client: AsyncWandDemo) -> None:
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
    async def test_streaming_response_create(self, async_client: AsyncWandDemo) -> None:
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
    async def test_method_query(self, async_client: AsyncWandDemo) -> None:
        object_ = await async_client.objects.query(
            project_id="user/project",
        )
        assert_matches_type(ObjectQueryResponse, object_, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncWandDemo) -> None:
        object_ = await async_client.objects.query(
            project_id="user/project",
            filter={
                "base_object_classes": ["Model"],
                "is_op": True,
                "latest_only": True,
                "object_ids": ["my_favorite_model"],
            },
            limit=100,
            metadata_only=True,
            offset=0,
            sort_by=[
                {
                    "direction": "asc",
                    "field": "created_at",
                }
            ],
        )
        assert_matches_type(ObjectQueryResponse, object_, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncWandDemo) -> None:
        response = await async_client.objects.with_raw_response.query(
            project_id="user/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectQueryResponse, object_, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncWandDemo) -> None:
        async with async_client.objects.with_streaming_response.query(
            project_id="user/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectQueryResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_read(self, async_client: AsyncWandDemo) -> None:
        object_ = await async_client.objects.read(
            digest="digest",
            object_id="object_id",
            project_id="project_id",
        )
        assert_matches_type(ObjectReadResponse, object_, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncWandDemo) -> None:
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
    async def test_streaming_response_read(self, async_client: AsyncWandDemo) -> None:
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
