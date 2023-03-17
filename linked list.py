class Node:
    def __init__(self,value):
        self.data=value#initializing
        self.next=None
class linkedlist:
    def add_ele(self,head,value):
        
        new_node=Node(value)#to create node
        temp=head
        while temp.next!=None:#to treaverse till the end
            temp=temp.next
        temp.next=new_node
    def del_ele(self,head):
        temp=head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None        
    def printing_ele(self,head):
        temp=head
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def rev_ele(self,head):
        cur=head
        pre=None
        while(cur!=None):
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre
obj=linkedlist()
head=Node(20)
obj.add_ele(head,10)
obj.add_ele(head,30)
obj.add_ele(head,40)
obj.add_ele(head,50)
obj.add_ele(head,60)
#obj.del_ele(head)
head = obj.rev_ele(head)
obj.printing_ele(head)
print()
