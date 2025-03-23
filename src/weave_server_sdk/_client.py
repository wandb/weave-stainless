# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import refs, calls, costs, files, tables, objects, feedback, services
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, WeaveTraceError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "WeaveTrace",
    "AsyncWeaveTrace",
    "Client",
    "AsyncClient",
]


class WeaveTrace(SyncAPIClient):
    services: services.ServicesResource
    calls: calls.CallsResource
    objects: objects.ObjectsResource
    tables: tables.TablesResource
    refs: refs.RefsResource
    files: files.FilesResource
    costs: costs.CostsResource
    feedback: feedback.FeedbackResource
    with_raw_response: WeaveTraceWithRawResponse
    with_streaming_response: WeaveTraceWithStreamedResponse

    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous WeaveTrace client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `USERNAME`
        - `password` from `PASSWORD`
        """
        if username is None:
            username = os.environ.get("USERNAME")
        if username is None:
            raise WeaveTraceError(
                "The username client option must be set either by passing username to the client or by setting the USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("PASSWORD")
        if password is None:
            raise WeaveTraceError(
                "The password client option must be set either by passing password to the client or by setting the PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("WEAVE_TRACE_BASE_URL")
        if base_url is None:
            base_url = f"https://trace.wandb.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.services = services.ServicesResource(self)
        self.calls = calls.CallsResource(self)
        self.objects = objects.ObjectsResource(self)
        self.tables = tables.TablesResource(self)
        self.refs = refs.RefsResource(self)
        self.files = files.FilesResource(self)
        self.costs = costs.CostsResource(self)
        self.feedback = feedback.FeedbackResource(self)
        self.with_raw_response = WeaveTraceWithRawResponse(self)
        self.with_streaming_response = WeaveTraceWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncWeaveTrace(AsyncAPIClient):
    services: services.AsyncServicesResource
    calls: calls.AsyncCallsResource
    objects: objects.AsyncObjectsResource
    tables: tables.AsyncTablesResource
    refs: refs.AsyncRefsResource
    files: files.AsyncFilesResource
    costs: costs.AsyncCostsResource
    feedback: feedback.AsyncFeedbackResource
    with_raw_response: AsyncWeaveTraceWithRawResponse
    with_streaming_response: AsyncWeaveTraceWithStreamedResponse

    # client options
    username: str
    password: str

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncWeaveTrace client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `USERNAME`
        - `password` from `PASSWORD`
        """
        if username is None:
            username = os.environ.get("USERNAME")
        if username is None:
            raise WeaveTraceError(
                "The username client option must be set either by passing username to the client or by setting the USERNAME environment variable"
            )
        self.username = username

        if password is None:
            password = os.environ.get("PASSWORD")
        if password is None:
            raise WeaveTraceError(
                "The password client option must be set either by passing password to the client or by setting the PASSWORD environment variable"
            )
        self.password = password

        if base_url is None:
            base_url = os.environ.get("WEAVE_TRACE_BASE_URL")
        if base_url is None:
            base_url = f"https://trace.wandb.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.services = services.AsyncServicesResource(self)
        self.calls = calls.AsyncCallsResource(self)
        self.objects = objects.AsyncObjectsResource(self)
        self.tables = tables.AsyncTablesResource(self)
        self.refs = refs.AsyncRefsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.costs = costs.AsyncCostsResource(self)
        self.feedback = feedback.AsyncFeedbackResource(self)
        self.with_raw_response = AsyncWeaveTraceWithRawResponse(self)
        self.with_streaming_response = AsyncWeaveTraceWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class WeaveTraceWithRawResponse:
    def __init__(self, client: WeaveTrace) -> None:
        self.services = services.ServicesResourceWithRawResponse(client.services)
        self.calls = calls.CallsResourceWithRawResponse(client.calls)
        self.objects = objects.ObjectsResourceWithRawResponse(client.objects)
        self.tables = tables.TablesResourceWithRawResponse(client.tables)
        self.refs = refs.RefsResourceWithRawResponse(client.refs)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.costs = costs.CostsResourceWithRawResponse(client.costs)
        self.feedback = feedback.FeedbackResourceWithRawResponse(client.feedback)


class AsyncWeaveTraceWithRawResponse:
    def __init__(self, client: AsyncWeaveTrace) -> None:
        self.services = services.AsyncServicesResourceWithRawResponse(client.services)
        self.calls = calls.AsyncCallsResourceWithRawResponse(client.calls)
        self.objects = objects.AsyncObjectsResourceWithRawResponse(client.objects)
        self.tables = tables.AsyncTablesResourceWithRawResponse(client.tables)
        self.refs = refs.AsyncRefsResourceWithRawResponse(client.refs)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.costs = costs.AsyncCostsResourceWithRawResponse(client.costs)
        self.feedback = feedback.AsyncFeedbackResourceWithRawResponse(client.feedback)


class WeaveTraceWithStreamedResponse:
    def __init__(self, client: WeaveTrace) -> None:
        self.services = services.ServicesResourceWithStreamingResponse(client.services)
        self.calls = calls.CallsResourceWithStreamingResponse(client.calls)
        self.objects = objects.ObjectsResourceWithStreamingResponse(client.objects)
        self.tables = tables.TablesResourceWithStreamingResponse(client.tables)
        self.refs = refs.RefsResourceWithStreamingResponse(client.refs)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.costs = costs.CostsResourceWithStreamingResponse(client.costs)
        self.feedback = feedback.FeedbackResourceWithStreamingResponse(client.feedback)


class AsyncWeaveTraceWithStreamedResponse:
    def __init__(self, client: AsyncWeaveTrace) -> None:
        self.services = services.AsyncServicesResourceWithStreamingResponse(client.services)
        self.calls = calls.AsyncCallsResourceWithStreamingResponse(client.calls)
        self.objects = objects.AsyncObjectsResourceWithStreamingResponse(client.objects)
        self.tables = tables.AsyncTablesResourceWithStreamingResponse(client.tables)
        self.refs = refs.AsyncRefsResourceWithStreamingResponse(client.refs)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.costs = costs.AsyncCostsResourceWithStreamingResponse(client.costs)
        self.feedback = feedback.AsyncFeedbackResourceWithStreamingResponse(client.feedback)


Client = WeaveTrace

AsyncClient = AsyncWeaveTrace
