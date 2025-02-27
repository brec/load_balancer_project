import socket
import pytest
from unittest.mock import patch
from load_balancer import setup_listener


def test_setup_listener():
    with patch("socket.socket") as mock_socket:
        lb = YourClass()
        lb.setup_listener()

        assert mock_instance.bind.called
        assert mock_instance.listen.called

        assert lb.lb_socket == mock_instance

    assert setup_listener()
