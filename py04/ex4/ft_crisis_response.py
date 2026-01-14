def crisis_handler(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
