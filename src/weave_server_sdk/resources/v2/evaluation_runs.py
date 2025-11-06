# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import (
    evaluation_run_list_params,
    evaluation_run_create_params,
    evaluation_run_finish_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ..._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ...types.v2.evaluation_run_list_response import EvaluationRunListResponse
from ...types.v2.evaluation_run_read_response import EvaluationRunReadResponse
from ...types.v2.evaluation_run_create_response import EvaluationRunCreateResponse
from ...types.v2.evaluation_run_delete_response import EvaluationRunDeleteResponse
from ...types.v2.evaluation_run_finish_response import EvaluationRunFinishResponse

__all__ = ["EvaluationRunsResource", "AsyncEvaluationRunsResource"]


class EvaluationRunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return EvaluationRunsResourceWithStreamingResponse(self)

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
    ) -> EvaluationRunCreateResponse:
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
                evaluation_run_create_params.EvaluationRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunCreateResponse,
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
    ) -> JSONLDecoder[EvaluationRunListResponse]:
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
                    evaluation_run_list_params.EvaluationRunListParams,
                ),
            ),
            cast_to=JSONLDecoder[EvaluationRunListResponse],
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
    ) -> EvaluationRunDeleteResponse:
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
            cast_to=EvaluationRunDeleteResponse,
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
    ) -> EvaluationRunFinishResponse:
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
            body=maybe_transform({"summary": summary}, evaluation_run_finish_params.EvaluationRunFinishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunFinishResponse,
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
    ) -> EvaluationRunReadResponse:
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
            cast_to=EvaluationRunReadResponse,
        )


class AsyncEvaluationRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncEvaluationRunsResourceWithStreamingResponse(self)

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
    ) -> EvaluationRunCreateResponse:
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
                evaluation_run_create_params.EvaluationRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunCreateResponse,
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
    ) -> AsyncJSONLDecoder[EvaluationRunListResponse]:
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
                    evaluation_run_list_params.EvaluationRunListParams,
                ),
            ),
            cast_to=AsyncJSONLDecoder[EvaluationRunListResponse],
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
    ) -> EvaluationRunDeleteResponse:
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
            cast_to=EvaluationRunDeleteResponse,
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
    ) -> EvaluationRunFinishResponse:
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
                {"summary": summary}, evaluation_run_finish_params.EvaluationRunFinishParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationRunFinishResponse,
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
    ) -> EvaluationRunReadResponse:
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
            cast_to=EvaluationRunReadResponse,
        )


class EvaluationRunsResourceWithRawResponse:
    def __init__(self, evaluation_runs: EvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = to_raw_response_wrapper(
            evaluation_runs.create,
        )
        self.list = to_raw_response_wrapper(
            evaluation_runs.list,
        )
        self.delete = to_raw_response_wrapper(
            evaluation_runs.delete,
        )
        self.finish = to_raw_response_wrapper(
            evaluation_runs.finish,
        )
        self.read = to_raw_response_wrapper(
            evaluation_runs.read,
        )


class AsyncEvaluationRunsResourceWithRawResponse:
    def __init__(self, evaluation_runs: AsyncEvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = async_to_raw_response_wrapper(
            evaluation_runs.create,
        )
        self.list = async_to_raw_response_wrapper(
            evaluation_runs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evaluation_runs.delete,
        )
        self.finish = async_to_raw_response_wrapper(
            evaluation_runs.finish,
        )
        self.read = async_to_raw_response_wrapper(
            evaluation_runs.read,
        )


class EvaluationRunsResourceWithStreamingResponse:
    def __init__(self, evaluation_runs: EvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = to_streamed_response_wrapper(
            evaluation_runs.create,
        )
        self.list = to_streamed_response_wrapper(
            evaluation_runs.list,
        )
        self.delete = to_streamed_response_wrapper(
            evaluation_runs.delete,
        )
        self.finish = to_streamed_response_wrapper(
            evaluation_runs.finish,
        )
        self.read = to_streamed_response_wrapper(
            evaluation_runs.read,
        )


class AsyncEvaluationRunsResourceWithStreamingResponse:
    def __init__(self, evaluation_runs: AsyncEvaluationRunsResource) -> None:
        self._evaluation_runs = evaluation_runs

        self.create = async_to_streamed_response_wrapper(
            evaluation_runs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluation_runs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evaluation_runs.delete,
        )
        self.finish = async_to_streamed_response_wrapper(
            evaluation_runs.finish,
        )
        self.read = async_to_streamed_response_wrapper(
            evaluation_runs.read,
        )
