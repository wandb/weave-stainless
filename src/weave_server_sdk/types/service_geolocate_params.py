# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ServiceGeolocateParams"]


class ServiceGeolocateParams(TypedDict, total=False):
    ip: Optional[str]
    """IP address to geolocate, defaults to client IP address"""
