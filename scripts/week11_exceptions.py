def safe_input():
    try:
        return int(input('Enter choice: '))
    except:
        print('Invalid')
        return 0
