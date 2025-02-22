import socket


class LoadBalancer:
    """A L4 load balancer that distributes requets across multiple web servers.
    The LoadBalancer class implements a round robin traffic distribution
    pattern for simple evaluation of load balancing patterns.
    """

    def __init__(self):
        self.backend_server_endpoints = {}
        self.upstream_listener = None

    def setup_listener(self):
        """
        Spawns socket for IPv4 addresses using TCP
        """
        self.upstream_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.upstream_listener.bind(("localhost", 8080))
        self.upstream_listener.listen(4)
        print("Load Balancer is listening on port 8080")

    def add_server(self, server_address):
        server_address.append(self.backend_server_endpoints)

    def forward_request(self, client_socket):
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        backend_socket.connect(("localhost", 5050))

        data = client_socket.recv(4096)
        print(f"Received from client: {data}")
        backend_socket.send(data)

        response = backend_socket.recv(4096)
        print(f"Received from backend: {response}")
        client_socket.send(response)

        backend_socket.close()
        client_socket.close()

    def run(self):
        self.setup_listener()
        while True:
            client_socket, address = self.upstream_listener.accept()
            print(f"Connection from {address}")
            self.forward_request(client_socket)


if __name__ == "__main__":
    lb = LoadBalancer()
    lb.run()
