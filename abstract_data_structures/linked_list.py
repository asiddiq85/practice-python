class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e


## printing all the element values of a linked list
def print_all_elements():
    current = a
    while current:
        print(current.value)
        current = current.next_node


# print_all_elements()

def remove_head():
    head = a.next_node
    return head


def delete_value(value):
   pass


# def reverse_linked_list(head):
#     current = head
#     nextnode = None
#     previous = None
#
#
#     while current:
#         nextnode = current.next_node
#         previous = current
#         current = current.next_node
#
#
#     return current


def category_price(object_fields, value):
    return_obj = {}
    if object_fields[0] in ['dutiablePrice', 'salePrice']:
        return_obj['ccyfield'] = 'dutiablePriceCurrency' if object_fields[0] == 'dutiablePrice' else 'salePriceCurrency'
        parts = value.split(' ')
        if len(parts) > 1:
            return_obj['obj_ccyfield'] = parts[1]
        return_obj['obj_obj_fields_0'] = parts[0]
    else:
        return_obj['obj_obj_fields_0'] = value

    return return_obj


class C:

    def __init__(self):
        pass

    def t(self):
        return self.__class__.__name__

c = C()

print(c.t())