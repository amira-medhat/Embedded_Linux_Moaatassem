import re
import openpyxl
import webbrowser
import os


# Function to parse the header file and extract function prototypes
def parse_header_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # Regular expression pattern for matching function prototypes
    pattern = r"\b(?:[\w\s\*]+)\s+[\w]+\s*\([\w\s\*,\*\s]*\)\s*(?:;|\{)"
    prototypes = re.findall(pattern, content)

    return prototypes


# Function to save prototypes to an Excel file
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


def main():
    header_file_path = "header.h"  # Replace with your header file path
    output_excel_file = (
        "prototypes.xlsx"  # Replace with your desired output Excel file path
    )

    # Parse the header file
    prototypes = parse_header_file(header_file_path)

    # Save prototypes to Excel
    save_to_excel(prototypes, output_excel_file)
    webbrowser.open(output_excel_file)


if __name__ == "__main__":
    main()
