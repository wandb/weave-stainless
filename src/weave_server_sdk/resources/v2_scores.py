# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import v2_score_list_params, v2_score_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.v2_score_list_response import V2ScoreListResponse
from ..types.v2_score_create_response import V2ScoreCreateResponse

__all__ = ["V2ScoresResource", "AsyncV2ScoresResource"]


class V2ScoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return V2ScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return V2ScoresResourceWithStreamingResponse(self)

    def create(
        self,
        project: str,
        *,
        entity: str,
        prediction_id: str,
        scorer: str,
        value: float,
        evaluation_run_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ScoreCreateResponse:
        """
        Create a score.

        Args:
          prediction_id: The prediction ID

          scorer: The scorer reference (weave:// URI)

          value: The value of the score

          evaluation_run_id: Optional evaluation run ID to link this score as a child call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        return self._post(
            f"/object/{entity}/{project}/scores",
            body=maybe_transform(
                {
                    "prediction_id": prediction_id,
                    "scorer": scorer,
                    "value": value,
                    "evaluation_run_id": evaluation_run_id,
                },
                v2_score_create_params.V2ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ScoreCreateResponse,
        )

    def list(
        self,
        project: str,
        *,
        entity: str,
        evaluation_run_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JSONLDecoder[V2ScoreListResponse]:
        """
        List scores.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        return self._get(
            f"/object/{entity}/{project}/scores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "evaluation_run_id": evaluation_run_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    v2_score_list_params.V2ScoreListParams,
                ),
            ),
            cast_to=JSONLDecoder[V2ScoreListResponse],
            stream=True,
        )


class AsyncV2ScoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncV2ScoresResourceWithStreamingResponse(self)

    async def create(
        self,
        project: str,
        *,
        entity: str,
        prediction_id: str,
        scorer: str,
        value: float,
        evaluation_run_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ScoreCreateResponse:
        """
        Create a score.

        Args:
          prediction_id: The prediction ID

          scorer: The scorer reference (weave:// URI)

          value: The value of the score

          evaluation_run_id: Optional evaluation run ID to link this score as a child call

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        return await self._post(
            f"/object/{entity}/{project}/scores",
            body=await async_maybe_transform(
                {
                    "prediction_id": prediction_id,
                    "scorer": scorer,
                    "value": value,
                    "evaluation_run_id": evaluation_run_id,
                },
                v2_score_create_params.V2ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ScoreCreateResponse,
        )

    async def list(
        self,
        project: str,
        *,
        entity: str,
        evaluation_run_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncJSONLDecoder[V2ScoreListResponse]:
        """
        List scores.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        return await self._get(
            f"/object/{entity}/{project}/scores",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "evaluation_run_id": evaluation_run_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    v2_score_list_params.V2ScoreListParams,
                ),
            ),
            cast_to=AsyncJSONLDecoder[V2ScoreListResponse],
            stream=True,
        )


class V2ScoresResourceWithRawResponse:
    def __init__(self, v2_scores: V2ScoresResource) -> None:
        self._v2_scores = v2_scores

        self.create = to_raw_response_wrapper(
            v2_scores.create,
        )
        self.list = to_raw_response_wrapper(
            v2_scores.list,
        )


class AsyncV2ScoresResourceWithRawResponse:
    def __init__(self, v2_scores: AsyncV2ScoresResource) -> None:
        self._v2_scores = v2_scores

        self.create = async_to_raw_response_wrapper(
            v2_scores.create,
        )
        self.list = async_to_raw_response_wrapper(
            v2_scores.list,
        )


class V2ScoresResourceWithStreamingResponse:
    def __init__(self, v2_scores: V2ScoresResource) -> None:
        self._v2_scores = v2_scores

        self.create = to_streamed_response_wrapper(
            v2_scores.create,
        )
        self.list = to_streamed_response_wrapper(
            v2_scores.list,
        )


class AsyncV2ScoresResourceWithStreamingResponse:
    def __init__(self, v2_scores: AsyncV2ScoresResource) -> None:
        self._v2_scores = v2_scores

        self.create = async_to_streamed_response_wrapper(
            v2_scores.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v2_scores.list,
        )
