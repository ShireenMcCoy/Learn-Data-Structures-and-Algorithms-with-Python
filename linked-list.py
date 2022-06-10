# Find the nth from last node in a linked list.
# An exercise from the "Learn Data Structures and Algorithms With Python" 
# course on CodeCademy

from LinkedList import LinkedList
# LinkedList is defined in a separate file on codecademy

def nth_last_node(linked_list, n):
  nth_last_pointer = None
  tail_pointer = linked_list.head_node
  count = 1

  while tail_pointer:
    tail_pointer = tail_pointer.get_next_node()
    count += 1

    if count >= n + 1:
      if nth_last_pointer == None:
        nth_last_pointer = linked_list.head_node
      else:
        nth_last_pointer = nth_last_pointer.get_next_node()

  return nth_last_pointer




def generate_test_linked_list():
  linked_list = LinkedList()
  for i in range(50, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list


test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 4)
print(nth_last.value)
