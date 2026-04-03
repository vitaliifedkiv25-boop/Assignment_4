my_poly = {0: -10, 2: 3, 4: 1}
def evaluate_polynomial(poly_dict, x):
    result = 0
    for p, k in poly_dict.items():
        result = result + k*(x**p)
    return result
result1 = evaluate_polynomial(my_poly,2)
print(result1)
result2 = evaluate_polynomial(my_poly,-1.5)
print(result2)