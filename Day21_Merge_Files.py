def merge_files(file1, file2, output_file):
    try:
        # Read content of first file
        with open(file1, "r") as f1:
            data1 = f1.read()

        # Read content of second file
        with open(file2, "r") as f2:
            data2 = f2.read()

        # Merge and write into new file
        with open(output_file, "w") as out:
            out.write(data1 + "\n" + data2)

        print(f"Files '{file1}' and '{file2}' merged successfully into '{output_file}'.")
    
    except FileNotFoundError:
        print("One or more files not found. Please check filenames.")

merge_files("file1.txt", "file2.txt", "merged.txt")
