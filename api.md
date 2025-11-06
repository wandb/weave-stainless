# Shared Types

```python
from weave_server_sdk.types import (
    AndOperation,
    ContainsOperation,
    ContainsSpec,
    ConvertOperation,
    ConvertSpec,
    EqOperation,
    Expr,
    GetFieldOperator,
    GtOperation,
    GteOperation,
    InOperation,
    LiteralOperation,
    NotOperation,
    Operation,
    OrOperation,
)
```

# Services

Types:

```python
from weave_server_sdk.types import ServerInfoRes, ServiceHealthCheckResponse
```

Methods:

- <code title="get /health">client.services.<a href="./src/weave_server_sdk/resources/services.py">health_check</a>() -> <a href="./src/weave_server_sdk/types/service_health_check_response.py">ServiceHealthCheckResponse</a></code>
- <code title="get /server_info">client.services.<a href="./src/weave_server_sdk/resources/services.py">server_info</a>() -> <a href="./src/weave_server_sdk/types/server_info_res.py">ServerInfoRes</a></code>

# Calls

Types:

```python
from weave_server_sdk.types import (
    CallDeleteResponse,
    CallQueryStatsResponse,
    CallReadResponse,
    CallStartResponse,
    CallStreamQueryResponse,
    CallUpsertBatchResponse,
)
```

Methods:

- <code title="post /call/update">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">update</a>(\*\*<a href="src/weave_server_sdk/types/call_update_params.py">params</a>) -> object</code>
- <code title="post /calls/delete">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">delete</a>(\*\*<a href="src/weave_server_sdk/types/call_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_delete_response.py">CallDeleteResponse</a></code>
- <code title="post /call/end">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">end</a>(\*\*<a href="src/weave_server_sdk/types/call_end_params.py">params</a>) -> object</code>
- <code title="post /calls/query_stats">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">query_stats</a>(\*\*<a href="src/weave_server_sdk/types/call_query_stats_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_query_stats_response.py">CallQueryStatsResponse</a></code>
- <code title="post /call/read">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">read</a>(\*\*<a href="src/weave_server_sdk/types/call_read_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_read_response.py">CallReadResponse</a></code>
- <code title="post /call/start">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">start</a>(\*\*<a href="src/weave_server_sdk/types/call_start_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_start_response.py">CallStartResponse</a></code>
- <code title="post /calls/stream_query">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">stream_query</a>(\*\*<a href="src/weave_server_sdk/types/call_stream_query_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_stream_query_response.py">JSONLDecoder[CallStreamQueryResponse]</a></code>
- <code title="post /call/upsert_batch">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">upsert_batch</a>(\*\*<a href="src/weave_server_sdk/types/call_upsert_batch_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_upsert_batch_response.py">CallUpsertBatchResponse</a></code>

# Objects

Types:

```python
from weave_server_sdk.types import (
    ObjectCreateResponse,
    ObjectDeleteResponse,
    ObjectQueryResponse,
    ObjectReadResponse,
)
```

Methods:

