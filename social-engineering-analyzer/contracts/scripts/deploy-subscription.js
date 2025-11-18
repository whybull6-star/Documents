/**
 * Deployment script for Subscription contract
 * Deploys with owner address that receives all payments
 */

const hre = require("hardhat");

async function main() {
  console.log("Deploying Subscription contract...");
  
  // Check if private key is set
  if (!process.env.PRIVATE_KEY) {
    throw new Error("PRIVATE_KEY not found in .env file. Please add your private key to contracts/.env");
  }
  
  // Owner wallet address - receives all subscription payments
  const ownerAddress = "0x78b92b73ef9f2469c29fd0acbb54fc9b5204a079";
  
  // Get signers (accounts with private keys from .env)
  const signers = await hre.ethers.getSigners();
  
  if (!signers || signers.length === 0) {
    throw new Error("No signers found. Check your PRIVATE_KEY in .env file.");
  }
  
  const deployer = signers[0];
  console.log("Deploying with account:", deployer.address);
  
  // Check balance
  const balance = await hre.ethers.provider.getBalance(deployer.address);
  console.log("Account balance:", hre.ethers.formatEther(balance), "xDAI");
  
  // Get the contract factory with signer
  const Subscription = await hre.ethers.getContractFactory("Subscription", deployer);
  
  // Deploy the contract with owner address
  console.log("Deploying contract...");
  const subscription = await Subscription.deploy(ownerAddress);
  
  // Wait for deployment
  await subscription.waitForDeployment();
  
  const address = await subscription.getAddress();
  
  console.log("✅ Subscription contract deployed to:", address);
  console.log("   Network:", hre.network.name);
  console.log("   Owner address:", ownerAddress);
  console.log("   Monthly price: 8.99 xDAI");
  
  // If deploying to testnet/mainnet, verify contract on explorer
  if (hre.network.name !== "hardhat") {
    console.log("\nWaiting for block confirmations...");
    await subscription.deploymentTransaction().wait(5);
    
    console.log("\n✅ Contract deployed successfully!");
    console.log("   Explorer:", getExplorerUrl(hre.network.name, address));
    console.log("\n⚠️  Remember to:");
    console.log("   1. Save the contract address:", address);
    console.log("   2. Update frontend .env with NEXT_PUBLIC_SUBSCRIPTION_CONTRACT=", address);
    console.log("   3. Verify contract on explorer");
  }
}

function getExplorerUrl(network, address) {
  if (network === "gnosis-mainnet") {
    return `https://gnosisscan.io/address/${address}`;
  } else if (network === "gnosis-testnet") {
    return `https://blockscout.chiadochain.net/address/${address}`;
  }
  return address;
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });

