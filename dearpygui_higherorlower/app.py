
from tokenize import Number
import dearpygui.dearpygui as dpg
import random

dpg.create_context()
dpg.create_viewport(title='Higher Or Lower', width=600, height=300)

output_id = dpg.generate_uuid()

guesses = 10
number_to_guess = random.randint(1,100)

with dpg.window(label="Example Window"):
    dpg.add_text("Guess the number between 1-100, you have " + str(guesses) + " guesses")
    dpg.add_input_text(label="Guess", default_value="")
    dpg.add_button(label="Confirm", callback = Number)

def Number():
    print("Go higher");
    

with dpg.handler_registry():
    dpg.add_mouse_down_handler

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()