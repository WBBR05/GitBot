// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract MinecraftItems is ERC1155{
    uint256 public constant COBBLESTONE = 0;
    uint256 public constant OAKWOOD = 1;
    uint256 public constant DRAGONEGG = 2;

    constructor() ERC1155("https://bafybeicbss26l5qpcxdvakjmkygmiypp74arh6psxhoakxyi5oaatbrdy4.ipfs.nftstorage.link/{id}.json") {
        _mint(msg.sender, COBBLESTONE, 64, "");
        _mint(msg.sender, OAKWOOD, 64, "");
        _mint(msg.sender, DRAGONEGG, 1, "");
    }
    function uri(uint256 _tokenId) override public view returns (string memory) {
        return string(
            abi.encodePacked(
                "https://bafybeicbss26l5qpcxdvakjmkygmiypp74arh6psxhoakxyi5oaatbrdy4.ipfs.nftstorage.link/",
                Strings.toString(_tokenId),
                ".json"
            )
        );
    }
}
