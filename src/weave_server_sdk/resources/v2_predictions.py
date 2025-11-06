# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import v2_prediction_list_params, v2_prediction_create_params
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
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.v2_prediction_list_response import V2PredictionListResponse
from ..types.v2_prediction_create_response import V2PredictionCreateResponse
from ..types.v2_prediction_finish_response import V2PredictionFinishResponse

__all__ = ["V2PredictionsResource", "AsyncV2PredictionsResource"]


class V2PredictionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2PredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return V2PredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2PredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return V2PredictionsResourceWithStreamingResponse(self)

    def create(
        self,
        project: str,
        *,
        entity: str,
        inputs: Dict[str, object],
        model: str,
        output: object,
        evaluation_run_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2PredictionCreateResponse:
        """
        Create a prediction.

        Args:
          inputs: The inputs to the prediction

          model: The model reference (weave:// URI)

          output: The output of the prediction

          evaluation_run_id: Optional evaluation run ID to link this prediction as a child call

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
            f"/v2/{entity}/{project}/predictions",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "model": model,
                    "output": output,
                    "evaluation_run_id": evaluation_run_id,
                },
                v2_prediction_create_params.V2PredictionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2PredictionCreateResponse,
        )

    def list(
        self,
        project: str,
        *,
        entity: str,
        evaluation_run_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JSONLDecoder[V2PredictionListResponse]:
        """
        List predictions.

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
            f"/v2/{entity}/{project}/predictions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "evaluation_run_id": evaluation_run_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    v2_prediction_list_params.V2PredictionListParams,
                ),
            ),
            cast_to=JSONLDecoder[V2PredictionListResponse],
            stream=True,
        )

    def finish(
        self,
        prediction_id: str,
        *,
        entity: str,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2PredictionFinishResponse:
        """
        Finish a prediction.

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
        if not prediction_id:
            raise ValueError(f"Expected a non-empty value for `prediction_id` but received {prediction_id!r}")
        return self._post(
            f"/v2/{entity}/{project}/predictions/{prediction_id}/finish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2PredictionFinishResponse,
        )


class AsyncV2PredictionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2PredictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2PredictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2PredictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncV2PredictionsResourceWithStreamingResponse(self)

    async def create(
        self,
        project: str,
        *,
        entity: str,
        inputs: Dict[str, object],
        model: str,
        output: object,
        evaluation_run_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2PredictionCreateResponse:
        """
        Create a prediction.

        Args:
          inputs: The inputs to the prediction

          model: The model reference (weave:// URI)

          output: The output of the prediction

          evaluation_run_id: Optional evaluation run ID to link this prediction as a child call

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
            f"/v2/{entity}/{project}/predictions",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "model": model,
                    "output": output,
                    "evaluation_run_id": evaluation_run_id,
                },
                v2_prediction_create_params.V2PredictionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2PredictionCreateResponse,
        )

    async def list(
        self,
        project: str,
        *,
        entity: str,
        evaluation_run_id: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncJSONLDecoder[V2PredictionListResponse]:
        """
        List predictions.

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
            f"/v2/{entity}/{project}/predictions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "evaluation_run_id": evaluation_run_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    v2_prediction_list_params.V2PredictionListParams,
                ),
            ),
            cast_to=AsyncJSONLDecoder[V2PredictionListResponse],
            stream=True,
        )

    async def finish(
        self,
        prediction_id: str,
        *,
        entity: str,
        project: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2PredictionFinishResponse:
        """
        Finish a prediction.

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
        if not prediction_id:
            raise ValueError(f"Expected a non-empty value for `prediction_id` but received {prediction_id!r}")
        return await self._post(
            f"/v2/{entity}/{project}/predictions/{prediction_id}/finish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2PredictionFinishResponse,
        )


class V2PredictionsResourceWithRawResponse:
    def __init__(self, v2_predictions: V2PredictionsResource) -> None:
        self._v2_predictions = v2_predictions

        self.create = to_raw_response_wrapper(
            v2_predictions.create,
        )
        self.list = to_raw_response_wrapper(
            v2_predictions.list,
        )
        self.finish = to_raw_response_wrapper(
            v2_predictions.finish,
        )


class AsyncV2PredictionsResourceWithRawResponse:
    def __init__(self, v2_predictions: AsyncV2PredictionsResource) -> None:
        self._v2_predictions = v2_predictions

        self.create = async_to_raw_response_wrapper(
            v2_predictions.create,
        )
        self.list = async_to_raw_response_wrapper(
            v2_predictions.list,
        )
        self.finish = async_to_raw_response_wrapper(
            v2_predictions.finish,
        )


class V2PredictionsResourceWithStreamingResponse:
    def __init__(self, v2_predictions: V2PredictionsResource) -> None:
        self._v2_predictions = v2_predictions

        self.create = to_streamed_response_wrapper(
            v2_predictions.create,
        )
        self.list = to_streamed_response_wrapper(
            v2_predictions.list,
        )
        self.finish = to_streamed_response_wrapper(
            v2_predictions.finish,
        )


class AsyncV2PredictionsResourceWithStreamingResponse:
    def __init__(self, v2_predictions: AsyncV2PredictionsResource) -> None:
        self._v2_predictions = v2_predictions

        self.create = async_to_streamed_response_wrapper(
            v2_predictions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v2_predictions.list,
        )
        self.finish = async_to_streamed_response_wrapper(
            v2_predictions.finish,
        )
