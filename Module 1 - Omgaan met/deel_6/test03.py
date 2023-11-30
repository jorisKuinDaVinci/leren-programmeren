import random
def get_random_compliment(naam: str) -> str:
    MIJN_COMPLIMENTEN = ("Je doet het goed:", "Je kan het:", "Je bent goed bezig:")
    compliment = random.choice(MIJN_COMPLIMENTEN)
    return f"{compliment} {naam}"

print(get_random_compliment("Joris"))