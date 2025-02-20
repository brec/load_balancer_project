import socket


class LoadBalancer:
    """A L7 load balancer that distributes requets across multiple web servers.
    The LoadBalancer class implements a round robin traffic distribution
    pattern for simple evaluation of load balancing patterns.
    """

    def __init__(self):
        self.servers = []
        self.network_listener()

    def network_listener(self):
        """
        Spawns socket for IPv4 addresses using TCP
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 8080))
        server_socket.listen(1)

        print("Load Balancer is listening on port 8080")

        client_socket, address = server_socket.accept()
        print(
            f"Load balancer has opened a socket with source "
            f"and destination info: {client_socket}"
        )

    def add_server(self, server_address):
        pass

    def round_robin(self):
        pass


if __name__ == "__main__":
    lb = LoadBalancer()
