"""
Space Station Data Validation using Pydantic.
"""

from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Pydantic model for space station data validation."""

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    # Create a valid space station
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T10:30:00",
            is_operational=True,
            notes="All systems nominal"
        )

        print("Valid station created:")
        print(f"    ID: {station.station_id}")
        print(f"    Name: {station.name}")
        print(f"    Crew: {station.crew_size} people")
        print(f"    Power: {station.power_level}%")
        print(f"    Oxygen: {station.oxygen_level}%")
        print(
            "    Status:",
            f"{'Operational' if station.is_operational else 'Offline'}"
            )

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 40)

    # Try to create an invalid station
    print("Testing invalid data (crew_size=50):")
    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Test Station",
            crew_size=50,  # Invalid! Max is 20
            power_level=75.0,
            oxygen_level=88.0,
            last_maintenance="2024-01-15"
        )
        print(invalid_station)
    except ValidationError as e:
        print("    Expected validation error:")
        for error in e.errors():
            print(f"    - {error['msg']}")


if __name__ == "__main__":
    main()
