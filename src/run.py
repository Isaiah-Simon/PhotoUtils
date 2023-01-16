from Commands import Commands
from ColorUtils import bcolors

print(f'{bcolors.HEADER}Available Commands{bcolors.ENDC}')

commands = Commands.get_commands()
for index, command in enumerate(Commands.get_commands()):
    print(f'[{index+1}] {command.description}')
print(f'[0] Exit\n')

while True:
    try:
        selected_option=int(input(f'Select a number from above: {bcolors.ENDC}'))
        if selected_option > len(commands):
            raise ValueError
        break
    except ValueError:
        print(f'{bcolors.FAIL}Invalid option. Please try again.{bcolors.ENDC}')

commands[selected_option-1].command()