import sys

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            if lines1 == lines2:
                print("The files are the same.")
            else:
                print("The files are different.")
                print("Differences:")
                for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
                    if line1 != line2:
                        print(f"Line {i}:")
                        print(f"  File1: {line1.rstrip()}")
                        print(f"  File2: {line2.rstrip()}")
                # Check if one file has extra lines
                if len(lines1) > len(lines2):
                    print(f"File1 has {len(lines1) - len(lines2)} additional line(s):")
                    for line in lines1[len(lines2):]:
                        print(f"  {line.rstrip()}")
                elif len(lines2) > len(lines1):
                    print(f"File2 has {len(lines2) - len(lines1)} additional line(s):")
                    for line in lines2[len(lines1):]:
                        print(f"  {line.rstrip()}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_command.py <file1> <file2>")
    else:
        file1, file2 = sys.argv[1], sys.argv[2]
        compare_files(file1, file2)
