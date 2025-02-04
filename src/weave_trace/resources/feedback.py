# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional

import httpx

from ..types import (
    feedback_purge_params,
    feedback_query_params,
    feedback_create_params,
    feedback_replace_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.feedback_query_response import FeedbackQueryResponse
from ..types.feedback_create_response import FeedbackCreateResponse
from ..types.feedback_replace_response import FeedbackReplaceResponse

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return FeedbackResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        feedback_type: str,
        payload: Dict[str, object],
        project_id: str,
        weave_ref: str,
        annotation_ref: Optional[str] | NotGiven = NOT_GIVEN,
        call_ref: Optional[str] | NotGiven = NOT_GIVEN,
        creator: Optional[str] | NotGiven = NOT_GIVEN,
        runnable_ref: Optional[str] | NotGiven = NOT_GIVEN,
        trigger_ref: Optional[str] | NotGiven = NOT_GIVEN,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackCreateResponse:
        """Add feedback to a call or object.

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/feedback/create",
            body=maybe_transform(
                {
                    "feedback_type": feedback_type,
                    "payload": payload,
                    "project_id": project_id,
                    "weave_ref": weave_ref,
                    "annotation_ref": annotation_ref,
                    "call_ref": call_ref,
                    "creator": creator,
                    "runnable_ref": runnable_ref,
                    "trigger_ref": trigger_ref,
                    "wb_user_id": wb_user_id,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateResponse,
        )

    def purge(
        self,
        *,
        project_id: str,
        query: feedback_purge_params.Query,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently delete feedback.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/feedback/purge",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "query": query,
                },
                feedback_purge_params.FeedbackPurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def query(
        self,
        *,
        project_id: str,
        fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        query: Optional[feedback_query_params.Query] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[feedback_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackQueryResponse:
        """
        Query for feedback.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/feedback/query",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "fields": fields,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort_by": sort_by,
                },
                feedback_query_params.FeedbackQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackQueryResponse,
        )

    def replace(
        self,
        *,
        feedback_id: str,
        feedback_type: str,
        payload: Dict[str, object],
        project_id: str,
        weave_ref: str,
        annotation_ref: Optional[str] | NotGiven = NOT_GIVEN,
        call_ref: Optional[str] | NotGiven = NOT_GIVEN,
        creator: Optional[str] | NotGiven = NOT_GIVEN,
        runnable_ref: Optional[str] | NotGiven = NOT_GIVEN,
        trigger_ref: Optional[str] | NotGiven = NOT_GIVEN,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackReplaceResponse:
        """Feedback Replace

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/feedback/replace",
            body=maybe_transform(
                {
                    "feedback_id": feedback_id,
                    "feedback_type": feedback_type,
                    "payload": payload,
                    "project_id": project_id,
                    "weave_ref": weave_ref,
                    "annotation_ref": annotation_ref,
                    "call_ref": call_ref,
                    "creator": creator,
                    "runnable_ref": runnable_ref,
                    "trigger_ref": trigger_ref,
                    "wb_user_id": wb_user_id,
                },
                feedback_replace_params.FeedbackReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackReplaceResponse,
        )


class AsyncFeedbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncFeedbackResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        feedback_type: str,
        payload: Dict[str, object],
        project_id: str,
        weave_ref: str,
        annotation_ref: Optional[str] | NotGiven = NOT_GIVEN,
        call_ref: Optional[str] | NotGiven = NOT_GIVEN,
        creator: Optional[str] | NotGiven = NOT_GIVEN,
        runnable_ref: Optional[str] | NotGiven = NOT_GIVEN,
        trigger_ref: Optional[str] | NotGiven = NOT_GIVEN,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackCreateResponse:
        """Add feedback to a call or object.

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/feedback/create",
            body=await async_maybe_transform(
                {
                    "feedback_type": feedback_type,
                    "payload": payload,
                    "project_id": project_id,
                    "weave_ref": weave_ref,
                    "annotation_ref": annotation_ref,
                    "call_ref": call_ref,
                    "creator": creator,
                    "runnable_ref": runnable_ref,
                    "trigger_ref": trigger_ref,
                    "wb_user_id": wb_user_id,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateResponse,
        )

    async def purge(
        self,
        *,
        project_id: str,
        query: feedback_purge_params.Query,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently delete feedback.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/feedback/purge",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "query": query,
                },
                feedback_purge_params.FeedbackPurgeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def query(
        self,
        *,
        project_id: str,
        fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        query: Optional[feedback_query_params.Query] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[feedback_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackQueryResponse:
        """
        Query for feedback.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/feedback/query",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "fields": fields,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort_by": sort_by,
                },
                feedback_query_params.FeedbackQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackQueryResponse,
        )

    async def replace(
        self,
        *,
        feedback_id: str,
        feedback_type: str,
        payload: Dict[str, object],
        project_id: str,
        weave_ref: str,
        annotation_ref: Optional[str] | NotGiven = NOT_GIVEN,
        call_ref: Optional[str] | NotGiven = NOT_GIVEN,
        creator: Optional[str] | NotGiven = NOT_GIVEN,
        runnable_ref: Optional[str] | NotGiven = NOT_GIVEN,
        trigger_ref: Optional[str] | NotGiven = NOT_GIVEN,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackReplaceResponse:
        """Feedback Replace

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/feedback/replace",
            body=await async_maybe_transform(
                {
                    "feedback_id": feedback_id,
                    "feedback_type": feedback_type,
                    "payload": payload,
                    "project_id": project_id,
                    "weave_ref": weave_ref,
                    "annotation_ref": annotation_ref,
                    "call_ref": call_ref,
                    "creator": creator,
                    "runnable_ref": runnable_ref,
                    "trigger_ref": trigger_ref,
                    "wb_user_id": wb_user_id,
                },
                feedback_replace_params.FeedbackReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackReplaceResponse,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_raw_response_wrapper(
            feedback.create,
        )
        self.purge = to_raw_response_wrapper(
            feedback.purge,
        )
        self.query = to_raw_response_wrapper(
            feedback.query,
        )
        self.replace = to_raw_response_wrapper(
            feedback.replace,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_raw_response_wrapper(
            feedback.create,
        )
        self.purge = async_to_raw_response_wrapper(
            feedback.purge,
        )
        self.query = async_to_raw_response_wrapper(
            feedback.query,
        )
        self.replace = async_to_raw_response_wrapper(
            feedback.replace,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_streamed_response_wrapper(
            feedback.create,
        )
        self.purge = to_streamed_response_wrapper(
            feedback.purge,
        )
        self.query = to_streamed_response_wrapper(
            feedback.query,
        )
        self.replace = to_streamed_response_wrapper(
            feedback.replace,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_streamed_response_wrapper(
            feedback.create,
        )
        self.purge = async_to_streamed_response_wrapper(
            feedback.purge,
        )
        self.query = async_to_streamed_response_wrapper(
            feedback.query,
        )
        self.replace = async_to_streamed_response_wrapper(
            feedback.replace,
        )
