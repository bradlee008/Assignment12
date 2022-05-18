def filter(d, threshold):

    max_key = 0
    max_value = -1

    for key in d:
        if d[key] >= threshold:
            max_key = key
            max_value = d[key]

    return {max_key: max_value}