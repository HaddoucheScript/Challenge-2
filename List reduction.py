#List reduction 
def list_reduc(list):
    for i in range(len(list)-2):
        list.pop(1)
    print(list)
list_reduc([2,5,6,8,6,9])
