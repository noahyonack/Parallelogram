import helpers
import threading
import Queue
import cloudpickle as pickle
import time

class Server(threading.Thread):
    '''
    Server class that should be run on each machine that wants to act as a 
    computational entity for the system. Extends threading. Thread to make the 
    server threaded and thus nonblocking
    '''
    def __init__(self, port):
        '''
        Initializes server listening on given port
        :param port: port that server should listen on
        '''
        self.queue = Queue.Queue()
        self.port = port
        self._abort = False
        threading.Thread.__init__(self)

    def run(self):
        '''
        Runs core loop of server. It continually listens on a port and waits 
        until it receives a message, which is added to the queue. The server 
        then determines the type of operation wanted, processes the chunk, 
        and sends the results back to the calling client. It continues to 
        process these commands until the queue is empty, at which point it 
        returns to waiting
        '''
        #infinite looping listening thread
        self.sstr = helpers._Server_Socket_Thread_Receive(self.port, self.queue)
        self.sstr.start()
        #infinitely loops until calling process calls stop()
        while not self._abort:
            if not self.queue.empty():
                dict_received = pickle.loads(self.queue.get())
                chunk = dict_received['chunk']
                func = dict_received['func']
                op = dict_received['op']

                if op == 'map':
                    processed_chunk = helpers._single_map(func, chunk)
                elif op == 'filter':
                    processed_chunk = helpers._single_filter(func, chunk)
                elif op == 'reduce':
                    processed_chunk = helpers._single_reduce(func, chunk)
                # TODO: raise an error here
                else:
                    processed_chunk = 'This operation does not exist.'
                
                dict_sent = {
                    'chunk': processed_chunk, 
                    'index': dict_received['index']
                }

                #sends results back on port+1
                #todo: find more elegant way of agreeing on a response port
                self.ssts = threading.Thread(
                    target = helpers._server_socket_thread_send, 
                    args = (self.port + 1, pickle.dumps(dict_sent))
                )
                self.ssts.start()
        self.sstr.stop() #nicely close sockets at the end


    def stop(self):
        self._abort = True

if __name__ == '__main__':
    a = Server(1001)
    a.start()