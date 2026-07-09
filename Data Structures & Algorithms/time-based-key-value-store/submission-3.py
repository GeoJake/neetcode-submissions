class TimeMap:

    def __init__(self):
        self.t_map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t_map:
            self.t_map[key] = []
        self.t_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:        
        closest, val_arr = "", self.t_map.get(key, [])
        l, r = 0, len(val_arr) - 1
        while l <= r:
            m = l + ((r-l)//2)
            if timestamp >= val_arr[m][1]:
                closest = val_arr[m][0]
                l = m + 1
            else:
                r = m - 1

        return closest
