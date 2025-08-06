# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ServiceGeolocateResponse", "Location"]


class Location(BaseModel):
    country_code: str
    """2-letter country code in ISO 3166-1 Alpha 2 format"""

    file_index: int
    """row in CSV file"""

    range_end_int: int
    """End of IP range as integer"""

    range_end_ip: str
    """End of IP range in dotted decimal notation"""

    range_start_int: int
    """Start of IP range as integer"""

    range_start_ip: str
    """Start of IP range in dotted decimal notation"""

    country_name: Optional[str] = None
    """Country name, None if could not be determined"""


class ServiceGeolocateResponse(BaseModel):
    ip: str
    """Resolved IP address, useful for debugging"""

    allowed: Optional[bool] = None
    """Whether the IP address is allowed to be used for inference."""

    location: Optional[Location] = None
    """
    Information about the location of the IP address, None if could not be
    determined
    """
