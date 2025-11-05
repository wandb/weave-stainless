# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import otel_export_params
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
from ..types.otel_export_response import OtelExportResponse

__all__ = ["OtelResource", "AsyncOtelResource"]


class OtelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OtelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return OtelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OtelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return OtelResourceWithStreamingResponse(self)

    def export(
        self,
        *,
        project_id: str,
        traces: object,
        wb_run_id: Optional[str] | Omit = omit,
        wb_user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtelExportResponse:
        """Export Trace

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/otel/v1/trace",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "traces": traces,
                    "wb_run_id": wb_run_id,
                    "wb_user_id": wb_user_id,
                },
                otel_export_params.OtelExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtelExportResponse,
        )


class AsyncOtelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOtelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOtelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOtelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncOtelResourceWithStreamingResponse(self)

    async def export(
        self,
        *,
        project_id: str,
        traces: object,
        wb_run_id: Optional[str] | Omit = omit,
        wb_user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OtelExportResponse:
        """Export Trace

        Args:
          wb_user_id: Do not set directly.

        Server will automatically populate this field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/otel/v1/trace",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "traces": traces,
                    "wb_run_id": wb_run_id,
                    "wb_user_id": wb_user_id,
                },
                otel_export_params.OtelExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OtelExportResponse,
        )


class OtelResourceWithRawResponse:
    def __init__(self, otel: OtelResource) -> None:
        self._otel = otel

        self.export = to_raw_response_wrapper(
            otel.export,
        )


class AsyncOtelResourceWithRawResponse:
    def __init__(self, otel: AsyncOtelResource) -> None:
        self._otel = otel

        self.export = async_to_raw_response_wrapper(
            otel.export,
        )


class OtelResourceWithStreamingResponse:
    def __init__(self, otel: OtelResource) -> None:
        self._otel = otel

        self.export = to_streamed_response_wrapper(
            otel.export,
        )


class AsyncOtelResourceWithStreamingResponse:
    def __init__(self, otel: AsyncOtelResource) -> None:
        self._otel = otel

        self.export = async_to_streamed_response_wrapper(
            otel.export,
        )
