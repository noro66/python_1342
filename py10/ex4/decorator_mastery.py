"""Master's Tower - Decorator mastery."""

import time
from functools import wraps
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that times function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.time()
            duration = end_time - start_time
            print(f"Spell completed in {duration:.3f} seconds")

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates power levels."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = None
            if 'power' in kwargs:
                power = kwargs['power']
            else:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break

            if power is not None and power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Mage guild with static and instance methods."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate name: 3+ chars, only letters/spaces."""
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast spell with power validation."""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Test decorators and class methods."""
    print("Testing spell timer...")

    @spell_timer
    def slow_spell():
        time.sleep(0.1)
        return "Fireball cast!"

    result = slow_spell()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(min_power=20)
    def simple_cast(power: int):
        return "Spell cast!"

    print(f"Power 25: {simple_cast(25)}")
    print(f"Power 15: {simple_cast(15)}")

    print("\nTesting retry spell...")

    attempt_count = [0]  # Use a list to make it mutable

    @retry_spell(max_attempts=3)
    def unstable_spell():
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise ValueError("Fizzled")
        return "Success on third try!"

    print(unstable_spell())

    print("\nTesting MageGuild...")
    print(f"Is 'Gandalf' valid? {MageGuild.validate_mage_name('Gandalf')}")
    print(f"Is 'Mage123' valid? {MageGuild.validate_mage_name('Mage123')}")
    print(f"Is 'Al' valid? {MageGuild.validate_mage_name('Al')}")

    guild = MageGuild()
    print(f"Casting with 15 power: {guild.cast_spell('Lightning', 15)}")
    print(f"Casting with 5 power: {guild.cast_spell('Spark', 5)}")


if __name__ == "__main__":
    main()
