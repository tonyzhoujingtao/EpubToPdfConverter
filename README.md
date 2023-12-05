# EpubToPdfConverter

## Description

EpubToPdfConverter is a Python script that converts EPUB files to PDF format. It is designed to process all EPUB files
in a specified directory, converting them into PDFs and saving them in a newly created directory. This tool is useful
for easily converting a batch of EPUB files for compatibility with PDF-supported devices or applications.

## Features

- Batch conversion of EPUB files to PDF.
- Automatic creation of a target directory for the converted PDF files.
- Command-line interface for easy operation.

## Installation

Before running the script, ensure you have Python installed on your system. This program has been tested with Python
3.10. Additional dependencies are required:

1. Install the required Python packages:

   ```bash
   pip install PyMuPDF ebooklib WeasyPrint
   ```

2. Clone the repository or download the script files to your local machine.

## Usage

To use the EpubToPdfConverter, follow these steps:

1. Place all the EPUB files you want to convert into a single directory.

2. Run the script from the command line, specifying the source directory:

   ```bash
   python epub_to_pdf_converter.py /path/to/epub/files
   ```

   Replace `/path/to/epub/files` with the path to your directory containing EPUB files.

3. The script will create a new directory named `<source_directory_name>_converted_to_pdf` and save all the converted
   PDFs there.

## Structure

- `epub_to_pdf_converter.py`: Main script for running the program.
- `converter.py`: Module handling the conversion of EPUB to PDF.
- `file_manager.py`: Module managing file operations.

## Contributing

Contributions to improve EpubToPdfConverter are welcome. Please feel free to fork the repository and submit pull
requests.

## Disclaimer

This script is provided "as is", without warranty of any kind. The conversion quality may vary based on the complexity
and format of the source EPUB files.
