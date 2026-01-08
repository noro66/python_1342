import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    arg_list = sys.argv
    arg_len = len(arg_list)

    if arg_len > 1:
        print(f"Program name: {arg_list[0]}")
        print(f"Arguments received: {arg_len - 1}")
        i = 0
        for arg in arg_list[1:]:
            i += 1
            print(f"Argument {i}: {arg}")
    else:
        print("No arguments provided!")
        print(f"Program name: {arg_list[0]}")

    print(f"Total arguments: {arg_len}")
