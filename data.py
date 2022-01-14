import requests, json


def indexFullCollectionByName(name):
	dataAboutCollection = json.loads(requests.get(f"https://api.opensea.io/api/v1/collection/{name}").text)
	if(list(dataAboutCollection.keys())[0] == 'success'):
		print("error, name does not exists")
	else:
		dataAboutCollection = dataAboutCollection['collection']

		address = dataAboutCollection['primary_asset_contracts'][0]['address']
		count = dataAboutCollection['stats']['count']
		traits = dataAboutCollection['traits']
		slug = dataAboutCollection['slug']

		traitCount = 0
		i = 0
		dataToFile = []

		for x in traits:
			traitCount+= len(traits[x])

		t = requests.get(f"https://api.opensea.io/api/v1/assets?asset_contract_address={address}&order_direction=asc&offset={0}&limit=50",headers={"X-API-KEY":"57093273b7a8421399da391f07e8ebd2"}).json()

		for x in range(100):
			print(str(i) + " | " + str(x))
			t = requests.get(f"https://api.opensea.io/api/v1/assets?asset_contract_address={address}&order_direction=asc&offset={i}&limit=50", headers={"X-API-KEY":"57093273b7a8421399da391f07e8ebd2"}).json()
			#print(t)
			i+=50

			for y in t['assets']:
				a = {
	#			'slug': slug,
				'trait_count': traitCount,
				'owner' : y['owner'],
				'image' : y['image_preview_url'],
				'token_id' : y['token_id'],
				'name' : y['name'],
				'traits' : y['traits']
				}
				dataToFile.append(a)
			#data['assets'].extend(t['assets'])

		# with open(f"{name}.json", "w") as f:
		# 	f.write(json.dumps(dataToFile))
	return

indexFullCollectionByName("cryptopunks")