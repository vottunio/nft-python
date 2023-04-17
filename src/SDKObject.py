import requests 
import json
import base64
from io import BytesIO

URLNFTV3 = 'https://api.vottun.tech/nft/v3'
URLIPFS = 'https://ipfsapi.vottun.tech/ipfs/v1'

class SDK:
    def __init__(self, auth, app_id, url_nft, url_ipfs):
        print("Initialize the new instance of Vottun-SDK")
        self.auth = auth
        self.app_id = app_id
        if url_nft == URLNFTV3:
            self.url_nft = url_nft
        else:
            raise ValidationError("Wanted a valid nft URL, got " + url_nft)
        if url_ipfs == URLIPFS:
            self.url_ipfs = url_ipfs
        else:
            raise ValidationError("Wanted a valid ipfs URL, got " + url_ipfs)

    def getAvailableNetworks(self):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}
        response = requests.get(self.url_nft + '/networks', headers=header_data)
        try:
            data = response.json()     
            return data 
        except requests.exceptions.RequestException:
            return response.text

    def getWallets(self):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}
        response = requests.get(self.url_nft + '/vottun/wallets?refresh=kk', headers=header_data)
        try:
            data = response.json()    
            return data 
        except requests.exceptions.RequestException:
            return response.text


    def getTransactionReceipt(self, tx, blockchainNet):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}

        response = requests.get(self.url_nft + '/vottun/transaction/'+ tx + '?network='+ str(blockchainNet), headers=header_data)
        try:
            data = response.json()     
            return data 
        except requests.exceptions.RequestException:
            return response.text

    def createWallet(self):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}
        response = requests.get(self.url_nft + '/vottun/wallet', headers=header_data)
        try:
            data = response.json()    
            return data 
        except requests.exceptions.RequestException:
            return response.text


    def getGasPrice(self, blockchainNet):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}

        response = requests.get(self.url_nft + '/vottun/gasprice?network=' + str(blockchainNet), headers=header_data)
        try:
            data = response.json()     
            print(data)                
        except requests.exceptions.RequestException:
            return response.text

    def getOp(self, operationId):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}

        response = requests.get(self.url_nft + '/operation/'+ operationId , headers=header_data)
        try:
            data = response.json()     
            return data
        except requests.exceptions.RequestException:
            return response.text

    def getBalance(self, address, blockchainNet):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}

        payload = {
            'walletAddress': address,
            'networkId': blockchainNet,
        }
        response = requests.get(self.url_nft + '/balance', json=payload, headers=header_data)
        try:
            data = response.json()     
            return data
        except requests.exceptions.RequestException:
            return response.text

    def getContracts(self):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}

        response = requests.get(self.url_nft + '/contracts' , headers=header_data)
        try:
            data = response.json()     
            return data
        except requests.exceptions.RequestException:
            return response.text

    def mint(self, contractAddress, receiver, ipfsUri, ipfsHash, blockchainNet, royaltyPercentage):
        header_data = { 'Content-Type': 'application/json' ,'Authorization': self.auth, 'x-application-vkn': self.app_id}

        payload = {
            'contractAddress': contractAddress,
            'recipientAddress': receiver,
            'ipfsUri': ipfsUri,
            'ipfsHash': ipfsHash,
            'blockchainNetwork': blockchainNet,
            'royaltyPercentage': royaltyPercentage
        }
        response = requests.post(self.url_nft + '/vottun/mint', json=payload, headers=header_data)
        try:
            data = response.json()     
            return data
        except requests.exceptions.RequestException:
            return response.text

        
    def transfer(self, contract_address, from_wallet, to, tokenId, price, blockchainNet):
        header_data = { 'Content-Type': 'application/json' , 'Authorization': self.auth, 'x-application-vkn': self.app_id}

        payload = {
            'contractAddress': contract_address,
            'from': from_wallet,
            'to': to,
            'tokenId': tokenId,
            'price': price,
            'blockchainNetwork': blockchainNet
        }
        response = requests.post(self.url_nft + '/vottun/transfer', json=payload, headers=header_data)
        try:
            data = response.json()     
            return data
        except requests.exceptions.RequestException:
            return response.text

    def setIpfs(self, imagepath, filename):

        files = {'file': open(imagepath, 'rb'), 'filename': filename}
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}
        
        response = requests.post(self.url_ipfs +'/file/upload', files=files, headers=header_data)
        print(response)                
        try:
            data = response.json()     
            return data
        except requests.exceptions.RequestException:
            return response.text

    def setIpfsMetadata(self, name, imageUri, description, external_url, artist, mediaType, numberTokens):
        header_data = { 'Content-Type': 'application/json' , 'Authorization': self.auth, 'x-application-vkn': self.app_id}

        payload = {"name": name, "image": imageUri, "description": description, "external_url": external_url}
        response = requests.post(self.url_ipfs  +'/file/metadata?name='+ name, json=payload, headers=header_data)
        try:
            data = response.json()     
            return data
        except requests.exceptions.RequestException:
            return response.text

    def getTokenInfo(self, tokenId, blockchainNet, c):
        header_data = {  'Authorization': self.auth, 'x-application-vkn': self.app_id}

        response = requests.get(self.url_nft+ '/vottun/token/'+str(tokenId) +'/info?network=' + str(blockchainNet) +'&c='+c , headers=header_data)
        try:
            data = response.json()
            return data
        except requests.exceptions.RequestException:
            return response.text

    def deployERC721(self, name, symbol, blockchainNetwork, gasLimit):
        header_data = {'Content-Type': 'application/json',
                       'Authorization': self.auth, 'x-application-vkn': self.app_id}
        payload = {
            "name": name,
            "symbol": symbol,
            "blockchainNetwork": blockchainNetwork,
            "gasLimit": gasLimit
        }

        response = requests.post(
            self.url_nft + '/erc721/deploy', json=payload, headers=header_data)

        try:
            data = response.json()
            return data
        except requests.exceptions.RequestException:
            return response.text
    
    def getTokenOwner(self, tokenId, blockchainNet, contract):
        header_data = {'Authorization': self.auth,
                       'x-application-vkn': self.app_id}

        response = requests.get(self.url_nft + '/vottun/contract/'+str(contract) +
                                '/token/' + str(tokenId) + '?network=' + str(blockchainNet), headers=header_data)
        try:
            data = response.json()
            return data
        except requests.exceptions.RequestException:
            return response.text
