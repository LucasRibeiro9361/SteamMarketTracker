from genericFuntion import *
import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 2')],
            [sg.Text('Enter something on Row 2'), sg.InputText(),],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    itemName = values[0]
    event, values = window.read()
    itemPricePaid = float( values[0] )

    itemPriceNow = queryItem( itemName )
    priceDifference( itemPricePaid, itemPriceNow[0] )
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break

window.close()

print('Program Closed')