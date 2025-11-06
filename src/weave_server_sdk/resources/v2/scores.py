# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import score_list_params, score_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ..._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ...types.v2.score_list_response import ScoreListResponse
from ...types.v2.score_read_response import ScoreReadResponse
from ...types.v2.score_create_response import ScoreCreateResponse
from ...types.v2.score_delete_response import ScoreDeleteResponse

__all__ = ["ScoresResource", "AsyncScoresResource"]


class ScoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return ScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return ScoresResourceWithStreamingResponse(self)

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
    ) -> ScoreCreateResponse:
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
            f"/v2/{entity}/{project}/scores",
            body=maybe_transform(
                {
                    "prediction_id": prediction_id,
                    "scorer": scorer,
                    "value": value,
                    "evaluation_run_id": evaluation_run_id,
                },
                score_create_params.ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreCreateResponse,
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
    ) -> JSONLDecoder[ScoreListResponse]:
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
            f"/v2/{entity}/{project}/scores",
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
                    score_list_params.ScoreListParams,
                ),
            ),
            cast_to=JSONLDecoder[ScoreListResponse],
            stream=True,
        )

    def delete(
        self,
        project: str,
        *,
        entity: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoreDeleteResponse:
        """
        Delete scores.

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
        return self._delete(
            f"/v2/{entity}/{project}/scores",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreDeleteResponse,
        )

    def read(
        self,
        score_id: str,
        *,
        entity: str,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoreReadResponse:
        """
        Get a score.

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
        if not score_id:
            raise ValueError(f"Expected a non-empty value for `score_id` but received {score_id!r}")
        return self._get(
            f"/v2/{entity}/{project}/scores/{score_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreReadResponse,
        )


class AsyncScoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncScoresResourceWithStreamingResponse(self)

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
    ) -> ScoreCreateResponse:
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
            f"/v2/{entity}/{project}/scores",
            body=await async_maybe_transform(
                {
                    "prediction_id": prediction_id,
                    "scorer": scorer,
                    "value": value,
                    "evaluation_run_id": evaluation_run_id,
                },
                score_create_params.ScoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreCreateResponse,
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
    ) -> AsyncJSONLDecoder[ScoreListResponse]:
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
            f"/v2/{entity}/{project}/scores",
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
                    score_list_params.ScoreListParams,
                ),
            ),
            cast_to=AsyncJSONLDecoder[ScoreListResponse],
            stream=True,
        )

    async def delete(
        self,
        project: str,
        *,
        entity: str,
        body: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoreDeleteResponse:
        """
        Delete scores.

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
        return await self._delete(
            f"/v2/{entity}/{project}/scores",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreDeleteResponse,
        )

    async def read(
        self,
        score_id: str,
        *,
        entity: str,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoreReadResponse:
        """
        Get a score.

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
        if not score_id:
            raise ValueError(f"Expected a non-empty value for `score_id` but received {score_id!r}")
        return await self._get(
            f"/v2/{entity}/{project}/scores/{score_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoreReadResponse,
        )


class ScoresResourceWithRawResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.create = to_raw_response_wrapper(
            scores.create,
        )
        self.list = to_raw_response_wrapper(
            scores.list,
        )
        self.delete = to_raw_response_wrapper(
            scores.delete,
        )
        self.read = to_raw_response_wrapper(
            scores.read,
        )


class AsyncScoresResourceWithRawResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.create = async_to_raw_response_wrapper(
            scores.create,
        )
        self.list = async_to_raw_response_wrapper(
            scores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scores.delete,
        )
        self.read = async_to_raw_response_wrapper(
            scores.read,
        )


class ScoresResourceWithStreamingResponse:
    def __init__(self, scores: ScoresResource) -> None:
        self._scores = scores

        self.create = to_streamed_response_wrapper(
            scores.create,
        )
        self.list = to_streamed_response_wrapper(
            scores.list,
        )
        self.delete = to_streamed_response_wrapper(
            scores.delete,
        )
        self.read = to_streamed_response_wrapper(
            scores.read,
        )


class AsyncScoresResourceWithStreamingResponse:
    def __init__(self, scores: AsyncScoresResource) -> None:
        self._scores = scores

        self.create = async_to_streamed_response_wrapper(
            scores.create,
        )
        self.list = async_to_streamed_response_wrapper(
            scores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scores.delete,
        )
        self.read = async_to_streamed_response_wrapper(
            scores.read,
        )
