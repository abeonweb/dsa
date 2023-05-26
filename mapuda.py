def mapping():
    """
    Cities to add:
    Bangalore (India, Asia)
    Atlanta (USA, North America)
    Cairo (Egypt, Africa)
    Shanghai (China, Asia)
    :return:
    """
    locations = {
        'North America': {'USA': ['Atlanta', 'Mountain View']},
        'Asia': [{'India': ['Bangalore']}, {'China': ['Shanghai']}],
        'Africa': {'Egypt': ['Cairo']}
    }
    count = 1
    print(count)
    count += 1
    for i in range(len(locations['North America']['USA'])):
        print(locations['North America']['USA'][i])

    print(count)
    for location in locations['Asia']:
        for country in location:
            for city in range(len(location[country])):
                print("%s - %s" % (location[country][city], country))


mapping()
