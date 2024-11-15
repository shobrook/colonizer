# colonizer

Command-line tool that lets you register a package on PyPi or npm before you have any code ready. Yes, this is a terrible idea. And yes, it's potentially damaging to the OSS ecosystem. Using this might make you a bad person.

## Installation

```bash
$ pip install colonizer
```

## Usage

I don't recommend actually using this, but if you must...

**For Python:**

```bash
$ colonizer --pypi your_package_name
```

By default, it will use the author information from your local git config, but you can explicitly specify this like so:

```bash
$ colonizer --pypi your_package_name --author your_username --author-email your_email
```

**For Node:**

```bash
$ colonizer --npm your_package_name
```
