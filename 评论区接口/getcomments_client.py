import grpc
import getcomments_pb2, getcomments_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = getcomments_pb2_grpc.getcommentsStub(channel = conn)
    response = client.getcomments(getcomments_pb2.input())

if __name__ == '__main__':
    main()
