my_list = [1,2,3]

def add_to_my_list(lsp, add):
    nl = lsp.copy()
    nl.append(add)
    return nl

new_list = add_to_my_list(my_list, 4)

print(my_list)
print(new_list)
