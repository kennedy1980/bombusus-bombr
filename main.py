import sys, os
from StructService import Distribution_Service
from config import attack

attack_number_phone=Distribution_Service()
os.system('clear');print('BOMBUSUS Create by Kenned.Y\n')
print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⠋⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⠈⢻⣿⣿⡄⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⣸⣿⡏⠄⠄⠄⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⣿⣿⠁⠄⠄⢰⣿⣿⣯⠁⠄⠄⠄⠄⠄⠄⠄⠈⠙⢿⣷⡄⠄\n\
⠄⠄⣀⣤⣴⣶⣶⣿⡟⠄⠄⠄⢸⣿⣿⣿⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣷⠄\n\
⠄⢰⣿⡟⠋⠉⣹⣿⡇⠄⠄⠄⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠄\n\
⠄⢸⣿⡇⠄⠄⣿⣿⡇⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄\n\
⠄⣸⣿⡇⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠄⠄\n\
⠄⣿⣿⠁⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣧⠄⠄\n\
⠄⣿⣿⠄⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⠄⠄\n\
⠄⣿⣿⠄⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⠄⠄\n\
⠄⢿⣿⡆⠄⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⡇⠄⠄\n\
⠄⠸⣿⣧⡀⠄⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⠃⠄⠄\n\
⠄⠄⠛⢿⣿⣿⣿⣿⣇⠄⠄⠄⠄⠄⣰⣿⣿⣷⣶⣶⣶⣶⠶⠄⢠⣿⣿⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄⠄⠄⠄⠄⣿⣿⡇⠄⣽⣿⡏⠁⠄⠄⢸⣿⡇⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄⠄⠄⠄⠄⣿⣿⡇⠄⢹⣿⡆⠄⠄⠄⣸⣿⠇⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠄⠈⠻⣿⣿⣿⣿⡿⠏⠄⠄⠄⠄\n\
⠄⠄⠄⠄⠄⠄⠄⠈⠛⠻⠿⠿⠿⠿⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n")


target=input('Phone: ')

try:
    attack_number_phone.phone(target)
except Exception as error:
    print(f'Phone - +7666666666')
    sys.exit()

while True:
    try:
        attack_number_phone.random_service()
        attack += 1
        print(f"Query: {attack}")
    except Exception:
        pass

#
