import argparse

def main():
    parser = argparse.ArgumentParser(description='Start the MoveNet ROS2 server.')
    parser.add_argument('-m', '--mock', action='store_true', help='Start the server in mock mode.')
    parser.add_argument('-p', '--port', type=int, help='The port number to run the server on.', default=50051)

    args = parser.parse_args()

    if args.mock:
        from scripts import movenet_server_mock
        print(f"Starting MoveNET Mock Server on port {args.port} ...")
        movenet_server_mock.start_server(port=args.port)
    else:
        from scripts import movenet_server
        print(f"Starting MoveNET Server on port {args.port} ...")
        movenet_server.start_server(port=args.port)

if __name__ == '__main__':
    main()
