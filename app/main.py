from __future__ import annotations
from numbers import Real


class Distance:
    def __init__(self, km: Real) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        km_value = (
            int(self.km)
            if self.km.is_integer()
            else self.km
        )
        return f"Distance(km={km_value})"

    @staticmethod
    def _as_km(other: object) -> float | NotImplemented:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, Real):
            return float(other)
        return NotImplemented

    def __add__(self, other: object) -> Distance:
        km = self._as_km(other)
        if km is NotImplemented:
            return NotImplemented
