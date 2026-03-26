# MCP Demo Application

A demonstration of the Model Context Protocol (MCP) with a client-server architecture featuring tool capabilities for weather queries and arithmetic operations.

## Project Overview

This project demonstrates how to build and interact with an MCP server that exposes tools for:
- **get_weather**: Retrieve weather information for supported cities
- **add_numbers**: Perform addition operations on two integers

The application consists of two main components:
- **Server** (`server.py`): An MCP server built with FastMCP that defines and exposes tools
- **Client** (`client.py`): An MCP client that connects to the server and calls available tools

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Navigate to the project directory:
   ```bash
   cd d:\oAPPs\PyThOn!\mcp-demo
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - **Windows (PowerShell)**:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (Command Prompt)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

The application follows a client-server architecture. The client spawns the server as a subprocess.

### Simple Execution

Run the client, which automatically starts the server:
```bash
python client.py
```

This will:
1. Start the MCP server in the background
2. Connect the client to the server
3. Initialize the session
4. List available tools
5. Call `get_weather` with "Johannesburg" as input
6. Call `add_numbers` with inputs 5 and 7
7. Display the results

### Expected Output

```
Available tools: [...]
Weather: Sunny, 24C
Addition result: 12
```

## Project Structure

```
mcp-demo/
├── server.py           # MCP server with tool definitions
├── client.py           # MCP client that calls server tools
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Architecture

### Server (server.py)

The server uses FastMCP to create an MCP-compliant server with two tools:

- **`get_weather(city: str)`**: Returns weather information for a given city
  - Supported cities: London, Johannesburg, New York
  - Returns formatted string with conditions and temperature

- **`add_numbers(a: int, b: int)`**: Returns the sum of two integers

### Client (client.py)

The client establishes a connection to the server via stdio and demonstrates:
1. Tool discovery via `list_tools()`
2. Tool invocation via `call_tool()`
3. Async/await pattern for server communication

## Dependencies

- **mcp**: Model Context Protocol client and server libraries
- **fastapi**: Web framework (used by FastMCP)
- **uvicorn**: ASGI server (used by FastMCP)

## Troubleshooting

### Virtual Environment Issues
Ensure the virtual environment is activated before running commands. Check that the Python interpreter is from the virtual environment:
```bash
python --version
```

### Module Not Found Errors
Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Permission Denied on Windows
If you get execution policy errors, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## License

This is a demonstration project.