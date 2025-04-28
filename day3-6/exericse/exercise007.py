todos =[]
while True:
    user_country =input("enter your country")
    user_country =user_country.strip()

    match user_country:
        case 'america':
            print('Hellow')
        case 'somali':
            print('seetahay')
        case 'india':
            print('namaste')
        case _:
            print('please this country is not recognised')
