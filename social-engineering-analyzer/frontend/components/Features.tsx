'use client'

import { motion, useInView } from 'framer-motion'
import { useRef } from 'react'

export default function Features() {
  const containerRef = useRef<HTMLDivElement>(null)
  const isInView = useInView(containerRef, { once: true, amount: 0.2 })

  const features = [
    {
      title: 'Vector Search AI',
      description: '768-dimensional embeddings via Sentence Transformers (all-mpnet-base-v2) with cosine similarity matching across 5 specialized Qdrant collections for semantic pattern recognition',
      icon: '🔍',
    },
    {
      title: 'Real-Time Analysis',
      description: 'FastAPI-powered approximate nearest neighbor search with multi-collection querying for instant threat detection and behavioral clustering',
      icon: '⚡',
    },
    {
      title: 'Blockchain Powered',
      description: 'Gnosis Chain integration with ERC-20 subscription contracts, Web3.py on-chain analysis, and MetaMask wallet connectivity',
      icon: '⛓️',
    },
    {
      title: 'Comprehensive Database',
      description: 'Patterns sourced from FBI IC3, CISA Advisories, Ethereum Foundation Security, OpenZeppelin, Rekt.news, and Chainabuse with verified incident metadata',
      icon: '📊',
    },
    {
      title: 'API Access',
      description: 'RESTful FastAPI endpoints for wallet analysis, transaction pattern detection, anomaly identification, and risk scoring with credit-based access control',
      icon: '🔌',
    },
    {
      title: 'Privacy First',
      description: 'Stateless analysis architecture with ephemeral vector processing and zero-persistence data handling for sensitive content',
      icon: '🔒',
    },
  ]

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.2,
      },
    },
  }

  const itemVariants = {
    hidden: { opacity: 0, y: 50, scale: 0.9 },
    visible: {
      opacity: 1,
      y: 0,
      scale: 1,
      transition: {
        duration: 0.5,
        ease: [0.22, 1, 0.36, 1],
      },
    },
  }

  return (
    <section id="features" className="relative py-32 px-4 sm:px-6 lg:px-8 bg-white overflow-hidden">
      {/* Subtle gradient mesh */}
      <div className="absolute inset-0 gradient-mesh opacity-30" />
      {/* Network overlay - subtle */}
      <div className="absolute inset-0 network-overlay opacity-10" />
      {/* Background decoration */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(16,185,129,0.1),transparent_50%)]" />
      
      <div ref={containerRef} className="max-w-7xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 30 }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="text-center mb-20"
        >
          <h2 className="text-5xl md:text-6xl lg:text-7xl font-bold mb-6">
            Powerful <span className="gradient-text">Features</span>
          </h2>
          <p className="text-xl md:text-2xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            Everything you need to protect yourself and your organization from social engineering attacks
          </p>
        </motion.div>

        <motion.div
          variants={containerVariants}
          initial="hidden"
          animate={isInView ? 'visible' : 'hidden'}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        >
          {features.map((feature, index) => (
            <motion.div
              key={index}
              variants={itemVariants}
              whileHover={{ 
                scale: 1.05, 
                y: -10,
                transition: { duration: 0.3 }
              }}
              className="group relative p-8 rounded-2xl border border-gray-200/50 bg-white/90 hover:border-primary-300 hover:shadow-2xl transition-all duration-300 overflow-hidden backdrop-blur-sm"
              style={{ WebkitBackdropFilter: 'blur(4px)', backdropFilter: 'blur(4px)' }}
            >
              {/* Hover effect gradient */}
              <div 
                className="absolute inset-0 transition-opacity duration-300 opacity-0 group-hover:opacity-100"
                style={{
                  background: 'linear-gradient(to bottom right, rgba(236, 253, 245, 0.5), rgba(209, 250, 229, 0.3))',
                }}
              />
              
              <div className="relative z-10">
                <motion.div 
                  className="text-5xl mb-6 inline-block"
                  whileHover={{ 
                    rotate: [0, -10, 10, -10, 0],
                    scale: 1.2
                  }}
                  transition={{ duration: 0.5 }}
                >
                  {feature.icon}
                </motion.div>
                <h3 className="text-2xl font-bold mb-3 group-hover:text-primary-600 transition-colors duration-300">
                  {feature.title}
                </h3>
                <p className="text-gray-600 leading-relaxed">
                  {feature.description}
                </p>
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  )
}
