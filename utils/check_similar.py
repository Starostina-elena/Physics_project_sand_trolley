def check_similar(user, generated):
    print(user, generated)
    print(abs(user - float(generated)) / float(generated))
    if abs(user - float(generated)) / float(generated) < 0.15:
        return True
    return False
