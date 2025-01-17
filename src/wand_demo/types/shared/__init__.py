# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

# import last
from wand_demo._compat import PYDANTIC_V2

from .expr import Expr as Expr
from .query import Query as Query
from .operation import Operation as Operation
from .convert_spec import ConvertSpec as ConvertSpec
from .eq_operation import EqOperation as EqOperation
from .gt_operation import GtOperation as GtOperation
from .in_operation import InOperation as InOperation
from .or_operation import OrOperation as OrOperation
from .and_operation import AndOperation as AndOperation
from .contains_spec import ContainsSpec as ContainsSpec
from .gte_operation import GteOperation as GteOperation
from .not_operation import NotOperation as NotOperation
from .convert_operation import ConvertOperation as ConvertOperation
from .literal_operation import LiteralOperation as LiteralOperation
from .contains_operation import ContainsOperation as ContainsOperation
from .get_field_operator import GetFieldOperator as GetFieldOperator

if PYDANTIC_V2:
    AndOperation.model_rebuild(_types_namespace=locals())
    ContainsOperation.model_rebuild(_types_namespace=locals())
    ContainsSpec.model_rebuild(_types_namespace=locals())
    ConvertOperation.model_rebuild(_types_namespace=locals())
    ConvertSpec.model_rebuild(_types_namespace=locals())
    EqOperation.model_rebuild(_types_namespace=locals())
    GtOperation.model_rebuild(_types_namespace=locals())
    GteOperation.model_rebuild(_types_namespace=locals())
    InOperation.model_rebuild(_types_namespace=locals())
    NotOperation.model_rebuild(_types_namespace=locals())
    OrOperation.model_rebuild(_types_namespace=locals())
else:
    AndOperation.update_forward_refs()  # type: ignore
    ContainsOperation.update_forward_refs()  # type: ignore
    ContainsSpec.update_forward_refs()  # type: ignore
    ConvertOperation.update_forward_refs()  # type: ignore
    ConvertSpec.update_forward_refs()  # type: ignore
    EqOperation.update_forward_refs()  # type: ignore
    GtOperation.update_forward_refs()  # type: ignore
    GteOperation.update_forward_refs()  # type: ignore
    InOperation.update_forward_refs()  # type: ignore
    NotOperation.update_forward_refs()  # type: ignore
    OrOperation.update_forward_refs()  # type: ignore
