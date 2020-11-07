def velocity(distance, second):
    li = [distance, second]
    li_in_str = list(map(str, li))
    
    v = distance / second
    return li_in_str

var_velocity = velocity(5.0, 3.32)
print(var_velocity)
