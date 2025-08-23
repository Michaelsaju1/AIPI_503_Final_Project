import functions

print("Please enter 2 countries to compare its emissions from using an e-commerce website.")
print("CA, MX, AT, NO, IT, RU, JP")
country1 = input("Enter country 1: ")
country2 = input("Enter country 2: ")

df = functions.read_and_process_data("../data/ecommerce-website-logs.csv", country1, country2)

print("Completed!")