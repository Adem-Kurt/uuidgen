# uuidgen

uuidgen is a simple command-line tool written in Python for generating Universally Unique Identifiers (UUIDs) directly from your terminal.

## Description

This tool provides an easy way to generate various versions of UUIDs (v1, v3, v4, and v5) and offers options to specify the number of UUIDs, save them to a file, or copy them to the clipboard.

## Installation

You can install uuidgen using pip:

```
pip install uuidgen
```

## Usage

The tool is available as the `uuidgen` command.

```
uuidgen [OPTIONS]
```

### Options:

*   `-n, --number INTEGER`: Number of UUIDs to generate (default: 1).
*   `-v, --version [1|3|4|5]`: UUID version (1, 3, 4, or 5) (default: 4).
*   `-o, --output TEXT`: File path to save the generated UUIDs. Each UUID will be on a new line.
*   `-c, --copy`: Copy generated UUIDs to the clipboard.

## Examples

Generate a single UUID (version 4, default):

```
uuidgen
```

Generate 5 UUIDs of version 1:

```
uuidgen -n 5 -v 1
```

Generate 10 UUIDs of version 4 and save them to a file named `uuids.txt`:

```
uuidgen -n 10 -o uuids.txt
```

Generate a single UUID of version 5 and copy it to the clipboard:

```
uuidgen -v 5 -c
```

Generate 3 UUIDs of version 3 and print them to the console:

```
uuidgen -n 3 -v 3
```

## License

This project is open-source and distributed under the MIT License.
