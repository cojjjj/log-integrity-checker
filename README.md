# Log Integrity Checker

A Python-based file integrity monitoring tool that uses SHA-256 hashing to detect unauthorized modifications to log files.

## Features

* SHA-256 hash generation
* Single file or directory monitoring
* Baseline hash initialization
* Integrity verification
* Tamper detection reporting
* Manual hash updates after approved changes

## Requirements

* Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/cojjjjj/log-integrity-checker.git
cd log-integrity-checker
```

## Usage

Initialize hashes:

```bash
python3 integrity-check.py init /var/log
```

Check file integrity:

```bash
python3 integrity-check.py check /var/log/syslog
```

Update stored hashes:

```bash
python3 integrity-check.py update /var/log/syslog
```

## Example Output

```text
Hashes stored successfully.
```

```text
/var/log/syslog: Status: Modified (Hash mismatch)
```

```text
/var/log/auth.log: Status: Unmodified
```

## Security Concepts Demonstrated

* File Integrity Monitoring (FIM)
* SHA-256 Cryptographic Hashing
* Tamper Detection
* Log Security
* Blue Team Security Monitoring

## Author Tyler Deppa

Tyler Deppa
https://github.com/cojjjj/log-integrity-checker/tree/main?tab=readme-ov-file
