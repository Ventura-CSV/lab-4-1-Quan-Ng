def main():

    N = int(input('Enter the number N: '))
    result = [ ]

    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    for num in range(N):
        num = ( 2 ** num)
        result.append(num)
    print(result)
    
    
   
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
