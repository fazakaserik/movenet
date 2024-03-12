from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
from generated import movenet_pb2
from generated import movenet_pb2_grpc

class MovenetServer(movenet_pb2_grpc.MovenetServiceServicer):
    def StreamJointStates(self, request, context):
        # This is just an example implementation
        for i in range(10):
            print("Received request")
            yield movenet_pb2.JointStateMessage(
                header=movenet_pb2.HeaderMessage(
                    stamp=movenet_pb2.HeaderMessage.Time(sec=123, nanosec=456),
                    frame_id="example_frame"
                ),
                name=["joint1", "joint2", "joint3", "joint4", "joint5", "joint6"],
                position=[1.056, -4.142, 2.023, 1.324, -4.981, 2.133],
                velocity=[-0.292, 0.900, -0.727, -0.575, -0.063, -0.274],
                effort=[7.313, -5.952, 3.896, -3.589, -5.907, 5.413]
            )

def start_server(port: int = 50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movenet_pb2_grpc.add_MovenetServiceServicer_to_server(movenet_pb2_grpc.MovenetServiceServicer(), server)

    # Add reflection
    SERVICE_NAMES = (
        movenet_pb2.DESCRIPTOR.services_by_name['MovenetService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Started MoveNET Mock Server on http://127.0.0.1:{port}")
    server.wait_for_termination()