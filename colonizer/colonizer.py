# Standard library
import sys
import argparse
from subprocess import check_output

# Local
from colonizer.pypi import claim_pypi_package
from colonizer.npm import claim_npm_package


#########
# HELPERS
#########


def get_author() -> str:
    return check_output(["git", "config", "user.name"], encoding="utf-8").strip()


def get_author_email() -> str:
    return check_output(["git", "config", "user.email"], encoding="utf-8").strip()


######
# MAIN
######


def main():
    parser = argparse.ArgumentParser(description="Claim a package name on PyPI or npm.")
    parser.add_argument(
        "--pypi", type=str, help="The name of the package to claim on PyPI"
    )
    parser.add_argument(
        "--npm", type=str, help="The name of the package to claim on npm"
    )
    parser.add_argument(
        "--author",
        type=str,
        default=None,
        required=False,
        help="The author of the package",
    )
    parser.add_argument(
        "--author-email",
        type=str,
        default=None,
        required=False,
        help="The author email of the package",
    )

    args = parser.parse_args()
    author = args.author if args.author else get_author()
    author_email = args.author_email if args.author_email else get_author_email()

    if args.pypi:
        claim_pypi_package(args.pypi, author, author_email)
    elif args.npm:
        claim_npm_package(args.npm, author, author_email)
    else:
        print(
            "Please specify either --pypi or --npm with a package name. And optionally --author and --author-email."
        )
        sys.exit(1)
