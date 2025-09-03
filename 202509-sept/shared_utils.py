"""
Shared utilities for all part modules in the 202509-sept project.
This module contains all utility functions and classes needed by part modules.
"""

import os

def read_file_to_array(file_path):
    """
    Read a text file and return an array of lines.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        list: Array of lines from the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Remove newline characters from each line
            return [line.rstrip('\n\r') for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return []


def read_file_to_array_with_strip(file_path):
    """
    Read a text file and return an array of lines with whitespace stripped.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        list: Array of lines from the file with leading/trailing whitespace removed
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Remove all leading and trailing whitespace from each line
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return []


def read_file_to_array_no_empty(file_path):
    """
    Read a text file and return an array of non-empty lines.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        list: Array of non-empty lines from the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Remove empty lines and strip whitespace
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return []

def get_project_root():
    """
    Get the project root directory (where this utilities module is located).
    
    Returns:
        str: Path to the project root directory (202509-sept folder)
    """
    return os.path.dirname(os.path.abspath(__file__))
