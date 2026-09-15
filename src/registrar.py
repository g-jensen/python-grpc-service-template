import grpc
from typing import Callable

from .protos.echo_pb2_grpc import add_EchoServicer_to_server
from .servicers.echo import EchoServicer


def services_to_register():
    return [
        (add_EchoServicer_to_server, EchoServicer()),
    ]


def register_services(services: tuple[Callable, object], server: grpc.Server):
    for (add_fn, servicer) in services:
        add_fn(servicer, server)