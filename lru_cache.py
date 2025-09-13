class Node(object):
  def __init__(self, results):
    self.results = results
    self.prev = None
    self.next = None


class LinkedList(object):

  def __init__(self):
    self.head = None
    self.tail = None

  def append_to_front(self, node):
    if not self.head:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head.prev = node
      self.head = node

  def remove_from_tail(self):
    if not self.tail:
      return
    if self.tail is self.head:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None

  def move_to_front(self, node):
    if node is self.head:
      return
    if node is self.tail:
      self.tail = node.prev
      self.tail.next = None
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
    node.prev = None
    node.next = self.head
    self.head.prev = node
    self.head = node


class Cache(object):

  def __init__(self, max_size):
    self.MAX_SIZE = max_size
    self.size = 0
    self.lookup = {}
    self.linked_list = LinkedList()

  def get(self, query):
    """Get the stored query result from the cache.

            Accessing a node updates its position to the front of the LRU list.
            """
    node = self.lookup.get(query)
    if node is None:
      return None
    self.linked_list.move_to_front(node)
    return node.results


def set(self, query, results):
  """Set the result for the given query key in the cache.

          When updating an entry, updates its position to the front of the LRU list.
          If the entry is new and the cache is at capacity, removes the oldest entry
          before the new entry is added.
          """
  node = self.lookup.get(query)
  if node is not None:
    node.results = results
    self.linked_list.move_to_front(node)
  else:
    if self.size == self.MAX_SIZE:
      self.lookup.pop(self.linked_list.tail.query, None)
      self.linked_list.remove_from_tail()
    else:
      self.size += 1
    new_node = Node(results)
    self.linked_list.append_to_front(new_node)
    self.lookup[query] = new_node
