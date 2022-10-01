
import vimeo

client = vimeo.VimeoClient(
    token='c036cd8338653e5c7cf87d92b4660ea4',
    key='dee2969f3618385d60e0b6d50e9f799b2990ddbc',
    secret='sUYsN6kOMQrnYHOaFEri3WDOVo/U49WSIDmPe27LheUa61Vsn1ckKjddGMcW0i0mpDasNSgQVAILqeS2lJOshqEmMAICfHWgbZpJyTQzi6Oj7rOSZjuJ+ff/1SMg5y/X'
  )

response = client.get(uri)
print(response.json())