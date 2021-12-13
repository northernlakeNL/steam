import requests

access_token= "eyJhdWQiOiIyM0JLRkwiLCJzdWIiOiI5NVM4RzIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIiLCJleHAiOjE2NDAwMjg3NDAsImlhdCI6MTYzOTQyNDA5N30"

header = {'Authorization' : 'Bearer{}'.format(access_token)}
response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()

print(response)