import grpc

from protos.echo_pb2_grpc import add_EchoServicer_to_server
from servicers.echo import EchoServicer
def register_echo(server: grpc.Server):
    add_EchoServicer_to_server(EchoServicer(), server)
