/**
 * Deployment script for CreditsToken contract
 * 
 * ELI5: This script sends the smart contract to the blockchain
 * like uploading a file, but to a special network everyone can see
 */

const hre = require("hardhat");

async function main() {
  console.log("Deploying CreditsToken contract...");
  
  // Get the contract factory
  const CreditsToken = await hre.ethers.getContractFactory("CreditsToken");
  
  // Set initial price: 0.001 GNO per credit (adjust as needed)
  // 1 GNO = 1e18 wei, so 0.001 GNO = 1e15 wei
  const pricePerCredit = hre.ethers.parseEther("0.001");
  
  // Deploy the contract
  const creditsToken = await CreditsToken.deploy(pricePerCredit);
  
  // Wait for deployment
  await creditsToken.waitForDeployment();
  
  const address = await creditsToken.getAddress();
  
  console.log("✅ CreditsToken deployed to:", address);
  console.log("   Network:", hre.network.name);
  console.log("   Price per credit:", hre.ethers.formatEther(pricePerCredit), "GNO");
  
  // If deploying to testnet/mainnet, verify contract on explorer
  if (hre.network.name !== "hardhat") {
    console.log("\nWaiting for block confirmations...");
    await creditsToken.deploymentTransaction().wait(5);
    
    console.log("\n✅ Contract deployed successfully!");
    console.log("   Explorer:", getExplorerUrl(hre.network.name, address));
    console.log("\n⚠️  Remember to:");
    console.log("   1. Save the contract address");
    console.log("   2. Update .env files with the address");
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


