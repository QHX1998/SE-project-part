import time
import grpc
from concurrent import futures
import like_pb2, like_pb2_grpc
import comment

class likeservice(like_pb2_grpc.likeServicer):
    def add(self, request, ctx):
        message= comment.like(request.token, request.news_id, request.id)
        return addcoment_pb2.output(result = message)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    like_pb2_grpc.add_likeServicer_to_server(likeservice(),server)
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
