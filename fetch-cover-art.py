import discogs_client

print(1)
d = discogs_client.Client('ExampleApplication/0.1',
                          user_token="AugrlbeikovAiGkBIqufmThyfiuRkyNboopdSFWD")
results = d.search(artist='Heptones', type='master', format='LP')
print(1)
#print(dir(results.page(1)))
first = results.page(1)[0]
#print(results.page(1))
image = first.images[0]
print(image['uri'])
#print(dir(image))
