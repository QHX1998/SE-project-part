import time
import grpc
from concurrent import futures
import removecomment_pb2, removecomment_pb2_grpc
import comment

class removecommentservice(removecomment_pb2_grpc.removecommentServicer):
    def add(self, request, ctx):
        message = comment.removecomment(request.token, request.news_id, request.comment_id)
        return addcoment_pb2.output(result = message)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    removecomment_pb2_grpc.add_removecommentServicer_to_server(removecommentservice(),server)
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
