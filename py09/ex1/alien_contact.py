"""
Alien Contact Log Validation using Pydantic with custom validation.
"""

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Types of alien contact."""
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model for alien contact reports with custom validation."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_contact_rules(self):
        """Custom validation rules for alien contact reports."""

        # Rule 1: Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        # Rule 2: Physical contact must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: Telepathic contact requires at least 3 witnesses
        if self.contact_type == ContactType.telepathic \
                and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        # Rule 4: Strong signals (> 7.0) should include received messages
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include a received message"
                )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    # Create a valid contact report
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-03-15T22:30:00",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )

        print("Valid contact report:")
        print(f"    ID: {contact.contact_id}")
        print(f"    Type: {contact.contact_type.value}")
        print(f"    Location: {contact.location}")
        print(f"    Signal: {contact.signal_strength}/10")
        print(f"    Duration: {contact.duration_minutes} minutes")
        print(f"    Witnesses: {contact.witness_count}")
        print(f"    Message: '{contact.message_received}'")
        print(f"    Verified: {contact.is_verified}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 40)

    # Test validation errors
    test_invalid_contacts()


def test_invalid_contacts() -> None:
    """Test various validation error scenarios."""

    # Test 1: Invalid contact ID (doesn't start with AC)
    print("Test 1: Invalid contact ID")
    try:
        AlienContact(
            contact_id="XX_2024_001",
            timestamp="2024-03-15T22:30:00",
            location="Unknown",
            contact_type="radio",
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")

    print()

    # Test 2: Telepathic contact with insufficient witnesses
    print("Test 2: Telepathic contact with only 2 witnesses")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-03-15T22:30:00",
            location="Mount Shasta, California",
            contact_type="telepathic",
            signal_strength=6.0,
            duration_minutes=60,
            witness_count=2
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")

    print()

    # Test 3: Physical contact not verified
    print("Test 3: Physical contact not verified")
    try:
        AlienContact(
            contact_id="AC_2024_003",
            timestamp="2024-03-15T22:30:00",
            location="Roswell, New Mexico",
            contact_type="physical",
            signal_strength=9.0,
            duration_minutes=120,
            witness_count=10,
            message_received="We come in peace",
            is_verified=False
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")

    print()

    # Test 4: Strong signal without message
    print("Test 4: Strong signal (8.5) without message")
    try:
        AlienContact(
            contact_id="AC_2024_004",
            timestamp="2024-03-15T22:30:00",
            location="Somewhere",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=30,
            witness_count=3
            # No message_received!
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"    Error: {error['msg']}")


if __name__ == "__main__":
    main()
