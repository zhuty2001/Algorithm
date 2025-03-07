def sequential_search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return True
    return False

print(sequential_search([1,2,3],2))