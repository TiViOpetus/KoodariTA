# MAIN APPLICATION 

# Ask user name
firstName = 'Mika'
likeCats = input('Pidätkö kissoista? (k/e)')
print('Morjensta', firstName)

if likeCats == 'k':
    print('Olet kissaihminen')

def nameLength(name):
    """Calculates length of the name

    Args:
        name (str): name of the person

    Returns:
        int: length of the name 
    """
    length = len(name)
    return length

# Calculate name lenght
length = nameLength(firstName)
print(firstName, 'sanassa on', length, 'kirjainta')