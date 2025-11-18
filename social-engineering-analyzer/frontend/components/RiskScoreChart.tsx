'use client'

import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts'

interface RiskScoreChartProps {
  riskScore: number
  riskLevel: string
  patternMatches: number
  maxPatternSimilarity: number
}

const COLORS = {
  CRITICAL: '#EF4444',
  HIGH: '#F97316',
  MEDIUM: '#EAB308',
  LOW: '#22C55E',
}

export default function RiskScoreChart({ riskScore, riskLevel, patternMatches, maxPatternSimilarity }: RiskScoreChartProps) {
  // Create data for pie chart showing risk breakdown
  const riskData = [
    { name: 'Risk Score', value: riskScore, fill: COLORS[riskLevel as keyof typeof COLORS] || COLORS.LOW },
    { name: 'Remaining', value: 100 - riskScore, fill: '#E5E7EB' },
  ]

  // Create data for pattern similarity gauge
  const similarityData = [
    { name: 'Pattern Match', value: maxPatternSimilarity * 100, fill: '#3B82F6' },
    { name: 'Remaining', value: 100 - (maxPatternSimilarity * 100), fill: '#E5E7EB' },
  ]

  return (
    <div className="grid md:grid-cols-2 gap-6 mt-6">
      {/* Risk Score Gauge */}
      <div className="bg-white rounded-lg p-4 border border-gray-200">
        <h4 className="text-sm font-semibold text-gray-700 mb-4 text-center">Risk Score</h4>
        <ResponsiveContainer width="100%" height={200}>
          <PieChart>
            <Pie
              data={riskData}
              cx="50%"
              cy="50%"
              innerRadius={60}
              outerRadius={80}
              startAngle={90}
              endAngle={-270}
              dataKey="value"
            >
              {riskData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.fill} />
              ))}
            </Pie>
            <Tooltip />
            <text
              x="50%"
              y="50%"
              textAnchor="middle"
              dominantBaseline="middle"
              className="text-2xl font-bold"
              fill={COLORS[riskLevel as keyof typeof COLORS] || COLORS.LOW}
            >
              {riskScore.toFixed(0)}
            </text>
          </PieChart>
        </ResponsiveContainer>
        <div className="text-center mt-2">
          <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
            riskLevel === 'CRITICAL' ? 'bg-red-100 text-red-800' :
            riskLevel === 'HIGH' ? 'bg-orange-100 text-orange-800' :
            riskLevel === 'MEDIUM' ? 'bg-yellow-100 text-yellow-800' :
            'bg-green-100 text-green-800'
          }`}>
            {riskLevel} RISK
          </span>
        </div>
      </div>

      {/* Pattern Similarity Gauge */}
      <div className="bg-white rounded-lg p-4 border border-gray-200">
        <h4 className="text-sm font-semibold text-gray-700 mb-4 text-center">Pattern Match Similarity</h4>
        <ResponsiveContainer width="100%" height={200}>
          <PieChart>
            <Pie
              data={similarityData}
              cx="50%"
              cy="50%"
              innerRadius={60}
              outerRadius={80}
              startAngle={90}
              endAngle={-270}
              dataKey="value"
            >
              {similarityData.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.fill} />
              ))}
            </Pie>
            <Tooltip />
            <text
              x="50%"
              y="50%"
              textAnchor="middle"
              dominantBaseline="middle"
              className="text-2xl font-bold"
              fill="#3B82F6"
            >
              {(maxPatternSimilarity * 100).toFixed(0)}%
            </text>
          </PieChart>
        </ResponsiveContainer>
        <div className="text-center mt-2">
          <span className="text-xs text-gray-600">
            {patternMatches} pattern{patternMatches !== 1 ? 's' : ''} matched
          </span>
        </div>
      </div>
    </div>
  )
}

