# TASK: Add type hints using the greetings.pyi file


def greeting(name):
    return 'Hi {}!'.format(name)


def greetings(names):
    return 'Hi {}!'.format(', '.join(names))
