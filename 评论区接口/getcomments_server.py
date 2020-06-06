import time
import grpc
from concurrent import futures
import getcomments_pb2, getcomments_pb2_grpc
import comment

class getcommentsservice(getcomments_pb2_grpc.getcommentsServicer):
    def add(self, request, ctx):
        page = comment.getcomments(request.token, request.news_id)
        return addcoment_pb2.output(result = page)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    getcomments_pb2_grpc.add_getcommentsServicer_to_server(getcommentsservice(),server)
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
