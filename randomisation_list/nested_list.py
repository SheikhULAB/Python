#IndexOutOfRange error
#Lets say we have a list l with number of elements n
#index of left most element is 0 and index of last element is n-1 
#If you try to print element at index [n] you get the error as last element in the list was present at index n-1.
#NESTED LISTS
dirty_dozen=["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]
fruits=["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables=["Spinach","Kale","Celery","Potatoes"]
nested_list=[fruits,vegetables]

print(nested_list)
