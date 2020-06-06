import time
import grpc
from concurrent import futures
import click_news_pb2, click_news_pb2_grpc
import clicknews

class click_newsservice(click_news_pb2_grpc.click_newsServicer):
    def add(self, request, ctx):
        count = clicknews.click_news(request.token, request.news_id)
        return addcoment_pb2.output(result = count)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    click_news_pb2_grpc.add_click_newsServicer_to_server(click_newsservice(),server)
    server.add_insecure_port('127.0.0.1:7777')
    server.start()
    try:
        print("running...")
        time.sleep(1000)
    except KeyboardInterrupt:
        print("stopping...")
        server.stop(0)

if __name__ == '__main__':
    main()
