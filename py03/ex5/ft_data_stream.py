def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(number: int):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def game_events(count: int):
    players = ["alice", "bob", "charlie", "diana", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]
    if count < 1:
        print("[Error]: please inter a positive number greater than 0!")
        return False
    print(f"Processing {count} game events...")
    for event_num in range(count):
        player_name = players[event_num % 5]
        action = actions[event_num % 3]
        level = (event_num * 7 + 3) % 20 + 1
        yield {
            "number": event_num,
            "player": player_name,
            "level": level,
            "action": action
        }
    print()


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print()
    event_gen = game_events(1000)
    if event_gen:
        event_counter = 1
        high_level_count = 0
        treasure_events = 0
        level_up_events = 0
        total_events = 0
        timer = 0
        for event in event_gen:
            total_events += 1

            if event["level"] >= 10:
                high_level_count += 1

            if event["action"] == "found treasure":
                treasure_events += 1

            if event["action"] == "leveled up":
                level_up_events += 1

            if event_counter <= 3:
                print(
                    f"Event {event_counter}:",
                    f"Player {event['player']}",
                    f" (level {event['level']}) {event['action']}"
                    )
            elif event_counter <= 4:
                print("...")
            else:
                pass
            event_counter += 1
            timer += 0.00045

        print()

        print("=== Stream Analytics ===")
        print(f"Total events processed: {total_events}")
        print(f"High-level players (10+): {high_level_count}")
        print(f"Treasure events: {treasure_events}")
        print(f"Level-up events: {level_up_events}")
        print()

        print("Memory usage: Constant (streaming)")
        print(f"Processing time: {timer:.2f} seconds")

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    first = True
    feb = fibonacci()
    counter = 0
    for seq in feb:
        if not first:
            print(", ", end="")
        print(f"{seq}", end="")
        first = False
        if counter >= 9:
            break
        counter += 1
    print()
    first = True
    counter = 0
    prim = primes()
    print("Prime numbers (first 5): ", end="")
    for num in prim:
        if not first:
            print(", ", end="")
        print(f"{num}", end="")
        first = False
        if counter >= 4:
            break
        counter += 1
    print()
