class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0


    def append(self, item):            
        if len(self.data) < self.capacity:
            self.data.append(item)
        elif len(self.data) == self.capacity:
            
            if self.current == 0:
                self.data.pop(0)
                self.data.insert(0, item)
                self.current += 1
            elif self.current < self.capacity -1:
                self.data.pop(self.current)
                self.data.insert(self.current, item)
                self.current += 1
            elif self.current == 4:
                self.data.pop(self.current)
                self.data.insert(self.current, item)
                self.current = 0
            elif self.current == self.capacity:
                self.data.pop(4)
                self.data.insert(4, item)
                self.current = 0
            print('data', self.data)
            print("current", self.current)
            
        
            


    def get(self):
        return self.data

