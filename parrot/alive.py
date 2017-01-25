
def is_alive(breathing, parrot):
    if not parrot and not breathing:
        raise Exception
    if breathing:
        alive = True
    elif parrot:
        alive = False
    return alive
