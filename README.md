# colonizer

Command-line tool that lets you register a package on PyPi or npm before you have any code ready. Yes, it's a provocative name, and yes, this could very well be damaging to the OSS ecosystem. Please don't use this tool!

## Installation

```bash
$ pip install colonizer
```

## Usage

Again, I don't recommend using this, but if you must...

For Python packages:

```bash
$ colonizer --pypi your_package_name
```

For Node:

```bash
$ colonizer --npm your_package_name
```

It will use author information from your local git config.
