class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.maps = {}
        self.arrs = []

    def get(self, key: int) -> int:
        for i, v in enumerate(self.arrs):
            if v == key:
                self.arrs.pop(i)
                self.arrs.append(key)
                break
 
        return self.maps.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.maps[key] = value
            for i, v in enumerate(self.arrs):
                if v == key:
                    self.arrs.pop(i)
                    self.arrs.append(key)
                    break
            return
        if len(self.arrs) == self.capacity:
            removeKey = self.arrs.pop(0)
            if removeKey in self.maps:
                self.maps.pop(removeKey)
        self.arrs.append(key)
        self.maps[key] = value
        

            
