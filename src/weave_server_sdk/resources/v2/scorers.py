# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import scorer_list_params, scorer_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ..._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ...types.v2.scorer_list_response import ScorerListResponse
from ...types.v2.scorer_read_response import ScorerReadResponse
from ...types.v2.scorer_create_response import ScorerCreateResponse
from ...types.v2.scorer_delete_response import ScorerDeleteResponse

__all__ = ["ScorersResource", "AsyncScorersResource"]


class ScorersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScorersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return ScorersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScorersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return ScorersResourceWithStreamingResponse(self)

    def create(
        self,
        project: str,
        *,
        entity: str,
        name: str,
        op_source_code: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerCreateResponse:
        """Create a scorer object.

        Args:
          name: The name of this scorer.

        Scorers with the same name will be versioned together.

          op_source_code: Complete source code for the Scorer.score op including imports

          description: A description of this scorer

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
            f"/v2/{entity}/{project}/scorers",
            body=maybe_transform(
                {
                    "name": name,
                    "op_source_code": op_source_code,
                    "description": description,
                },
                scorer_create_params.ScorerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerCreateResponse,
        )

    def list(
        self,
        project: str,
        *,
        entity: str,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JSONLDecoder[ScorerListResponse]:
        """
        List scorer objects.

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
            f"/v2/{entity}/{project}/scorers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    scorer_list_params.ScorerListParams,
                ),
            ),
            cast_to=JSONLDecoder[ScorerListResponse],
            stream=True,
        )

    def delete(
        self,
        object_id: str,
        *,
        entity: str,
        project: str,
        body: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerDeleteResponse:
        """
        Delete a scorer object.

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
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._delete(
            f"/v2/{entity}/{project}/scorers/{object_id}",
            body=maybe_transform(body, Optional[SequenceNotStr[str]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerDeleteResponse,
        )

    def read(
        self,
        digest: str,
        *,
        entity: str,
        project: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerReadResponse:
        """
        Get a scorer object.

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
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not digest:
            raise ValueError(f"Expected a non-empty value for `digest` but received {digest!r}")
        return self._get(
            f"/v2/{entity}/{project}/scorers/{object_id}/versions/{digest}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerReadResponse,
        )


class AsyncScorersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScorersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScorersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScorersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncScorersResourceWithStreamingResponse(self)

    async def create(
        self,
        project: str,
        *,
        entity: str,
        name: str,
        op_source_code: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerCreateResponse:
        """Create a scorer object.

        Args:
          name: The name of this scorer.

        Scorers with the same name will be versioned together.

          op_source_code: Complete source code for the Scorer.score op including imports

          description: A description of this scorer

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
            f"/v2/{entity}/{project}/scorers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "op_source_code": op_source_code,
                    "description": description,
                },
                scorer_create_params.ScorerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerCreateResponse,
        )

    async def list(
        self,
        project: str,
        *,
        entity: str,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncJSONLDecoder[ScorerListResponse]:
        """
        List scorer objects.

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
            f"/v2/{entity}/{project}/scorers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    scorer_list_params.ScorerListParams,
                ),
            ),
            cast_to=AsyncJSONLDecoder[ScorerListResponse],
            stream=True,
        )

    async def delete(
        self,
        object_id: str,
        *,
        entity: str,
        project: str,
        body: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerDeleteResponse:
        """
        Delete a scorer object.

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
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._delete(
            f"/v2/{entity}/{project}/scorers/{object_id}",
            body=await async_maybe_transform(body, Optional[SequenceNotStr[str]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerDeleteResponse,
        )

    async def read(
        self,
        digest: str,
        *,
        entity: str,
        project: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScorerReadResponse:
        """
        Get a scorer object.

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
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not digest:
            raise ValueError(f"Expected a non-empty value for `digest` but received {digest!r}")
        return await self._get(
            f"/v2/{entity}/{project}/scorers/{object_id}/versions/{digest}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScorerReadResponse,
        )


class ScorersResourceWithRawResponse:
    def __init__(self, scorers: ScorersResource) -> None:
        self._scorers = scorers

        self.create = to_raw_response_wrapper(
            scorers.create,
        )
        self.list = to_raw_response_wrapper(
            scorers.list,
        )
        self.delete = to_raw_response_wrapper(
            scorers.delete,
        )
        self.read = to_raw_response_wrapper(
            scorers.read,
        )


class AsyncScorersResourceWithRawResponse:
    def __init__(self, scorers: AsyncScorersResource) -> None:
        self._scorers = scorers

        self.create = async_to_raw_response_wrapper(
            scorers.create,
        )
        self.list = async_to_raw_response_wrapper(
            scorers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scorers.delete,
        )
        self.read = async_to_raw_response_wrapper(
            scorers.read,
        )


class ScorersResourceWithStreamingResponse:
    def __init__(self, scorers: ScorersResource) -> None:
        self._scorers = scorers

        self.create = to_streamed_response_wrapper(
            scorers.create,
        )
        self.list = to_streamed_response_wrapper(
            scorers.list,
        )
        self.delete = to_streamed_response_wrapper(
            scorers.delete,
        )
        self.read = to_streamed_response_wrapper(
            scorers.read,
        )


class AsyncScorersResourceWithStreamingResponse:
    def __init__(self, scorers: AsyncScorersResource) -> None:
        self._scorers = scorers

        self.create = async_to_streamed_response_wrapper(
            scorers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            scorers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scorers.delete,
        )
        self.read = async_to_streamed_response_wrapper(
            scorers.read,
        )
