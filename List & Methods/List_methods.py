items = ["apple","banana","orange"]
# print(len(items))   #Use the len() function to get the number of elements in a list.

# items.append("strawberries")  #append() Adds an element to the end of the list.
# items.insert(1,"strawberries")  #insert() Inserts an element at a specific index.
# items.append(["more bananas","pineapples"])
# items.remove("apple")  #remove() Removes the first occurrence of a value.
# items.pop(0)  #pop() Removes and returns an element at a given index. If no index is provided, it removes the last element.
# items.clear() #clear() Removes all elements from the list
# print(items.index("banana"))  #index() Returns the index of the first occurrence of a value
# print(items.count("banana")) #count() Counts how many times a value appears in the list.

print(items)

numbers = [23,3,56,90,5,7,9,20,10,0]
numbers.sort(reverse=True)  #sort() Sorts the list in ascending order   #reverse() Reverses the order of elements in the list.
print(numbers)





# print(items)
# items[1] = "grapes"   #Lists are mutable, which means their values can be changed
# print(items)       #List elements are accessed using indexes