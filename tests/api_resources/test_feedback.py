# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from weave_trace import WeaveTrace, AsyncWeaveTrace
from weave_trace.types import (
    FeedbackQueryResponse,
    FeedbackCreateResponse,
    FeedbackReplaceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WeaveTrace) -> None:
        feedback = client.feedback.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: WeaveTrace) -> None:
        feedback = client.feedback.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
            annotation_ref="weave:///entity/project/object/name:digest",
            call_ref="weave:///entity/project/call/call_id",
            creator="Jane Smith",
            runnable_ref="weave:///entity/project/op/name:digest",
            trigger_ref="weave:///entity/project/object/name:digest",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WeaveTrace) -> None:
        response = client.feedback.with_raw_response.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WeaveTrace) -> None:
        with client.feedback.with_streaming_response.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_purge(self, client: WeaveTrace) -> None:
        feedback = client.feedback.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    def test_raw_response_purge(self, client: WeaveTrace) -> None:
        response = client.feedback.with_raw_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    def test_streaming_response_purge(self, client: WeaveTrace) -> None:
        with client.feedback.with_streaming_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(object, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: WeaveTrace) -> None:
        feedback = client.feedback.query(
            project_id="entity/project",
        )
        assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: WeaveTrace) -> None:
        feedback = client.feedback.query(
            project_id="entity/project",
            fields=["id", "feedback_type", "payload.note"],
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
        assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: WeaveTrace) -> None:
        response = client.feedback.with_raw_response.query(
            project_id="entity/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: WeaveTrace) -> None:
        with client.feedback.with_streaming_response.query(
            project_id="entity/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replace(self, client: WeaveTrace) -> None:
        feedback = client.feedback.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )
        assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: WeaveTrace) -> None:
        feedback = client.feedback.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
            annotation_ref="weave:///entity/project/object/name:digest",
            call_ref="weave:///entity/project/call/call_id",
            creator="Jane Smith",
            runnable_ref="weave:///entity/project/op/name:digest",
            trigger_ref="weave:///entity/project/object/name:digest",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: WeaveTrace) -> None:
        response = client.feedback.with_raw_response.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: WeaveTrace) -> None:
        with client.feedback.with_streaming_response.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWeaveTrace) -> None:
        feedback = await async_client.feedback.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        feedback = await async_client.feedback.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
            annotation_ref="weave:///entity/project/object/name:digest",
            call_ref="weave:///entity/project/call/call_id",
            creator="Jane Smith",
            runnable_ref="weave:///entity/project/op/name:digest",
            trigger_ref="weave:///entity/project/object/name:digest",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.feedback.with_raw_response.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.feedback.with_streaming_response.create(
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_purge(self, async_client: AsyncWeaveTrace) -> None:
        feedback = await async_client.feedback.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    async def test_raw_response_purge(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.feedback.with_raw_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(object, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_purge(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.feedback.with_streaming_response.purge(
            project_id="entity/project",
            query={"expr": {"and_": []}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(object, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncWeaveTrace) -> None:
        feedback = await async_client.feedback.query(
            project_id="entity/project",
        )
        assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        feedback = await async_client.feedback.query(
            project_id="entity/project",
            fields=["id", "feedback_type", "payload.note"],
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
        assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.feedback.with_raw_response.query(
            project_id="entity/project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.feedback.with_streaming_response.query(
            project_id="entity/project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackQueryResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replace(self, async_client: AsyncWeaveTrace) -> None:
        feedback = await async_client.feedback.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )
        assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncWeaveTrace) -> None:
        feedback = await async_client.feedback.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
            annotation_ref="weave:///entity/project/object/name:digest",
            call_ref="weave:///entity/project/call/call_id",
            creator="Jane Smith",
            runnable_ref="weave:///entity/project/op/name:digest",
            trigger_ref="weave:///entity/project/object/name:digest",
            wb_user_id="wb_user_id",
        )
        assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncWeaveTrace) -> None:
        response = await async_client.feedback.with_raw_response.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncWeaveTrace) -> None:
        async with async_client.feedback.with_streaming_response.replace(
            feedback_id="feedback_id",
            feedback_type="custom",
            payload={"key": "value"},
            project_id="entity/project",
            weave_ref="weave:///entity/project/object/name:digest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackReplaceResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
