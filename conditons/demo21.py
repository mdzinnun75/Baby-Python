weight = float(input("Weight: "))
weight_scale = input("KG or Pound: ")

if weight_scale.upper() == "L":
    lb_to_kg = weight / 2.20462262
    print(lb_to_kg)

elif weight_scale.upper() == "K":
    kg_to_lb = weight * 2.20462262
    print(kg_to_lb)

else:
    print("invalid input")
