""" ex_4_1.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def num_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdown_count = 0 
    with open(logfile) as file:
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            shutdown_count = shutdown_count+line.count("Shutdown")
             
    return shutdown_count/2


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{num_shutdowns(FILENAME)=}')
