import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    coord = (10, 20, 5)
    print(f"Position created: {coord}")
    origin = (0, 0, 0)
    distance = math.sqrt((coord[0] - origin[0]) ** 2
                         + (coord[1] - origin[1]) ** 2
                         + (coord[2] - origin[2]) ** 2
                         )
    print(f"Distance between {origin} and {coord}: {distance:.2f}")
    print()
    str_coord = "3,4,0"
    x, y, z = str_coord.split(",")
    parsed_coord = int(x), int(y), int(z)
    print(f'Parsing coordinates: "{str_coord}"')
    print(f"Parsed position: {parsed_coord}")
    distance = math.sqrt((parsed_coord[0] - origin[0]) ** 2
                         + (parsed_coord[1] - origin[1]) ** 2
                         + (parsed_coord[2] - origin[2]) ** 2
                         )
    print(f"Distance between {origin} and {parsed_coord}: {distance:.1f}")
    print()
    non_digit_numbers = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{non_digit_numbers}"')
    try:
        x, y, z = non_digit_numbers.split(',')
        parsed_coord = int(x), int(y), int(z)

    except ValueError as e:
        print(
            "Error parsing coordinates:",
            f"{e}"
            )
        print("Error details - Type: ValueError, Args:",
              f"{e.args}"
              )
    print()

    print("Unpacking demonstration:")
    print(f"Player at x={parsed_coord[0]}, y={parsed_coord[1]},",
          f"z={parsed_coord[2]}")
    x, y, z = parsed_coord
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
