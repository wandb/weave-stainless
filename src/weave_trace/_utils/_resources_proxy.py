from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `weave_trace.resources` module.

    This is used so that we can lazily import `weave_trace.resources` only when
    needed *and* so that users can just import `weave_trace` and reference `weave_trace.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("weave_trace.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
