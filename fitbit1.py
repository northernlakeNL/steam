import requests
import fitbit1
import gather_keys_oauth2 as Oauth2
import datetime

OAuth_code = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM0JLRkwiLCJzdWIiOiI5NVM4RzIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd251dCB3cHJvIHdzbGUgd3dlaSB3c29jIHdzZXQgd2FjdCB3bG9jIiwiZXhwIjoxNjQwMDQxNjU5LCJpYXQiOjE2Mzk0MzY4NTl9.NVC5NcvyKJiV5LWANI8O8PhWFj0TnGp_FRlVhGQvTZw"

header = {'Authorization' : 'Bearer{}'.format(OAuth_code)}
response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()

print(response)