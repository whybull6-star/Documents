'use client'

import { useState, useEffect, useCallback, useRef } from 'react'
import { ethers } from 'ethers'

/**
 * Gnosis Chain Configuration
 * Chain ID: 100 (mainnet)
 * Native token: xDAI
 */
const GNOSIS_CHAIN_ID = '0x64' // 100 in hex
const GNOSIS_RPC = process.env.NEXT_PUBLIC_GNOSIS_RPC || 'https://rpc.gnosischain.com'

interface WalletState {
  address: string | null
  balance: string | null
  isConnected: boolean
  isConnecting: boolean
  error: string | null
}

/**
 * Wallet hook for MetaMask on Gnosis chain
 * 
 * ELI5: This hook connects to MetaMask, switches to Gnosis chain,
 * gets your wallet address, and shows your xDAI balance
 */
export function useWallet() {
  const [state, setState] = useState<WalletState>({
    address: null,
    balance: null,
    isConnected: false,
    isConnecting: false,
    error: null,
  })

  // Track if user manually disconnected
  const [manuallyDisconnected, setManuallyDisconnected] = useState(false)
  const manuallyDisconnectedRef = useRef(false)

  // Check if wallet is already connected on page load
  useEffect(() => {
    if (!manuallyDisconnectedRef.current) {
      checkConnection()
    }
    
    // Listen for account changes
    if (typeof window !== 'undefined' && window.ethereum) {
      const handleAccountsChangedWrapper = (accounts: string[]) => {
        if (manuallyDisconnectedRef.current) {
          return // Don't auto-reconnect if manually disconnected
        }
        handleAccountsChanged(accounts)
      }
      
      window.ethereum.on('accountsChanged', handleAccountsChangedWrapper)
      window.ethereum.on('chainChanged', handleChainChanged)
      
      return () => {
        window.ethereum.removeListener('accountsChanged', handleAccountsChangedWrapper)
        window.ethereum.removeListener('chainChanged', handleChainChanged)
      }
    }
  }, [])

  const checkConnection = async () => {
    // NEVER check connection if manually disconnected
    if (typeof window === 'undefined' || !window.ethereum || manuallyDisconnectedRef.current) {
      console.log('checkConnection skipped - manually disconnected:', manuallyDisconnectedRef.current)
      return
    }

    try {
      const provider = new ethers.BrowserProvider(window.ethereum)
      const accounts = await provider.listAccounts()
      
      // Double-check we're still not manually disconnected before connecting
      if (accounts.length > 0 && !manuallyDisconnectedRef.current) {
        console.log('Auto-connecting to account:', accounts[0].address)
        await connectWallet(accounts[0].address)
      } else {
        console.log('No accounts or manually disconnected - not connecting')
      }
    } catch (error) {
      console.error('Error checking connection:', error)
    }
  }

  const handleAccountsChanged = (accounts: string[]) => {
    // NEVER auto-reconnect if manually disconnected
    if (manuallyDisconnectedRef.current) {
      console.log('handleAccountsChanged ignored - manually disconnected')
      return
    }
    
    if (accounts.length === 0) {
      // User disconnected from MetaMask
      setState({
        address: null,
        balance: null,
        isConnected: false,
        isConnecting: false,
        error: null,
      })
      setManuallyDisconnected(true)
      manuallyDisconnectedRef.current = true
    } else {
      // User switched accounts - only reconnect if not manually disconnected
      if (!manuallyDisconnectedRef.current) {
        console.log('Account changed, reconnecting to:', accounts[0])
        connectWallet(accounts[0])
      }
    }
  }

  const handleChainChanged = () => {
    // Reload page when chain changes
    window.location.reload()
  }

  const switchToGnosis = async () => {
    if (!window.ethereum) {
      throw new Error('MetaMask not installed')
    }

    try {
      // Try to switch to Gnosis chain
      await window.ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: GNOSIS_CHAIN_ID }],
      })
    } catch (switchError: any) {
      // If chain doesn't exist, add it
      if (switchError.code === 4902) {
        await window.ethereum.request({
          method: 'wallet_addEthereumChain',
          params: [
            {
              chainId: GNOSIS_CHAIN_ID,
              chainName: 'Gnosis Chain',
              nativeCurrency: {
                name: 'xDAI',
                symbol: 'xDAI',
                decimals: 18,
              },
              rpcUrls: [GNOSIS_RPC],
              blockExplorerUrls: ['https://gnosisscan.io/'],
            },
          ],
        })
      } else {
        throw switchError
      }
    }
  }

  const connectWallet = async (address?: string) => {
    // Reset manual disconnect flag FIRST before connecting
    manuallyDisconnectedRef.current = false
    setManuallyDisconnected(false)
    
    setState((prev) => ({ ...prev, isConnecting: true, error: null }))

    try {
      if (!window.ethereum) {
        throw new Error('Please install MetaMask to connect your wallet')
      }

      const provider = new ethers.BrowserProvider(window.ethereum)
      
      // Always request accounts to trigger MetaMask popup (especially after disconnect)
      // This ensures the user gets a popup even if MetaMask has cached the connection
      const accounts = await provider.send('eth_requestAccounts', [])
      if (!accounts || accounts.length === 0) {
        throw new Error('No accounts found. Please approve the connection in MetaMask.')
      }
      
      // Use the requested account, or the provided address if given
      address = address || accounts[0]

      if (!address) {
        throw new Error('No address available')
      }
      
      // Double-check we're not manually disconnected (user might have clicked disconnect while connecting)
      if (manuallyDisconnectedRef.current) {
        console.log('Connection cancelled - user manually disconnected')
        setState({
          address: null,
          balance: null,
          isConnected: false,
          isConnecting: false,
          error: null,
        })
        return
      }

      // Switch to Gnosis chain
      await switchToGnosis()

      // Get balance in xDAI
      const balance = await provider.getBalance(address)
      const balanceInXDAI = ethers.formatEther(balance)

      // Format address (show first 6 and last 4 characters)
      const formattedBalance = parseFloat(balanceInXDAI).toFixed(4)

      setState({
        address: address,
        balance: formattedBalance,
        isConnected: true,
        isConnecting: false,
        error: null,
      })
    } catch (error: any) {
      setState({
        address: null,
        balance: null,
        isConnected: false,
        isConnecting: false,
        error: error.message || 'Failed to connect wallet',
      })
      console.error('Wallet connection error:', error)
    }
  }

  const disconnect = useCallback(() => {
    console.log('=== DISCONNECT CALLED ===')
    console.log('Current state before disconnect:', state)
    
    // Mark as manually disconnected FIRST - this prevents auto-reconnection
    manuallyDisconnectedRef.current = true
    setManuallyDisconnected(true)
    
    // Clear state immediately - use a new object to force React to detect the change
    setState({
      address: null,
      balance: null,
      isConnected: false,
      isConnecting: false,
      error: null,
    })

    console.log('Disconnect complete - state cleared, manuallyDisconnectedRef:', manuallyDisconnectedRef.current)
    
    // Force a small delay to ensure state is cleared before any other operations
    setTimeout(() => {
      console.log('After disconnect timeout - state should be cleared')
    }, 100)
  }, [])

  const formatAddress = (address: string) => {
    if (!address) return ''
    return `${address.slice(0, 6)}...${address.slice(-4)}`
  }

  return {
    ...state,
    connect: connectWallet,
    disconnect,
    formatAddress,
  }
}

// Extend Window interface for TypeScript
declare global {
  interface Window {
    ethereum?: any
  }
}

