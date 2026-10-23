
from api_fetch import fetch_countries



# 2. Transform raw API data into clean country records
def transform_countries(countries):
    """Extract fields and handle missing or nested values."""

    cleaned_countries = [] #list of dictionaries for countries with required fields

    for country in countries:
        languages = country.get("languages") or []

        if isinstance(languages, list):
            language_names = []     #list of values for languages
            for language in languages:
                if isinstance(language, dict):
                    language_names.append(
                        language.get("name", "Unknown")
                    )
        else:
            language_names = []

        cleaned_country = {
            "name": country.get("name") or "Unknown",
            "capital": country.get("capital") or "N/A",
            "region": country.get("region") or "Unknown",
            "population": country.get("population"),
            "area": country.get("area"),
            "languages": ", ".join(language_names) or "N/A"
        }

        cleaned_countries.append(cleaned_country)

    return cleaned_countries


# 3. Safely convert numeric fields
def get_number(country, field):
    """Return a numeric value or None if it is missing or invalid."""

    value = country.get(field)

    if isinstance(value, bool):
        return None

    if isinstance(value, (int, float)) and value >= 0:
        return value

    return None


# 4. Format numeric values for readable output
def format_number(value):
    if value is None:
        return "N/A"

    return f"{value:,.0f}"


# 5. Display country information
def display_country(country):
    print(f"Country:    {country['name']}")
    print(f"Capital:    {country['capital']}")
    print(f"Region:     {country['region']}")
    print(f"Population: {format_number(country['population'])}")
    print(f"Area:       {format_number(country['area'])} km²")
    print(f"Languages:  {country['languages']}")


def display_table(countries):
    """Display a compact list of countries."""

    if not countries:
        print("No matching countries found.")
        return

    print(
        f"{'Country':<55}"
        f"{'Population':>18}"
        f"{'Area (km²)':>16}"
    )
    print("-" * 80)

    for country in countries:
        name = country["name"][:54]
        population = format_number(country["population"])
        area = format_number(country["area"])

        print(
            f"{name:<55}"
            f"{population:>18}"
            f"{area:>16}"
        )


# 6. Filter countries by region
def filter_by_region(countries):
    region = input("Enter a region (Africa, Americas, Asia, Europe, Oceania): ").strip()

    if not region:
        print("Region cannot be empty.")
        return

    matches = [
        country for country in countries
        if country["region"].casefold() == region.casefold()
    ]

    if not matches:
        print("No countries found for that region.")
        return

    print(f"Countries in {region.title()}:")
    display_table(matches)


# 7. Find the largest or most populous countries
def show_top_countries(countries, field, label):
    valid_countries = [
        country for country in countries
        if get_number(country, field) is not None
    ]

    if not valid_countries:
        print("No valid data is available.")
        return

    top_countries = sorted(
        valid_countries,
        key=lambda country: get_number(country, field),
        reverse=True
    )[:10]

    print(f"Top 10 countries by {label}:")
    display_table(top_countries)


# 8. Search for a country by name
def search_country(countries):
    search_term = input("\nEnter a country name: ").strip()

    if not search_term:
        print("Country name cannot be empty.")
        return

    matches = [
        country for country in countries
        if search_term.casefold() in country["name"].casefold()
    ]

    if not matches:
        print("No country matched your search.")
        return

    for country in matches:
        display_country(country)


def process_choice(choice, countries): 
    if choice == "1":
        filter_by_region(countries)
    
    elif choice == "2":
        show_top_countries(countries, "area", "area" )

    elif choice == "3":
        show_top_countries(countries, "population", "population")

    elif choice == "4":
        search_country(countries)
  
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")


def display_menu():
    """Display the menu and handle user selections."""
    while True:
        print("=" * 60)
        print("         COUNTRY EXPLORER")
        print("=" * 60)
        print("1. Countries by region   2. Top 10 largest countries   3. Top 10 most populous countries   4. Search for a country   5. Exit")
    
        choice = input("\nChoose an option (1-5): ").strip()
        # if choice == "5":
        #     print("Thank you for using Country Explorer!")
        #     break
        # process_choice(choice, countries)
        return choice


#define main menu
def main():
    print("Welcome to Country Explorer CLI!")
    raw_countries = fetch_countries()
    
    if not raw_countries:
        print("Unable to load country data. Exiting.")
        return

    countries = transform_countries(raw_countries)
   #print(f"Loaded {len(countries)} country records.")
    while True:
        choice = display_menu()

        if choice == "5":
            print("Thank you for using Country Explorer!")
            break

        process_choice(choice, countries)
    
   
if __name__ == "__main__":
    main()




