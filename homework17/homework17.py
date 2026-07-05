# ლექციაზე დაწერილ LinkedList კლასში დაამატეთ prepend მეთოდი რომელიც სიის დასაწყისში დაამატებს ახალ ელემენტს.
# ლექციაზე დაწერილ LinkedList კლასში დაამატეთ delete მეთოდი რომელიც გადაცემული მნიშვნელობის მიხედვით წაშლის ელემენტს LinkedList-დან.

class Node:
    def __init__(self, data):
        self.data = data  # ინახავს მონაცემს
        self.next = None  # ინახავს შემდეგი მონაცემის მისამართს, რომელიც თავდაპირველად არის None
       

class LinkedList:
    def __init__(self):
        self.head = None  # ინახავს სიას, რომელიც თავდაპირველად ცარიელია, სანამ არ დავამატებთ პირველ ელემენტს

    def append(self, data):
        """Adds a new node containing 'data' to the very end of the list."""
        new_node = Node(data)
        
        # თუკი სია ცარიელია, ახალი ელემენტი ხდება სიასის თავი
        if not self.head:
            self.head = new_node
            return
        
        # თუ სია არ არის ცარიელი, უნდა გავიდეთ ბოლომდე და დავამატოთ ახალი ელემენტი ბოლოში.
        current = self.head
        while current.next is not None:
            current = current.next
            
        # დავამატოთ ახალი ელემენტი ბოლოში
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        """
        ყველაზე მარტივი გზა linked list-ის მონაცემების გამოსახატად.
        """
        current = self.head
    
        while current is not None:
        # დაბეჭდე მონაცემები და შემდეგი ელემენტის მისამართი
            print(current.data, end=" -> ")
            current = current.next
        # გადაიტანე ფოინთერი შემდეგ ელემენტზე
        
        
    # დაბეჭდე None, რათა გამოიხატოს, რომ სიის ბოლო ელემენტის შემდეგ არაფერი მოდის.
        print("None")

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.display() 

my_list.prepend(0)
my_list.delete(2)
my_list.display()