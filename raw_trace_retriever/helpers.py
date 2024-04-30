from contextlib import closing
import socket

from logging_config import setup_logging

# Create a logger
logger = setup_logging()

def low(x):
    """
    Converts the input string to lowercase. If the input is not a string, 
    an appropriate error is raised.

    Args:
        x (str): The string to be converted to lowercase.

    Returns:
        str: A new string with all characters in lowercase.

    Raises:
        TypeError: If the input is not a string.

    Example:
        >>> low("HeLLo WoRLD")
        'hello world'
        >>> low(123)  # This will raise a TypeError
    """
    if not isinstance(x, str):
        raise TypeError("Input must be a string")

    try:
        return x.lower()
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise ValueError(f"Failed to convert to lowercase due to an unexpected error: {e}")


# Check if the server can be reached and the port is open
def check_socket(host, port):
    """
    Checks if a given port on a host is open.

    Args:
        host (str): The hostname or IP address to check.
        port (int): The port number to check.

    Raises:
        PortNotOpenError: If the port is not open on the specified host.
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            logger.info(f"Port {port} on {host} is open.")
        else:
            logger.error(f"Port {port} on {host} is not open.")
            
            
# Use this for testing the resulting dataframe of the JSON output (number of entries / lines)
def count_string_occurrences_in_keys(data, target_string):
    # generated by GPT, edited by the author
    """
    Counts the occurrences of a target string within the keys of a dictionary, 
    including keys of any nested dictionaries or lists of dictionaries.

    This function recursively searches through the data structure, incrementing a count
    whenever it finds the target string within a key. The search includes keys in nested
    dictionaries and keys in dictionaries that are elements of lists.

    Args:
        data (dict | list): The data structure to search through. Can be a dictionary
            or a list containing dictionaries (including nested structures).
        target_string (str): The string to search for within the keys.

    Returns:
        int: The total count of occurrences of the target string in all keys.

    Example:
        >>> data = {'key1_subkey': {'key2': 'value'}, 'list_key': [{'key3': 'value'}]}
        >>> count_string_occurrences_in_keys(data, 'key')
        5
    """
    count = 0

    if isinstance(data, dict):
        for key in data.keys():
            count += key.count(target_string)  # Count occurrences in the key
        for value in data.values():
            count += count_string_occurrences_in_keys(value, target_string)  # Recursively search in nested structures

    elif isinstance(data, list):
        for item in data:
            count += count_string_occurrences_in_keys(item, target_string)  # Recursively search in items of the list

    return count