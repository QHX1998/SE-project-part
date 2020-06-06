import grpc
import addreply_pb2, addreply_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = addreply_pb2_grpc.addreplyStub(channel = conn)
    response = client.addreply(addreply_pb2.input())

if __name__ == '__main__':
    main()
