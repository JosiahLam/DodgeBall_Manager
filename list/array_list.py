# Copyright 2023, Oliver S. Schneider
# Copyright 2013, Michael H. Goldwasser
#
# Adapted from the Dynamic Array object, which was
# developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ctypes                                      # provides low-level arrays

class ArrayList:
  """ ArrayList
    A simplified List implemented using an array.
    Uses explicit "get" and "set" functions rather
    than sequence indexing notation.
  """

  def __init__(self):
    """Create an empty array."""
    self._n = 0                                    # count actual elements
    self._capacity = 1                             # default array capacity
    self._A = self._make_array(self._capacity)     # low-level array
  

  ###################
	#    Accessors    #
	###################

  def length(self) -> int:
    """Return number of elements stored in the array."""
    return self._n
  
  def contains(self, value, map_to_key=lambda x : x) -> bool:
    """ contains
      Returns True if value is in the list, False otherwise
      
      map_to_key: an optional mapping function from the stored
        object type to the key to compare with.
    """
    return self.find_index_byvalue(value, map_to_key=map_to_key) >= 0


  def find_index_byvalue(self, value, map_to_key=lambda x : x) -> int:
    """ find_index_byvalue
      Returns the first index of value, or -1 if not found
      
      value: .the value to find as an object,
        or the key to compare to (if using map_to_key)

      map_to_key: an optional mapping function from the stored
        object type to the key to compare with.
    """
    for i in range(self.length()):
      if map_to_key(self.get(i)) == value:
        return i
    return -1
  

    
  def get(self, k : int) -> object:
    """Return element at index k."""
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]                              # retrieve from array
  

  ##################
	#    Mutators    #
	##################

  def set(self, k, value):
    """Set element at index k"""
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    self._A[k] = value


  def append(self, obj):
    """Add object to end of the array."""
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    self._A[self._n] = obj
    self._n += 1

  def _resize(self, c):                            # nonpublic utitity
    """Resize internal array to capacity c."""
    B = self._make_array(c)                        # new (bigger) array
    for k in range(self._n):                       # for each existing value
      B[k] = self._A[k]
    self._A = B                                    # use the bigger array
    self._capacity = c

  def _make_array(self, c):                        # nonpublic utitity
    """Return new array with capacity c."""   
    return (c * ctypes.py_object)()               # see ctypes documentation

  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
    if self._n == self._capacity:                  # not enough room
      self._resize(2 * self._capacity)             # so double capacity
    for j in range(self._n, k, -1):                # shift rightmost first
      self._A[j] = self._A[j-1]
    self._A[k] = value                             # store newest element
    self._n += 1

  def remove(self, k : int) -> object:
    """Remove the value at index k, returning it
    """
    # note: we do not consider shrinking the dynamic array in this version
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    removed_value = self._A[k]
    for j in range(k, self._n - 1):    # shift others to fill gap
      self._A[j] = self._A[j+1]
    self._A[self._n - 1] = None        # help garbage collection
    self._n -= 1                       # we have one less item
    return removed_value               # exit immediately



	#################
	#    Sorting    #
	#################

  def _swap(self, i : int, j : int):
    """_swap
      Private helper function to swap two objects in place.
      Intended to help with sorting algorithms
    """

    # check if both indices are within range
    if not 0 <= i < self._n:
      raise IndexError("i is out of index range")
    if not 0 <= j < self._n:
      raise IndexError("j is out of index range")
    
    # swaps the items from location i to location j
    tmp = self._A[i]
    self._A[i] = self._A[j]
    self._A[j] = tmp



  def sort(self, map_to_key=lambda x : x, descending=False):
    """ sort
      Sorts the list in-place using mergesort algorithm.
      Default is to sort in ascending order.

      map_to_key: an optional mapping function from the stored
        object type to the key to sort by with.

      descending: an optional boolean to declare if the sort
      should be descending rather than ascending.
    """
    #######################
    #   _selection_sort   #
    #######################
    n = self.length()
    
    if descending == False: #ascending order
      for i in range(n):
          # Find the minimum element in the remaining unsorted array
          min_index = i
          for j in range(i + 1, n):
              if map_to_key(self.get(j)) < map_to_key(self.get(min_index)):
                  min_index = j

          # Swap the found minimum element with the first element
          self._swap(i,min_index)
                      
    elif descending == True: #descending order
        for i in range(n-1):
          # Find the minimum element in the remaining unsorted array
          max_index = i
          for j in range(i + 1, n):
              if map_to_key(self.get(j)) > map_to_key(self.get(max_index)):
                  max_index = j

          # Swap the found maximum element with the first element
          self._swap(i,max_index)   

    return self._A
