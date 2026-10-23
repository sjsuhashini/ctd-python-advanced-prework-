
def transform_countries(countries):
    """Extract fields and handle missing or nested values."""

    cleaned_countries = []

    for country in countries:
        languages = country.get("languages") or []
        language_names = []

        if isinstance(languages, list):
            for language in languages:
                if isinstance(language, dict):
                    language_names.append(
                        language.get("name") or "Unknown"
                    )

        cleaned_country = {
            "name": country.get("name") or "Unknown",
            "capital": country.get("capital") or "N/A",
            "region": country.get("region") or "Unknown",
            "population": country.get("population"),
            "area": country.get("area"),
            "languages": ", ".join(language_names) or "N/A",
        }

        cleaned_countries.append(cleaned_country)

    return cleaned_countries


def get_number(country, field):
    """Return a non-negative numeric value or None if invalid."""

    value = country.get(field)

    if isinstance(value, bool):
        return None

    if isinstance(value, (int, float)) and value >= 0:
        return value

    return None

def format_number(value):
    if value is None:
        return "N/A"

    return f"{value:,.0f}"



def filter_by_region(countries, region):
    """Return countries matching a region, ignoring case."""

    return [
        country for country in countries
        if country["region"].casefold() == region.casefold()
    ]


def get_top_countries(countries, field, limit=10):
    """Return countries sorted by a numeric field, highest first."""

    valid_countries = [
        country for country in countries
        if get_number(country, field) is not None
    ]

    return sorted(
        valid_countries,
        key=lambda country: get_number(country, field),
        reverse=True,
    )[:limit]


def search_countries(countries, search_term):
    """Return countries whose names contain the search term."""

    return [
        country for country in countries
        if search_term.casefold() in country["name"].casefold()
    ]
