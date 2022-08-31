from typing import List
from threading import Lock

NUMBER_OF_RESPONSES_FOR_ACCEPTED = 3

class BlockProcessor:
    def __init__(self):
        # received_blocks is a dictionary containing the name of the block and the number of times it 
        # has been received
        self.received_blocks = {}
        self.lock = Lock()

    def process_block(self, start_height: int, blocks: List[str]) -> int:
        max_accepted_height = 0
        print("Received blocks before processing:" + str(self.received_blocks))
        print("Processing block: " + str(blocks))
        # We lock the thread so the received_blocks dictionary cannot be changed by another thread
        self.lock.acquire()
        received_list = list(self.received_blocks.keys())
        for block in blocks:
            try:
                received_index = received_list.index(block)
                # If the block index is not the same as the previously stored block, we ignore it.
                # We could instead create a new entry in the dictionary with the new index but that's a 
                # design implementation that would need to be discussed
                if (received_index == blocks.index(block)):
                    received_number = self.received_blocks[block] + 1
                    self.received_blocks[block] = received_number
                    if (received_number >= NUMBER_OF_RESPONSES_FOR_ACCEPTED):
                        max_accepted_height = start_height + received_index
            except ValueError:
                self.received_blocks[block] = 1
        self.lock.release()
        print("Received blocks after processing:" + str(self.received_blocks))
        print("Max accepted height: " + str(max_accepted_height) + "\n\n")
        return max_accepted_height

def main():
    p = BlockProcessor()
    mah = p.process_block(1, ["A", "B", "C", "D"])
    mah = p.process_block(1, ["A", "B", "C", "D"])
    mah = p.process_block(1, ["A", "B", "C"])

if __name__ == "__main__":
    main()