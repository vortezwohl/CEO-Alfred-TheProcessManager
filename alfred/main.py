import sys

from colorama import Style, Fore

from process_manager.agent import process_manager
from alfred.action import find_information_about_the_assistant

process_manager.grant_ability(find_information_about_the_assistant)
sys.set_int_max_str_digits(10**8)


def main():
    if len(sys.argv) > 1:
        query = ''
        for arg in sys.argv[1:]:
            query += arg
        process_manager.assign(query)
    try:
        print(f'{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}Alfred: {Style.RESET_ALL}', flush=True, end='')
        process_manager.just_do_it()
    except KeyboardInterrupt:
        pass
    exit(0)


if __name__ == "__main__":
    main()
