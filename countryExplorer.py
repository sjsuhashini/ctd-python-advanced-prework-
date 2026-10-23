
from api_fetch import fetch_countries
import processing
import display

   
def process_choice(choice, countries):
    if choice == "1":
        region = input(
            "Enter a region (Africa, Americas, Asia, Europe, Oceania): "
        ).strip()

        if not region:
            print("Region cannot be empty.")
            return

        matches = processing.filter_by_region(countries, region)

        if not matches:
            print("No countries found for that region.")
            return

        print(f"Countries in {region.title()}:")
        display.display_table(matches)

    elif choice == "2":
        top_countries = processing.get_top_countries(countries, "area")

        if not top_countries:
            print("No valid data is available.")
            return

        print("Top 10 countries by area:")
        display.display_table(top_countries)

    elif choice == "3":
        top_countries = processing.get_top_countries(countries, "population")

        if not top_countries:
            print("No valid data is available.")
            return

        print("Top 10 countries by population:")
        display.display_table(top_countries)

    elif choice == "4":
        search_term = input("\nEnter a country name: ").strip()

        if not search_term:
            print("Country name cannot be empty.")
            return

        matches = processing.search_countries(countries, search_term)

        if not matches:
            print("No country matched your search.")
            return

        for country in matches:
            display.display_country(country)
            print()

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

    countries = processing.transform_countries(raw_countries)
   #print(f"Loaded {len(countries)} country records.")
    while True:
        choice = display_menu()

        if choice == "5":
            print("Thank you for using Country Explorer!")
            break

        process_choice(choice, countries)
    
   
if __name__ == "__main__":
    main()




