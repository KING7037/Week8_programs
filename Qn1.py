import sys

def print_file_with_line_numbers(file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number:>4}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py <filename>")
    else:
        file_name = sys.argv[1]
        print_file_with_line_numbers(file_name)
