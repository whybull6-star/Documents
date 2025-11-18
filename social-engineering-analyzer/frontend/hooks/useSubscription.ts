'use client'

import { useState, useEffect } from 'react'
import { ethers } from 'ethers'

// Subscription contract ABI (just the functions we need)
const SUBSCRIPTION_ABI = [
  "function subscribe() payable",
  "function hasActiveSubscription(address) view returns (bool)",
  "function getSubscriptionEndTime(address) view returns (uint256)",
  "function getDaysRemaining(address) view returns (uint256)",
  "function MONTHLY_PRICE() view returns (uint256)",
]

// Contract address - will be set from env or passed as prop
const SUBSCRIPTION_CONTRACT = process.env.NEXT_PUBLIC_SUBSCRIPTION_CONTRACT || ''

interface SubscriptionState {
  isSubscribed: boolean
  endTime: number | null
  daysRemaining: number | null
  isLoading: boolean
  error: string | null
  isPurchasing: boolean
}

/**
 * Hook for managing subscriptions
 * 
 * ELI5: This hook lets you:
 * - Check if you have an active subscription
 * - Buy a subscription (pay 8.99 xDAI)
 * - See how many days are left
 */
export function useSubscription(contractAddress?: string) {
  const contractAddr = contractAddress || SUBSCRIPTION_CONTRACT
  
  // Debug: Log contract address
  useEffect(() => {
    console.log('Subscription contract address:', contractAddr || 'NOT SET')
    console.log('From env:', SUBSCRIPTION_CONTRACT)
  }, [contractAddr])
  
  const [state, setState] = useState<SubscriptionState>({
    isSubscribed: false,
    endTime: null,
    daysRemaining: null,
    isLoading: true,
    error: null,
    isPurchasing: false,
  })

  const checkSubscription = async (userAddress: string) => {
    if (!contractAddr || !window.ethereum || !userAddress) {
      setState(prev => ({ ...prev, isLoading: false }))
      return
    }

    try {
      const provider = new ethers.BrowserProvider(window.ethereum)
      const contract = new ethers.Contract(contractAddr, SUBSCRIPTION_ABI, provider)
      
      const [isSubscribed, endTime, daysRemaining] = await Promise.all([
        contract.hasActiveSubscription(userAddress),
        contract.getSubscriptionEndTime(userAddress),
        contract.getDaysRemaining(userAddress),
      ])

      // In ethers v6, BigInt values need to be converted with Number()
      setState({
        isSubscribed,
        endTime: Number(endTime),
        daysRemaining: Number(daysRemaining),
        isLoading: false,
        error: null,
        isPurchasing: false,
      })
    } catch (error: any) {
      console.error('Error checking subscription:', error)
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: error.message || 'Failed to check subscription',
      }))
    }
  }

  const purchaseSubscription = async () => {
    // Check if contract address is set
    if (!contractAddr || contractAddr === '') {
      console.error('Subscription contract address not set:', contractAddr)
      setState(prev => ({ 
        ...prev, 
        error: 'Subscription contract not configured. Please set NEXT_PUBLIC_SUBSCRIPTION_CONTRACT in your .env file.',
        isPurchasing: false
      }))
      return
    }

    // Check if MetaMask is available
    if (typeof window === 'undefined' || !window.ethereum) {
      console.error('MetaMask not available')
      setState(prev => ({ 
        ...prev, 
        error: 'MetaMask not found. Please install MetaMask to subscribe.',
        isPurchasing: false
      }))
      return
    }

    setState(prev => ({ ...prev, isPurchasing: true, error: null }))

    try {
      console.log('Connecting to contract:', contractAddr)
      const provider = new ethers.BrowserProvider(window.ethereum)
      const signer = await provider.getSigner()
      const userAddress = await signer.getAddress()
      console.log('User address:', userAddress)
      
      // Check user balance (for info only, don't block)
      const balance = await provider.getBalance(userAddress)
      console.log('User balance:', ethers.formatEther(balance), 'xDAI')
      
      // Verify contract exists by checking code
      const code = await provider.getCode(contractAddr)
      if (code === '0x') {
        throw new Error('Contract does not exist at this address. Please verify the contract address.')
      }
      console.log('Contract verified, code length:', code.length)
      
      const contract = new ethers.Contract(contractAddr, SUBSCRIPTION_ABI, signer)
      
      // Get the monthly price from contract
      console.log('Getting monthly price...')
      const monthlyPrice = await contract.MONTHLY_PRICE()
      console.log('Monthly price:', ethers.formatEther(monthlyPrice), 'xDAI')
      
      // Warn if balance is low, but don't block
      if (balance < monthlyPrice) {
        console.warn(`⚠️ Low balance: Need ${ethers.formatEther(monthlyPrice)} xDAI, but you have ${ethers.formatEther(balance)} xDAI. Transaction may fail.`)
      }
      
      // Estimate gas first
      console.log('Estimating gas...')
      try {
        const gasEstimate = await contract.subscribe.estimateGas({ value: monthlyPrice })
        console.log('Gas estimate:', gasEstimate.toString())
      } catch (gasError: any) {
        console.error('Gas estimation failed:', gasError)
        throw new Error(`Transaction will fail: ${gasError.reason || gasError.message || 'Unknown error'}`)
      }
      
      // Send transaction
      console.log('Sending transaction...')
      const tx = await contract.subscribe({ value: monthlyPrice })
      console.log('Transaction sent:', tx.hash)
      
      // Wait for transaction to be mined
      console.log('Waiting for confirmation...')
      const receipt = await tx.wait()
      console.log('Transaction confirmed:', receipt.hash)
      
      // Refresh subscription status
      await checkSubscription(userAddress)
      
      setState(prev => ({ ...prev, isPurchasing: false }))
    } catch (error: any) {
      console.error('Error purchasing subscription:', error)
      let errorMessage = 'Failed to purchase subscription'
      
      if (error.reason) {
        errorMessage = error.reason
      } else if (error.message) {
        errorMessage = error.message
      } else if (error.data?.message) {
        errorMessage = error.data.message
      }
      
      setState(prev => ({
        ...prev,
        isPurchasing: false,
        error: errorMessage,
      }))
    }
  }

  const getMonthlyPrice = async () => {
    if (!contractAddr || !window.ethereum) return null
    
    try {
      const provider = new ethers.BrowserProvider(window.ethereum)
      const contract = new ethers.Contract(contractAddr, SUBSCRIPTION_ABI, provider)
      const price = await contract.MONTHLY_PRICE()
      return ethers.formatEther(price)
    } catch (error) {
      console.error('Error getting price:', error)
      return '8.99' // Fallback
    }
  }

  return {
    ...state,
    checkSubscription,
    purchaseSubscription,
    getMonthlyPrice,
  }
}

