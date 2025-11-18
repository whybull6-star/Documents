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
      x: -30,
      scale: 0.95
    },
    visible: {
      opacity: 1,
      x: 0,
      scale: 1,
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
      className="relative py-32 px-4 sm:px-6 lg:px-8 bg-gray-50 overflow-hidden"
    >
      {/* Subtle organic blobs */}
      <motion.div
        className="organic-blob w-[400px] h-[400px] bg-gradient-to-br from-primary-200/20 via-blue-200/15 to-purple-200/15"
        style={{ top: '10%', right: '-5%' }}
        animate={{
          x: [0, 20, -15, 0],
          y: [0, -25, 15, 0],
        }}
        transition={{
          duration: 25,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div
        className="organic-blob w-[350px] h-[350px] bg-gradient-to-br from-emerald-200/15 via-teal-200/10 to-cyan-200/15"
        style={{ bottom: '10%', left: '-5%' }}
        animate={{
          x: [0, -20, 15, 0],
          y: [0, 25, -15, 0],
        }}
        transition={{
          duration: 30,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <div className="max-w-6xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 30 }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="text-center mb-20"
        >
          <h2 className="text-5xl md:text-6xl lg:text-7xl font-bold mb-6">
            How It <span className="gradient-text">Works</span>
          </h2>
          <p className="text-xl md:text-2xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
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
          <div className="hidden md:block absolute left-8 top-0 bottom-0 w-1 bg-gray-200" />
          
          <div className="space-y-12 md:space-y-16">
            {steps.map((step, index) => (
              <motion.div
                key={index}
                variants={stepVariants}
                whileHover={{ 
                  scale: 1.02,
                  x: 8,
                  transition: { duration: 0.2, ease: "easeOut" }
                }}
                className="relative flex items-start gap-6 md:gap-8 group"
              >
                {/* Timeline dot */}
                <div className="relative flex-shrink-0">
                  <div className="hidden md:block absolute left-8 top-6 w-4 h-4 bg-primary-600 rounded-full border-4 border-white shadow-lg z-10" />
                  
                  {/* Step number badge */}
                  <motion.div
                    whileHover={{ 
                      scale: 1.1,
                      transition: { duration: 0.2 }
                    }}
                    className="w-16 h-16 md:w-20 md:h-20 bg-primary-600 text-white rounded-xl flex items-center justify-center text-2xl md:text-3xl font-bold shadow-lg group-hover:shadow-xl transition-shadow duration-300"
                  >
                    {step.number}
                  </motion.div>
                </div>
                
                {/* Content card */}
                <motion.div
                  whileHover={{ 
                    scale: 1.01,
                    transition: { duration: 0.2 }
                  }}
                  className="flex-1 bg-gray-900 text-white rounded-xl p-6 md:p-8 shadow-lg group-hover:shadow-xl transition-all duration-300"
                >
                  <div className="mb-2">
                    <span className="text-xs md:text-sm font-semibold text-gray-400 uppercase tracking-wider">
                      STEP {step.number}
                    </span>
                  </div>
                  <h3 className="text-xl md:text-2xl font-bold mb-3 text-white group-hover:text-primary-400 transition-colors duration-300">
                    {step.title}
                  </h3>
                  <p className="text-gray-300 leading-relaxed text-sm md:text-base">
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
