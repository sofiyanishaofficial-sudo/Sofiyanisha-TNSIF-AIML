import pandas as pd

product_name = []
category = []
price = []
quantity = []

for i in range(8):
    print("\nProduct", i + 1)

    name = input("Enter Product Name: ")
    cat = input("Enter Category: ")
    pr = float(input("Enter Price: "))
    qty = int(input("Enter Quantity Sold: "))

    product_name.append(name)
    category.append(cat)
    price.append(pr)
    quantity.append(qty)

df = pd.DataFrame({
    "Product Name": product_name,
    "Category": category,
    "Price": price,
    "Quantity Sold": quantity
})

df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("\nProduct Sales Data:")
print(df)

highest_sales = df.loc[df["Total Sales"].idxmax()]
print("\nProduct with Highest Sales:")
print(highest_sales)

print("\nAverage Product Price:", df["Price"].mean())

print("\nProducts with Quantity Sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

print("\nProducts Sorted Based on Total Sales:")
print(df.sort_values("Total Sales"))
