/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
    NEXT_PUBLIC_CONTRACT_ADDRESS: process.env.NEXT_PUBLIC_CONTRACT_ADDRESS || '',
    NEXT_PUBLIC_SUBSCRIPTION_CONTRACT: process.env.NEXT_PUBLIC_SUBSCRIPTION_CONTRACT || '',
    NEXT_PUBLIC_GNOSIS_RPC: process.env.NEXT_PUBLIC_GNOSIS_RPC || 'https://rpc.gnosischain.com',
  },
}

module.exports = nextConfig


