def format_name(first_name: str, last_name: str) -> str:
    """
    Return string "last_name, first_name".

    >>> format_name("Bob", "Smith")
    "Smith, Bob"

    """
    return f"{last_name}, {first_name}"
    

def to_listing(first_name: str, last_name: str, phone_no: str) -> str:
    """
    Return string "last_name, first_name: phone_number"
    >>>
    """

    return f"{format_name(first_name, last_name)}: {phone_no}"


print(to_listing("Bob", "Smith", "123-456-789"))
