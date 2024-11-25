import shlex

def parse_command(input_line):
    """
    Parses a command line input.
    Handles quoted arguments correctly using `shlex`.
    
    Args:
        input_line (str): The raw command input from the user.

    Returns:
        tuple: The command name and a list of arguments.
    """
    parts = shlex.split(input_line)  # Handle quotes properly
    if not parts:
        raise ValueError("No command provided.")
    command = parts[0]
    args = parts[1:]
    return command, args
