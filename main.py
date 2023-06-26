def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    celcius = input("Input a temperature in Celcius: ")
    celcius = int(celcius)
    fahrenheit = (9 * celcius / 5) + 32

    print ("Fahrenheit temperature: \t " + str(format(fahrenheit, '.2f')))

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
