import grpc
import like_pb2, like_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = like_pb2_grpc.likeStub(channel = conn)
    response = client.like(like_pb2.input())

if __name__ == '__main__':
    main()
