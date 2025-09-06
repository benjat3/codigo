import random, sys, time
WIDTH = 70 #the number of columns

try:
    # For each column, when te counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # shuld be displayed in that column
    columns = [0]*WIDTH
    while True:
        #Loop over each column:
        for i in range(WIDTH):
            if random.random() < 0.05:
                # Restart a stream counter on this column.
                # The stream length is between 4 and 14 characters long.
                columns[i] = random.randint(4,14)

            # Print a character in this column
            if columns[i] == 0:
                # Change this to ' ' to '.' to see the empty spaces:
                print(' ', end='')
            else:
                # Print a 0 or 1:
                print(random.choice([0,1]), end='')
                columns[i] -= 1 # Decrement the counter for this column.
        print() #Print a new line at the end of the row of columns.
        time.sleep(0.1) #Each roow pauses for one tenth of a second
except KeyboardInterrupt:
    sys.exit() #When Ctrl-c is pressed, end the program.
