#!/usr/bin/env python3

import argparse
import os

from converter import convert_epub_to_pdf
from file_manager import list_epub_files, ensure_directory_exists


def convert_epubs_in_directory(source_dir, target_dir):
    """ Convert all EPUB files in a directory to PDF and save in another directory. """
    ensure_directory_exists(target_dir)
    for file in list_epub_files(source_dir):
        epub_path = os.path.join(source_dir, file)
        pdf_path = os.path.join(target_dir, os.path.splitext(file)[0] + '.pdf')
        convert_epub_to_pdf(epub_path, pdf_path)
        print(f"Converted {file} to PDF.")


def main():
    parser = argparse.ArgumentParser(description="Convert EPUB files in a directory to PDF.")
    parser.add_argument("source_directory", help="Directory containing EPUB files to convert")
    args = parser.parse_args()

    source_directory = args.source_directory
    target_directory = os.path.join(os.path.dirname(source_directory),
                                    os.path.basename(source_directory) + '_converted_to_pdf')

    convert_epubs_in_directory(source_directory, target_directory)
    print(f"PDF files saved in {target_directory}")


if __name__ == "__main__":
    main()
