'use client'

import { useWallet } from '@/hooks/useWallet'

export default function WalletButton() {
  const { address, balance, isConnected, isConnecting, error, connect, disconnect, formatAddress } = useWallet()

  if (isConnected && address) {
    return (
      <div className="flex items-center gap-3">
        <div className="text-right hidden sm:block">
          <div className="text-sm font-medium text-gray-700">
            {formatAddress(address)}
          </div>
          <div className="text-xs text-gray-500">
            {balance} xDAI
          </div>
        </div>
        <button
          onClick={(e) => {
            e.preventDefault()
            e.stopPropagation()
            console.log('Disconnect button clicked')
            disconnect()
          }}
          className="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg font-medium hover:bg-gray-200 transition text-sm"
        >
          Disconnect
        </button>
      </div>
    )
  }

  return (
    <>
      <button
        onClick={() => connect()}
        disabled={isConnecting}
        className="bg-primary-600 text-white px-6 py-2 rounded-lg font-medium hover:bg-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {isConnecting ? 'Connecting...' : 'Connect Wallet'}
      </button>
      {error && (
        <div className="text-red-600 text-xs mt-1">{error}</div>
      )}
    </>
  )
}

