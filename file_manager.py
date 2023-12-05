import os


def list_epub_files(directory):
    """ List all EPUB files in the given directory. """
    return [file for file in os.listdir(directory) if file.endswith('.epub')]


def ensure_directory_exists(directory):
    """ Ensure that the given directory exists, create if not. """
    if not os.path.exists(directory):
        os.makedirs(directory)
