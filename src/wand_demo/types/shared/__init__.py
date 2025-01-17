# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .expr import Expr as Expr
from ..._compat import PYDANTIC_V2
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
    ConvertSpec.model_rebuild()
    EqOperation.model_rebuild()
    GtOperation.model_rebuild()
    InOperation.model_rebuild()
    OrOperation.model_rebuild()
    AndOperation.model_rebuild()
    ContainsOperation.model_rebuild()
    GteOperation.model_rebuild()
    NotOperation.model_rebuild()
    ConvertOperation.model_rebuild()
    LiteralOperation.model_rebuild()
    GetFieldOperator.model_rebuild()
else:
    ConvertSpec.update_forward_refs()  # type: ignore
    EqOperation.update_forward_refs()  # type: ignore
    GtOperation.update_forward_refs()  # type: ignore
    InOperation.update_forward_refs()  # type: ignore
    OrOperation.update_forward_refs()  # type: ignore
    AndOperation.update_forward_refs()  # type: ignore
    ContainsOperation.update_forward_refs()  # type: ignore
    GteOperation.update_forward_refs()  # type: ignore
    NotOperation.update_forward_refs()  # type: ignore
    ConvertOperation.update_forward_refs()  # type: ignore
    LiteralOperation.update_forward_refs()  # type: ignore
    GetFieldOperator.update_forward_refs()  # type: ignore
