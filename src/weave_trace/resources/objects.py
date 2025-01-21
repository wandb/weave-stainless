# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import object_read_params, object_query_params, object_create_params
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
from ..types.object_read_response import ObjectReadResponse
from ..types.object_query_response import ObjectQueryResponse
from ..types.object_create_response import ObjectCreateResponse

__all__ = ["ObjectsResource", "AsyncObjectsResource"]


class ObjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/wand-demo-python#accessing-raw-response-data-eg-headers
        """
        return ObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/wand-demo-python#with_streaming_response
        """
        return ObjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        obj: object_create_params.Obj,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectCreateResponse:
        """
        Obj Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/obj/create",
            body=maybe_transform({"obj": obj}, object_create_params.ObjectCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectCreateResponse,
        )

    def query(
        self,
        *,
        project_id: str,
        filter: Optional[object_query_params.Filter] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        metadata_only: Optional[bool] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[object_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectQueryResponse:
        """
        Objs Query

        Args:
          project_id: The ID of the project to query

          filter: Filter criteria for the query. See `ObjectVersionFilter`

          limit: Maximum number of results to return

          metadata_only: If true, the `val` column is not read from the database and is empty.All other
              fields are returned.

          offset: Number of results to skip before returning

          sort_by: Sorting criteria for the query results. Currently only supports 'object_id' and
              'created_at'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/objs/query",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "filter": filter,
                    "limit": limit,
                    "metadata_only": metadata_only,
                    "offset": offset,
                    "sort_by": sort_by,
                },
                object_query_params.ObjectQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectQueryResponse,
        )

    def read(
        self,
        *,
        digest: str,
        object_id: str,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectReadResponse:
        """
        Obj Read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/obj/read",
            body=maybe_transform(
                {
                    "digest": digest,
                    "object_id": object_id,
                    "project_id": project_id,
                },
                object_read_params.ObjectReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectReadResponse,
        )


class AsyncObjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/wand-demo-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/wand-demo-python#with_streaming_response
        """
        return AsyncObjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        obj: object_create_params.Obj,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectCreateResponse:
        """
        Obj Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/obj/create",
            body=await async_maybe_transform({"obj": obj}, object_create_params.ObjectCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectCreateResponse,
        )

    async def query(
        self,
        *,
        project_id: str,
        filter: Optional[object_query_params.Filter] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        metadata_only: Optional[bool] | NotGiven = NOT_GIVEN,
        offset: Optional[int] | NotGiven = NOT_GIVEN,
        sort_by: Optional[Iterable[object_query_params.SortBy]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectQueryResponse:
        """
        Objs Query

        Args:
          project_id: The ID of the project to query

          filter: Filter criteria for the query. See `ObjectVersionFilter`

          limit: Maximum number of results to return

          metadata_only: If true, the `val` column is not read from the database and is empty.All other
              fields are returned.

          offset: Number of results to skip before returning

          sort_by: Sorting criteria for the query results. Currently only supports 'object_id' and
              'created_at'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/objs/query",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "filter": filter,
                    "limit": limit,
                    "metadata_only": metadata_only,
                    "offset": offset,
                    "sort_by": sort_by,
                },
                object_query_params.ObjectQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectQueryResponse,
        )

    async def read(
        self,
        *,
        digest: str,
        object_id: str,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectReadResponse:
        """
        Obj Read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/obj/read",
            body=await async_maybe_transform(
                {
                    "digest": digest,
                    "object_id": object_id,
                    "project_id": project_id,
                },
                object_read_params.ObjectReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectReadResponse,
        )


class ObjectsResourceWithRawResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.create = to_raw_response_wrapper(
            objects.create,
        )
        self.query = to_raw_response_wrapper(
            objects.query,
        )
        self.read = to_raw_response_wrapper(
            objects.read,
        )


class AsyncObjectsResourceWithRawResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.create = async_to_raw_response_wrapper(
            objects.create,
        )
        self.query = async_to_raw_response_wrapper(
            objects.query,
        )
        self.read = async_to_raw_response_wrapper(
            objects.read,
        )


class ObjectsResourceWithStreamingResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.create = to_streamed_response_wrapper(
            objects.create,
        )
        self.query = to_streamed_response_wrapper(
            objects.query,
        )
        self.read = to_streamed_response_wrapper(
            objects.read,
        )


class AsyncObjectsResourceWithStreamingResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.create = async_to_streamed_response_wrapper(
            objects.create,
        )
        self.query = async_to_streamed_response_wrapper(
            objects.query,
        )
        self.read = async_to_streamed_response_wrapper(
            objects.read,
        )
