print('________________________________________________')
print('')
print('      |_   _|  \/  |  __ \     /\   | \ | |     ')
print(' __  __ | | | \  / | |__) |   /  \  |  \| |_  __')
print(' \ \/ / | | | |\/| |  _  /   / /\ \ | . ` \ \/ /')
print('  >  < _| |_| |  | | | \ \  / ____ \| |\  |>  < ')
print(' /_/\_\_____|_|  |_|_|  \_\/_/    \_\_| \_/_/\_\ ')
print('________________________________________________')
print('Введите команды')

import sys

if __name__ == '__main__':
    for param in sys.argv:
        if param == 'create':
            print('Введите настройки сервера:')
            server_name = input('Название сервера: ')
            
