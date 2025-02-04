# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["TableCreateParams", "Table"]


class TableCreateParams(TypedDict, total=False):
    table: Required[Table]


class Table(TypedDict, total=False):
    project_id: Required[str]

    rows: Required[Iterable[object]]
