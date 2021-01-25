shopping_list = ["milk" "pasta" "eggs" "spam" "bread" "rice"]

item_to_find = "milk"
found_at = None

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
print("item found at position {}".format(found_at))