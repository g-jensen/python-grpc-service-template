# from protos import two_pb2_grpc
# from .servicers.two import TwoServicer

from protos import echo_pb2_grpc
from .servicers.echo import EchoServicer

import grpc
from typing import Callable


def services_to_register():
    return [
        (echo_pb2_grpc.add_EchoServicer_to_server, EchoServicer()),
        # (two_pb2_grpc.add_TwoServicer_to_server, TwoServicer()),
    ]


def register_services(services: tuple[Callable, object], server: grpc.Server):
    for (add_fn, servicer) in services:
        add_fn(servicer, server)
