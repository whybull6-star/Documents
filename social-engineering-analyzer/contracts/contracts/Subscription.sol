// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title Subscription
 * @dev Monthly subscription contract for Lurantis
 * 
 * ELI5: Users pay monthly to get access to the service.
 * Payment goes directly to the owner's wallet address.
 */
contract Subscription {
    // Owner wallet address - receives all payments
    address public immutable owner;
    
    // Monthly subscription price in xDAI (8.99 USD, using xDAI since 1 xDAI ≈ 1 USD)
    // 8.99 xDAI = 8.99 * 10^18 wei
    uint256 public constant MONTHLY_PRICE = 8990000000000000000; // 8.99 xDAI in wei
    
    // Subscription data: user address => subscription end timestamp
    mapping(address => uint256) public subscriptions;
    
    // Events
    event SubscriptionPurchased(address indexed user, uint256 endTime, uint256 amount);
    event SubscriptionRenewed(address indexed user, uint256 newEndTime, uint256 amount);
    
    /**
     * @dev Constructor sets the owner address
     * @param _owner The wallet address that receives payments
     */
    constructor(address _owner) {
        require(_owner != address(0), "Owner cannot be zero address");
        owner = _owner;
    }
    
    /**
     * @dev Subscribe for one month
     * User sends xDAI, gets 30 days of access
     * 
     * ELI5: Pay once, get 30 days of service access
     */
    function subscribe() public payable {
        require(msg.value == MONTHLY_PRICE, "Incorrect payment amount");
        require(msg.sender != address(0), "Invalid sender");
        
        // Calculate subscription end time (30 days from now)
        uint256 endTime;
        if (subscriptions[msg.sender] > block.timestamp) {
            // If user already has active subscription, extend it
            endTime = subscriptions[msg.sender] + 30 days;
        } else {
            // New subscription starts now
            endTime = block.timestamp + 30 days;
        }
        
        subscriptions[msg.sender] = endTime;
        
        // Send payment directly to owner wallet
        (bool success, ) = payable(owner).call{value: msg.value}("");
        require(success, "Payment transfer failed");
        
        // Emit event
        if (subscriptions[msg.sender] == block.timestamp + 30 days) {
            emit SubscriptionPurchased(msg.sender, endTime, msg.value);
        } else {
            emit SubscriptionRenewed(msg.sender, endTime, msg.value);
        }
    }
    
    /**
     * @dev Check if user has active subscription
     * @param user Address to check
     * @return True if subscription is active
     */
    function hasActiveSubscription(address user) public view returns (bool) {
        return subscriptions[user] > block.timestamp;
    }
    
    /**
     * @dev Get subscription end time for a user
     * @param user Address to check
     * @return Timestamp when subscription ends (0 if no subscription)
     */
    function getSubscriptionEndTime(address user) public view returns (uint256) {
        return subscriptions[user];
    }
    
    /**
     * @dev Get days remaining in subscription
     * @param user Address to check
     * @return Days remaining (0 if expired or no subscription)
     */
    function getDaysRemaining(address user) public view returns (uint256) {
        if (subscriptions[user] <= block.timestamp) {
            return 0;
        }
        return (subscriptions[user] - block.timestamp) / 1 days;
    }
}

