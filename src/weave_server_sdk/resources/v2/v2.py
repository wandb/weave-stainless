# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ops import (
    OpsResource,
    AsyncOpsResource,
    OpsResourceWithRawResponse,
    AsyncOpsResourceWithRawResponse,
    OpsResourceWithStreamingResponse,
    AsyncOpsResourceWithStreamingResponse,
)
from .models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from .scores import (
    ScoresResource,
    AsyncScoresResource,
    ScoresResourceWithRawResponse,
    AsyncScoresResourceWithRawResponse,
    ScoresResourceWithStreamingResponse,
    AsyncScoresResourceWithStreamingResponse,
)
from .scorers import (
    ScorersResource,
    AsyncScorersResource,
    ScorersResourceWithRawResponse,
    AsyncScorersResourceWithRawResponse,
    ScorersResourceWithStreamingResponse,
    AsyncScorersResourceWithStreamingResponse,
)
from .datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .evaluations import (
    EvaluationsResource,
    AsyncEvaluationsResource,
    EvaluationsResourceWithRawResponse,
    AsyncEvaluationsResourceWithRawResponse,
    EvaluationsResourceWithStreamingResponse,
    AsyncEvaluationsResourceWithStreamingResponse,
)
from .predictions import (
    PredictionsResource,
    AsyncPredictionsResource,
    PredictionsResourceWithRawResponse,
    AsyncPredictionsResourceWithRawResponse,
    PredictionsResourceWithStreamingResponse,
    AsyncPredictionsResourceWithStreamingResponse,
)
from .evaluation_runs import (
    EvaluationRunsResource,
    AsyncEvaluationRunsResource,
    EvaluationRunsResourceWithRawResponse,
    AsyncEvaluationRunsResourceWithRawResponse,
    EvaluationRunsResourceWithStreamingResponse,
    AsyncEvaluationRunsResourceWithStreamingResponse,
)

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def ops(self) -> OpsResource:
        return OpsResource(self._client)

    @cached_property
    def scorers(self) -> ScorersResource:
        return ScorersResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def evaluations(self) -> EvaluationsResource:
        return EvaluationsResource(self._client)

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResource:
        return EvaluationRunsResource(self._client)

    @cached_property
    def predictions(self) -> PredictionsResource:
        return PredictionsResource(self._client)

    @cached_property
    def scores(self) -> ScoresResource:
        return ScoresResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def ops(self) -> AsyncOpsResource:
        return AsyncOpsResource(self._client)

    @cached_property
    def scorers(self) -> AsyncScorersResource:
        return AsyncScorersResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResource:
        return AsyncEvaluationsResource(self._client)

    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResource:
        return AsyncEvaluationRunsResource(self._client)

    @cached_property
    def predictions(self) -> AsyncPredictionsResource:
        return AsyncPredictionsResource(self._client)

    @cached_property
    def scores(self) -> AsyncScoresResource:
        return AsyncScoresResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/weave-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/weave-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def ops(self) -> OpsResourceWithRawResponse:
        return OpsResourceWithRawResponse(self._v2.ops)

    @cached_property
    def scorers(self) -> ScorersResourceWithRawResponse:
        return ScorersResourceWithRawResponse(self._v2.scorers)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._v2.datasets)

    @cached_property
    def evaluations(self) -> EvaluationsResourceWithRawResponse:
        return EvaluationsResourceWithRawResponse(self._v2.evaluations)

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._v2.models)

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResourceWithRawResponse:
        return EvaluationRunsResourceWithRawResponse(self._v2.evaluation_runs)

    @cached_property
    def predictions(self) -> PredictionsResourceWithRawResponse:
        return PredictionsResourceWithRawResponse(self._v2.predictions)

    @cached_property
    def scores(self) -> ScoresResourceWithRawResponse:
        return ScoresResourceWithRawResponse(self._v2.scores)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def ops(self) -> AsyncOpsResourceWithRawResponse:
        return AsyncOpsResourceWithRawResponse(self._v2.ops)

    @cached_property
    def scorers(self) -> AsyncScorersResourceWithRawResponse:
        return AsyncScorersResourceWithRawResponse(self._v2.scorers)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._v2.datasets)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResourceWithRawResponse:
        return AsyncEvaluationsResourceWithRawResponse(self._v2.evaluations)

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._v2.models)

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResourceWithRawResponse:
        return AsyncEvaluationRunsResourceWithRawResponse(self._v2.evaluation_runs)

    @cached_property
    def predictions(self) -> AsyncPredictionsResourceWithRawResponse:
        return AsyncPredictionsResourceWithRawResponse(self._v2.predictions)

    @cached_property
    def scores(self) -> AsyncScoresResourceWithRawResponse:
        return AsyncScoresResourceWithRawResponse(self._v2.scores)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def ops(self) -> OpsResourceWithStreamingResponse:
        return OpsResourceWithStreamingResponse(self._v2.ops)

    @cached_property
    def scorers(self) -> ScorersResourceWithStreamingResponse:
        return ScorersResourceWithStreamingResponse(self._v2.scorers)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._v2.datasets)

    @cached_property
    def evaluations(self) -> EvaluationsResourceWithStreamingResponse:
        return EvaluationsResourceWithStreamingResponse(self._v2.evaluations)

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._v2.models)

    @cached_property
    def evaluation_runs(self) -> EvaluationRunsResourceWithStreamingResponse:
        return EvaluationRunsResourceWithStreamingResponse(self._v2.evaluation_runs)

    @cached_property
    def predictions(self) -> PredictionsResourceWithStreamingResponse:
        return PredictionsResourceWithStreamingResponse(self._v2.predictions)

    @cached_property
    def scores(self) -> ScoresResourceWithStreamingResponse:
        return ScoresResourceWithStreamingResponse(self._v2.scores)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def ops(self) -> AsyncOpsResourceWithStreamingResponse:
        return AsyncOpsResourceWithStreamingResponse(self._v2.ops)

    @cached_property
    def scorers(self) -> AsyncScorersResourceWithStreamingResponse:
        return AsyncScorersResourceWithStreamingResponse(self._v2.scorers)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._v2.datasets)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        return AsyncEvaluationsResourceWithStreamingResponse(self._v2.evaluations)

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._v2.models)

    @cached_property
    def evaluation_runs(self) -> AsyncEvaluationRunsResourceWithStreamingResponse:
        return AsyncEvaluationRunsResourceWithStreamingResponse(self._v2.evaluation_runs)

    @cached_property
    def predictions(self) -> AsyncPredictionsResourceWithStreamingResponse:
        return AsyncPredictionsResourceWithStreamingResponse(self._v2.predictions)

    @cached_property
    def scores(self) -> AsyncScoresResourceWithStreamingResponse:
        return AsyncScoresResourceWithStreamingResponse(self._v2.scores)
