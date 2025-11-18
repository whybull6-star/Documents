'use client'

import { useState } from 'react'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

interface AnalysisResult {
  threat_score: number
  similarity_score: number
  detected_patterns: string[]
  recommendation: string
  credits_used: number
}

interface EnhancedAnalysisResult {
  overall_threat_score: number
  threat_level: string
  detected_attacks: Array<{
    type: string
    severity: string
    confidence: number
  }>
  recommendations: string[]
  address_analysis?: {
    is_spoofed: boolean
    recommendation: string
  }
  sim_swap_analysis?: {
    is_sim_swap: boolean
    recommendation: string
  }
  wallet_stalking_analysis?: {
    is_stalking: boolean
    recommendation: string
  }
  detailed_analysis: {
    threat_breakdown: {
      pattern_similarity: number
      address_spoofing: number
      sim_swapping: number
      wallet_stalking: number
      red_flags: number
    }
  }
}

export function useAnalysis() {
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [result, setResult] = useState<AnalysisResult | EnhancedAnalysisResult | null>(null)
  const [error, setError] = useState<string | null>(null)

  const analyze = async (
    content: string,
    userAddress?: string,
    knownAddresses?: string[],
    useEnhanced: boolean = false
  ) => {
    setIsAnalyzing(true)
    setError(null)
    setResult(null)

    try {
      const endpoint = useEnhanced ? '/analyze-enhanced' : '/analyze'
      const body: any = { content }
      
      if (userAddress) {
        body.user_address = userAddress
      }
      
      if (useEnhanced && knownAddresses) {
        body.known_addresses = knownAddresses
      }

      const response = await fetch(`${API_URL}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }))
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      setResult(data)
      return data
    } catch (err: any) {
      const errorMessage = err.message || 'Failed to analyze content'
      setError(errorMessage)
      console.error('Analysis error:', err)
      throw err
    } finally {
      setIsAnalyzing(false)
    }
  }

  const reset = () => {
    setResult(null)
    setError(null)
    setIsAnalyzing(false)
  }

  return {
    analyze,
    isAnalyzing,
    result,
    error,
    reset,
  }
}

