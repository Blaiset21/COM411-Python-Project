import Basics.Output.simple_message as simple_message
import Basics.Output.multiline_message as multiline_message
import Basics.Output.ascii_robot as ascii_robot
import Basics.Output.data_types as data_types
import Basics.Output.escape_characters as escape_characters

def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "ascii robot":
        ascii_robot.run()
    elif response == "data types":
        data_types.run()
    elif response == "escape characters":
        escape_characters.run()

def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()