import grpc
import removereply_pb2, removereply_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = removereply_pb2_grpc.removereplyStub(channel = conn)
    response = client.removereply(removereply_pb2.input())

if __name__ == '__main__':
    main()
