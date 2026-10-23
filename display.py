
def format_number(value):
    """Format a number with thousands separators."""

    if value is None:
        return "N/A"

    return f"{value:,.0f}"


def display_country(country):
    """Display details for a single country."""

    print(f"Country:    {country['name']}")
    print(f"Capital:    {country['capital']}")
    print(f"Region:     {country['region']}")
    print(f"Population: {format_number(country['population'])}")
    print(f"Area:       {format_number(country['area'])} km²")
    print(f"Languages:  {country['languages']}")


def display_table(countries):
    """Display a compact table of countries."""

    if not countries:
        print("No matching countries found.")
        return

    print(
        f"{'Country':<55}"
        f"{'Population':>18}"
        f"{'Area (km²)':>16}"
    )
    print("-" * 89)

    for country in countries:
        name = country["name"][:54]
        population = format_number(country["population"])
        area = format_number(country["area"])

        print(f"{name:<55}{population:>18}{area:>16}")


def display_menu():
    """Display the menu and return the user's choice."""

    print("=" * 60)
    print("         COUNTRY EXPLORER")
    print("=" * 60)
    print("1. Countries by region")
    print("2. Top 10 largest countries")
    print("3. Top 10 most populous countries")
    print("4. Search for a country")
    print("5. Exit")

    return input("\nChoose an option (1-5): ").strip()
