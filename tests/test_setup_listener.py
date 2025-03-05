import socket
import pytest
from unittest.mock import patch
from b_load_balancer import LoadBalancer


def test_setup_listener():
    with patch("socket.socket") as mock_socket:
        mock_instance = mock_socket.return_value

        lb = LoadBalancer()
        lb.setup_listener()

        mock_instance.bind.assert_called_with(("localhost", 8080))
        mock_instance.listen.assert_called_with(5)
        assert lb.lb_socket == mock_instance
