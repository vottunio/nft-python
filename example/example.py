### Check the READMe.md file to know the details of the parameters

from SDKObject import SDK
TOKEN = '<your token here>'
APP_ID = '<your app_id here>'
URLNFT = 'https://api.vottun.tech/nft/v3'
URLIPFS = 'https://ipfsapi.vottun.tech/ipfs/v1'

#Two parameters are required to instantiate a objectSDK of Vottun:
    # - Token: the jwt token to authenticate the user to the server
    # - APP_ID: a required identifier to API which enables to provide different services from Vottun

objectSDK = SDK(auth= TOKEN, app_id= APP_ID, url_nft=URLNFT, url_ipfs=URLIPFS)
# The instatiation will print a message: Initialize the new instance of Vottun-SDK"
# Then you can proceed to make calls

#Return a list of available networks where to operate
res = objectSDK.getAvailableNetworks()
print(res)

#Return a ethereum wallet with the publickey and privatekey
res = objectSDK.createWallet()
print(res)

#Return a list of ethereum wallet with the publickey and privatekey
res = objectSDK.getWallets()
print(res)

#This method allows the user to know the current gasprice of the network, usefull in Ethereum main network as gasprice fluctuate significantly
res = objectSDK.getGasPrice(blockchainNet=80001)
print(res)

#The metadata of the asset: This information is the used to represent the NFT, as the token as its own does not represent any asset
res = objectSDK.setIpfsMetadata(name="myNFT", imageUri="https://ipfsgw.vottun.tech/ipfs/QmbGGMYHqJE7DNnxDFd8MKqEFXn4U5BFpwN9adMJCmQU7K", description="Description number 1", external_url="https://page.com", artist='artistname',mediaType="png", numberTokens=10)
print(res)

#The media of the asset: Any NFT will need some media like a image, video, gif that will represent the asset
res = objectSDK.setIpfs(imagepath="/home/vottun/Downloads/1241691675.jpg",filename="image-name.jpg")
print(res)

#This method will mint the NFT
res = objectSDK.mint(contract_address='0x88B32cCB066623B3125E749302A0e64Ce117eecD', receiver='0x7e9b0Ce605C4E16C33C5f7fe3F24B616a1d2fA84',ipfsUri='http://54.77.224.235:8080/ipfs/QmSTdnwrVWBFEpHcEE2eW8V2UTpmASKXQ2cnVuYto1bGwc',ipfsHash='QmSTdnwrVWBFEpHcEE2eW8V2UTpmASKXQ2cnVuYto1bGwc', blockchainNet=80001, royaltyPercentage=10)
print(res)

#Return the data from the operationID identifying a mint or transfer method in blockchain. It will show the status of your operation
res = objectSDK.getOp(operationId='5ced8921-b10a-4971-bbd8-c1af4e3c9023')
print(res)

#Return the token metadata and more information
res = objectSDK.getTokenInfo(tokenId='3609',blockchainNet='1', c='0xba0a8ff51f281f7e49c6182390cfbe518f965433')
print(res)

#Transfer the NFT from the owner wallet to the receiver wallet
res = objectSDK.transfer(contract_address='0x88B32cCB066623B3125E749302A0e64Ce117eecD', from_wallet='0x7e9b0Ce605C4E16C33C5f7fe3F24B616a1d2fA84',to='0x9A94FBb1b4b6b6B924Ba6AbA83a47CBEaAe2a412', tokenId=11, price=12000, blockchainNet=80001)
print(res)

#Return data from the transaction hash
res = objectSDK.getTransactionReceipt(tx='0x8d1d40d8f69ff5d3ab71dccb2e6c3fce0ffd951238b2fb4216c1ceb66e988fe7',blockchainNet=80001)
print(res)

#Return the balance of the wallet
res = objectSDK.getBalance(address='0x975d9fef562de52905a3e0187ce3eefabfc8b14c',blockchainNet=43113)
print(res)

#Return all the contracts deployed from this account 
res = objectSDK.getContracts()
print(res)


