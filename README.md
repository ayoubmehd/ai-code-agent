# Coder Agent

A Python-based AI coding agent that uses Google's Gemini AI to perform automated coding tasks. The agent can read files, execute Python code, write files, and manage project structures through natural language commands.

## ⚠️ **SECURITY WARNING** ⚠️

**This AI agent can execute arbitrary Python code and modify files on your system. Use with extreme caution!**

- The agent has full access to read, write, and execute files within the working directory
- It can run any Python code with system-level access
- Only use this tool in isolated environments or with trusted code
- Never run this agent on production systems or with sensitive data
- Always review any code changes before applying them

## Features

- **File Operations**: List directories, read file contents, and write new files
- **Code Execution**: Run Python scripts with custom arguments
- **AI-Powered**: Uses Google Gemini 2.0 Flash for intelligent code analysis and generation
- **Function Calling**: Structured function calls for reliable automation
- **Verbose Mode**: Detailed logging for debugging and monitoring
- **Example Calculator**: Includes a sample calculator application

## Prerequisites

- Python 3.10 or higher
- Google Gemini API key
- `uv` package manager (recommended) or `pip`

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd coder-agen
   ```

2. **Install dependencies:**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

## Usage

### Basic Usage

```bash
python main.py "Your natural language command here"
```

### Examples

```bash
# List files in the current directory
python main.py "List all files in the current directory"

# Read a specific file
python main.py "Read the contents of main.py"

# Create a new Python file
python main.py "Create a hello world script that prints 'Hello, World!'"

# Run a Python script
python main.py "Run the calculator example with the expression '2 + 3 * 4'"
```

### Verbose Mode

Add `--verbose` flag for detailed logging:

```bash
python main.py "Your command here" --verbose
```

### Calculator Example

The project includes a sample calculator application:

```bash
# Run the calculator directly
cd calculator
python main.py "3 + 5 * 2"

# Or use the agent to run it
python main.py "Run the calculator with expression '10 / 2 + 3'"
```

## Available Functions

The agent has access to these functions:

- **`get_files_info`**: List files and directories with metadata
- **`get_file_content`**: Read file contents (limited to 10,000 characters)
- **`run_python_file`**: Execute Python scripts with optional arguments
- **`write_file`**: Create or overwrite files

## Configuration

Edit `config.py` to adjust settings:

- `MAX_READ_FILE_CHAR`: Maximum characters to read from files (default: 10,000)
- `RUN_PYTHON_FILE_TIMEOUT`: Timeout for Python execution in seconds (default: 30)

## Project Structure

```
coder-agen/
├── main.py                 # Main agent application
├── config.py              # Configuration settings
├── functions/             # Function implementations
│   ├── call_function.py   # Function dispatcher
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── calculator/            # Example calculator application
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
└── pyproject.toml         # Project dependencies
```

## Safety Considerations

1. **Sandbox Environment**: Always run in a virtual environment or container
2. **Code Review**: Review all generated code before execution
3. **Backup**: Keep backups of important files before running the agent
4. **Permissions**: Run with minimal necessary permissions
5. **Network Access**: Consider network isolation for sensitive operations

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure `GEMINI_API_KEY` is set in your `.env` file
2. **Permission Denied**: Check file permissions for the working directory
3. **Timeout Errors**: Increase `RUN_PYTHON_FILE_TIMEOUT` in `config.py`
4. **Memory Issues**: Reduce `MAX_READ_FILE_CHAR` for large files

### Debug Mode

Use verbose mode to see detailed execution logs:

```bash
python main.py "your command" --verbose
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Disclaimer

This tool is provided as-is for educational and development purposes. The authors are not responsible for any damage caused by the execution of arbitrary code. Always use in isolated environments and review all generated code before execution.
