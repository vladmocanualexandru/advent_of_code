def organize(jsonArray, field):
    result = {}
    for entry in jsonArray:
        result[entry[field]] = {}
        for property in entry:
            if property != field:
                result[entry[field]][property] = entry[property]

    return result