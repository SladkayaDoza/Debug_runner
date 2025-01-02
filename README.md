# Debug Runner

`debug_runner.py` is a versatile Python script designed to facilitate **hot-reloading** during the development of Python applications. Similar to the debug mode in Flask, this runner monitors your Python files for changes and automatically restarts your application, ensuring a seamless and efficient development experience without manual restarts.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Example](#example)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automatic Reloading**: Monitors `.py` files and restarts the target script upon detecting changes.
- **Cross-Platform Support**: Works on Windows, macOS, and Linux.
- **Efficient Monitoring**: Utilizes the `watchfiles` library for low CPU usage and real-time file change detection.
- **Graceful Shutdown**: Ensures that the running process is properly terminated before restarting.
- **Easy Integration**: Can be used with any Python project by simply adding the `debug_runner.py` file.

## Requirements

- **Python 3.7+**
- **watchfiles** library

## Installation

1. **Clone or Download** the repository containing `debug_runner.py` to your project directory.

2. **Install Dependencies**:

   Ensure you have `watchfiles` installed. You can install it using `pip`:

   ```bash
   pip install watchfiles
   ```

## Usage

Run `debug_runner.py` by specifying the target Python script you want to monitor and execute. You can also pass additional arguments to your target script as needed.

```bash
python debug_runner.py <script.py> [args...]
```

### Parameters

- `<script.py>`: The path to the Python script you wish to run and monitor.
- `[args...]`: (Optional) Additional arguments to pass to your target script.

### Example

Assuming you have a `main.py` file that you want to run with hot-reloading:

```bash
python debug_runner.py main.py
```

If your `main.py` accepts command-line arguments:

```bash
python debug_runner.py main.py --port 8000 --debug
```

## Customization

### Watching Multiple Directories

By default, `debug_runner.py` watches the current directory and all its subdirectories for changes in `.py` files. To watch additional directories, modify the `watch` function call in `debug_runner.py`:

```python
for changes in watch(['.', '../another-directory'], watch_filter=PythonFilter(), recursive=True):
    # Your logic here
```

### Changing the File Filter

If you want to monitor file types other than `.py`, you can adjust the `watch_filter`. For example, to watch both Python and Markdown files:

```python
from watchfiles.filters import PatternMatch

custom_filter = PatternMatch(["*.py", "*.md"])

for changes in watch('.', watch_filter=custom_filter, recursive=True):
    # Your logic here
```

## Example

Here is a step-by-step example of how to use `debug_runner.py` in your project:

1. **Place `debug_runner.py` in your project root directory.**

2. **Ensure `watchfiles` is installed**:

   ```bash
   pip install watchfiles
   ```

3. **Run your application with `debug_runner.py`**:

   ```bash
   python debug_runner.py main.py
   ```

4. **Edit your `.py` files** in the project. Upon saving changes, `debug_runner.py` will automatically restart `main.py`, reflecting your updates immediately.

## Notes

- **Development Use Only**: `debug_runner.py` is intended for development and debugging purposes. It is **not recommended** to use it in production environments.
- **Graceful Termination**: The script attempts to terminate the running process gracefully using `terminate()`. If the process does not exit within 5 seconds, it forcefully kills it using `kill()`.
- **Extensibility**: You can extend `debug_runner.py` to include more sophisticated behaviors, such as logging, handling more file types, or integrating with other tools.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix.
3. **Commit your changes** with clear messages.
4. **Push to your fork** and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Happy Coding!** 🚀