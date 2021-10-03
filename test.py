import skypy

skypyapi = skypy.skypy()
bazaarapi = skypyapi.bazaar()

print (bazaarapi.fetchProduct("ENCHANTED_POTATO"))
