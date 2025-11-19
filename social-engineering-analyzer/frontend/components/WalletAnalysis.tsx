'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { useWallet } from '@/hooks/useWallet'
import RiskScoreChart from './RiskScoreChart'
import FloatingShapes from './FloatingShapes'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

interface WalletAnalysisResult {
  wallet: string
  balance_eth: number
  transaction_patterns: any
  behavioral_cluster: any
  relationships: any[]
  anomalies: any[]
  risk_analysis: {
    score: number
    level: string
    factors: string[]
    pattern_matches?: number
    max_pattern_similarity?: number
  }
  insights: string[]
  credits_used?: number
}

export default function WalletAnalysis() {
  const [walletAddress, setWalletAddress] = useState('')
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [result, setResult] = useState<WalletAnalysisResult | null>(null)
  const [error, setError] = useState<string | null>(null)
  const { address, isConnected } = useWallet()

  const handleAnalyze = async () => {
    if (!walletAddress.trim()) {
      alert('Please enter a wallet address')
      return
    }

    setIsAnalyzing(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch(`${API_URL}/analyze-wallet`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          wallet_address: walletAddress.trim(),
          user_address: address || undefined,
          include_transactions: true
        }),
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }))
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      setResult(data)
    } catch (err: any) {
      setError(err.message || 'Failed to analyze wallet')
      console.error('Wallet analysis error:', err)
    } finally {
      setIsAnalyzing(false)
    }
  }

  const getRiskColor = (score: number) => {
    if (score >= 80) return 'text-red-600'
    if (score >= 60) return 'text-orange-600'
    if (score >= 40) return 'text-yellow-600'
    return 'text-green-600'
  }

  const getRiskBgColor = (score: number) => {
    if (score >= 80) return 'bg-red-50 border-red-200'
    if (score >= 60) return 'bg-orange-50 border-orange-200'
    if (score >= 40) return 'bg-yellow-50 border-yellow-200'
    return 'bg-green-50 border-green-200'
  }

  const formatAddress = (addr: string) => {
    return `${addr.slice(0, 6)}...${addr.slice(-4)}`
  }

  return (
    <section id="wallet-analysis" className="relative py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-50 to-white overflow-hidden">
      {/* Subtle animated background */}
      <div className="absolute inset-0 opacity-15">
        <FloatingShapes />
      </div>
      <div className="max-w-6xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            <span className="gradient-text">On-Chain Wallet Analysis</span>
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Analyze wallet behavior, transaction patterns, and detect anomalies using advanced vector search
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="bg-white rounded-2xl shadow-xl p-8 border border-gray-200"
        >
          <div className="space-y-6">
            {/* Input */}
            <div>
              <label htmlFor="wallet" className="block text-sm font-semibold text-gray-700 mb-2">
                Wallet Address
              </label>
              <div className="flex gap-3">
                <input
                  id="wallet"
                  type="text"
                  value={walletAddress}
                  onChange={(e) => setWalletAddress(e.target.value)}
                  placeholder="0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"
                  className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 font-mono text-sm"
                  disabled={isAnalyzing}
                />
                <button
                  onClick={handleAnalyze}
                  disabled={isAnalyzing || !walletAddress.trim()}
                  className="bg-primary-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  {isAnalyzing ? (
                    <>
                      <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Analyzing...
                    </>
                  ) : (
                    '🔍 Analyze Wallet'
                  )}
                </button>
              </div>
              <p className="mt-2 text-xs text-gray-500">
                Enter a Gnosis Chain wallet address to analyze on-chain behavior and detect suspicious patterns
              </p>
            </div>

            {/* Error Display */}
            {error && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-red-50 border border-red-200 rounded-lg p-4"
              >
                <p className="text-red-600 font-medium">Error: {error}</p>
                {error.includes('credits') && (
                  <p className="text-red-500 text-sm mt-1">
                    You may need to subscribe. Check the <a href="#pricing" className="underline">Pricing</a> section.
                  </p>
                )}
              </motion.div>
            )}

            {/* Results */}
            {result && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
              >
                {/* Risk Score Card */}
                <div className={`${getRiskBgColor(result.risk_analysis.score)} border-2 rounded-xl p-6`}>
                  <div className="flex items-center justify-between mb-4">
                    <div>
                      <h3 className="text-2xl font-bold mb-1">Risk Assessment</h3>
                      <p className="text-sm text-gray-600">Wallet: {formatAddress(result.wallet)}</p>
                    </div>
                    <div className="text-right">
                      <div className={`text-5xl font-bold ${getRiskColor(result.risk_analysis.score)}`}>
                        {result.risk_analysis.score.toFixed(1)}
                      </div>
                      <div className={`px-3 py-1 rounded-full text-sm font-semibold mt-2 inline-block ${
                        result.risk_analysis.level === 'CRITICAL' ? 'bg-red-600 text-white' :
                        result.risk_analysis.level === 'HIGH' ? 'bg-orange-600 text-white' :
                        result.risk_analysis.level === 'MEDIUM' ? 'bg-yellow-600 text-white' :
                        'bg-green-600 text-white'
                      }`}>
                        {result.risk_analysis.level} RISK
                      </div>
                    </div>
                  </div>

                  {/* Risk Factors */}
                  {result.risk_analysis.factors.length > 0 && (
                    <div className="mt-4">
                      <h4 className="font-semibold text-gray-700 mb-2">Risk Factors:</h4>
                      <ul className="space-y-1">
                        {result.risk_analysis.factors.map((factor, idx) => (
                          <li key={idx} className="text-sm text-gray-700 flex items-start gap-2">
                            <span className="text-red-500 mt-1">•</span>
                            <span>{factor}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {/* Risk Score Charts */}
                  {result.risk_analysis.pattern_matches !== undefined && (
                    <RiskScoreChart
                      riskScore={result.risk_analysis.score}
                      riskLevel={result.risk_analysis.level}
                      patternMatches={result.risk_analysis.pattern_matches || 0}
                      maxPatternSimilarity={result.risk_analysis.max_pattern_similarity || 0}
                    />
                  )}
                </div>

                {/* Wallet Info Grid */}
                <div className="grid md:grid-cols-2 gap-4">
                  {/* Balance */}
                  <div className="bg-gray-50 rounded-lg p-4 border border-gray-200">
                    <h4 className="text-sm font-semibold text-gray-600 mb-1">Balance</h4>
                    <p className="text-2xl font-bold text-gray-900">{result.balance_eth.toFixed(4)} xDAI</p>
                  </div>

                  {/* Behavioral Cluster */}
                  {result.behavioral_cluster && (
                    <div className="bg-gray-50 rounded-lg p-4 border border-gray-200">
                      <h4 className="text-sm font-semibold text-gray-600 mb-1">Behavioral Cluster</h4>
                      <p className="text-lg font-semibold text-gray-900 capitalize">
                        {result.behavioral_cluster.pattern_type || 'Unknown'}
                      </p>
                      <p className="text-xs text-gray-500 mt-1">
                        Similarity: {(result.behavioral_cluster.similarity * 100).toFixed(1)}%
                      </p>
                    </div>
                  )}
                </div>

                {/* Anomalies */}
                {result.anomalies && result.anomalies.length > 0 && (
                  <div className="bg-orange-50 border border-orange-200 rounded-lg p-6">
                    <h4 className="font-semibold text-orange-800 mb-3 flex items-center gap-2">
                      <span>⚠️</span>
                      Detected Anomalies ({result.anomalies.length})
                    </h4>
                    <div className="space-y-3">
                      {result.anomalies.map((anomaly: any, idx: number) => (
                        <div key={idx} className="bg-white rounded-lg p-3 border border-orange-200">
                          <div className="flex items-center justify-between mb-1">
                            <span className="font-medium text-gray-900 capitalize">{anomaly.type?.replace('_', ' ')}</span>
                            <span className={`px-2 py-1 rounded text-xs font-semibold ${
                              anomaly.severity === 'critical' ? 'bg-red-100 text-red-800' :
                              anomaly.severity === 'high' ? 'bg-orange-100 text-orange-800' :
                              'bg-yellow-100 text-yellow-800'
                            }`}>
                              {anomaly.severity?.toUpperCase()}
                            </span>
                          </div>
                          <p className="text-sm text-gray-600">{anomaly.description}</p>
                          <p className="text-xs text-gray-500 mt-1">Confidence: {(anomaly.confidence * 100).toFixed(1)}%</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Relationships */}
                {result.relationships && result.relationships.length > 0 && (
                  <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
                    <h4 className="font-semibold text-blue-800 mb-3">Wallet Relationships</h4>
                    <div className="space-y-2">
                      {result.relationships.map((rel: any, idx: number) => (
                        <div key={idx} className="bg-white rounded-lg p-3 border border-blue-200">
                          <p className="text-sm font-medium text-gray-900 capitalize mb-1">{rel.type?.replace('_', ' ')}</p>
                          <p className="text-xs text-gray-600">{rel.pattern}</p>
                          <p className="text-xs text-gray-500 mt-1">Confidence: {(rel.confidence * 100).toFixed(1)}%</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Insights */}
                {result.insights && result.insights.length > 0 && (
                  <div className="bg-primary-50 border border-primary-200 rounded-lg p-6">
                    <h4 className="font-semibold text-primary-800 mb-3">Key Insights</h4>
                    <ul className="space-y-2">
                      {result.insights.map((insight: string, idx: number) => (
                        <li key={idx} className="text-sm text-gray-700 flex items-start gap-2">
                          <span className="text-primary-600 mt-1">•</span>
                          <span>{insight}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Reset Button */}
                <button
                  onClick={() => {
                    setResult(null)
                    setWalletAddress('')
                  }}
                  className="w-full py-2 text-gray-600 hover:text-gray-800 transition text-sm font-medium"
                >
                  Analyze Another Wallet →
                </button>
              </motion.div>
            )}
          </div>
        </motion.div>
      </div>
    </section>
  )
}

