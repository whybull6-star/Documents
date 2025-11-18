'use client'

import { useState } from 'react'
import { motion } from 'framer-motion'
import { useAnalysis } from '@/hooks/useAnalysis'
import { useWallet } from '@/hooks/useWallet'

export default function Analysis() {
  const [content, setContent] = useState('')
  const [knownAddresses, setKnownAddresses] = useState('')
  const { analyze, isAnalyzing, result, error, reset } = useAnalysis()
  const { address, isConnected } = useWallet()

  const handleAnalyze = async () => {
    if (!content.trim()) {
      alert('Please enter some content to analyze')
      return
    }

    const addresses = knownAddresses
      .split(',')
      .map(addr => addr.trim())
      .filter(addr => addr.length > 0)

    try {
      await analyze(content, address || undefined, addresses.length > 0 ? addresses : undefined, true)
    } catch (err) {
      // Error is handled by the hook
    }
  }

  const getThreatColor = (score: number) => {
    if (score >= 80) return 'text-red-600'
    if (score >= 60) return 'text-orange-600'
    if (score >= 40) return 'text-yellow-600'
    return 'text-green-600'
  }

  const getThreatBgColor = (score: number) => {
    if (score >= 80) return 'bg-red-50 border-red-200'
    if (score >= 60) return 'bg-orange-50 border-orange-200'
    if (score >= 40) return 'bg-yellow-50 border-yellow-200'
    return 'bg-green-50 border-green-200'
  }

  return (
    <section id="analyze" className="py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-white to-gray-50">
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            <span className="gradient-text">Analyze Threats</span>
          </h2>
          <p className="text-xl text-gray-600">
            Paste suspicious messages, links, or communications to detect social engineering attacks
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
            {/* Input Area */}
            <div>
              <label htmlFor="content" className="block text-sm font-semibold text-gray-700 mb-2">
                Content to Analyze
              </label>
              <textarea
                id="content"
                value={content}
                onChange={(e) => setContent(e.target.value)}
                placeholder="Paste the suspicious message, email, or communication here..."
                className="w-full h-40 px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500 resize-none"
                disabled={isAnalyzing}
              />
            </div>

            {/* Known Addresses (Optional) */}
            <div>
              <label htmlFor="addresses" className="block text-sm font-semibold text-gray-700 mb-2">
                Your Known Wallet Addresses (Optional - for address spoofing detection)
              </label>
              <input
                id="addresses"
                type="text"
                value={knownAddresses}
                onChange={(e) => setKnownAddresses(e.target.value)}
                placeholder="0x1234..., 0x5678... (comma-separated)"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                disabled={isAnalyzing}
              />
              <p className="mt-1 text-xs text-gray-500">
                Add your wallet addresses to detect if someone is trying to spoof them
              </p>
            </div>

            {/* Analyze Button */}
            <button
              onClick={handleAnalyze}
              disabled={isAnalyzing || !content.trim()}
              className="w-full bg-primary-600 text-white py-4 rounded-lg font-semibold text-lg hover:bg-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
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
                '🔍 Analyze Threat'
              )}
            </button>

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
                    You may need to subscribe to continue. Check the <a href="#pricing" className="underline">Pricing</a> section.
                  </p>
                )}
              </motion.div>
            )}

            {/* Results Display */}
            {result && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
              >
                {/* Threat Score Card */}
                {'overall_threat_score' in result ? (
                  // Enhanced result
                  <div className={`${getThreatBgColor(result.overall_threat_score)} border-2 rounded-xl p-6`}>
                    <div className="flex items-center justify-between mb-4">
                      <h3 className="text-2xl font-bold">Threat Analysis</h3>
                      <span className={`text-4xl font-bold ${getThreatColor(result.overall_threat_score)}`}>
                        {result.overall_threat_score.toFixed(1)}
                      </span>
                    </div>
                    <div className="flex items-center gap-2 mb-4">
                      <span className={`px-3 py-1 rounded-full text-sm font-semibold ${
                        result.threat_level === 'CRITICAL' ? 'bg-red-600 text-white' :
                        result.threat_level === 'HIGH' ? 'bg-orange-600 text-white' :
                        result.threat_level === 'MEDIUM' ? 'bg-yellow-600 text-white' :
                        'bg-green-600 text-white'
                      }`}>
                        {result.threat_level} RISK
                      </span>
                    </div>

                    {/* Detected Attacks */}
                    {result.detected_attacks.length > 0 && (
                      <div className="mb-4">
                        <h4 className="font-semibold text-gray-700 mb-2">Detected Attacks:</h4>
                        <div className="space-y-2">
                          {result.detected_attacks.map((attack, idx) => (
                            <div key={idx} className="flex items-center gap-2">
                              <span className="text-red-500">⚠️</span>
                              <span className="font-medium">{attack.type.replace('_', ' ').toUpperCase()}</span>
                              <span className="text-sm text-gray-600">({attack.severity})</span>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}

                    {/* Specialized Analysis Results */}
                    {result.address_analysis?.is_spoofed && (
                      <div className="mb-4 p-3 bg-red-100 border border-red-300 rounded-lg">
                        <p className="font-semibold text-red-800 mb-1">🚨 Address Spoofing Detected!</p>
                        <p className="text-sm text-red-700">{result.address_analysis.recommendation}</p>
                      </div>
                    )}

                    {result.sim_swap_analysis?.is_sim_swap && (
                      <div className="mb-4 p-3 bg-red-100 border border-red-300 rounded-lg">
                        <p className="font-semibold text-red-800 mb-1">🚨 SIM Swapping Attempt Detected!</p>
                        <p className="text-sm text-red-700">{result.sim_swap_analysis.recommendation}</p>
                      </div>
                    )}

                    {result.wallet_stalking_analysis?.is_stalking && (
                      <div className="mb-4 p-3 bg-orange-100 border border-orange-300 rounded-lg">
                        <p className="font-semibold text-orange-800 mb-1">⚠️ Wallet Stalking Detected!</p>
                        <p className="text-sm text-orange-700">{result.wallet_stalking_analysis.recommendation}</p>
                      </div>
                    )}

                    {/* Recommendations */}
                    <div>
                      <h4 className="font-semibold text-gray-700 mb-2">Recommendations:</h4>
                      <ul className="space-y-2">
                        {result.recommendations.map((rec, idx) => (
                          <li key={idx} className="text-sm text-gray-700 flex items-start gap-2">
                            <span className="text-primary-600 mt-1">•</span>
                            <span>{rec}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                ) : (
                  // Basic result
                  <div className={`${getThreatBgColor(result.threat_score)} border-2 rounded-xl p-6`}>
                    <div className="flex items-center justify-between mb-4">
                      <h3 className="text-2xl font-bold">Threat Analysis</h3>
                      <span className={`text-4xl font-bold ${getThreatColor(result.threat_score)}`}>
                        {result.threat_score.toFixed(1)}
                      </span>
                    </div>
                    <div className="mb-4">
                      <p className="text-sm text-gray-600 mb-2">Similarity Score: {(result.similarity_score * 100).toFixed(1)}%</p>
                      {result.detected_patterns.length > 0 && (
                        <div>
                          <h4 className="font-semibold text-gray-700 mb-2">Detected Patterns:</h4>
                          <ul className="space-y-1">
                            {result.detected_patterns.map((pattern, idx) => (
                              <li key={idx} className="text-sm text-gray-700">• {pattern}</li>
                            ))}
                          </ul>
                        </div>
                      )}
                    </div>
                    <div className="p-4 bg-white/50 rounded-lg">
                      <p className="text-sm font-medium text-gray-800">{result.recommendation}</p>
                    </div>
                  </div>
                )}

                {/* Reset Button */}
                <button
                  onClick={reset}
                  className="w-full py-2 text-gray-600 hover:text-gray-800 transition text-sm font-medium"
                >
                  Analyze Another Message →
                </button>
              </motion.div>
            )}
          </div>
        </motion.div>
      </div>
    </section>
  )
}

