def read_lines(filename):
    """
    Read the lines of a text file and return them as a list.
    
    Args:
        filename (str): The name of the file to read.
    
    Returns:
        list[str]: A list of lines from the file, or empty list if not found.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
        return []

def main():
    filename = input("Enter the file name: ")
    lines = read_lines(filename)
    print(f"Number of lines in the file: {len(lines)}")

if __name__ == "__main__":
    main()
