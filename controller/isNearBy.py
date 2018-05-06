def isNearBy(bl, l):
    """
    bl stand for blank tile location
    l stand for location of pressed tile
    """

    def inRow(bl, l):
        if bl[1] == l[1]:
            return True
        return False

    def inColumn(bl, l):
        if bl[0] == l[0]:
            return True
        return False

    if inColumn(bl, l) and bl[1] == l[1] + 1:
        return "above"
    elif inColumn(bl, l) and bl[1] == l[1] - 1:
        return "below"
    elif inRow(bl, l) and bl[0] == l[0] + 1:
        return "left"
    elif inRow(bl, l) and bl[0] == l[0] - 1:
        return "right"
    else:
        return None


if __name__ == "__main__":
    checkers = [{
        "bl": [1, 2],
        "l": [2, 2],
        "ans": "right"
    }, {
        "bl": [3, 2],
        "l": [3, 1],
        "ans": "above"
    }, {
        "bl": [3, 1],
        "l": [2, 1],
        "ans": "left"
    }, {
        "bl": [1, 2],
        "l": [1, 3],
        "ans": "below"
    }, {
        "bl": [1, 2],
        "l": [2, 3],
        "ans": None
    }]

    for c in checkers:
        print(isNearBy(c["bl"], c["l"]), c["ans"])
