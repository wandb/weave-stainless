# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_trace import WeaveTrace, AsyncWeaveTrace
from weave_trace.types import (
    CostQueryResponse,
    CostCreateResponse,
)
from weave_trace._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeaveTrace) -> None:
        cost = client.costs.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                }
            },
            project_id="entity/project",
        )
        assert_matches_type(CostCreateResponse, cost, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WeaveTrace) -> None:
        cost = client.costs.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                    "completion_token_cost_unit": "completion_token_cost_unit",
                    "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "prompt_token_cost_unit": "prompt_token_cost_unit",
                    "provider_id": "provider_id",
                }
            },
            project_id="entity/project",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(CostCreateResponse, cost, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeaveTrace) -> None:
        response = client.costs.with_raw_response.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                }
            },
            project_id="entity/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostCreateResponse, cost, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeaveTrace) -> None:
        with client.costs.with_streaming_response.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                }
            },
            project_id="entity/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = response.parse()
            assert_matches_type(CostCreateResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_purge(self, client: WeaveTrace) -> None:
        cost = client.costs.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )
        assert_matches_type(object, cost, path=["response"])

    @parametrize
    def test_raw_response_purge(self, client: WeaveTrace) -> None:
        response = client.costs.with_raw_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(object, cost, path=["response"])

    @parametrize
    def test_streaming_response_purge(self, client: WeaveTrace) -> None:
        with client.costs.with_streaming_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = response.parse()
            assert_matches_type(object, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: WeaveTrace) -> None:
        cost = client.costs.query(
            project_id="entity/project",
        )
        assert_matches_type(CostQueryResponse, cost, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: WeaveTrace) -> None:
        cost = client.costs.query(
            project_id="entity/project",
            fields=[
                "id",
                "llm_id",
                "prompt_token_cost",
                "completion_token_cost",
                "prompt_token_cost_unit",
                "completion_token_cost_unit",
                "effective_date",
                "provider_id",
            ],
            limit=10,
            offset=0,
            query={"expr": {"and_": []}},
            sort_by=[
                {
                    "direction": "asc",
                    "field": "field",
                }
            ],
        )
        assert_matches_type(CostQueryResponse, cost, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: WeaveTrace) -> None:
        response = client.costs.with_raw_response.query(
            project_id="entity/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostQueryResponse, cost, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: WeaveTrace) -> None:
        with client.costs.with_streaming_response.query(
            project_id="entity/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = response.parse()
            assert_matches_type(CostQueryResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCosts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWeaveTrace) -> None:
        cost = await async_client.costs.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                }
            },
            project_id="entity/project",
        )
        assert_matches_type(CostCreateResponse, cost, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        cost = await async_client.costs.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                    "completion_token_cost_unit": "completion_token_cost_unit",
                    "effective_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "prompt_token_cost_unit": "prompt_token_cost_unit",
                    "provider_id": "provider_id",
                }
            },
            project_id="entity/project",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(CostCreateResponse, cost, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.costs.with_raw_response.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                }
            },
            project_id="entity/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = await response.parse()
        assert_matches_type(CostCreateResponse, cost, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.costs.with_streaming_response.create(
            costs={
                "foo": {
                    "completion_token_cost": 0,
                    "prompt_token_cost": 0,
                }
            },
            project_id="entity/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = await response.parse()
            assert_matches_type(CostCreateResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_purge(self, async_client: AsyncWeaveTrace) -> None:
        cost = await async_client.costs.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )
        assert_matches_type(object, cost, path=["response"])

    @parametrize
    async def test_raw_response_purge(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.costs.with_raw_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = await response.parse()
        assert_matches_type(object, cost, path=["response"])

    @parametrize
    async def test_streaming_response_purge(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.costs.with_streaming_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = await response.parse()
            assert_matches_type(object, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncWeaveTrace) -> None:
        cost = await async_client.costs.query(
            project_id="entity/project",
        )
        assert_matches_type(CostQueryResponse, cost, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        cost = await async_client.costs.query(
            project_id="entity/project",
            fields=[
                "id",
                "llm_id",
                "prompt_token_cost",
                "completion_token_cost",
                "prompt_token_cost_unit",
                "completion_token_cost_unit",
                "effective_date",
                "provider_id",
            ],
            limit=10,
            offset=0,
            query={"expr": {"and_": []}},
            sort_by=[
                {
                    "direction": "asc",
                    "field": "field",
                }
            ],
        )
        assert_matches_type(CostQueryResponse, cost, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.costs.with_raw_response.query(
            project_id="entity/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = await response.parse()
        assert_matches_type(CostQueryResponse, cost, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.costs.with_streaming_response.query(
            project_id="entity/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = await response.parse()
            assert_matches_type(CostQueryResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True
