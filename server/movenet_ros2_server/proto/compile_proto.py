import subprocess
import os

def compile_proto(proto_file, proto_path, output_dir):
    """
    Compile a .proto file using protoc with a specified proto path and output directory.

    Parameters:
    proto_file (str): The path to the .proto file to compile.
    proto_path (str): The directory in which to search for imports.
    output_dir (str): The directory where the generated Python files should be placed.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Construct the protoc command
    command = [
        'protoc',
        f'--proto_path={proto_path}',  # Specify the proto path
        f'--python_out={output_dir}',  # Specify the output directory for Python files
        proto_file  # The .proto file to compile
    ]
    
    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Check if the command executed successfully
    if result.returncode == 0:
        print("Compilation successful.")
    else:
        print("Compilation failed.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

def main(args=None):
    proto_file = '../../../proto/movenet.proto'  # Path to your .proto file
    proto_path = '.'  # Directory to search for imports
    output_dir = '.'  # Where to place the generated files

    compile_proto(proto_file, proto_path, output_dir)

if __name__ == '__main__':
    main()