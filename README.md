# JoomBrutev2 - Joomla Bruteforcer (Python3 Edition)

## Overview:
This tool performs a dictionary attack against Joomla administrator login pages. It attempts to discover valid credentials by trying passwords from a supplied wordlist for a specified username. Based on [JoomBrute](https://github.com/0rbz/JoomBrute) from [0rbz_](https://github.com/0rbz).

## Modifications:
- Converted the original Python 2 script to Python 3 for modern compatibility.
- Integrated a progress bar (using tqdm) displaying completion percentage and count.
- Simplified execution to a single-threaded model for increased stability and reliability.
- Reduced console output to show only successful login attempts and final status.
- Added optional delay between login attempts to reduce server load or avoid rate limits.
- Updated comments and metadata to reflect changes and maintain attribution.

## Usage:
Run the script with required parameters:
```bash
python3 joombrute.py --url http://target/administrator --username admin --wordlist passwords.txt [--ua USER_AGENT] [--delay SECONDS]
```

## Requirements:
- Python 3.6+
- Packages: werkzeug, robobrowser, tqdm

## Disclaimer:
Use this tool only on systems you have explicit permission to test. Unauthorized use is illegal and unethical.
