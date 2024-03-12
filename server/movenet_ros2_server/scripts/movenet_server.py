import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import JointState

from moveit.planning import MoveItPy
from moveit_configs_utils import MoveItConfigsBuilder

from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
from generated import movenet_pb2
from generated import movenet_pb2_grpc
import google.protobuf.empty_pb2

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

    def Plan(self, request, context):
        # Mock implementation for Plan
        print("Planning...")
        return google.protobuf.empty_pb2.Empty()

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            'joint_states',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg: JointState):
        self.get_logger().info(f"x={msg.position[0]}\ty={msg.position[1]}\tz={msg.position[2]}")

def start_server(port: int = 50051):
    moveitpy = MoveItPy()
    trajactory_execution_manager = moveitpy.get_trajactory_execution_manager()
    trajactory_execution_manager.execute_and_wait()

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

def main2(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()