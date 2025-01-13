# Shared Types

```python
from wand_demo.types import (
    AndOperation,
    ContainsOperation,
    EqOperation,
    GetFieldOperator,
    GtOperation,
    GteOperation,
    InOperation,
    LiteralOperation,
    NotOperation,
    OrOperation,
)
```

# Services

Types:

```python
from wand_demo.types import ServerInfoRes, ServiceHealthCheckResponse
```

Methods:

- <code title="get /health">client.services.<a href="./src/wand_demo/resources/services.py">health_check</a>() -> <a href="./src/wand_demo/types/service_health_check_response.py">object</a></code>
- <code title="get /server_info">client.services.<a href="./src/wand_demo/resources/services.py">server_info</a>() -> <a href="./src/wand_demo/types/server_info_res.py">ServerInfoRes</a></code>

# Calls

Types:

```python
from wand_demo.types import (
    CallUpdateResponse,
    CallDeleteResponse,
    CallEndResponse,
    CallQueryStatsResponse,
    CallReadResponse,
    CallStartResponse,
    CallStreamQueryResponse,
    CallUpsertBatchResponse,
)
```

Methods:

- <code title="post /call/update">client.calls.<a href="./src/wand_demo/resources/calls.py">update</a>(\*\*<a href="src/wand_demo/types/call_update_params.py">params</a>) -> <a href="./src/wand_demo/types/call_update_response.py">object</a></code>
- <code title="post /calls/delete">client.calls.<a href="./src/wand_demo/resources/calls.py">delete</a>(\*\*<a href="src/wand_demo/types/call_delete_params.py">params</a>) -> <a href="./src/wand_demo/types/call_delete_response.py">object</a></code>
- <code title="post /call/end">client.calls.<a href="./src/wand_demo/resources/calls.py">end</a>(\*\*<a href="src/wand_demo/types/call_end_params.py">params</a>) -> <a href="./src/wand_demo/types/call_end_response.py">object</a></code>
- <code title="post /calls/query_stats">client.calls.<a href="./src/wand_demo/resources/calls.py">query_stats</a>(\*\*<a href="src/wand_demo/types/call_query_stats_params.py">params</a>) -> <a href="./src/wand_demo/types/call_query_stats_response.py">CallQueryStatsResponse</a></code>
- <code title="post /call/read">client.calls.<a href="./src/wand_demo/resources/calls.py">read</a>(\*\*<a href="src/wand_demo/types/call_read_params.py">params</a>) -> <a href="./src/wand_demo/types/call_read_response.py">CallReadResponse</a></code>
- <code title="post /call/start">client.calls.<a href="./src/wand_demo/resources/calls.py">start</a>(\*\*<a href="src/wand_demo/types/call_start_params.py">params</a>) -> <a href="./src/wand_demo/types/call_start_response.py">CallStartResponse</a></code>
- <code title="post /calls/stream_query">client.calls.<a href="./src/wand_demo/resources/calls.py">stream_query</a>(\*\*<a href="src/wand_demo/types/call_stream_query_params.py">params</a>) -> <a href="./src/wand_demo/types/call_stream_query_response.py">object</a></code>
- <code title="post /call/upsert_batch">client.calls.<a href="./src/wand_demo/resources/calls.py">upsert_batch</a>(\*\*<a href="src/wand_demo/types/call_upsert_batch_params.py">params</a>) -> <a href="./src/wand_demo/types/call_upsert_batch_response.py">CallUpsertBatchResponse</a></code>

# Objects

Types:

```python
from wand_demo.types import ObjectCreateResponse, ObjectQueryResponse, ObjectReadResponse
```

Methods:

- <code title="post /obj/create">client.objects.<a href="./src/wand_demo/resources/objects.py">create</a>(\*\*<a href="src/wand_demo/types/object_create_params.py">params</a>) -> <a href="./src/wand_demo/types/object_create_response.py">ObjectCreateResponse</a></code>
- <code title="post /objs/query">client.objects.<a href="./src/wand_demo/resources/objects.py">query</a>(\*\*<a href="src/wand_demo/types/object_query_params.py">params</a>) -> <a href="./src/wand_demo/types/object_query_response.py">ObjectQueryResponse</a></code>
- <code title="post /obj/read">client.objects.<a href="./src/wand_demo/resources/objects.py">read</a>(\*\*<a href="src/wand_demo/types/object_read_params.py">params</a>) -> <a href="./src/wand_demo/types/object_read_response.py">ObjectReadResponse</a></code>

# Tables

Types:

```python
from wand_demo.types import (
    TableCreateResponse,
    TableUpdateResponse,
    TableQueryResponse,
    TableQueryStatsResponse,
)
```