- <code title="post /obj/create">client.objects.<a href="./src/weave_server_sdk/resources/objects.py">create</a>(\*\*<a href="src/weave_server_sdk/types/object_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/object_create_response.py">ObjectCreateResponse</a></code>
- <code title="post /obj/delete">client.objects.<a href="./src/weave_server_sdk/resources/objects.py">delete</a>(\*\*<a href="src/weave_server_sdk/types/object_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/object_delete_response.py">ObjectDeleteResponse</a></code>
- <code title="post /objs/query">client.objects.<a href="./src/weave_server_sdk/resources/objects.py">query</a>(\*\*<a href="src/weave_server_sdk/types/object_query_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/object_query_response.py">ObjectQueryResponse</a></code>
- <code title="post /obj/read">client.objects.<a href="./src/weave_server_sdk/resources/objects.py">read</a>(\*\*<a href="src/weave_server_sdk/types/object_read_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/object_read_response.py">ObjectReadResponse</a></code>

# Tables

Types:

```python
from weave_server_sdk.types import (
    TableCreateResponse,
    TableUpdateResponse,
    TableQueryResponse,
    TableQueryStatsResponse,
)
```

Methods:

- <code title="post /table/create">client.tables.<a href="./src/weave_server_sdk/resources/tables.py">create</a>(\*\*<a href="src/weave_server_sdk/types/table_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/table_create_response.py">TableCreateResponse</a></code>
- <code title="post /table/update">client.tables.<a href="./src/weave_server_sdk/resources/tables.py">update</a>(\*\*<a href="src/weave_server_sdk/types/table_update_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/table_update_response.py">TableUpdateResponse</a></code>
- <code title="post /table/query">client.tables.<a href="./src/weave_server_sdk/resources/tables.py">query</a>(\*\*<a href="src/weave_server_sdk/types/table_query_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/table_query_response.py">TableQueryResponse</a></code>
- <code title="post /table/query_stats">client.tables.<a href="./src/weave_server_sdk/resources/tables.py">query_stats</a>(\*\*<a href="src/weave_server_sdk/types/table_query_stats_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/table_query_stats_response.py">TableQueryStatsResponse</a></code>

# Refs

Types:

```python
from weave_server_sdk.types import RefReadBatchResponse
```

Methods:

- <code title="post /refs/read_batch">client.refs.<a href="./src/weave_server_sdk/resources/refs.py">read_batch</a>(\*\*<a href="src/weave_server_sdk/types/ref_read_batch_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/ref_read_batch_response.py">RefReadBatchResponse</a></code>

# Files

Types:

```python
from weave_server_sdk.types import FileCreateResponse
```

Methods:

- <code title="post /file/create">client.files.<a href="./src/weave_server_sdk/resources/files.py">create</a>(\*\*<a href="src/weave_server_sdk/types/file_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="post /file/content">client.files.<a href="./src/weave_server_sdk/resources/files.py">content</a>(\*\*<a href="src/weave_server_sdk/types/file_content_params.py">params</a>) -> BinaryAPIResponse</code>

# Costs

Types:

```python
from weave_server_sdk.types import CostCreateResponse, CostQueryResponse
```

Methods:

- <code title="post /cost/create">client.costs.<a href="./src/weave_server_sdk/resources/costs.py">create</a>(\*\*<a href="src/weave_server_sdk/types/cost_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/cost_create_response.py">CostCreateResponse</a></code>
- <code title="post /cost/purge">client.costs.<a href="./src/weave_server_sdk/resources/costs.py">purge</a>(\*\*<a href="src/weave_server_sdk/types/cost_purge_params.py">params</a>) -> object</code>
- <code title="post /cost/query">client.costs.<a href="./src/weave_server_sdk/resources/costs.py">query</a>(\*\*<a href="src/weave_server_sdk/types/cost_query_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/cost_query_response.py">CostQueryResponse</a></code>

# Feedback

Types:

```python
from weave_server_sdk.types import (
    FeedbackCreateResponse,
    FeedbackQueryResponse,
    FeedbackReplaceResponse,
)
```

Methods:

- <code title="post /feedback/create">client.feedback.<a href="./src/weave_server_sdk/resources/feedback.py">create</a>(\*\*<a href="src/weave_server_sdk/types/feedback_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/feedback_create_response.py">FeedbackCreateResponse</a></code>
- <code title="post /feedback/purge">client.feedback.<a href="./src/weave_server_sdk/resources/feedback.py">purge</a>(\*\*<a href="src/weave_server_sdk/types/feedback_purge_params.py">params</a>) -> object</code>
- <code title="post /feedback/query">client.feedback.<a href="./src/weave_server_sdk/resources/feedback.py">query</a>(\*\*<a href="src/weave_server_sdk/types/feedback_query_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/feedback_query_response.py">FeedbackQueryResponse</a></code>
- <code title="post /feedback/replace">client.feedback.<a href="./src/weave_server_sdk/resources/feedback.py">replace</a>(\*\*<a href="src/weave_server_sdk/types/feedback_replace_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/feedback_replace_response.py">FeedbackReplaceResponse</a></code>

# Otel

Types:

```python
from weave_server_sdk.types import OtelExportResponse
```

Methods:

- <code title="post /otel/v1/trace">client.otel.<a href="./src/weave_server_sdk/resources/otel.py">export</a>(\*\*<a href="src/weave_server_sdk/types/otel_export_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/otel_export_response.py">OtelExportResponse</a></code>

# Completions

Types:

```python
from weave_server_sdk.types import CompletionCreateResponse, CompletionCreateStreamResponse
```

Methods:

- <code title="post /completions/create">client.completions.<a href="./src/weave_server_sdk/resources/completions.py">create</a>(\*\*<a href="src/weave_server_sdk/types/completion_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/completion_create_response.py">CompletionCreateResponse</a></code>
- <code title="post /completions/create_stream">client.completions.<a href="./src/weave_server_sdk/resources/completions.py">create_stream</a>(\*\*<a href="src/weave_server_sdk/types/completion_create_stream_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/completion_create_stream_response.py">JSONLDecoder[CompletionCreateStreamResponse]</a></code>

# Threads

Types:

```python
from weave_server_sdk.types import ThreadStreamQueryResponse
```

Methods:

- <code title="post /threads/stream_query">client.threads.<a href="./src/weave_server_sdk/resources/threads.py">stream_query</a>(\*\*<a href="src/weave_server_sdk/types/thread_stream_query_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/thread_stream_query_response.py">JSONLDecoder[ThreadStreamQueryResponse]</a></code>

# V2

## Ops

Types:

```python
from weave_server_sdk.types.v2 import (
    OpCreateResponse,
    OpListResponse,
    OpDeleteResponse,
    OpReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/ops">client.v2.ops.<a href="./src/weave_server_sdk/resources/v2/ops.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/op_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/op_create_response.py">OpCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/ops">client.v2.ops.<a href="./src/weave_server_sdk/resources/v2/ops.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/op_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/op_list_response.py">JSONLDecoder[OpListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/ops/{object_id}">client.v2.ops.<a href="./src/weave_server_sdk/resources/v2/ops.py">delete</a>(object_id, \*, entity, project, \*\*<a href="src/weave_server_sdk/types/v2/op_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/op_delete_response.py">OpDeleteResponse</a></code>
- <code title="get /v2/{entity}/{project}/ops/{object_id}/versions/{digest}">client.v2.ops.<a href="./src/weave_server_sdk/resources/v2/ops.py">read</a>(digest, \*, entity, project, object_id) -> <a href="./src/weave_server_sdk/types/v2/op_read_response.py">OpReadResponse</a></code>

## Scorers

Types:

```python
from weave_server_sdk.types.v2 import (
    ScorerCreateResponse,
    ScorerListResponse,
    ScorerDeleteResponse,
    ScorerReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/scorers">client.v2.scorers.<a href="./src/weave_server_sdk/resources/v2/scorers.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/scorer_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/scorer_create_response.py">ScorerCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/scorers">client.v2.scorers.<a href="./src/weave_server_sdk/resources/v2/scorers.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/scorer_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/scorer_list_response.py">JSONLDecoder[ScorerListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/scorers/{object_id}">client.v2.scorers.<a href="./src/weave_server_sdk/resources/v2/scorers.py">delete</a>(object_id, \*, entity, project, \*\*<a href="src/weave_server_sdk/types/v2/scorer_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/scorer_delete_response.py">ScorerDeleteResponse</a></code>
- <code title="get /v2/{entity}/{project}/scorers/{object_id}/versions/{digest}">client.v2.scorers.<a href="./src/weave_server_sdk/resources/v2/scorers.py">read</a>(digest, \*, entity, project, object_id) -> <a href="./src/weave_server_sdk/types/v2/scorer_read_response.py">ScorerReadResponse</a></code>

## Datasets

Types:

```python
from weave_server_sdk.types.v2 import (
    DatasetCreateResponse,
    DatasetListResponse,
    DatasetDeleteResponse,
    DatasetReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/datasets">client.v2.datasets.<a href="./src/weave_server_sdk/resources/v2/datasets.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/dataset_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/dataset_create_response.py">DatasetCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/datasets">client.v2.datasets.<a href="./src/weave_server_sdk/resources/v2/datasets.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/dataset_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/dataset_list_response.py">JSONLDecoder[DatasetListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/datasets/{object_id}">client.v2.datasets.<a href="./src/weave_server_sdk/resources/v2/datasets.py">delete</a>(object_id, \*, entity, project, \*\*<a href="src/weave_server_sdk/types/v2/dataset_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/dataset_delete_response.py">DatasetDeleteResponse</a></code>
- <code title="get /v2/{entity}/{project}/datasets/{object_id}/versions/{digest}">client.v2.datasets.<a href="./src/weave_server_sdk/resources/v2/datasets.py">read</a>(digest, \*, entity, project, object_id) -> <a href="./src/weave_server_sdk/types/v2/dataset_read_response.py">DatasetReadResponse</a></code>

## Evaluations

Types:

```python
from weave_server_sdk.types.v2 import (
    EvaluationCreateResponse,
    EvaluationListResponse,
    EvaluationDeleteResponse,
    EvaluationReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/evaluations">client.v2.evaluations.<a href="./src/weave_server_sdk/resources/v2/evaluations.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/evaluation_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/evaluation_create_response.py">EvaluationCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/evaluations">client.v2.evaluations.<a href="./src/weave_server_sdk/resources/v2/evaluations.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/evaluation_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/evaluation_list_response.py">JSONLDecoder[EvaluationListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/evaluations/{object_id}">client.v2.evaluations.<a href="./src/weave_server_sdk/resources/v2/evaluations.py">delete</a>(object_id, \*, entity, project, \*\*<a href="src/weave_server_sdk/types/v2/evaluation_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/evaluation_delete_response.py">EvaluationDeleteResponse</a></code>
- <code title="get /v2/{entity}/{project}/evaluations/{object_id}/versions/{digest}">client.v2.evaluations.<a href="./src/weave_server_sdk/resources/v2/evaluations.py">read</a>(digest, \*, entity, project, object_id) -> <a href="./src/weave_server_sdk/types/v2/evaluation_read_response.py">EvaluationReadResponse</a></code>

## Models

Types:

```python
from weave_server_sdk.types.v2 import (
    ModelCreateResponse,
    ModelListResponse,
    ModelDeleteResponse,
    ModelReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/models">client.v2.models.<a href="./src/weave_server_sdk/resources/v2/models.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/model_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/model_create_response.py">ModelCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/models">client.v2.models.<a href="./src/weave_server_sdk/resources/v2/models.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/model_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/model_list_response.py">JSONLDecoder[ModelListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/models/{object_id}">client.v2.models.<a href="./src/weave_server_sdk/resources/v2/models.py">delete</a>(object_id, \*, entity, project, \*\*<a href="src/weave_server_sdk/types/v2/model_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/model_delete_response.py">ModelDeleteResponse</a></code>
- <code title="get /v2/{entity}/{project}/models/{object_id}/versions/{digest}">client.v2.models.<a href="./src/weave_server_sdk/resources/v2/models.py">read</a>(digest, \*, entity, project, object_id) -> <a href="./src/weave_server_sdk/types/v2/model_read_response.py">ModelReadResponse</a></code>

## EvaluationRuns

Types:

```python
from weave_server_sdk.types.v2 import (
    EvaluationRunCreateResponse,
    EvaluationRunListResponse,
    EvaluationRunDeleteResponse,
    EvaluationRunFinishResponse,
    EvaluationRunReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/evaluation_runs">client.v2.evaluation_runs.<a href="./src/weave_server_sdk/resources/v2/evaluation_runs.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/evaluation_run_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/evaluation_run_create_response.py">EvaluationRunCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/evaluation_runs">client.v2.evaluation_runs.<a href="./src/weave_server_sdk/resources/v2/evaluation_runs.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/evaluation_run_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/evaluation_run_list_response.py">JSONLDecoder[EvaluationRunListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/evaluation_runs">client.v2.evaluation_runs.<a href="./src/weave_server_sdk/resources/v2/evaluation_runs.py">delete</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/evaluation_run_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/evaluation_run_delete_response.py">EvaluationRunDeleteResponse</a></code>
- <code title="post /v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}/finish">client.v2.evaluation_runs.<a href="./src/weave_server_sdk/resources/v2/evaluation_runs.py">finish</a>(evaluation_run_id, \*, entity, project, \*\*<a href="src/weave_server_sdk/types/v2/evaluation_run_finish_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/evaluation_run_finish_response.py">EvaluationRunFinishResponse</a></code>
- <code title="get /v2/{entity}/{project}/evaluation_runs/{evaluation_run_id}">client.v2.evaluation_runs.<a href="./src/weave_server_sdk/resources/v2/evaluation_runs.py">read</a>(evaluation_run_id, \*, entity, project) -> <a href="./src/weave_server_sdk/types/v2/evaluation_run_read_response.py">EvaluationRunReadResponse</a></code>

## Predictions

Types:

```python
from weave_server_sdk.types.v2 import (
    PredictionCreateResponse,
    PredictionListResponse,
    PredictionDeleteResponse,
    PredictionFinishResponse,
    PredictionReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/predictions">client.v2.predictions.<a href="./src/weave_server_sdk/resources/v2/predictions.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/prediction_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/prediction_create_response.py">PredictionCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/predictions">client.v2.predictions.<a href="./src/weave_server_sdk/resources/v2/predictions.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/prediction_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/prediction_list_response.py">JSONLDecoder[PredictionListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/predictions">client.v2.predictions.<a href="./src/weave_server_sdk/resources/v2/predictions.py">delete</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/prediction_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/prediction_delete_response.py">PredictionDeleteResponse</a></code>
- <code title="post /v2/{entity}/{project}/predictions/{prediction_id}/finish">client.v2.predictions.<a href="./src/weave_server_sdk/resources/v2/predictions.py">finish</a>(prediction_id, \*, entity, project) -> <a href="./src/weave_server_sdk/types/v2/prediction_finish_response.py">PredictionFinishResponse</a></code>
- <code title="get /v2/{entity}/{project}/predictions/{prediction_id}">client.v2.predictions.<a href="./src/weave_server_sdk/resources/v2/predictions.py">read</a>(prediction_id, \*, entity, project) -> <a href="./src/weave_server_sdk/types/v2/prediction_read_response.py">PredictionReadResponse</a></code>

## Scores

Types:

```python
from weave_server_sdk.types.v2 import (
    ScoreCreateResponse,
    ScoreListResponse,
    ScoreDeleteResponse,
    ScoreReadResponse,
)
```

Methods:

- <code title="post /v2/{entity}/{project}/scores">client.v2.scores.<a href="./src/weave_server_sdk/resources/v2/scores.py">create</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/score_create_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/score_create_response.py">ScoreCreateResponse</a></code>
- <code title="get /v2/{entity}/{project}/scores">client.v2.scores.<a href="./src/weave_server_sdk/resources/v2/scores.py">list</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/score_list_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/score_list_response.py">JSONLDecoder[ScoreListResponse]</a></code>
- <code title="delete /v2/{entity}/{project}/scores">client.v2.scores.<a href="./src/weave_server_sdk/resources/v2/scores.py">delete</a>(project, \*, entity, \*\*<a href="src/weave_server_sdk/types/v2/score_delete_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/v2/score_delete_response.py">ScoreDeleteResponse</a></code>
- <code title="get /v2/{entity}/{project}/scores/{score_id}">client.v2.scores.<a href="./src/weave_server_sdk/resources/v2/scores.py">read</a>(score_id, \*, entity, project) -> <a href="./src/weave_server_sdk/types/v2/score_read_response.py">ScoreReadResponse</a></code>
