import socket


class LoadBalancer:
    """A L4 load balancer that distributes requets across multiple web servers.
    The LoadBalancer class implements a round robin traffic distribution
    pattern for simple evaluation of load balancing patterns.
    """

    def __init__(self):
        self.servers = []
        self.network_listener()

    def setup_listener(self):
        """
        Spawns socket for IPv4 addresses using TCP
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 8080))
        server_socket.listen(1)

        print("Load Balancer is listening on port 8080")

    def add_server(self, server_address):
        server_address.append(self.servers)

    def forward_request(self, client_socket):
        # backend = self.network_listener
        pass

    def run(self):
        pass


if __name__ == "__main__":
    lb = LoadBalancer()