Methods:

- <code title="post /table/create">client.tables.<a href="./src/wand_demo/resources/tables.py">create</a>(\*\*<a href="src/wand_demo/types/table_create_params.py">params</a>) -> <a href="./src/wand_demo/types/table_create_response.py">TableCreateResponse</a></code>
- <code title="post /table/update">client.tables.<a href="./src/wand_demo/resources/tables.py">update</a>(\*\*<a href="src/wand_demo/types/table_update_params.py">params</a>) -> <a href="./src/wand_demo/types/table_update_response.py">TableUpdateResponse</a></code>
- <code title="post /table/query">client.tables.<a href="./src/wand_demo/resources/tables.py">query</a>(\*\*<a href="src/wand_demo/types/table_query_params.py">params</a>) -> <a href="./src/wand_demo/types/table_query_response.py">TableQueryResponse</a></code>
- <code title="post /table/query_stats">client.tables.<a href="./src/wand_demo/resources/tables.py">query_stats</a>(\*\*<a href="src/wand_demo/types/table_query_stats_params.py">params</a>) -> <a href="./src/wand_demo/types/table_query_stats_response.py">TableQueryStatsResponse</a></code>

# Refs

Types:

```python
from wand_demo.types import RefReadBatchResponse
```

Methods:

- <code title="post /refs/read_batch">client.refs.<a href="./src/wand_demo/resources/refs.py">read_batch</a>(\*\*<a href="src/wand_demo/types/ref_read_batch_params.py">params</a>) -> <a href="./src/wand_demo/types/ref_read_batch_response.py">RefReadBatchResponse</a></code>

# Files

Types:

```python
from wand_demo.types import FileCreateResponse, FileContentResponse
```

Methods:

- <code title="post /file/create">client.files.<a href="./src/wand_demo/resources/files.py">create</a>(\*\*<a href="src/wand_demo/types/file_create_params.py">params</a>) -> <a href="./src/wand_demo/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="post /file/content">client.files.<a href="./src/wand_demo/resources/files.py">content</a>(\*\*<a href="src/wand_demo/types/file_content_params.py">params</a>) -> <a href="./src/wand_demo/types/file_content_response.py">object</a></code>

# Costs

Types:

```python
from wand_demo.types import CostCreateResponse, CostPurgeResponse, CostQueryResponse
```

Methods:

- <code title="post /cost/create">client.costs.<a href="./src/wand_demo/resources/costs.py">create</a>(\*\*<a href="src/wand_demo/types/cost_create_params.py">params</a>) -> <a href="./src/wand_demo/types/cost_create_response.py">CostCreateResponse</a></code>
- <code title="post /cost/purge">client.costs.<a href="./src/wand_demo/resources/costs.py">purge</a>(\*\*<a href="src/wand_demo/types/cost_purge_params.py">params</a>) -> <a href="./src/wand_demo/types/cost_purge_response.py">object</a></code>
- <code title="post /cost/query">client.costs.<a href="./src/wand_demo/resources/costs.py">query</a>(\*\*<a href="src/wand_demo/types/cost_query_params.py">params</a>) -> <a href="./src/wand_demo/types/cost_query_response.py">CostQueryResponse</a></code>

# Feedback

Types:

```python
from wand_demo.types import (
    FeedbackCreateResponse,
    FeedbackPurgeResponse,
    FeedbackQueryResponse,
    FeedbackReplaceResponse,
)
```

Methods:

- <code title="post /feedback/create">client.feedback.<a href="./src/wand_demo/resources/feedback.py">create</a>(\*\*<a href="src/wand_demo/types/feedback_create_params.py">params</a>) -> <a href="./src/wand_demo/types/feedback_create_response.py">FeedbackCreateResponse</a></code>
- <code title="post /feedback/purge">client.feedback.<a href="./src/wand_demo/resources/feedback.py">purge</a>(\*\*<a href="src/wand_demo/types/feedback_purge_params.py">params</a>) -> <a href="./src/wand_demo/types/feedback_purge_response.py">object</a></code>
- <code title="post /feedback/query">client.feedback.<a href="./src/wand_demo/resources/feedback.py">query</a>(\*\*<a href="src/wand_demo/types/feedback_query_params.py">params</a>) -> <a href="./src/wand_demo/types/feedback_query_response.py">FeedbackQueryResponse</a></code>
- <code title="post /feedback/replace">client.feedback.<a href="./src/wand_demo/resources/feedback.py">replace</a>(\*\*<a href="src/wand_demo/types/feedback_replace_params.py">params</a>) -> <a href="./src/wand_demo/types/feedback_replace_response.py">FeedbackReplaceResponse</a></code>
