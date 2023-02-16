def my_bio(first, last, **info):
    info['first_name'] = first
    info['last_name'] = last
    return info
