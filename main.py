from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Triple Infuse"
owner_name = "Lavilla, Ava Samantha G."

# Integer data type
year_since = 3012

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
savory_products = ["Cucumber Sandwiches", "Turkey Tea with Basil and Mayonnaise Sandwiches", "Mint Cucumber Tomato Sandwiches"]
sweet_products = ["Earl Grey Cookies", "Strawberries n Cream Scones", "Hazelnut Chocolate Chip Scones"]
tea_products = ["Sunburst Tea", "Spiced Apple Tea"]


# Tuple data type
business_hours = ("11:00 AM", "10:00 PM")

# Dictionary data type
menu = {
    "Cucumber Sandwiches": 240.00,
    "Turkey Tea with Basil and Mayonnaise Sandwiches": 270.00,
    "Mint Cucumber Tomato Sandwiches": 230.00,
    "Earl Grey Cookies": 150.00,
    "Strawberries n Cream Scones": 140.00,
    "Hazelnut Chocolate Chip Scones": 130.00,
    "Sunburst Tea": 160.00,
    "Spiced Apple Tea": 120.00
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(savory_products[0], target="prod1")
display(f"₱{menu['Cucumber Sandwiches']:.2f}", target="price1")
display(savory_products[1], target="prod2")
display(f"₱{menu['Turkey Tea with Basil and Mayonnaise Sandwiches']:.2f}", target="price2")
display(savory_products[2], target="prod3")
display(f"₱{menu['Mint Cucumber Tomato Sandwiches']:.2f}", target="price3")

display(sweet_products[0], target="prod4")
display(f"₱{menu['Earl Grey Cookies']:.2f}", target="price4")
display(sweet_products[1], target="prod5")
display(f"₱{menu['Strawberries n Cream Scones']:.2f}", target="price5")
display(sweet_products[1], target="prod6")
display(f"₱{menu['Hazelnut Chocolate Chip Scones']:.2f}", target="price6")

display(tea_products[0], target="prod7")
display(f"₱{menu['Sunburst Tea']:.2f}", target="price7")
display(tea_products[1], target="prod8")
display(f"₱{menu['Spiced Apple Tea']:.2f}", target="price8")


# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"Dine-in Available", target="orderType")
