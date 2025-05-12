"""A1 - 015"""
def password(sir,las,age):
    """password"""
    if len(sir) > 5 and len(las) > 5:
        return f"{sir[:2]}{las[-1]}{age[-1]}"
    return f"{sir[0]}{age}{las[-1]}"

print(password(input(),input(),input()))
