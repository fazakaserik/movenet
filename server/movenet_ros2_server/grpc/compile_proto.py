import grpc_tools.protoc
import os

def compile_proto(proto_file, proto_path, output_dir):
    """
    Compile a .proto file using grpc_tools.protoc with a specified proto path and output directory.

    Parameters:
    proto_file (str): The path to the .proto file to compile.
    proto_path (str): The directory in which to search for imports.
    output_dir (str): The directory where the generated Python files should be placed.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the protoc command arguments
    command = [
        'grpc_tools.protoc',
        f'--proto_path={proto_path}',
        f'--python_out={output_dir}',
        f'--grpc_python_out={output_dir}',
        proto_file
    ]

    # Call grpc_tools.protoc with the specified arguments
    if grpc_tools.protoc.main(command) != 0:
        print("Compilation failed.")
    else:
        print("Compilation successful.")

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    proto_dir_path = os.path.join(dir_path, "..", "..", "..", "proto")
    proto_file_path = os.path.join(proto_dir_path, "movenet.proto")

    proto_file = proto_file_path  # Path to your .proto file
    proto_path = proto_dir_path  # Directory to search for imports
    output_dir = dir_path  # Where to place the generated files

    compile_proto(proto_file, proto_path, output_dir)

if __name__ == '__main__':
    main()
