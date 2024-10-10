import win32ui  # pywin32
import dde
import time


class FluidsimDdeClient:
    def __init__(self, server='FLSIMP', topic='IOPanel', item_rx='GET_0', item_tx='SET_0'):
        self.server = server
        self.topic = topic
        self.item_rx = item_rx
        self.item_tx = item_tx

        self.value_rx = 0
        self.value_tx = 0

        self._server_obj = None
        self._conversation = None

    def connect(self):
        # Create DDE Client
        self._server_obj = dde.CreateServer()
        self._server_obj.Create("FLSIMP_Py")

        # Connect to the DDE server
        try:
            self._conversation = dde.CreateConversation(self._server_obj)
            self._conversation.ConnectTo(self.server, self.topic)
        except Exception as e:
            pass

    def disconnect(self):
        # # Disconnect
        try:
            # self._conversation.Disconnect()
            self._server_obj.Shutdown()
        except Exception as e:
            pass

    def update(self):
        # Request data
        try:
            self.value_rx = int(self._conversation.Request(self.item_rx))
            # print(f"Received data: {self.value_rx}")
        except Exception as e:
            print(f"Error in DDE request communication: {e}")
            self.disconnect()
            self.connect()
            # self.value_rx = 0

        # Transmit data
        try:
            # conversation.Poke(item_tx, r'255')
            self._conversation.Poke(self.item_tx, f'{str(self.value_tx)}'.encode('utf-8'))
            # print(f"Data '{data}' successfully sent to {server} {topic} {item}")
        except Exception as e:
            print(f"Error in DDE poke communication: {e}")
            self.disconnect()
            self.connect()


if __name__ == "__main__":
    start_time = time.perf_counter()

    fs_client = FluidsimDdeClient()
    fs_client.connect()

    for i in range(10):
        fs_client.value_tx = i
        fs_client.update()
        time.sleep(0.05)

    fs_client.disconnect()

    print(f'processing time => {(time.perf_counter() - start_time):0.3f}s')