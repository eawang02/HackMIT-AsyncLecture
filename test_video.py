import vimeo

client = vimeo.VimeoClient(
    token='92921aaaaa5a045bda497dff39a51bc9',
    key='dee2969f3618385d60e0b6d50e9f799b2990ddbc',
    secret='sUYsN6kOMQrnYHOaFEri3WDOVo/U49WSIDmPe27LheUa61Vsn1ckKjddGMcW0i0mpDasNSgQVAILqeS2lJOshqEmMAICfHWgbZpJyTQzi6Oj7rOSZjuJ+ff/1SMg5y/X'
  )

about_me = client.get('/me', params={"fields": "uri,name,pictures"})

# https://vimeo.com/747752214, "Chains of Habit"
video = client.get('https://api.vimeo.com/videos/747752214')
print(video.json()['name'])