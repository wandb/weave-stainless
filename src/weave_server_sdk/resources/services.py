# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import service_geolocate_params
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
from ..types.server_info_res import ServerInfoRes
from ..types.service_geolocate_response import ServiceGeolocateResponse

__all__ = ["ServicesResource", "AsyncServicesResource"]


class ServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return ServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return ServicesResourceWithStreamingResponse(self)

    def geolocate(
        self,
        *,
        ip: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceGeolocateResponse:
        """
        Lookup the geographic location of a user based on their IP address.

        This API exists for debugging purposes and may not be available in the future.

        Args:
          ip: IP address to geolocate, defaults to client IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/geolocate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ip": ip}, service_geolocate_params.ServiceGeolocateParams),
            ),
            cast_to=ServiceGeolocateResponse,
        )

    def health_check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Read Root"""
        return self._get(
            "/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def server_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServerInfoRes:
        """Server Info"""
        return self._get(
            "/server_info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerInfoRes,
        )

    def version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Read Version"""
        return self._get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncServicesResourceWithStreamingResponse(self)

    async def geolocate(
        self,
        *,
        ip: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceGeolocateResponse:
        """
        Lookup the geographic location of a user based on their IP address.

        This API exists for debugging purposes and may not be available in the future.

        Args:
          ip: IP address to geolocate, defaults to client IP address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/geolocate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ip": ip}, service_geolocate_params.ServiceGeolocateParams),
            ),
            cast_to=ServiceGeolocateResponse,
        )

    async def health_check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Read Root"""
        return await self._get(
            "/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def server_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServerInfoRes:
        """Server Info"""
        return await self._get(
            "/server_info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServerInfoRes,
        )

    async def version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Read Version"""
        return await self._get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ServicesResourceWithRawResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.geolocate = to_raw_response_wrapper(
            services.geolocate,
        )
        self.health_check = to_raw_response_wrapper(
            services.health_check,
        )
        self.server_info = to_raw_response_wrapper(
            services.server_info,
        )
        self.version = to_raw_response_wrapper(
            services.version,
        )


class AsyncServicesResourceWithRawResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.geolocate = async_to_raw_response_wrapper(
            services.geolocate,
        )
        self.health_check = async_to_raw_response_wrapper(
            services.health_check,
        )
        self.server_info = async_to_raw_response_wrapper(
            services.server_info,
        )
        self.version = async_to_raw_response_wrapper(
            services.version,
        )


class ServicesResourceWithStreamingResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.geolocate = to_streamed_response_wrapper(
            services.geolocate,
        )
        self.health_check = to_streamed_response_wrapper(
            services.health_check,
        )
        self.server_info = to_streamed_response_wrapper(
            services.server_info,
        )
        self.version = to_streamed_response_wrapper(
            services.version,
        )


class AsyncServicesResourceWithStreamingResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.geolocate = async_to_streamed_response_wrapper(
            services.geolocate,
        )
        self.health_check = async_to_streamed_response_wrapper(
            services.health_check,
        )
        self.server_info = async_to_streamed_response_wrapper(
            services.server_info,
        )
        self.version = async_to_streamed_response_wrapper(
            services.version,
        )
