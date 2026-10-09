import random
import platform
import sys

_alternate_screen_active = False


def changeterminal():
    global _alternate_screen_active

    if not sys.stdout.isatty():
        raise RuntimeError("A terminal is required to securely display player words.")

    system = platform.system()
    if system not in ("Windows", "Darwin", "Linux"):
        raise OSError("Terminal clearing is not supported on this operating system.")

    if not _alternate_screen_active:
        sys.stdout.write("\033[?1049h")
        _alternate_screen_active = True
    sys.stdout.write("\033[3J\033[2J\033[H")
    sys.stdout.flush()


def getwords(possiblewords, playerdatabase, playercount):
    global _alternate_screen_active

    selected = random.choice(possiblewords)
    word, hint = next(iter(selected.items()))

    try:
        for i in range(1, playercount + 1):
            changeterminal()
            print(f"Pass the device to {playerdatabase[i]['name']}")
            input("Press enter to continue...\t")

            if playerdatabase[i]["imposter"]:
                print()
                print(f"You are the imposter! Your hint is '{hint}'.")
                input("Once you have memorized your hint, press enter...\t")
            else:
                print()
                print(f"Your word is '{word}'.")
                input("Once you have memorized your word, press enter...\t")
            changeterminal()
    finally:
        if _alternate_screen_active:
            sys.stdout.write("\033[?1049l")
            sys.stdout.flush()
            _alternate_screen_active = False

    return word, hint