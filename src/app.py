import functions

print("Please enter at least 2 countries to compare its emissions from using an e-commerce website.")

print("All available countries are listed below:")
df = functions.read_data("../data/ecommerce-website-logs.csv")
print(df['country'].unique())

countries = []
while True:
    country = input("Enter a country code (press Enter when you are done): ")
    if country == "":
        break
    countries.append(country)

if not countries:
    print("No countries entered.")
else:
    df = functions.process_data("../data/ecommerce-website-logs.csv", countries)
    print(df)
    functions.plot_country(df)
    print("Completed! Plot saved in ../figures/country-plot.png")