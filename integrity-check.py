#!/usr/bin/env python3

import argparse
import hashlib
import json
from pathlib import Path

HASH_DB = Path.home() / ".log_integrity_hashes.json"


def sha256_file(file_path):
    hasher = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def get_files(path):
    path = Path(path)

    if path.is_file():
        return [path]

    if path.is_dir():
        return [file for file in path.rglob("*") if file.is_file()]

    raise FileNotFoundError(f"{path} does not exist")


def load_hashes():
    if HASH_DB.exists():
        with open(HASH_DB, "r") as file:
            return json.load(file)
    return {}


def save_hashes(hashes):
    with open(HASH_DB, "w") as file:
        json.dump(hashes, file, indent=4)


def init_hashes(path):
    hashes = load_hashes()

    for file in get_files(path):
        hashes[str(file.resolve())] = sha256_file(file)

    save_hashes(hashes)
    print("Hashes stored successfully.")


def check_hashes(path):
    hashes = load_hashes()

    for file in get_files(path):
        file_path = str(file.resolve())
        current_hash = sha256_file(file)

        if file_path not in hashes:
            print(f"{file}: New file / not initialized")
        elif hashes[file_path] != current_hash:
            print(f"{file}: Status: Modified (Hash mismatch)")
        else:
            print(f"{file}: Status: Unmodified")


def update_hash(path):
    hashes = load_hashes()

    for file in get_files(path):
        hashes[str(file.resolve())] = sha256_file(file)

    save_hashes(hashes)
    print("Hash updated successfully.")


def main():
    parser = argparse.ArgumentParser(
        description="Log file integrity checker using SHA-256"
    )

    parser.add_argument(
        "command",
        choices=["init", "check", "update"],
        help="init, check, or update hashes"
    )

    parser.add_argument(
        "path",
        help="Path to a log file or directory"
    )

    args = parser.parse_args()

    if args.command == "init":
        init_hashes(args.path)
    elif args.command == "check":
        check_hashes(args.path)
    elif args.command == "update":
        update_hash(args.path)


if __name__ == "__main__":
    main()
