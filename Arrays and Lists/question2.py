while True:
    date = input('Please enter the date in the form of dd/mm/yyyy: ')

    if len(date.split('/')) == 3:
        day = date.split('/')[0]
        month = date.split('/')[1]
        year = date.split('/')[2]

        if day.isdigit() and month.isdigit() and year.isdigit():
            print('Date: ', day)
            print('Month: ', month)
            print('Year: ', year)
            break