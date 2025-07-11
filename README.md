# Configuration-File-Parser-with-JSON-and-API-Integration
A tool to parse configuration files, extract key-value pairs, and store them as JSON in a database. Handles errors gracefully if the file is missing or unreadable. Includes a RESTful GET API to retrieve the data, streamlining configuration management for DevOps automation.

## Features
- **INI File Parsing:** Reads and extracts data from configuration files in the INI format.
- **JSON Export:** Converts the parsed data into a JSON structure and saves it with an attached timestamp.
- **Validation:** Ensures that input file paths and output destinations are valid.
- **Interactive:** Provides user-friendly prompts to specify file paths and validate directories.

## Prerequisites
Before using the program, ensure the following:
- Python 3.6 or higher is installed on your system.
- `configparser` and `os` libraries are available (part of Python's standard library).
- The configuration file is in a valid INI format.

## Requirements
- Operating System: Windows, macOS, or Linux.
- Python Environment: Any Python 3.6+ compatible interpreter.

## Usage
1. Place your INI configuration file in a known directory.
2. Run the program using `python Configuration\ Management\ System.py`.
3. Provide the path to the INI file when prompted.
4. Specify the desired output path for the JSON file.
5. The parsed data will be displayed and saved to the specified JSON file.

### Example
#### Sample Input (INI File)
```ini
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
```

#### Process
1. Run the script: `python Configuration Management System.py`
2. Input paths when prompted:
   - Input file: `/path/to/config.ini`
   - Output file: `/path/to/output/config.json`

#### Sample Output (JSON File)
```json
{
    "timestamp": "2024-11-23T07:58:40.850294",
    "config": {
        "Database": {
            "host": "localhost",
            "port": "3306",
            "username": "admin",
            "password": "secret"
        },
        "Server": {
            "address": "192.168.0.1",
            "port": "8080"
        }
    }
}
```

#### Console Output
```plaintext
Configuration File Parser
=========================
Please enter the full path to your config file (e.g., C:\Users\YourName\config.ini): /path/to/config.ini
Please enter the full path for the output JSON file (e.g., C:\Users\YourName\output.json): /path/to/output/config.json

Configuration File Parser Results:

Database:
- host: localhost
- port: 3306
- username: admin
- password: secret

Server:
- address: 192.168.0.1
- port: 8080

Configuration successfully saved to: /path/to/output/config.json
```

## Notes
- Ensure that the INI file follows the correct syntax, with sections enclosed in brackets (`[ ]`) and key-value pairs separated by `=` or `:` characters.
- The tool does not encrypt sensitive data like passwords; handle output files with care.

---

