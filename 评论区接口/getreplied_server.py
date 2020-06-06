import time
import grpc
from concurrent import futures
import getreplied_pb2, getreplied_pb2_grpc
import comment

class getrepliedservice(getreplied_pb2_grpc.getrepliedServicer):
    def add(self, request, ctx):
        page = comment.getreplied(request.token, request.news_id, request.comment_id)
        return addcoment_pb2.output(result = page)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    getreplied_pb2_grpc.add_getrepliedServicer_to_server(getrepliedservice(),server)
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
