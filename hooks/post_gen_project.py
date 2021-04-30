from __future__ import print_function

import os
import random
import shutil
import string

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = '\x1b[0m'
WARNING = '\x1b[1;33m [WARNING]: '
INFO = '\x1b[1;33m [INFO]: '
HINT = '\x1b[3;33m'
SUCCESS = '\x1b[1;32m [SUCCESS]: '


def remove_vue_files():
    file_names = [
        os.path.join('templates', 'index.html')
    ]
    for file_name in file_names:
        os.remove(file_name)
    remove_vue_related_directories()


def remove_vue_related_directories():
    shutil.rmtree(os.path.join('apps', 'client'))
    shutil.rmtree(os.path.join('resources', 'vue'))


def remove_non_vue_files():
    file_names = [
        os.path.join('templates', 'welcome.html')
    ]
    for file_name in file_names:
        os.remove(file_name)
    remove_none_vue_related_directories()


def remove_none_vue_related_directories():
    shutil.rmtree(os.path.join('templates', 'layouts'))


def remove_heroku_files():
    file_names = ['Procfile', 'runtime.txt']
    for file_name in file_names:
        os.remove(file_name)
    remove_heroku_build_hooks()


def remove_heroku_build_hooks():
    shutil.rmtree('bin')


def remove_async_files():
    file_names = [
        os.path.join('config', 'asgi.py')
    ]
    for file_name in file_names:
        os.remove(file_name)


def generate_random_string(
    length, using_digits=False, using_ascii_letters=False, using_punctuation=False
):
    """
    Example:
        opting out for 50 symbol-long, [a-z][A-Z][0-9] string
        would yield log_2((26+26+50)^50) ~= 334 bit strength.
    """
    if not using_sysrandom:
        return None

    symbols = []
    if using_digits:
        symbols += string.digits
    if using_ascii_letters:
        symbols += string.ascii_letters
    if using_punctuation:
        all_punctuation = set(string.punctuation)
        # These symbols can cause issues in environment variables
        unsuitable = {"'", '"', "\\", "$"}
        suitable = all_punctuation.difference(unsuitable)
        symbols += "".join(suitable)
    return "".join([random.choice(symbols) for _ in range(length)])


def set_flag(file_path, flag, value=None, formatted=None, *args, **kwargs):
    if value is None:
        random_string = generate_random_string(*args, **kwargs)
        if random_string is None:
            print(
                "We couldn't find a secure pseudo-random number generator on your system. "
                'Please, make sure to manually {} later.'.format(flag)
            )
            random_string = flag
        if formatted is not None:
            random_string = formatted.format(random_string)
        value = random_string

    with open(file_path, 'r+') as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value


def set_django_secret_key(file_path):
    django_secret_key = set_flag(
        file_path,
        '!!!SET DJANGO_SECRET_KEY!!!',
        length=64,
        using_digits=True,
        using_ascii_letters=True,
    )
    return django_secret_key


def set_flags_in_envs():
    django_secret_key_envs_path = os.path.join('.env')
    set_django_secret_key(django_secret_key_envs_path)


def set_flags_in_settings_files():
    set_django_secret_key(os.path.join('settings', 'development.py'))


def main():
    set_flags_in_envs()
    set_flags_in_settings_files()

    if '{{ cookiecutter.use_vuejs }}'.lower() == 'n':
        remove_vue_files()

    if '{{ cookiecutter.use_vuejs }}'.lower() == 'y':
        remove_non_vue_files()

    if '{{ cookiecutter.use_heroku }}'.lower() == 'n':
        remove_heroku_files()

    if '{{ cookiecutter.use_async }}'.lower() == 'n':
        remove_async_files()

    print(SUCCESS + 'Cookies are ready to eat. 🍪🍪' + TERMINATOR)


if __name__ == '__main__':
    main()
