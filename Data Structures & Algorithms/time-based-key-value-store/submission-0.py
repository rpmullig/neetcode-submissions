class TimeMap:

    # chaining
    class ListNode:
        def __init__(self, val, key: str):
            self.key = key
            self.val = val
            self.next = None

    def __init__(self):
        self.m = 10
        self.n = 0 
        self.data = [None] * self.m
        self.keys = set()

    def _resize(self):
        self.m *= 2
        expanded_data = [None] * self.m
        for elm in self.data:
            while elm:
                key = elm.key
                idx = hash(key) % self.m
                new_location = expanded_data[idx]
                if not new_location:
                    expanded_data[idx] = self.ListNode(val=elm.val, key=elm.key) 
                else:
                    while new_location.next:
                        new_location = new_location.next
                    new_location.next = self.ListNode(val=elm.val, key=elm.key)
                elm = elm.next
        self.data = expanded_data

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys and (self.n + 1) / self.m >= 0.70:
            self._resize()

        if key not in self.keys:
            self.n += 1
            self.keys.add(key)
        
        add_location = None
        if self.data[hash(key) % self.m]:
            chain = self.data[hash(key) % self.m]
            while chain.next and chain.key != key:
                chain = chain.next
            if chain.key != key:
                chain.next = self.ListNode(val=list(), key=key)
                add_location = chain.next.val
            else:
                add_location = chain.val
        else:
            self.data[hash(key) % self.m] = self.ListNode(val=list(), key=key)
            add_location = self.data[hash(key) % self.m].val


        add_location.append((key, value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        
        loc = self.data[hash(key) % self.m]
        while loc and loc.key != key:
            loc = loc.next

        if not loc:
            return ""

        arr = loc.val
        left, right = 0, len(arr) - 1
        ans = ""
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][2] <= timestamp:
                ans = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans