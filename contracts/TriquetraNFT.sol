pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract TriquetraNFT is ERC721 {
    // String NFT Name
    string NFTName;

    // String IPFS Link
    string IPFSLink;

    // String Decription
    string Description;

    // struct TNFT_1 {
    //     string NFTName;
    //     string IPFSLink;
    //     string Description;
    // }

    // TNFT_1[] dataBase;

    // //////////////////////////
    
    address private owner;
    // event for EVM logging
    event OwnerSet(address indexed oldOwner, address indexed newOwner);
    event checNFT();

    uint256 ChainlinkVRF;
    mapping(uint256 => string) verifiedTriquetraNFT;
    // //////////////////////////


    //Connecting with ChainLinkVRF

    constructor(string memory entry1, string memory entry2, string memory entry3) ERC721("TriquetraNFT", "TNFT") {

        NFTName = entry1;
        IPFSLink = entry2;
        Description = entry3;
        
        owner = msg.sender; // 'msg.sender' is sender of current call, contract deployer for a constructor
        emit OwnerSet(address(0), owner);
    }
}