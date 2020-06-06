import time
import grpc
from concurrent import futures
import addreply_pb2, addreply_pb2_grpc
import comment

class addreplyservice(addreply_pb2_grpc.addreplyServicer):
    def add(self, request, ctx):
        message = comment.addreply(request.token, request.news_id, request.comment_id, request.content)
        return addcoment_pb2.output(result = message)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    addreply_pb2_grpc.add_addreplyServicer_to_server(addreplyservice(),server)
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
