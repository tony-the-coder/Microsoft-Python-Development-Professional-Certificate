import logging
from datetime import datetime
import time

# Set up logging
logging.basicConfig(# STEP 2.1: YOUR CODE HERE
                    )

def log_action(func):
    """Decorator to log task actions.

    This decorator logs the function name and its arguments 
    to the 'task_manager.log' file whenever the decorated 
    function is called.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function.
    """
    def wrapper(*args, **kwargs):
        current_datetime = datetime.now()
        # STEP 2.2: YOUR CODE HERE
        logging.info(f"{current_datetime}: Executing function: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def timer(func):
    """Decorator to measure execution time of a function.

    This decorator calculates and logs the time taken 
    for the decorated function to execute.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        # STEP 2.3: YOUR CODE HERE
        return result
    return wrapper