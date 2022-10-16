def get_group(number):
    sum = 0
    while number != 0:
        number, k = divmod(number, 10)
        sum += k
    return sum

def sort_by_group(n_customers, *n_first_id):
    d = {}

    n_first = 0

    if len(n_first_id) != 0:
        n_first = n_first_id[0]
    
    for i in range(n_first ,n_customers):
        key = get_group(i)
        count = d.setdefault(key, 0)
        d[key] = count + 1    
    

    print(d)

print(get_group(12311))
sort_by_group(5, 1)