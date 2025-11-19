'use client'

import { motion, useInView } from 'framer-motion'
import { useRef } from 'react'

export default function HowItWorks() {
  const containerRef = useRef<HTMLDivElement>(null)
  const isInView = useInView(containerRef, { once: true, amount: 0.2 })

  const steps = [
    {
      number: '1',
      title: 'Connect Your Wallet',
      description: 'MetaMask integration with Gnosis Chain RPC for EVM-compatible wallet authentication and xDAI balance verification',
    },
    {
      number: '2',
      title: 'Submit Wallet Address',
      description: 'Input Gnosis Chain wallet address for on-chain behavioral analysis and transaction pattern extraction',
    },
    {
      number: '3',
      title: 'Vector Search Analysis',
      description: 'Qdrant semantic similarity search across 5 specialized collections using 768-dimensional embeddings and cosine similarity scoring',
    },
    {
      number: '4',
      title: 'Risk Assessment',
      description: 'Comprehensive threat scoring with behavioral clustering, anomaly detection, and pattern match confidence metrics',
    },
  ]

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.15,
        delayChildren: 0.2,
      },
    },
  }

  const stepVariants = {
    hidden: { 
      opacity: 0, 
      y: 20,
    },
    visible: {
      opacity: 1,
      y: 0,
      transition: {
        duration: 0.5,
        ease: [0.22, 1, 0.36, 1],
      },
    },
  }

  return (
    <section 
      ref={containerRef}
      id="how-it-works" 
      className="relative py-32 px-4 sm:px-6 lg:px-8 bg-[#0a0a0a] overflow-hidden"
    >
      <div className="max-w-5xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 30 }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="text-center mb-20"
        >
          <h2 className="text-5xl md:text-6xl lg:text-7xl font-bold mb-6 text-white">
            How It <span className="text-primary-400">Works</span>
          </h2>
          <p className="text-xl md:text-2xl text-gray-400 max-w-3xl mx-auto leading-relaxed">
            Simple, fast, and secure threat detection in four easy steps
          </p>
        </motion.div>

        <motion.div
          variants={containerVariants}
          initial="hidden"
          animate={isInView ? 'visible' : 'hidden'}
          className="relative"
        >
          {/* Vertical timeline line */}
          <div className="absolute left-0 top-0 bottom-0 w-0.5 bg-gray-700" />
          
          <div className="space-y-8">
            {steps.map((step, index) => (
              <motion.div
                key={index}
                variants={stepVariants}
                whileHover={{ 
                  x: 8,
                  transition: { duration: 0.2, ease: "easeOut" }
                }}
                className="relative flex items-start gap-6 group"
              >
                {/* Step number - normal font, promptingcompany style */}
                <div className="relative flex-shrink-0">
                  <div className="absolute left-0 top-0 w-4 h-4 bg-primary-500 rounded-full -translate-x-1/2 border-2 border-[#0a0a0a] z-10" />
                  <div className="w-14 h-14 bg-primary-500 text-white rounded-lg flex items-center justify-center text-xl font-semibold shadow-lg">
                    {step.number}
                  </div>
                </div>
                
                {/* Content card - dark background like promptingcompany */}
                <motion.div
                  className="flex-1 bg-gray-900 text-white rounded-lg p-6 border border-gray-800 group-hover:border-primary-500/30 transition-all duration-300"
                >
                  <div className="mb-1">
                    <span className="text-xs font-medium text-gray-400 uppercase tracking-wider">
                      STEP {step.number}
                    </span>
                  </div>
                  <h3 className={`text-xl font-bold mb-2 transition-colors duration-300 ${
                    index === 2 ? 'text-primary-400' : 'text-white'
                  }`}>
                    {step.title}
                  </h3>
                  <p className="text-gray-400 leading-relaxed text-sm">
                    {step.description}
                  </p>
                </motion.div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  )
}
