from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Возвращает заданной строны ее Pygal код."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return  code
    # Если страна не найдена, вернуть None.
    return None
