import re
import openpyxl
import webbrowser
import os

## @package header_parser
#  A script to parse C/C++ header files and save function prototypes to an Excel sheet.


## Parses a header file and extracts function prototypes.
#  @param file_path The path to the header file to parse.
#  @return A list of function prototypes extracted from the header file.
def parse_header_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Regular expression pattern for matching function prototypes
    pattern = r"\b(?:[\w\s\*]+)\s+[\w]+\s*\([\w\s\*,\*\s]*\)\s*(?:;|\{)"
    prototypes = re.findall(pattern, content)

    return prototypes


## Saves function prototypes to an Excel file.
#  @param prototypes A list of function prototypes to save.
#  @param output_file The path to the output Excel file.
def save_to_excel(prototypes, output_file):
    # Create a new workbook and select the active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Function Prototypes"

    # Write the header
    ws.append(["ID", "Prototype"])

    # Write the prototypes with unique IDs
    for idx, prototype in enumerate(prototypes):
        ws.append([f"IDX{idx}", prototype])

    # Save the workbook
    wb.save(output_file)


## Main function to parse a header file and save the prototypes to an Excel file.
def main():
    header_file_path = "header.h"  # Replace with your header file path
    output_excel_file = (
        "prototypes.xlsx"  # Replace with your desired output Excel file path
    )

    # Parse the header file
    prototypes = parse_header_file(header_file_path)

    # Save prototypes to Excel
    save_to_excel(prototypes, output_excel_file)

    # Open the generated Excel file using the default application
    webbrowser.open(output_excel_file)


## Entry point of the script.
if __name__ == "__main__":
    main()
