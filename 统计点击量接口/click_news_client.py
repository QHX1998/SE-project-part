import grpc
import click_news_pb2, click_news_pb2_grpc
import comment

_host = 'localhost'
_port = '8080'

def main():
    conn = grpc.insecure_channel(_host + ':' + _port)
    client = click_news_pb2_grpc.click_newsStub(channel = conn)
    response = client.click_news(click_news_pb2.input())

if __name__ == '__main__':
    main()
