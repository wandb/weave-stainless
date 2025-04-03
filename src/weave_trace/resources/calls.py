# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import (
    call_end_params,
    call_read_params,
    call_start_params,
    call_delete_params,
    call_update_params,
    call_query_stats_params,
    call_stream_query_params,
    call_upsert_batch_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
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
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.call_read_response import CallReadResponse
from ..types.call_start_response import CallStartResponse
from ..types.call_query_stats_response import CallQueryStatsResponse
from ..types.call_upsert_batch_response import CallUpsertBatchResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        call_id: str,
        project_id: str,
        display_name: Optional[str] | NotGiven = NOT_GIVEN,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Call Update

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/call/update",
            body=maybe_transform(
                {
                    "call_id": call_id,
                    "project_id": project_id,
                    "display_name": display_name,
                    "wb_user_id": wb_user_id,
                },
                call_update_params.CallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete(
        self,
        *,
        call_ids: List[str],
        project_id: str,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Calls Delete

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calls/delete",
            body=maybe_transform(
                {
                    "call_ids": call_ids,
                    "project_id": project_id,
                    "wb_user_id": wb_user_id,
                },
                call_delete_params.CallDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def end(
        self,
        *,
        end: call_end_params.End,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Call End

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/call/end",
            body=maybe_transform({"end": end}, call_end_params.CallEndParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def query_stats(
        self,
        *,
        project_id: str,
        filter: Optional[call_query_stats_params.Filter] | NotGiven = NOT_GIVEN,
        query: Optional[call_query_stats_params.Query] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallQueryStatsResponse:
        """
        Calls Query Stats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calls/query_stats",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "filter": filter,
                    "query": query,
                },
                call_query_stats_params.CallQueryStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallQueryStatsResponse,
        )

    def read(
        self,
        *,
        id: str,
        project_id: str,
        include_costs: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallReadResponse:
        """
        Call Read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/call/read",
            body=maybe_transform(
                {
                    "id": id,
                    "project_id": project_id,
                    "include_costs": include_costs,
                },
                call_read_params.CallReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallReadResponse,
        )

    def start(
        self,
        *,
        start: call_start_params.Start,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallStartResponse:
        """
        Call Start

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/call/start",
            body=maybe_transform({"start": start}, call_start_params.CallStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallStartResponse,
        )

    def stream_query(
        self,
        *,
        project_id: str,
        columns: Optional[List[str]] | NotGiven = NOT_GIVEN,
        expand_columns: Optional[List[str]] | NotGiven = NOT_GIVEN,
        filter: Optional[call_stream_query_params.Filter] | NotGiven = NOT_GIVEN,
        include_costs: Optional[bool] | NotGiven = NOT_GIVEN,
        include_feedback: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        query: Optional[call_stream_query_params.Query] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[call_stream_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        accept: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JSONLDecoder[object]:
        """Calls Query Stream

        Args:
          expand_columns: Columns to expand, i.e.

        refs to other objects

          include_costs: Beta, subject to change. If true, the response will include any model costs for
              each call.

          include_feedback: Beta, subject to change. If true, the response will include feedback for each
              call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"accept": accept}), **(extra_headers or {})}
        return self._post(
            "/calls/stream_query",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "columns": columns,
                    "expand_columns": expand_columns,
                    "filter": filter,
                    "include_costs": include_costs,
                    "include_feedback": include_feedback,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort_by": sort_by,
                },
                call_stream_query_params.CallStreamQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[object],
            stream=True,
        )

    def upsert_batch(
        self,
        *,
        batch: Iterable[call_upsert_batch_params.Batch],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallUpsertBatchResponse:
        """
        Call Start Batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/call/upsert_batch",
            body=maybe_transform({"batch": batch}, call_upsert_batch_params.CallUpsertBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallUpsertBatchResponse,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        call_id: str,
        project_id: str,
        display_name: Optional[str] | NotGiven = NOT_GIVEN,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Call Update

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/call/update",
            body=await async_maybe_transform(
                {
                    "call_id": call_id,
                    "project_id": project_id,
                    "display_name": display_name,
                    "wb_user_id": wb_user_id,
                },
                call_update_params.CallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete(
        self,
        *,
        call_ids: List[str],
        project_id: str,
        wb_user_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Calls Delete

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calls/delete",
            body=await async_maybe_transform(
                {
                    "call_ids": call_ids,
                    "project_id": project_id,
                    "wb_user_id": wb_user_id,
                },
                call_delete_params.CallDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def end(
        self,
        *,
        end: call_end_params.End,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Call End

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/call/end",
            body=await async_maybe_transform({"end": end}, call_end_params.CallEndParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def query_stats(
        self,
        *,
        project_id: str,
        filter: Optional[call_query_stats_params.Filter] | NotGiven = NOT_GIVEN,
        query: Optional[call_query_stats_params.Query] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallQueryStatsResponse:
        """
        Calls Query Stats

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calls/query_stats",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "filter": filter,
                    "query": query,
                },
                call_query_stats_params.CallQueryStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallQueryStatsResponse,
        )

    async def read(
        self,
        *,
        id: str,
        project_id: str,
        include_costs: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallReadResponse:
        """
        Call Read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/call/read",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "project_id": project_id,
                    "include_costs": include_costs,
                },
                call_read_params.CallReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallReadResponse,
        )

    async def start(
        self,
        *,
        start: call_start_params.Start,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallStartResponse:
        """
        Call Start

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/call/start",
            body=await async_maybe_transform({"start": start}, call_start_params.CallStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallStartResponse,
        )

    async def stream_query(
        self,
        *,
        project_id: str,
        columns: Optional[List[str]] | NotGiven = NOT_GIVEN,
        expand_columns: Optional[List[str]] | NotGiven = NOT_GIVEN,
        filter: Optional[call_stream_query_params.Filter] | NotGiven = NOT_GIVEN,
        include_costs: Optional[bool] | NotGiven = NOT_GIVEN,
        include_feedback: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        query: Optional[call_stream_query_params.Query] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[call_stream_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        accept: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncJSONLDecoder[object]:
        """Calls Query Stream

        Args:
          expand_columns: Columns to expand, i.e.

        refs to other objects

          include_costs: Beta, subject to change. If true, the response will include any model costs for
              each call.

          include_feedback: Beta, subject to change. If true, the response will include feedback for each
              call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"accept": accept}), **(extra_headers or {})}
        return await self._post(
            "/calls/stream_query",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "columns": columns,
                    "expand_columns": expand_columns,
                    "filter": filter,
                    "include_costs": include_costs,
                    "include_feedback": include_feedback,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort_by": sort_by,
                },
                call_stream_query_params.CallStreamQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[object],
            stream=True,
        )

    async def upsert_batch(
        self,
        *,
        batch: Iterable[call_upsert_batch_params.Batch],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallUpsertBatchResponse:
        """
        Call Start Batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/call/upsert_batch",
            body=await async_maybe_transform({"batch": batch}, call_upsert_batch_params.CallUpsertBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallUpsertBatchResponse,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.update = to_raw_response_wrapper(
            calls.update,
        )
        self.delete = to_raw_response_wrapper(
            calls.delete,
        )
        self.end = to_raw_response_wrapper(
            calls.end,
        )
        self.query_stats = to_raw_response_wrapper(
            calls.query_stats,
        )
        self.read = to_raw_response_wrapper(
            calls.read,
        )
        self.start = to_raw_response_wrapper(
            calls.start,
        )
        self.stream_query = to_raw_response_wrapper(
            calls.stream_query,
        )
        self.upsert_batch = to_raw_response_wrapper(
            calls.upsert_batch,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.update = async_to_raw_response_wrapper(
            calls.update,
        )
        self.delete = async_to_raw_response_wrapper(
            calls.delete,
        )
        self.end = async_to_raw_response_wrapper(
            calls.end,
        )
        self.query_stats = async_to_raw_response_wrapper(
            calls.query_stats,
        )
        self.read = async_to_raw_response_wrapper(
            calls.read,
        )
        self.start = async_to_raw_response_wrapper(
            calls.start,
        )
        self.stream_query = async_to_raw_response_wrapper(
            calls.stream_query,
        )
        self.upsert_batch = async_to_raw_response_wrapper(
            calls.upsert_batch,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.update = to_streamed_response_wrapper(
            calls.update,
        )
        self.delete = to_streamed_response_wrapper(
            calls.delete,
        )
        self.end = to_streamed_response_wrapper(
            calls.end,
        )
        self.query_stats = to_streamed_response_wrapper(
            calls.query_stats,
        )
        self.read = to_streamed_response_wrapper(
            calls.read,
        )
        self.start = to_streamed_response_wrapper(
            calls.start,
        )
        self.stream_query = to_streamed_response_wrapper(
            calls.stream_query,
        )
        self.upsert_batch = to_streamed_response_wrapper(
            calls.upsert_batch,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.update = async_to_streamed_response_wrapper(
            calls.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            calls.delete,
        )
        self.end = async_to_streamed_response_wrapper(
            calls.end,
        )
        self.query_stats = async_to_streamed_response_wrapper(
            calls.query_stats,
        )
        self.read = async_to_streamed_response_wrapper(
            calls.read,
        )
        self.start = async_to_streamed_response_wrapper(
            calls.start,
        )
        self.stream_query = async_to_streamed_response_wrapper(
            calls.stream_query,
        )
        self.upsert_batch = async_to_streamed_response_wrapper(
            calls.upsert_batch,
        )
