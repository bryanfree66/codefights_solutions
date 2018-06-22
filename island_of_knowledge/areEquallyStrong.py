def get_strongest(left, right):
    return max(left, right)


def get_weakest(left, right):
    return min(left, right)


def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    your_strongest = get_strongest(yourLeft, yourRight)
    your_weakest = get_weakest(yourLeft, yourRight)
    friends_strongest = get_strongest(friendsLeft, friendsRight)
    friends_weakest = get_weakest(friendsLeft, friendsRight)
    if your_strongest == friends_strongest and your_weakest == friends_weakest:
        return True
    return False
