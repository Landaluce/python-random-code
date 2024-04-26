from typing import Callable
from functools import wraps
import inspect
import sqlite3
import psutil
import time


def profile(output_mode: str = 'stdout', output_file: str = None, return_result: bool = False) -> Callable:
    """
    Decorator that profiles the execution time, CPU usage, and memory usage of a function.

    Args:
        output_mode (str): Specifies the output mode ('stdout', 'file', 'return').
        output_file (str): File path to write profiling results if `output_mode` is 'file'.
        return_result (bool): Whether to return the profiling results.

    Returns:
        The wrapper function that profiles the input function.
    """
    step = 1024

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                start_cpu_usage = psutil.cpu_percent(interval=None)
                start_memory_usage = psutil.Process().memory_info().rss

                result = func(*args, **kwargs)

                end_time = time.time()
                end_cpu_usage = psutil.cpu_percent(interval=None)
                end_memory_usage = psutil.Process().memory_info().rss

                execution_time = end_time - start_time
                cpu_usage = end_cpu_usage - start_cpu_usage
                memory_usage = (end_memory_usage - start_memory_usage) / (step * step)  # Convert memory usage to MB

                module_name = inspect.getmodule(func).__name__
                file_name = inspect.getfile(func)

                output = [f"\nFunction: {func.__name__} (Defined in {file_name})", f"Module: {module_name}",
                          f"args: {args}, kwargs: {kwargs}", f"returned: {result}",
                          f"\nExecution Time: {execution_time:.6f} seconds", f"CPU Usage: {cpu_usage:.2f}%",
                          f"Memory Usage: {memory_usage:.2f} MB"]

                output_text = "\n".join(output)

                if output_mode == 'stdout':
                    print(output_text)
                elif output_mode == 'file' and output_file:
                    with open(output_file, 'a') as f:
                        f.write(output_text + '\n')
                elif output_mode == 'return':
                    if return_result:
                        return result
                    else:
                        return {
                            'function': func.__name__,
                            'module': module_name,
                            'args': args,
                            'kwargs': kwargs,
                            'returned': result,
                            'execution_time': execution_time,
                            'cpu_usage': cpu_usage,
                            'memory_usage': memory_usage
                        }
                print()
                return result

            except Exception as e:
                print(f"\nFunction: {func.__name__} (FAILED)")
                print(f"Error: {str(e)}")
                raise e  # Reraise the exception for caller to handle

        return inner_wrapper

    return wrapper


class Database:
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()  # Commit transaction if no exceptions
        else:
            self.conn.rollback()  # Rollback transaction if exception occurred
        self.conn.close()


def transactional(db_file: str) -> Callable:
    """
    Decorator factory that creates a transactional decorator for database operations.

    Args:
        db_file: The path to the database file.

    Returns:
        The transactional decorator function.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            with Database(db_file) as cursor:
                try:
                    result = func(cursor, *args, **kwargs)  # Pass cursor to function
                except Exception as e:
                    print(f"Error occurred: {e}")
                    result = None
                return result
        return wrapper
    return decorator


def create_table(table_name: str, columns: list) -> Callable:
    """
    Decorator factory that creates a decorator to ensure a database table exists.

    Args:
        table_name: The name of the database table.
        columns: List of column definitions in SQL format.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            with Database("example.db") as cursor:
                # Check if table exists
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
                existing_table = cursor.fetchone()
                if not existing_table:
                    # Table doesn't exist, create it
                    columns_str = ', '.join(columns)
                    cursor.execute(f"CREATE TABLE {table_name} ({columns_str})")

                # Execute the original function
                return func(*args, **kwargs)

        return wrapper
    return decorator


def check_duplicate_data(table_name: str, unique_columns: list) -> Callable:
    """
    Decorator factory that creates a decorator to check for duplicate data in a database table.

    Args:
        table_name: The name of the database table.
        unique_columns: List of column names that define uniqueness.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            with Database("example.db") as cursor:
                # Build the WHERE clause for checking duplicates
                where_clause = " AND ".join(f"{col} = ?" for col in unique_columns)
                query = f"SELECT COUNT(*) FROM {table_name} WHERE {where_clause}"

                # Extract unique values from arguments
                unique_values = [kwargs[col] for col in unique_columns]

                # Execute the query to check for duplicates
                cursor.execute(query, tuple(unique_values))
                count = cursor.fetchone()[0]

                if count > 0:
                    raise ValueError("Duplicate data already exists in the database")

                # Execute the original function if no duplicates found
                return func(*args, **kwargs)

        return wrapper
    return decorator


def delete_data(table_name: str, condition: str) -> Callable:
    """
    Decorator factory that creates a decorator to delete data from a database table.

    Args:
        table_name: The name of the database table.
        condition: The SQL condition for data deletion.

    Returns:
        The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            with Database("example.db") as cursor:
                # Build DELETE query with specified condition
                query = f"DELETE FROM {table_name} WHERE {condition}"

                # Execute the DELETE query
                cursor.execute(query)

                # Execute the original function
                return func(*args, **kwargs)

        return wrapper
    return decorator


@transactional("example.db")
@create_table("users", ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER"])
@check_duplicate_data("users", ["name"])
# @delete_data("users", "age < 31")
def insert_data(cursor: sqlite3.Cursor, name: str, age: int) -> None:
    """
    Inserts data into the 'users' table in the database.

    Args:
        cursor: The database cursor object.
        name: The name of the user to insert.
        age: The age of the user to insert.

    Returns:
        None
    """
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))


# @profile(output_mode='file', output_file='profile_results.txt')
@profile(output_mode='stdout', return_result=True)
def factorial(n: int) -> int:
    """
    Computes the factorial of a given integer using memoization.

    Args:
        n: The integer for which factorial is computed.

    Returns:
        The factorial of n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


@profile(output_mode='stdout')
def tst_profile(x) -> None:
    """
    Example function to demonstrate profiling using the 'profile' decorator.
    """
    ns = []
    for i in range(0, 10000000):
        ns.append(i)
    print(ns[-1])
    print("hello_world!!")


def main() -> None:
    """
    Main function to demonstrate profiling and other database operations.
    """
    factorial(5)
    tst_profile(0)

    # insert_data("Alice", 31)


if __name__ == "__main__":
    main()
