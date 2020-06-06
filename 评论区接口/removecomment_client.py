import grpc
import removecomment_pb2, removecomment_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = removecomment_pb2_grpc.removecommentStub(channel = conn)
    response = client.removecomment(removecomment_pb2.input())

if __name__ == '__main__':
    main()
