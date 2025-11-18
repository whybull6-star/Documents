// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title CreditsToken
 * @dev ERC20 token for Social Engineering Analyzer credits
 * 
 * ELI5: This is like a digital coin for our service.
 * Users buy these coins, then spend them to use the service.
 * They're stored on blockchain so they can't be faked.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CreditsToken is ERC20, ERC20Burnable, Ownable {
    // Price in wei (smallest unit of ETH/GNO) per credit
    uint256 public pricePerCredit;
    
    // Address of the service contract that can mint credits
    address public serviceContract;
    
    // Events for logging
    event CreditsPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event CreditsRedeemed(address indexed user, uint256 amount);
    event PriceUpdated(uint256 newPrice);
    
    /**
     * @dev Constructor
     * @param _pricePerCredit Initial price per credit in wei
     * 
     * ELI5: When contract is created, set the price for buying credits
     */
    constructor(uint256 _pricePerCredit) ERC20("SEA Credits", "SEAC") Ownable(msg.sender) {
        pricePerCredit = _pricePerCredit;
    }
    
    /**
     * @dev Buy credits by sending ETH
     * 
     * ELI5: Send money, get credits. Like buying tokens at an arcade.
     */
    function buyCredits() public payable {
        require(msg.value > 0, "Must send ETH to buy credits");
        require(msg.value >= pricePerCredit, "Not enough ETH for credits");
        
        // Calculate how many credits to give
        uint256 creditsToGive = msg.value / pricePerCredit;
        
        // Mint credits to buyer
        _mint(msg.sender, creditsToGive);
        
        // Emit event
        emit CreditsPurchased(msg.sender, creditsToGive, msg.value);
    }
    
    /**
     * @dev Redeem credits (called by service when user uses API)
     * @param user Address of user redeeming credits
     * @param amount Amount of credits to redeem
     * 
     * ELI5: When user uses the service, this function takes their credits
     */
    function redeemCredits(address user, uint256 amount) public {
        require(msg.sender == serviceContract || msg.sender == owner(), "Not authorized");
        require(balanceOf(user) >= amount, "Insufficient credits");
        
        // Burn credits
        _burn(user, amount);
        
        emit CreditsRedeemed(user, amount);
    }
    
    /**
     * @dev Set service contract address (can redeem credits)
     * @param _serviceContract Address of service contract
     */
    function setServiceContract(address _serviceContract) public onlyOwner {
        serviceContract = _serviceContract;
    }
    
    /**
     * @dev Update price per credit
     * @param _newPrice New price in wei
     */
    function updatePrice(uint256 _newPrice) public onlyOwner {
        require(_newPrice > 0, "Price must be greater than 0");
        pricePerCredit = _newPrice;
        emit PriceUpdated(_newPrice);
    }
    
    /**
     * @dev Withdraw ETH from contract (owner only)
     * 
     * ELI5: Owner can take out the money people paid for credits
     */
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Withdrawal failed");
    }
    
    /**
     * @dev Get credit balance for user
     * @param user Address to check
     * @return Balance in credits
     */
    function getCreditBalance(address user) public view returns (uint256) {
        return balanceOf(user);
    }
}


