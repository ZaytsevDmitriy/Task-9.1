import requests
from pprint import pprint
Super_hero_list = ['Hulk', 'Captain America', 'Thanos']

class super_hero():
    def __init__(self, name):
        self.name = name
        # self.intelligence

    def super_hero_request(self):
        name = self.name
        url = ("https://superheroapi.com/api/2619421814940190/search/" + name)

        response = requests.get(url)

        intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
    #  ['results']['powerstats']['intelligence']

        return intelligence

def comparison_intelligence(list):
    hero_dict = {}
    for i in list:
        super_hero1 = super_hero(i)
        hero_dict[super_hero1.super_hero_request()] = super_hero1.name
    cleverest_hero = hero_dict[max(hero_dict.keys())]

    print((f'Самый умный супергерой - {cleverest_hero}'))

comparison_intelligence(Super_hero_list)


# def comparison_intelligence (name1, name2, name3):
#     super_hero1 = super_hero(name1)
#     super_hero1_intelligence = super_hero1.super_hero_request()
#     super_hero2 = super_hero(name2)
#     super_hero2_intelligence = super_hero2.super_hero_request()
#     super_hero3 = super_hero(name3)
#     super_hero3_intelligence = super_hero3.super_hero_request()
#     if super_hero3_intelligence > super_hero2_intelligence \
#             and  super_hero3_intelligence > super_hero1_intelligence:
#         print((f'Самый умный супергерой - {super_hero3.name}'))
#     elif super_hero2_intelligence > super_hero1_intelligence \
#             and super_hero2_intelligence > super_hero3_intelligence:
#         print((f'Самый умный супергерой - {super_hero2.name}'))
#     else:
#         print((f'Самый умный супергерой - {super_hero1.name}'))









