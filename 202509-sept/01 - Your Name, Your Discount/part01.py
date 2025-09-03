"""
Part 01 module - Your Name, Your Discount
"""

import os
import sys

# Add the parent directory (202509-sept) to the path so we can import shared_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the shared utilities directly
import shared_utils

def parse_data(filepath):
    """Reads a file and returns its content as a list of lines."""
    data = shared_utils.read_file_to_array(filepath)
    return data


def execute():
    """Main execution function for this module."""
    # Use absolute path relative to the current file's directory
    filepath = os.path.join(os.path.dirname(__file__), "sample01.txt")
    file_data = parse_data(filepath)
    print(f"File data from {filepath}:")
    for line in file_data:
        print(f" - {line}")


if __name__ == "__main__":
    # This code runs only when the file is executed directly
    print("Running part01.py directly...")
    execute()
