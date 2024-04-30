from contextlib import closing
import socket

def low(x):
    return x.lower()

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print("Port is open")
        else:
            print("Port is not open")
            
# Use this for testing the resulting dataframe of the JSON output (number of entries / lines)
def count_string_occurrences_in_keys(data, target_string):
    # generated by GPT
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
