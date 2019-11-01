import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(ws, message):
    print (message)

def on_error(ws, error):
    print (error)

def on_open(ws):
    print("opened")
    def run(*args):
        ws.send("wazza")
        ws.close()
    thread.start_new_thread(run, ())

def on_close(ws):
    print("closed")

def initiate():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws/v1/guard/live/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()

if __name__ == "__main__":
    initiate()
