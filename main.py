import colorama  # type: ignore

# region Step 0: Setup for colored terminal printing
colorama.init()


def p(message: str) -> None:
    print('\n{}'.format(colorama.Fore.LIGHTGREEN_EX + message))
# endregion

