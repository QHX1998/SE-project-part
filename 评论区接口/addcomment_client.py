import grpc
import addcomment_pb2, addcomment_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = addcomment_pb2_grpc.addcommentStub(channel = conn)
    response = client.addcomment(addcomment_pb2.input())

if __name__ == '__main__':
    main()
