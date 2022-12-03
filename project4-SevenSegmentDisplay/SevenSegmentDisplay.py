'''
A seven-segment display is a type of LCD
component used to display numbers in
pocket calculators, microwave ovens, and
other small electronic devices. Through different
combinations of seven line-shaped segments in an
LCD, a seven-segment display can represent the digits
0 through 9. They look like this:
 __     __  __        __   __ __   __   __
|  | |  __| __| |__| |__  |__   | |__| |__|
|__| | |__  __|    |  __| |__|  | |__|  __|
''' 
def get_sevensegmentdiaplay(number,width=3):
    final_number = number.zfill(width)
    result=['','','']
    for i,x in enumerate(final_number):
        match x:
            case '.':
                result[0]+=' '
                result[1]+=' '
                result[2]+='.'
            case '1':
                result[0]+='    '
                result[1]+='  | '
                result[2]+='  | '
            case '2':
                result[0]+=' __ '
                result[1]+=' __|'
                result[2]+='|__ '
            case '3':
                result[0]+=' __ '
                result[1]+=' __|'
                result[2]+=' __|'            
            case '4':
                result[0]+='    '
                result[1]+='|__|'
                result[2]+='   |'
            case '5':
                result[0]+=' __ '
                result[1]+='|__ '
                result[2]+=' __|'
            case '6':
                result[0]+=' __ '
                result[1]+='|__ '
                result[2]+='|__|'
            case '7':
                result[0]+=' __ '
                result[1]+='   |'
                result[2]+='   |'
            case '8':
                result[0]+=' __ '
                result[1]+='|__|'
                result[2]+='|__|'
            case '9':
                result[0]+=' __ '
                result[1]+='|__|'
                result[2]+=' __|'            
            case '0':
                result[0]+=' __ '
                result[1]+='|  |'
                result[2]+='|__|' 
        #add space if the current character is not the last
        if i != len(final_number):
            result[0]+=' '
            result[1]+=' '
            result[2]+=' '                   

    return "\n".join(result)         
            


if __name__ == "__main__":
    print()
    print("_________________________SEVEN SEGMENT DISPLAY______________________")
    indigo = input("number(integer or floating point):> ")
    print("using a default width of 3....")
    print(get_sevensegmentdiaplay(indigo))


                        
