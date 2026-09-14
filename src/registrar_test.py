import registrar as sut
import grpc
import pytest
import test_util
from unittest.mock import MagicMock
from pytest_mock import MockerFixture
from servicers.echo import EchoServicer


@pytest.fixture
def mocker(pytestconfig): return test_util.mocker(pytestconfig)


def patch_grpc_echo(mocker: MockerFixture):
    stub = mocker.stub()
    mocker.patch("registrar.add_EchoServicer_to_server", new=stub)
    return stub


def assert_registered_echo(echo_stub: MagicMock, mock_server: grpc.Server):
    assert len(echo_stub.call_args_list) == 1
    (servicer, server) = echo_stub.call_args_list[0].args
    assert isinstance(servicer, EchoServicer)
    assert mock_server == server


def test__register_echo(mocker):
    echo_stub = patch_grpc_echo(mocker)
    mock_server = mocker.MagicMock(spec=grpc.Server)

    sut.register_echo(mock_server)

    assert_registered_echo(echo_stub, mock_server)
