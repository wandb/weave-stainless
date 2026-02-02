# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import v2_test_create_params
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
from ..types.v2_test_create_response import V2TestCreateResponse

__all__ = ["V2TestResource", "AsyncV2TestResource"]


class V2TestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2TestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return V2TestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2TestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return V2TestResourceWithStreamingResponse(self)

    def create(
        self,
        project: str,
        *,
        entity: str,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2TestCreateResponse:
        """
        Create a v2 test object (placeholder endpoint).

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
        return self._post(
            f"/object/{entity}/{project}/v2_test/create",
            body=maybe_transform({"message": message}, v2_test_create_params.V2TestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2TestCreateResponse,
        )


class AsyncV2TestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2TestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2TestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2TestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncV2TestResourceWithStreamingResponse(self)

    async def create(
        self,
        project: str,
        *,
        entity: str,
        message: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2TestCreateResponse:
        """
        Create a v2 test object (placeholder endpoint).

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
        return await self._post(
            f"/object/{entity}/{project}/v2_test/create",
            body=await async_maybe_transform({"message": message}, v2_test_create_params.V2TestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2TestCreateResponse,
        )


class V2TestResourceWithRawResponse:
    def __init__(self, v2_test: V2TestResource) -> None:
        self._v2_test = v2_test

        self.create = to_raw_response_wrapper(
            v2_test.create,
        )


class AsyncV2TestResourceWithRawResponse:
    def __init__(self, v2_test: AsyncV2TestResource) -> None:
        self._v2_test = v2_test

        self.create = async_to_raw_response_wrapper(
            v2_test.create,
        )


class V2TestResourceWithStreamingResponse:
    def __init__(self, v2_test: V2TestResource) -> None:
        self._v2_test = v2_test

        self.create = to_streamed_response_wrapper(
            v2_test.create,
        )


class AsyncV2TestResourceWithStreamingResponse:
    def __init__(self, v2_test: AsyncV2TestResource) -> None:
        self._v2_test = v2_test

        self.create = async_to_streamed_response_wrapper(
            v2_test.create,
        )
