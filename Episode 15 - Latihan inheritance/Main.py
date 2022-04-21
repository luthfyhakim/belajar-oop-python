from Hero import HeroIntelligent, HeroStrength


thv = HeroIntelligent('thv')
jm = HeroStrength('jm')

thv.show_info()
jm.show_info()

thv.gainExp = 200
jm.gainExp = 250

thv.show_info()
jm.show_info()