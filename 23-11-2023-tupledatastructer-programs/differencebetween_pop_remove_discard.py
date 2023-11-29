#pop()

#1).remove on elemnt from the set
#2).syntax:list.pop()
#3).indeing and duplicate values are not allowed
#4).as a sets are unordered,the popped elemnt may not follow any specific order
#5).syntax: list.pop(index postion)--not allowed indexing
#6).you can repeatedly call pop() to remove multiple elements
#7).pop is not supported to frozen sets since they're immutable
#8)if the set is empty calling pop() raises key Error.

#remove()
#1).delete a specified elemnt from the set if it exits
#2).if the element specified in remove() doesn't exit in the set, it raise a keyError
#3).to remove multiple elemnts,remove( needs to be called repeatedly for each element
#4).diffence between remove and discard- 
#unlike discard and remove raises an error if the  specified element is not found in the set
#5.)syntax:set.remove()
#6).hetrogenous values are allowed and duplicate values are not allowed.


#discard()

#1).the discard method remove the specified item from the set
#2).if the specified element is not present in the set,calling discard()
# doesn't raise any error,it simply does nothng
#3).discard work for both immutable and mutable objects similar to remove().
#4).syntax:set.discard()
#5).it delete one element at a time to remove multiple elements,discard(),
#  need to be called repeatedly for each element.
#6).hetrogenous values are allowed and duplicate values are not allowed
#7).incase we can use duplicate values to remove all duplicate values from the set.



