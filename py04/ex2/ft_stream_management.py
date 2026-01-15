import sys


def stream_manager() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    try:
        archivist_id = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")
        print()
        print(
            f"[STANDARD] Archive status from {archivist_id}: {status_report}"
            )
        print("[ALERT] System diagnostic: Communication channels verified",
              file=sys.stderr)
        print("[STANDARD] Data transmission complete")
        print("Three-channel communication test successful.")
    except Exception as e:
        print(f"ERROR: Unexpected Error Occurs {e}")


if __name__ == "__main__":
    stream_manager()
