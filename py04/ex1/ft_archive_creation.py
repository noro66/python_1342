def archive_creator() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    new_discovery = None
    try:
        print("Initializing new storage unit: new_discovery.txt")
        new_discovery = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        discovery_content = (
            "[ENTRY 001] New quantum algorithm discovered\n",
            "[ENTRY 002] Efficiency increased by 347%\n",
            "[ENTRY 003] Archived by Data Archivist trainee\n"
        )
        for content in discovery_content:
            new_discovery.write(content)
            print(content, end="")

        print()
        print("Data inscription complete. Storage unit sealed.")

        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError:
        print("ERROR: we can't initialize the new storage!, permission denied")

    except Exception as e:
        print(f"ERROR: Unexpected Error '{e}'")

    finally:
        if new_discovery:
            new_discovery.close()


if __name__ == "__main__":
    archive_creator()
