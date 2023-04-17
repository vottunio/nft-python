## VOTTUN NFT SDK

The Python Vottun SDK is a set of methods for interacting with EVM blockchains. The main feature is that allows users to create NFTs in a simply way and on any blockchain they choose as Poylgon or Avalanche for example.
With this set of methods you can create NFT, transfer the asset, check the status of the network and integrate your app to web3.

## Installation & Initialization

Python3.8 >= is required

pip3 install -i <sdk_package>

```sh
from SDKObject import SDK

"token: Is the Bearer token to authenticate the user"
"app_id: Identifier for the service of NFT and IPFS of Vottun"

object_sdk_python = SDK(auth=<token>, app_id=<app_id>)
print(object_sdk_python.getAvailableNetworks())

```

## Blockchain network

Return a list of available networks where to operate

Method: getAvailableNetworks

| Method parameter | Description |
| ---------------- | ----------- |

| Response      | Description                                        |
| ------------- | -------------------------------------------------- |
| id            | Id of the network                                  |
| name          | Name of the network                                |
| explorer      | Explorer url of the network                        |
| typeId        | Identifier for the network used in all the methods |
| typeName      | Type of blockchain                                 |
| testnetFaucet | Url of the faucet in case is a testnet             |

Inside the Ethereum ecosystem there are several networks and each network is identifed by an ID, which is necessary in the methods in order to select the network on which to operate.

| Network name    | Network ID |
| --------------- | ---------- |
| Ethereum        | 1          |
| Rinkeby         | 4          |
| Polygon Mumbai  | 80001      |
| Polygon mainnet | 137        |
| Avalanche       | 43114      |

## NFT methods

### MINT method

This method will mint the NFT

Method: mint

| Method parameter  | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| contractAddress   | The address of the smart contract in which the NFT is to be mined |
| receiver          | The ethereum address of the receiver of the NFT                   |
| ipfsUri           | Value returne from the IPFS api                                   |
| ipfsHash          | THash of the IPFS object                                          |
| blockchainNet     | Integer indentifier for the blockchain network                    |
| royaltyPercentage | The percentage expressed as an integer                            |

| Response    | Description                  |
| ----------- | ---------------------------- |
| operationId | Identifier of your operation |
| network     | Name of the network          |

### TRANSFER method

This method will transfer the token to another address wallet.

Method: transfer

| Method parameter | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| tokenId          | token id                                                          |
| contractAddress  | The address of the smart contract in which the NFT is to be mined |
| to               | The ethereum address of the receiver of the NFT                   |
| from_wallet      | owner of the token                                                |
| price            | price of the token                                                |
| blockchainNet    | Integer indentifier for the blockchain network                    |

| Response    | Description                  |
| ----------- | ---------------------------- |
| operationId | Identifier of your operation |
| network     | Name of the network          |

## IPFS methods

In order to successfully mint your NFT, you will need to complete the following steps.

### Upload media

1- The media of the asset: Any NFT will need some media like a image, video, gif that will represent the asset

Method: setIpfs

| Method parameter | Description                     |
| ---------------- | ------------------------------- |
| imagepath        | Absolute path of the media file |
| filename         | Name of the media file          |

| Response | Description                           |
| -------- | ------------------------------------- |
| ipfsURL  | URL created to display data from ipfs |

### Upload metadata

2- The metadata of the asset: This information is the used to represent the NFT, as the token as its own does not represent any asset

Method: setIpfsMetadata

| Method parameter | Description                                    |
| ---------------- | ---------------------------------------------- |
| name             | The name of the asset                          |
| imageUri         | This is the ipfs URL to the media file         |
| description      | Description of the asset                       |
| mediaType        | Type of the media: Ex 'png'                    |
| artist           | Integer indentifier for the blockchain network |

| Response | Description                           |
| -------- | ------------------------------------- |
| ipfsURL  | URL created to display data from ipfs |

## Status methods

### Check status of operation

Return the data from the operationID identifying a mint or transfer method in blockchain. It will show the status of your operation.

Method: getOp

| Method parameter | Description                                             |
| ---------------- | ------------------------------------------------------- |
| operationId      | The unique identifier for the operation mint / transfer |

| Response             | Description                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| transactionHash      | Transaction hash inside the blockchain                                                                              |
| statusId             | 1: Requested ; 2: Posted on the blockchain; 3: Processing in server; 4: Confirmed transaction; 5: Error transaction |
| transactionTimestamp | creation of the operation                                                                                           |
| errorDescription     | In case the statusID is an error this will return the error code                                                    |

### Get gas price of the network

Return current gasprice of the network, usefull in Ethereum main network as gasprice fluctuate significantly

Method: getGasPrice

| Method parameter | Description                                    |
| ---------------- | ---------------------------------------------- |
| blockchainNet    | Integer indentifier for the blockchain network |

| Response     | Description                 |
| ------------ | --------------------------- |
| gasPriceGwei | Price in wei of the network |

### Create wallet

Return a ethereum wallet with the publickey and privatekey

Method: createWallet

| Method parameter | Description |
| ---------------- | ----------- |

| Response   | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| publickey  | Public address of the wallet                                           |
| privatekey | Private key of the address used to sign transactions and import wallet |

### Get transaction receipt

Return data from the transaction hash

Method: getTransactionReceipt

| Method parameter | Description                                    |
| ---------------- | ---------------------------------------------- |
| tx               | Transaction hash of the blockchain             |
| blockchainNet    | Integer indentifier for the blockchain network |

| Response | Description                            |
| -------- | -------------------------------------- |
| hash     | Transaction hash inside the blockchain |
| value    |                                        |
| gas      | gas cost of the transaction            |
| gasPrice | gas price of the transaction           |
| nonce    | operation identifier of the account    |
| from     | address from where we get the asset    |
| to       | address to where we send the asset     |
| pending  | if the transaction still pending       |

### Get wallet balance

Return the balance of the wallet

Method: getBalance

| Method parameter | Description                                    |
| ---------------- | ---------------------------------------------- |
| blockchainNet    | Integer indentifier for the blockchain network |
| address          | Target address of which get the balance        |

| Response      | Description                                       |
| ------------- | ------------------------------------------------- |
| walletAddress | address from where we get the balance             |
| networkId     | Identifier of the network                         |
| balance       | balance in of the account for an specific network |

### Get contracts of a wallet

Return all the contracts deployed from this account

Method: getContracts

| Method parameter | Description                                    |
| ---------------- | ---------------------------------------------- |
| blockchainNet    | Integer indentifier for the blockchain network |

| Response          | Description                             |
| ----------------- | --------------------------------------- |
| contractAddress   | address of the contract deployed        |
| isDefault         |                                         |
| walletAddress     | address from where we get the contracts |
| blockchainNetwork | information about the network           |

### Get token data

Return the token metadata and more information

Method: getTokenInfo

| Method parameter | Description                                    |
| ---------------- | ---------------------------------------------- |
| blockchainNet    | Integer indentifier for the blockchain network |
| tokenId          | Token ID                                       |
| c                | Contract address used to mint the NFT          |

| Response          | Description                             |
| ----------------- | --------------------------------------- |
| contractAddress   | address of the contract deployed        |
| isDefault         |                                         |
| walletAddress     | address from where we get the contracts |
| blockchainNetwork | information about the network           |
