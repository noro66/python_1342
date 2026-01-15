def archive_reader() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file = None
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print("RECOVERED DATA:")
        print(file.read())
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

    except PermissionError:
        print("ERROR: Access denied to storage vault.")

    except Exception:
        print("ERROR: unexpected error accrued")

    finally:
        if file:
            file.close()


if __name__ == "__main__":
    archive_reader()
