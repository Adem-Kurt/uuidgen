import uuid
import argparse
import sys
import pyperclip


def generate_uuids(count, version):
    if version == 1:
        return [str(uuid.uuid1()) for _ in range(count)]
    elif version == 3:
        return [str(uuid.uuid3(uuid.NAMESPACE_DNS, f"name{i}")) for i in range(count)]
    elif version == 4:
        return [str(uuid.uuid4()) for _ in range(count)]
    elif version == 5:
        return [str(uuid.uuid5(uuid.NAMESPACE_DNS, f"name{i}")) for i in range(count)]
    else:
        raise ValueError("Unsupported UUID version.")


def main():
    parser = argparse.ArgumentParser(description="UUID generator application")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of UUIDs to generate (default: 1)")
    parser.add_argument("-v", "--version", type=int, choices=[1, 3, 4, 5], default=4,
                        help="UUID version (1, 3, 4, 5) (default: 4)")
    parser.add_argument("-o", "--output", type=str, help="File path to save the UUIDs")
    parser.add_argument("-c", "--copy", action="store_true", help="Copy generated UUIDs to clipboard instead of printing to standard output")

    args = parser.parse_args()

    try:
        uuids = generate_uuids(args.number, args.version)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    for u in uuids:
        print(u)
    print(f"Generated {len(uuids)} UUIDs of version {args.version}")

    if args.copy:
        try:
            pyperclip.copy("\n".join(uuids))
            print("Copied to clipboard.")
        except pyperclip.PyperclipException as e:
            print("Clipboard error:", e)

    if args.output:
        try:
            with open(args.output, "w") as f:
                for u in uuids:
                    f.write(u + "\n")
            print(f"Saved to {args.output}")
        except Exception as e:
            print("File writing error:", e)
            sys.exit(1)
