"""
Space Crew Management using Pydantic with nested models.
"""

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Crew member ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Pydantic model for individual crew members."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Pydantic model for space missions with crew validation."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self):
        """Custom validation rules for space missions."""

        # Rule 1: Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Rule 2: Must have at least one Commander or Captain
        has_leader = False
        for member in self.crew:
            if member.rank in [Rank.commander, Rank.captain]:
                has_leader = True
                break

        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        # Rule 3: Long missions (> 365 days) need 50% experienced crew (5+ y)
        if self.duration_days > 365:
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1

            required_experienced = len(self.crew) / 2
            if experienced_count < required_experienced:
                raise ValueError(
                    "Long missions (> 365 days)"
                    + " require at least 50% experienced crew. "
                    f"Found {experienced_count}/{len(self.crew)}"
                    + " experienced members."
                )

        # Rule 4: All crew members must be active
        for member in self.crew:
            if not member.is_active:
                raise ValueError(
                 f"All crew members must be active. {member.name} is inactive."
                )

        return self


def display_mission(mission: SpaceMission):
    """Display mission details in a formatted way."""
    print(f"Mission: {mission.mission_name}")
    print(f"    ID: {mission.mission_id}")
    print(f"    Destination: {mission.destination}")
    print(f"    Duration: {mission.duration_days} days")
    print(f"    Budget: ${mission.budget_millions}M")
    print(f"    Status: {mission.mission_status}")
    print(f"    Crew size: {len(mission.crew)}")
    print("    Crew members:")
    for member in mission.crew:
        print(
            f"        - {member.name} ({member.rank.value})"
            + f" - {member.specialization}"
        )


def main():
    print("Space Mission Crew Validation")
    print("=" * 45)

    # Create a valid mission with crew
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-06-15T08:00:00",
            duration_days=900,
            crew=[
                {
                    "member_id": "CMD001",
                    "name": "Sarah Connor",
                    "rank": "commander",
                    "age": 45,
                    "specialization": "Mission Command",
                    "years_experience": 20,
                    "is_active": True,
                },
                {
                    "member_id": "LT001",
                    "name": "John Smith",
                    "rank": "lieutenant",
                    "age": 35,
                    "specialization": "Navigation",
                    "years_experience": 10,
                    "is_active": True,
                },
                {
                    "member_id": "OFF001",
                    "name": "Alice Johnson",
                    "rank": "officer",
                    "age": 28,
                    "specialization": "Engineering",
                    "years_experience": 6,
                    "is_active": True,
                },
            ],
            budget_millions=2500.0,
        )

        print("Valid mission created:")
        display_mission(mission)

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 45)

    # Test validation errors
    test_invalid_missions()


def test_invalid_missions():
    """Test various validation error scenarios."""

    # Test 1: Invalid mission ID
    print("Test 1: Mission ID doesn't start with 'M'")
    try:
        SpaceMission(
            mission_id="X2024_TEST",
            mission_name="Test Mission",
            destination="Moon",
            launch_date="2024-06-15",
            duration_days=30,
            crew=[
                {
                    "member_id": "CMD001",
                    "name": "Test Commander",
                    "rank": "commander",
                    "age": 40,
                    "specialization": "Command",
                    "years_experience": 15,
                    "is_active": True,
                }
            ],
            budget_millions=100.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")

    print()

    # Test 2: No Commander or Captain
    print("Test 2: No Commander or Captain in crew")
    try:
        SpaceMission(
            mission_id="M2024_TEST2",
            mission_name="Test Mission 2",
            destination="Moon",
            launch_date="2024-06-15",
            duration_days=30,
            crew=[
                {
                    "member_id": "OFF001",
                    "name": "Junior Officer",
                    "rank": "officer",
                    "age": 25,
                    "specialization": "Engineering",
                    "years_experience": 3,
                    "is_active": True,
                },
                {
                    "member_id": "CAD001",
                    "name": "New Cadet",
                    "rank": "cadet",
                    "age": 22,
                    "specialization": "Training",
                    "years_experience": 1,
                    "is_active": True,
                },
            ],
            budget_millions=50.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")

    print()

    # Test 3: Long mission without enough experienced crew
    print("Test 3: Long mission (500 days) with inexperienced crew")
    try:
        SpaceMission(
            mission_id="M2024_TEST3",
            mission_name="Long Mission",
            destination="Jupiter",
            launch_date="2024-06-15",
            duration_days=500,
            crew=[
                {
                    "member_id": "CMD001",
                    "name": "Experienced Commander",
                    "rank": "commander",
                    "age": 50,
                    "specialization": "Command",
                    "years_experience": 25,
                    "is_active": True,
                },
                {
                    "member_id": "CAD001",
                    "name": "New Cadet 1",
                    "rank": "cadet",
                    "age": 20,
                    "specialization": "Training",
                    "years_experience": 1,
                    "is_active": True,
                },
                {
                    "member_id": "CAD002",
                    "name": "New Cadet 2",
                    "rank": "cadet",
                    "age": 21,
                    "specialization": "Training",
                    "years_experience": 2,
                    "is_active": True,
                },
                {
                    "member_id": "CAD003",
                    "name": "New Cadet 3",
                    "rank": "cadet",
                    "age": 22,
                    "specialization": "Training",
                    "years_experience": 1,
                    "is_active": True,
                },
            ],
            budget_millions=500.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")

    print()

    # Test 4: Inactive crew member
    print("Test 4: Crew contains inactive member")
    try:
        SpaceMission(
            mission_id="M2024_TEST4",
            mission_name="Test Mission 4",
            destination="Moon",
            launch_date="2024-06-15",
            duration_days=30,
            crew=[
                {
                    "member_id": "CMD001",
                    "name": "Active Commander",
                    "rank": "commander",
                    "age": 45,
                    "specialization": "Command",
                    "years_experience": 20,
                    "is_active": True,
                },
                {
                    "member_id": "OFF001",
                    "name": "Retired Officer",
                    "rank": "officer",
                    "age": 60,
                    "specialization": "Engineering",
                    "years_experience": 30,
                    "is_active": False,  # Inactive!
                },
            ],
            budget_millions=100.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")


if __name__ == "__main__":
    main()
