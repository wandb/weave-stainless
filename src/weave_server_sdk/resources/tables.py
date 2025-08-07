# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import table_query_params, table_create_params, table_update_params, table_query_stats_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.table_query_response import TableQueryResponse
from ..types.table_create_response import TableCreateResponse
from ..types.table_update_response import TableUpdateResponse
from ..types.table_query_stats_response import TableQueryStatsResponse

__all__ = ["TablesResource", "AsyncTablesResource"]


class TablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return TablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return TablesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        table: table_create_params.Table,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableCreateResponse:
        """
        Table Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/table/create",
            body=maybe_transform({"table": table}, table_create_params.TableCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableCreateResponse,
        )

    def update(
        self,
        *,
        base_digest: str,
        project_id: str,
        updates: Iterable[table_update_params.Update],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableUpdateResponse:
        """
        Table Update

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/table/update",
            body=maybe_transform(
                {
                    "base_digest": base_digest,
                    "project_id": project_id,
                    "updates": updates,
                },
                table_update_params.TableUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableUpdateResponse,
        )

    def query(
        self,
        *,
        digest: str,
        project_id: str,
        filter: Optional[table_query_params.Filter] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[table_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableQueryResponse:
        """
        Table Query

        Args:
          digest: The digest of the table to query

          project_id: The ID of the project

          filter: Optional filter to apply to the query. See `TableRowFilter` for more details.

          limit: Maximum number of rows to return

          offset: Number of rows to skip before starting to return rows

          sort_by: List of fields to sort by. Fields can be dot-separated to access dictionary
              values. No sorting uses the default table order (insertion order).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/table/query",
            body=maybe_transform(
                {
                    "digest": digest,
                    "project_id": project_id,
                    "filter": filter,
                    "limit": limit,
                    "offset": offset,
                    "sort_by": sort_by,
                },
                table_query_params.TableQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableQueryResponse,
        )

    def query_stats(
        self,
        *,
        digest: str,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableQueryStatsResponse:
        """
        Table Query Stats

        Args:
          digest: The digest of the table to query

          project_id: The ID of the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/table/query_stats",
            body=maybe_transform(
                {
                    "digest": digest,
                    "project_id": project_id,
                },
                table_query_stats_params.TableQueryStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableQueryStatsResponse,
        )


class AsyncTablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncTablesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        table: table_create_params.Table,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableCreateResponse:
        """
        Table Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/table/create",
            body=await async_maybe_transform({"table": table}, table_create_params.TableCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableCreateResponse,
        )

    async def update(
        self,
        *,
        base_digest: str,
        project_id: str,
        updates: Iterable[table_update_params.Update],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableUpdateResponse:
        """
        Table Update

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/table/update",
            body=await async_maybe_transform(
                {
                    "base_digest": base_digest,
                    "project_id": project_id,
                    "updates": updates,
                },
                table_update_params.TableUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableUpdateResponse,
        )

    async def query(
        self,
        *,
        digest: str,
        project_id: str,
        filter: Optional[table_query_params.Filter] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[table_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableQueryResponse:
        """
        Table Query

        Args:
          digest: The digest of the table to query

          project_id: The ID of the project

          filter: Optional filter to apply to the query. See `TableRowFilter` for more details.

          limit: Maximum number of rows to return

          offset: Number of rows to skip before starting to return rows

          sort_by: List of fields to sort by. Fields can be dot-separated to access dictionary
              values. No sorting uses the default table order (insertion order).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/table/query",
            body=await async_maybe_transform(
                {
                    "digest": digest,
                    "project_id": project_id,
                    "filter": filter,
                    "limit": limit,
                    "offset": offset,
                    "sort_by": sort_by,
                },
                table_query_params.TableQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableQueryResponse,
        )

    async def query_stats(
        self,
        *,
        digest: str,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TableQueryStatsResponse:
        """
        Table Query Stats

        Args:
          digest: The digest of the table to query

          project_id: The ID of the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/table/query_stats",
            body=await async_maybe_transform(
                {
                    "digest": digest,
                    "project_id": project_id,
                },
                table_query_stats_params.TableQueryStatsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TableQueryStatsResponse,
        )


class TablesResourceWithRawResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.create = to_raw_response_wrapper(
            tables.create,
        )
        self.update = to_raw_response_wrapper(
            tables.update,
        )
        self.query = to_raw_response_wrapper(
            tables.query,
        )
        self.query_stats = to_raw_response_wrapper(
            tables.query_stats,
        )


class AsyncTablesResourceWithRawResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.create = async_to_raw_response_wrapper(
            tables.create,
        )
        self.update = async_to_raw_response_wrapper(
            tables.update,
        )
        self.query = async_to_raw_response_wrapper(
            tables.query,
        )
        self.query_stats = async_to_raw_response_wrapper(
            tables.query_stats,
        )


class TablesResourceWithStreamingResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.create = to_streamed_response_wrapper(
            tables.create,
        )
        self.update = to_streamed_response_wrapper(
            tables.update,
        )
        self.query = to_streamed_response_wrapper(
            tables.query,
        )
        self.query_stats = to_streamed_response_wrapper(
            tables.query_stats,
        )


class AsyncTablesResourceWithStreamingResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.create = async_to_streamed_response_wrapper(
            tables.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tables.update,
        )
        self.query = async_to_streamed_response_wrapper(
            tables.query,
        )
        self.query_stats = async_to_streamed_response_wrapper(
            tables.query_stats,
        )
