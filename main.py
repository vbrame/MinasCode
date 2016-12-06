from LinkedStack import LinkedStack


def merge_sorted_linked_list(list_a, list_b):
    # get elements
    list_a_element = []
    list_b_element = []
    list_new_element = []

    for i in list_a.data:
        list_a_element.append(i.get_element())
    # sort the stack
    list_a_element.sort()
    for i in list_b.data:
        list_b_element.append(i.get_element())

    # sort the stack
    list_b_element.sort()
    print list_a_element, list_b_element

    while list_a_element and list_b_element:
        if list_a_element[0] > list_b_element[0]:
            list_new_element.append(list_b_element.pop(0))
        else:
            list_new_element.append(list_a_element.pop(0))

    list_new_element = list_new_element + list_a_element + list_b_element
    linked = LinkedStack()
    for i in list_new_element:
        linked.push(i)

    return linked


x = LinkedStack()

x.push(1)
x.push(5)
x.push(16)

x.view()

y = LinkedStack()

y.push(4)
y.push(6)
y.push(19)

y.view()

my_linked_list = merge_sorted_linked_list(y, x)

print my_linked_list.view()
