# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import (
    v2_evaluation_run_list_params,
    v2_evaluation_run_create_params,
    v2_evaluation_run_finish_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.v2_evaluation_run_list_response import V2EvaluationRunListResponse
from ..types.v2_evaluation_run_read_response import V2EvaluationRunReadResponse
from ..types.v2_evaluation_run_create_response import V2EvaluationRunCreateResponse
from ..types.v2_evaluation_run_delete_response import V2EvaluationRunDeleteResponse
from ..types.v2_evaluation_run_finish_response import V2EvaluationRunFinishResponse

__all__ = ["V2EvaluationRunsResource", "AsyncV2EvaluationRunsResource"]


class V2EvaluationRunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2EvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return V2EvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2EvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return V2EvaluationRunsResourceWithStreamingResponse(self)

    def create(
        self,
        project: str,
        *,
        entity: str,
        evaluation: str,
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2EvaluationRunCreateResponse:
        """
        Create an evaluation run.

        Args:
          evaluation: Reference to the evaluation (weave:// URI)

          model: Reference to the model (weave:// URI)

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
            f"/v2/{entity}/{project}/evaluation_runs",
            body=maybe_transform(
                {
                    "evaluation": evaluation,
                    "model": model,
                },
                v2_evaluation_run_create_params.V2EvaluationRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunCreateResponse,
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
    ) -> JSONLDecoder[V2EvaluationRunListResponse]:
        """
        List evaluation runs.

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
            f"/v2/{entity}/{project}/evaluation_runs",
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
                    v2_evaluation_run_list_params.V2EvaluationRunListParams,
                ),
            ),
            cast_to=JSONLDecoder[V2EvaluationRunListResponse],
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
    ) -> V2EvaluationRunDeleteResponse:
        """
        Delete evaluation runs.

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
            f"/v2/{entity}/{project}/evaluation_runs",
            body=maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunDeleteResponse,
        )

    def finish(
        self,
        evaluation_run_id: str,
        *,
        entity: str,
        project: str,
        summary: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2EvaluationRunFinishResponse:
        """
        Finish an evaluation run.

        Args:
          summary: Optional summary dictionary for the evaluation run

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not evaluation_run_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_run_id` but received {evaluation_run_id!r}")
        return self._post(
            f"/v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}/finish",
            body=maybe_transform({"summary": summary}, v2_evaluation_run_finish_params.V2EvaluationRunFinishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunFinishResponse,
        )

    def read(
        self,
        evaluation_run_id: str,
        *,
        entity: str,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2EvaluationRunReadResponse:
        """
        Get an evaluation run.

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
        if not evaluation_run_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_run_id` but received {evaluation_run_id!r}")
        return self._get(
            f"/v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunReadResponse,
        )


class AsyncV2EvaluationRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2EvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2EvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2EvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncV2EvaluationRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        project: str,
        *,
        entity: str,
        evaluation: str,
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2EvaluationRunCreateResponse:
        """
        Create an evaluation run.

        Args:
          evaluation: Reference to the evaluation (weave:// URI)

          model: Reference to the model (weave:// URI)

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
            f"/v2/{entity}/{project}/evaluation_runs",
            body=await async_maybe_transform(
                {
                    "evaluation": evaluation,
                    "model": model,
                },
                v2_evaluation_run_create_params.V2EvaluationRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunCreateResponse,
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
    ) -> AsyncJSONLDecoder[V2EvaluationRunListResponse]:
        """
        List evaluation runs.

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
            f"/v2/{entity}/{project}/evaluation_runs",
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
                    v2_evaluation_run_list_params.V2EvaluationRunListParams,
                ),
            ),
            cast_to=AsyncJSONLDecoder[V2EvaluationRunListResponse],
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
    ) -> V2EvaluationRunDeleteResponse:
        """
        Delete evaluation runs.

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
            f"/v2/{entity}/{project}/evaluation_runs",
            body=await async_maybe_transform(body, SequenceNotStr[str]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunDeleteResponse,
        )

    async def finish(
        self,
        evaluation_run_id: str,
        *,
        entity: str,
        project: str,
        summary: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2EvaluationRunFinishResponse:
        """
        Finish an evaluation run.

        Args:
          summary: Optional summary dictionary for the evaluation run

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity:
            raise ValueError(f"Expected a non-empty value for `entity` but received {entity!r}")
        if not project:
            raise ValueError(f"Expected a non-empty value for `project` but received {project!r}")
        if not evaluation_run_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_run_id` but received {evaluation_run_id!r}")
        return await self._post(
            f"/v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}/finish",
            body=await async_maybe_transform(
                {"summary": summary}, v2_evaluation_run_finish_params.V2EvaluationRunFinishParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunFinishResponse,
        )

    async def read(
        self,
        evaluation_run_id: str,
        *,
        entity: str,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2EvaluationRunReadResponse:
        """
        Get an evaluation run.

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
        if not evaluation_run_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_run_id` but received {evaluation_run_id!r}")
        return await self._get(
            f"/v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2EvaluationRunReadResponse,
        )


class V2EvaluationRunsResourceWithRawResponse:
    def __init__(self, v2_evaluation_runs: V2EvaluationRunsResource) -> None:
        self._v2_evaluation_runs = v2_evaluation_runs

        self.create = to_raw_response_wrapper(
            v2_evaluation_runs.create,
        )
        self.list = to_raw_response_wrapper(
            v2_evaluation_runs.list,
        )
        self.delete = to_raw_response_wrapper(
            v2_evaluation_runs.delete,
        )
        self.finish = to_raw_response_wrapper(
            v2_evaluation_runs.finish,
        )
        self.read = to_raw_response_wrapper(
            v2_evaluation_runs.read,
        )


class AsyncV2EvaluationRunsResourceWithRawResponse:
    def __init__(self, v2_evaluation_runs: AsyncV2EvaluationRunsResource) -> None:
        self._v2_evaluation_runs = v2_evaluation_runs

        self.create = async_to_raw_response_wrapper(
            v2_evaluation_runs.create,
        )
        self.list = async_to_raw_response_wrapper(
            v2_evaluation_runs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v2_evaluation_runs.delete,
        )
        self.finish = async_to_raw_response_wrapper(
            v2_evaluation_runs.finish,
        )
        self.read = async_to_raw_response_wrapper(
            v2_evaluation_runs.read,
        )


class V2EvaluationRunsResourceWithStreamingResponse:
    def __init__(self, v2_evaluation_runs: V2EvaluationRunsResource) -> None:
        self._v2_evaluation_runs = v2_evaluation_runs

        self.create = to_streamed_response_wrapper(
            v2_evaluation_runs.create,
        )
        self.list = to_streamed_response_wrapper(
            v2_evaluation_runs.list,
        )
        self.delete = to_streamed_response_wrapper(
            v2_evaluation_runs.delete,
        )
        self.finish = to_streamed_response_wrapper(
            v2_evaluation_runs.finish,
        )
        self.read = to_streamed_response_wrapper(
            v2_evaluation_runs.read,
        )


class AsyncV2EvaluationRunsResourceWithStreamingResponse:
    def __init__(self, v2_evaluation_runs: AsyncV2EvaluationRunsResource) -> None:
        self._v2_evaluation_runs = v2_evaluation_runs

        self.create = async_to_streamed_response_wrapper(
            v2_evaluation_runs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v2_evaluation_runs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v2_evaluation_runs.delete,
        )
        self.finish = async_to_streamed_response_wrapper(
            v2_evaluation_runs.finish,
        )
        self.read = async_to_streamed_response_wrapper(
            v2_evaluation_runs.read,
        )
