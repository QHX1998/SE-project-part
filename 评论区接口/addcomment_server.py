import time
import grpc
from concurrent import futures
import addcomment_pb2, addcomment_pb2_grpc
import comment

class addcommentservice(addcomment_pb2_grpc.addcommentServicer):
    def add(self, request, ctx):
        message = comment.addcomment(request.token, request.news_id, request. content)
        return addcoment_pb2.output(result = message)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    addcomment_pb2_grpc.add_addcommentServicer_to_server(addcommentservice(),server)
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
