arr: list = [i for i in range(6, 11)]
print("Original array:", arr,"\nNew array:", [i+2 for i in arr if i > 5])