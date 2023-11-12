#!/usr/bin/env python3
import os
from langlib.reader import get_prompt, get_text
from langlib.utils import test_fun, clean_response, create_dict
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--text_name",
        help="the name of txt file, no extension needed",
        default="texts",
    )

    parser.add_argument(
        "--output_name",
        help="the name of output file, no extension needed",
        default=None,
    )
    parser.add_argument(
        "--out_dir_path",
        help="the path of directory of output file",
    )
    args = parser.parse_args()

    out_dir_path = args.out_dir_path
    text_name = args.text_name
    output_name = args.output_name
    if out_dir_path is None:
        out_dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    if output_name is None:
        output_name = text_name + "_dict"

    create_dict(text_name, output_name)


if __name__ == "__main__":
    main()
