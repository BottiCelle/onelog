# onelog 📝

**[中文](README.md) | English**

A lightweight Python logging module built on [Rich](https://github.com/textualize/rich).

## Features

- 🎨 Color-coded terminal output (WARNING=yellow, ERROR=red, FATAL=purple)
- 📁 Optional file logging (plain text)
- 📍 File path & line number display (toggleable)
- 📊 Auto log summary on script exit
- 💀 `log.fatal()` — print and exit
- 🔧 Multi-module support — top-level config overrides sub-modules

## Requirements

- Python 3.8+
- `rich` (only dependency)

```bash
python3 -m pip install onelogg
```

You can also install a tagged release directly from GitHub:

```bash
python3 -m pip install "git+https://github.com/BottiCelle/onelog.git@v0.1.2"
```

The current package version is `0.1.2`. Its distribution name is
`onelogg`, while its import name remains `onelog`.

## Usage

```python
from onelog import get_logger

log = get_logger(__name__, level="DEBUG", show_loc=True, log_file="app.log")

log.debug("debug message")
log.info("info message")
log.warning("warning message")
log.error("error message")
log.fatal("fatal error, script exits here")
```

See [`examples/multi/`](examples/multi/) for the complete runnable multi-module
example:

```bash
python examples/multi/main.py
```

## Type checking

Starting with `onelogg` 0.1.2, the wheel ships PEP 561 inline types. Type
checkers such as Pyright and mypy discover the `onelog` types automatically,
so consumers no longer need to maintain a local `.pyi` file.

Log summary prints automatically when the script exits:

```
──────────────────────────────── 📊 Log Summary ────────────────────────────────
  DEBUG:   1
  INFO:    1
  WARNING: 1
  ERROR:   1

  Log File: /path/to/app.log
────────────────────────────────────────────────────────────────────────────────
```

## License

MIT
