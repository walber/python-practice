
class Node:
    def __init__(self, k: int):
        self.val = k
        self.next = None

    def __repr__(self):
        return f'{self.val}'

class SortedLinkedList:
    def __init__(self, l = []):
        self.head = None
        self.tail = None

        for i in l:
            self.insert(i)

    def __repr__(self) -> str:
        c = self.head
        r = "["

        if c:
            r += f'{c}'
            c = c.next

        while c:
            r += f', {c}'
            c = c.next

        r += ']' 

        return r


    def remove(self, k: int) -> None:
        if self.head.val == k:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            c = self.head
            done = False
        
            while not done:
                if c.next:
                    if c.next.val == k:
                        if c.next == self.tail:
                            self.tail = c

                        c.next = c.next.next
                        done = True
                    else:
                        c = c.next
                else:
                    done = True


    def insert(self, k: int) -> None:
        n = Node(k)
        if self.head:
            c = self.head
            
            if c.val >= k:
                n.next = c
                self.head = n
            else:
                done = False
                while not done:
                    if c.next:
                        if c.next.val < k:
                            c = c.next
                        else:
                            if not c.next:
                                self.tail = n

                            n.next = c.next
                            c.next = n
                            done = True
                    else:
                        c.next = n
                        done = True               
        else:
            self.head = n
            self.tail = n

