#Sangram S.S Assignment-6
def ds(roll_no, name):
    # Tuple
    t_ds = (roll_no, name)
    print("orignal tuple is",t_ds)
    new_no=int(input("Enter the new roll_no"))
    new_name=input("Enter the name")
    t_ds=(new_no,new_name)
    print("The updation in tuple during runtime is",t_ds)
    del t_ds
    
    
    # List
    l_ds = [roll_no, name]
    print("orignal tuple is",l_ds)
    new_no=int(input("Enter the new roll_no"))
    new_name=input("Enter the name")
    l_ds=[new_no,new_name]
    print("The updation in list during runtime is",l_ds)
    del l_ds

    
    # Set
    s_ds = {roll_no, name}
    print("orignal tuple is",s_ds)
    new_no=int(input("Enter the new roll_no"))
    new_name=input("Enter the new name ")
    s_ds={new_no,new_name}
    print("The updated set during runtime is",s_ds)
    del s_ds
    
    # Dictionary
    d_ds = {"roll_no": roll_no, "name": name}
    print("orignal tuple is",d_ds)
    new_no=int(input("Enter the new roll_no"))
    new_name=input("Enter the new name ")
    d_ds={new_no,new_name}
    print("The updation in dictonary during runtime is",d_ds)
    del d_ds

    return l_ds, t_ds, s_ds, d_ds
roll_no = 98
name = "Sangram S.S"

result = ds(roll_no, name)
print(result)
# orignal tuple is (98, 'Sangram S.S')
# Enter the new roll_no45
# Enter the nameKaran
# The updation in tuple during runtime is (45, 'Karan')
# orignal tuple is [98, 'Sangram S.S']
# Enter the new roll_no77
# Enter the namePriyaj
# The updation in list during runtime is [77, 'Priyaj']
# orignal tuple is {'Sangram S.S', 98}
# Enter the new roll_no87
# Enter the new name Darshan
# The updated set during runtime is {'Darshan', 87}      
# orignal tuple is {'roll_no': 98, 'name': 'Sangram S.S'}
# Enter the new roll_no12
# Enter the new name Vijay
# The updation in dictonary during runtime is {'Vijay', 12}








   




    
 