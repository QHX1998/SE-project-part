import grpc
import getreplied_pb2, getreplied_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = getreplied_pb2_grpc.getrepliedStub(channel = conn)
    response = client.getreplied(getreplied_pb2.input())

if __name__ == '__main__':
    main()
