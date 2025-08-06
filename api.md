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
from weave_server_sdk.types import ServerInfoRes
```

Methods:

- <code title="get /health">client.services.<a href="./src/weave_server_sdk/resources/services.py">health_check</a>() -> object</code>
- <code title="get /server_info">client.services.<a href="./src/weave_server_sdk/resources/services.py">server_info</a>() -> <a href="./src/weave_server_sdk/types/server_info_res.py">ServerInfoRes</a></code>

# Calls

Types:

```python
from weave_server_sdk.types import (
    CallQueryStatsResponse,
    CallReadResponse,
    CallStartResponse,
    CallUpsertBatchResponse,
)
```

Methods:

- <code title="post /call/update">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">update</a>(\*\*<a href="src/weave_server_sdk/types/call_update_params.py">params</a>) -> object</code>
- <code title="post /calls/delete">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">delete</a>(\*\*<a href="src/weave_server_sdk/types/call_delete_params.py">params</a>) -> object</code>
- <code title="post /call/end">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">end</a>(\*\*<a href="src/weave_server_sdk/types/call_end_params.py">params</a>) -> object</code>
- <code title="post /calls/query_stats">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">query_stats</a>(\*\*<a href="src/weave_server_sdk/types/call_query_stats_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_query_stats_response.py">CallQueryStatsResponse</a></code>
- <code title="post /call/read">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">read</a>(\*\*<a href="src/weave_server_sdk/types/call_read_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_read_response.py">CallReadResponse</a></code>
- <code title="post /call/start">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">start</a>(\*\*<a href="src/weave_server_sdk/types/call_start_params.py">params</a>) -> <a href="./src/weave_server_sdk/types/call_start_response.py">CallStartResponse</a></code>
- <code title="post /calls/stream_query">client.calls.<a href="./src/weave_server_sdk/resources/calls.py">stream_query</a>(\*\*<a href="src/weave_server_sdk/types/call_stream_query_params.py">params</a>) -> JSONLDecoder[object]</code>
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
- <code title="post /file/content">client.files.<a href="./src/weave_server_sdk/resources/files.py">content</a>(\*\*<a href="src/weave_server_sdk/types/file_content_params.py">params</a>) -> object</code>

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
