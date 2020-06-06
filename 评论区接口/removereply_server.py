import time
import grpc
from concurrent import futures
import removereply_pb2, removereply_pb2_grpc
import comment

class removereplyservice(removereply_pb2_grpc.removereplyServicer):
    def add(self, request, ctx):
        message = comment.removereply(request.token, request.news_id, request.reply_id)
        return addcoment_pb2.output(result = message)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    removereply_pb2_grpc.add_removereplyServicer_to_server(removereplyservice(),server)
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
