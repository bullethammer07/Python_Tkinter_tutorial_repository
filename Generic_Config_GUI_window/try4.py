# Importing argparse
import argparse
import re

# Creating an object of the Argument Paser
ap = argparse.ArgumentParser()

# Adding an argument(s). Here we are adding only one.
ap.add_argument("-f","--file",required=True, help="Specify input config file.")

# Parse all the added  arguments
args = vars(ap.parse_args())

# Accessing the arguments and storing them in variables
file_path = args['file']

# Remove all line and block comments from the file
def remove_all_comments(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        # Remove line comments (//)
        content = re.sub(r'//.*', '', content)

        # Remove block comments (/* ... */)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

# Remove all empty lines
def remove_empty_lines(file_name):
    # Reading the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Removing empty lines
    non_empty_lines = [line for line in lines if line.strip() != ""]

    # Writing the modified content back to the file
    with open(file_name, 'w') as file:
        file.writelines(non_empty_lines)

# Remove leading and trailing whitespaces
def remove_leading_and_trailing_whitespace(file_name):
    # Reading the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Removing leading and trailing whitespaces
    trimmed_lines = [line.strip() + '\n' for line in lines]

    # Writing the modified content back to the file
    with open(file_name, 'w') as file:
        file.writelines(trimmed_lines)

# Function to replace tabs with a single space in a file
def replace_tabs_with_space(file_name):
    # Reading the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Replacing tabs with a single space
    modified_lines = [line.replace('\t', ' ') for line in lines]

    # Writing the modified content back to the file
    with open(file_name, 'w') as file:
        file.writelines(modified_lines)

# Function to replace multiple spaces with a single space in a file
def replace_multiple_spaces_with_single(file_name):
    # Reading the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Replacing multiple spaces with a single space using regex
    modified_lines = [re.sub(' +', ' ', line) for line in lines]

    # Writing the modified content back to the file
    with open(file_name, 'w') as file:
        file.writelines(modified_lines)

def parse_module_ports_from_config(file_name):
    # Reading the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    port_arr = [] # Empty List, This will hold the list of all the parsed lines
    # Parse lines individually
    for i in lines:
        # print(f"{i}")
        i = i.replace("\n","")
        line_arr = i.split(',') # Creating an array based on the separator
        # print(len(line_arr), line_arr)
        port_arr.append(line_arr)

    # print(f"Number of ports :: {len(port_arr)}")
    # print(f"{port_arr}")

    return_list = [] # Empty List
                     # This list will contain dictionaries which will translate the entire configuration.
                     
    # Parsing the complete Ports File
    for port in port_arr:
        # Each config length check
        port_type           = port[0].strip()
        port_packed_width   = port[1].strip()
        port_name           = port[2].strip()

        # Function Check for packed/unpacked size (Numerical, Parameter or Full Width)
        def check_port_dimension_sanity(pw):
            if pw == '' or len(pw) == 0: # Empty Port
                print(f"Port Dimension is Empty and should be treated as 1")
            # elif type(pw) == int: # Integral Type
                # print(f"Port Dimension is Integral")
            elif type(pw) == str: # String Type, this can be '[]' or a parameter
                # print(f"Port Dimension is either Specific or parametric")

                alnum_and_underscore_pattern = r'^[a-zA-Z0-9_]+$'
                square_brackets_pattern = r'^\[.*\]$'

                if pw.isdigit():
                    print(f"Port is of type :: INTEGRAL")
                elif re.match(alnum_and_underscore_pattern, pw):
                    print(f"Port is of type :: PARAMETRIC")
                elif re.match(square_brackets_pattern, pw):
                    print(f"Port is of type :: SPECIFIC")
                else:
                    print(f"ERROR : Unsupported port type specified :: {pw}")

        if len(port) == 3:
            print(f"Port Name :: {port_name}, Packed Width :: {port_packed_width}, Port Type :: {port_type}")
            check_port_dimension_sanity(port_packed_width)
        elif len(port) == 4:
            port_unpacked_width = port[3].strip().replace("\n","")
            check_port_dimension_sanity(port_packed_width)
            check_port_dimension_sanity(port_unpacked_width)
            print(f"Port Name :: {port_name}, Packed Width :: {port_packed_width}, Port Type :: {port_type}, Port Unpacked Widthe :: {port_unpacked_width}")
        else:
            port_name           = port[2]
            err_msg = f"ERROR : Port : {port_name} definition has more than 4 fields defined .... Please rectify and update config script !!..."
            # exit(1) # Error is number of parameters are not aligned to 3 or 4
            return 1, err_msg

        # Check for valid port types
        pt_low = port_type.lower()
        if pt_low == 'i' or pt_low == 'input':
            print(f"Port {port_name} is of INPUT type")
        elif pt_low == 'o' or  pt_low == 'output':
            print(f"Port {port_name} is of OUTPUT type")
        elif pt_low == 'io' or pt_low ==  'inout':
            print(f"Port {port_name} is of INOUT type")
        else:
            err_msg = f"ERROR : Port : {port_name} definition is of an unknown type \'{port[0].strip()}\' ... Supported types are : input, INPUT, i , I, output, OUTPUT, o, O, inout, INOUT, io and IO\'"
            # exit(1) # Error is number of parameters are not aligned to 3 or 4
            return 1, err_msg
        
    return 0, return_list

remove_all_comments(file_path) # Remove all comments from file
remove_empty_lines(file_path) # Remove all empty lines
remove_leading_and_trailing_whitespace(file_path) # remove all leading and trailing whitespaces
replace_tabs_with_space(file_path)
replace_multiple_spaces_with_single(file_path)
parse_module_ports_from_config(file_path)