#-*- coding: utf-8 -*-



class HashTable:
    def __init__(self, elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)

    def _assign_buckets(self, elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key, value))

    def get_value(self, input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    
    def __str__(self) -> str:
        string = ""
        for bucket in self.buckets:
            string += str(bucket)+"\n"
        return string
    
    def __len__(self):
        return self.bucket_size



    
        
    

if __name__ == "__main__":

    hastTab = Hashtable([("coucou", 3), ("salut", 4), ("bonjour", 5)])
    print(hastTab.get_value("coucou"))
    print(hastTab.get_value("salut"))
    print(hastTab.get_value("bonjour"))


    
