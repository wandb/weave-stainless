# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .shared import (
    Expr as Expr,
    Query as Query,
    Operation as Operation,
    ConvertSpec as ConvertSpec,
    EqOperation as EqOperation,
    GtOperation as GtOperation,
    InOperation as InOperation,
    OrOperation as OrOperation,
    AndOperation as AndOperation,
    ContainsSpec as ContainsSpec,
    GteOperation as GteOperation,
    NotOperation as NotOperation,
    ConvertOperation as ConvertOperation,
    GetFieldOperator as GetFieldOperator,
    LiteralOperation as LiteralOperation,
    ContainsOperation as ContainsOperation,
)
from .call_end_params import CallEndParams as CallEndParams
from .server_info_res import ServerInfoRes as ServerInfoRes
from .call_read_params import CallReadParams as CallReadParams
from .call_start_params import CallStartParams as CallStartParams
from .cost_purge_params import CostPurgeParams as CostPurgeParams
from .cost_query_params import CostQueryParams as CostQueryParams
from .call_delete_params import CallDeleteParams as CallDeleteParams
from .call_read_response import CallReadResponse as CallReadResponse
from .call_update_params import CallUpdateParams as CallUpdateParams
from .cost_create_params import CostCreateParams as CostCreateParams
from .file_create_params import FileCreateParams as FileCreateParams
from .object_read_params import ObjectReadParams as ObjectReadParams
from .table_query_params import TableQueryParams as TableQueryParams
from .call_start_response import CallStartResponse as CallStartResponse
from .cost_query_response import CostQueryResponse as CostQueryResponse
from .file_content_params import FileContentParams as FileContentParams
from .object_query_params import ObjectQueryParams as ObjectQueryParams
from .table_create_params import TableCreateParams as TableCreateParams
from .table_update_params import TableUpdateParams as TableUpdateParams
from .cost_create_response import CostCreateResponse as CostCreateResponse
from .file_create_response import FileCreateResponse as FileCreateResponse
from .object_create_params import ObjectCreateParams as ObjectCreateParams
from .object_delete_params import ObjectDeleteParams as ObjectDeleteParams
from .object_read_response import ObjectReadResponse as ObjectReadResponse
from .table_query_response import TableQueryResponse as TableQueryResponse
from .feedback_purge_params import FeedbackPurgeParams as FeedbackPurgeParams
from .feedback_query_params import FeedbackQueryParams as FeedbackQueryParams
from .object_query_response import ObjectQueryResponse as ObjectQueryResponse
from .ref_read_batch_params import RefReadBatchParams as RefReadBatchParams
from .table_create_response import TableCreateResponse as TableCreateResponse
from .table_update_response import TableUpdateResponse as TableUpdateResponse
from .feedback_create_params import FeedbackCreateParams as FeedbackCreateParams
from .object_create_response import ObjectCreateResponse as ObjectCreateResponse
from .object_delete_response import ObjectDeleteResponse as ObjectDeleteResponse
from .call_query_stats_params import CallQueryStatsParams as CallQueryStatsParams
from .feedback_query_response import FeedbackQueryResponse as FeedbackQueryResponse
from .feedback_replace_params import FeedbackReplaceParams as FeedbackReplaceParams
from .ref_read_batch_response import RefReadBatchResponse as RefReadBatchResponse
from .call_stream_query_params import CallStreamQueryParams as CallStreamQueryParams
from .call_upsert_batch_params import CallUpsertBatchParams as CallUpsertBatchParams
from .feedback_create_response import FeedbackCreateResponse as FeedbackCreateResponse
from .table_query_stats_params import TableQueryStatsParams as TableQueryStatsParams
from .call_query_stats_response import CallQueryStatsResponse as CallQueryStatsResponse
from .feedback_replace_response import FeedbackReplaceResponse as FeedbackReplaceResponse
from .call_stream_query_response import CallStreamQueryResponse as CallStreamQueryResponse
from .call_upsert_batch_response import CallUpsertBatchResponse as CallUpsertBatchResponse
from .table_query_stats_response import TableQueryStatsResponse as TableQueryStatsResponse
from .service_health_check_response import ServiceHealthCheckResponse as ServiceHealthCheckResponse

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V2:
    shared.and_operation.AndOperation.model_rebuild(_parent_namespace_depth=0)
    shared.contains_operation.ContainsOperation.model_rebuild(_parent_namespace_depth=0)
    shared.contains_spec.ContainsSpec.model_rebuild(_parent_namespace_depth=0)
    shared.convert_operation.ConvertOperation.model_rebuild(_parent_namespace_depth=0)
    shared.convert_spec.ConvertSpec.model_rebuild(_parent_namespace_depth=0)
    shared.eq_operation.EqOperation.model_rebuild(_parent_namespace_depth=0)
    shared.gt_operation.GtOperation.model_rebuild(_parent_namespace_depth=0)
    shared.gte_operation.GteOperation.model_rebuild(_parent_namespace_depth=0)
    shared.in_operation.InOperation.model_rebuild(_parent_namespace_depth=0)
    shared.literal_operation.LiteralOperation.model_rebuild(_parent_namespace_depth=0)
    shared.not_operation.NotOperation.model_rebuild(_parent_namespace_depth=0)
    shared.or_operation.OrOperation.model_rebuild(_parent_namespace_depth=0)
    shared.query.Query.model_rebuild(_parent_namespace_depth=0)
else:
    shared.and_operation.AndOperation.update_forward_refs()  # type: ignore
    shared.contains_operation.ContainsOperation.update_forward_refs()  # type: ignore
    shared.contains_spec.ContainsSpec.update_forward_refs()  # type: ignore
    shared.convert_operation.ConvertOperation.update_forward_refs()  # type: ignore
    shared.convert_spec.ConvertSpec.update_forward_refs()  # type: ignore
    shared.eq_operation.EqOperation.update_forward_refs()  # type: ignore
    shared.gt_operation.GtOperation.update_forward_refs()  # type: ignore
    shared.gte_operation.GteOperation.update_forward_refs()  # type: ignore
    shared.in_operation.InOperation.update_forward_refs()  # type: ignore
    shared.literal_operation.LiteralOperation.update_forward_refs()  # type: ignore
    shared.not_operation.NotOperation.update_forward_refs()  # type: ignore
    shared.or_operation.OrOperation.update_forward_refs()  # type: ignore
    shared.query.Query.update_forward_refs()  # type: ignore
