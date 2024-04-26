import random
import os
from typing import Optional


def corrupt(file: str = "uncorrupted.txt", variant: int = 100) -> None:
    """
    Corrupts a file by introducing random changes to its binary content.

    Args:
        file (str): The path to the input file to be corrupted. Defaults to "uncorrupted.txt".
        variant (int): The amount of corruption to apply. Defaults to 100.

    Returns:
        None
    """
    # Extract file name and extension
    filename, extension = os.path.splitext(os.path.basename(file))

    # Read the content of the input file
    with open(file, 'rb') as f:
        file_content = bytearray(f.read())

    # Determine the amount of corruption
    amount = min(len(file_content), len(file_content))  # Ensure the amount is within the content length
    random.seed(len(file_content))  # Seed the random generator for consistency
    victims = random.sample(range(len(file_content)), amount)  # Select random positions for corruption

    # Corrupt the selected positions in the file content
    for v in victims:
        file_content[v] = (file_content[v] + variant) % 256

    # Prepare the output file name
    output_filename = f"{filename}_corrupted{extension}"

    # Write the corrupted content to a new file
    with open(output_filename, 'wb') as output:
        output.write(file_content)


def main() -> None:
    """
    Main function to demonstrate file corruption using the `corrupt` function.
    """
    corrupt()


if __name__ == "__main__":
    main()
