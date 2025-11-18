'use client'

import { motion, useScroll, useTransform, AnimatePresence } from 'framer-motion'
import { useRef, useEffect } from 'react'
import { useWallet } from '@/hooks/useWallet'

export default function Hero() {
  const { address, balance, isConnected, formatAddress } = useWallet()
  const containerRef = useRef<HTMLDivElement>(null)
  
  // Debug: Log wallet state changes
  useEffect(() => {
    console.log('Hero: Wallet state changed - isConnected:', isConnected, 'address:', address, 'balance:', balance)
  }, [isConnected, address, balance])
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ['start start', 'end start']
  })

  const y = useTransform(scrollYProgress, [0, 1], [0, -50])
  const opacity = useTransform(scrollYProgress, [0, 0.5], [1, 0])

  return (
    <section 
      ref={containerRef}
      className="relative min-h-screen flex items-center pt-20 pb-20 px-4 sm:px-6 lg:px-8 overflow-hidden premium-dark"
    >
      {/* Gradient mesh background */}
      <div className="gradient-mesh" />
      
      {/* Network overlay */}
      <div className="network-overlay" />
      
      {/* Organic blob shapes - inspired by SpoonOS */}
      <motion.div
        className="organic-blob w-[500px] h-[500px] bg-gradient-to-br from-primary-500/30 via-blue-500/20 to-purple-500/20"
        style={{ top: '10%', left: '-10%' }}
        animate={{
          x: [0, 30, -20, 0],
          y: [0, -40, 20, 0],
        }}
        transition={{
          duration: 25,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div
        className="organic-blob w-[600px] h-[600px] bg-gradient-to-br from-emerald-400/25 via-teal-400/20 to-cyan-400/15"
        style={{ bottom: '5%', right: '-5%' }}
        animate={{
          x: [0, -40, 30, 0],
          y: [0, 30, -25, 0],
        }}
        transition={{
          duration: 30,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div
        className="organic-blob w-[400px] h-[400px] bg-gradient-to-br from-primary-400/20 via-green-400/15 to-emerald-400/20"
        style={{ top: '50%', right: '15%' }}
        animate={{
          x: [0, 25, -15, 0],
          y: [0, -30, 20, 0],
        }}
        transition={{
          duration: 20,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      
      {/* Network nodes */}
      {[...Array(12)].map((_, i) => (
        <motion.div
          key={i}
          className="network-node"
          style={{
            left: `${10 + (i * 7.5)}%`,
            top: `${15 + (i % 3) * 25}%`,
            animationDelay: `${i * 0.3}s`,
          }}
          animate={{
            scale: [1, 1.3, 1],
            opacity: [0.3, 0.7, 0.3],
          }}
          transition={{
            duration: 2 + (i % 3),
            repeat: Infinity,
            ease: "easeInOut",
            delay: i * 0.2,
          }}
        />
      ))}

      <motion.div 
        style={{ y, opacity }}
        className="relative max-w-7xl mx-auto w-full z-10"
      >
        <div className="text-center">
          {/* Main heading with stylish, compact design */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
            className="mb-6"
          >
            <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold leading-tight mb-3 tracking-tight">
              <span className="text-white">Detect Social Engineering</span>
              <br />
              <span className="gradient-text">Before It's Too Late</span>
            </h1>
          </motion.div>

          {/* Welcome message when wallet is connected */}
          {isConnected && address ? (
            <motion.div
              key="welcome-connected"
              initial={{ opacity: 0, y: -10, scale: 0.95 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: -10, scale: 0.95 }}
              transition={{ 
                duration: 0.3,
                ease: [0.22, 1, 0.36, 1]
              }}
              className="mb-6 flex justify-center"
            >
              <div className="bg-gray-900/90 border border-primary-500/30 rounded-full px-6 py-3 shadow-lg backdrop-blur-md" style={{ WebkitBackdropFilter: 'blur(12px)', backdropFilter: 'blur(12px)' }}>
                <p className="text-lg font-semibold text-primary-400 mb-1">
                  Welcome, {address ? formatAddress(address) : ''}!
                </p>
                <p className="text-sm text-gray-300 text-center">
                  Your balance: <span className="font-semibold text-primary-400">{balance || '0.0000'} xDAI</span>
                </p>
              </div>
            </motion.div>
          ) : null}
          
          {/* Subheading with smooth reveal - more compact */}
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ 
              delay: 0.3,
              duration: 0.6,
              ease: [0.22, 1, 0.36, 1]
            }}
            className="text-lg md:text-xl lg:text-2xl text-gray-300 mb-10 max-w-3xl mx-auto leading-relaxed"
          >
            Qdrant-leveraged, AI-powered platform using advanced vector search to identify scam patterns, phishing attempts, 
            and social engineering attacks in <span className="text-primary-500 font-semibold">real-time</span>
          </motion.p>

          {/* CTA Buttons with smooth hover effects */}
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ 
              delay: 1.2,
              duration: 0.8,
              ease: [0.22, 1, 0.36, 1]
            }}
            className="flex flex-col sm:flex-row gap-6 justify-center items-center mb-16"
          >
            <motion.a
              href="#wallet-analysis"
              whileHover={{ scale: 1.05, y: -2 }}
              whileTap={{ scale: 0.95 }}
              className="group relative bg-primary-600 text-white px-10 py-5 rounded-xl text-lg font-semibold shadow-xl hover:shadow-2xl transition-all duration-300 overflow-hidden inline-block cursor-pointer"
            >
              <span className="relative z-10">Get Started Free</span>
              <motion.div
                className="absolute inset-0 bg-primary-700"
                initial={{ x: '-100%' }}
                whileHover={{ x: 0 }}
                transition={{ duration: 0.3 }}
              />
            </motion.a>
            
            <motion.button
              whileHover={{ scale: 1.05, y: -2 }}
              whileTap={{ scale: 0.95 }}
              className="group border-2 border-primary-400 text-primary-400 px-10 py-5 rounded-xl text-lg font-semibold hover:bg-primary-500/10 transition-all duration-300 bg-gray-900/50 backdrop-blur-sm"
              style={{ WebkitBackdropFilter: 'blur(4px)', backdropFilter: 'blur(4px)' }}
            >
              Watch Demo
            </motion.button>
          </motion.div>

          {/* Demo preview with enhanced animation */}
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ 
              delay: 1.4,
              duration: 0.8,
              ease: [0.22, 1, 0.36, 1]
            }}
            className="mt-16 relative max-w-5xl mx-auto"
          >
            <div className="bg-gray-900/90 rounded-2xl shadow-2xl p-8 border border-gray-700/50 transform hover:scale-[1.02] transition-transform duration-500 backdrop-blur-xl" style={{ WebkitBackdropFilter: 'blur(24px)', backdropFilter: 'blur(24px)' }}>
              <div className="space-y-4">
                <div className="flex items-center space-x-2 mb-6">
                  <div className="w-3 h-3 rounded-full bg-red-500 animate-pulse" />
                  <div className="w-3 h-3 rounded-full bg-yellow-500 animate-pulse" style={{ animationDelay: '0.2s' }} />
                  <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse" style={{ animationDelay: '0.4s' }} />
                </div>
                <div className="bg-gray-900 rounded-xl p-6 font-mono text-sm space-y-3 border border-gray-700">
                  <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ delay: 1.6, duration: 0.5 }}
                    className="text-gray-300 flex items-center gap-2"
                  >
                    <span className="animate-pulse">🔍</span>
                    <span>Analyzing message...</span>
                  </motion.div>
                  <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 1.8, duration: 0.5 }}
                    className="text-green-400 font-semibold flex items-center gap-2"
                  >
                    <span>✓</span>
                    <span>Pattern match: 87% similarity to CISA Alert AA24-073A (SIM Swap)</span>
                  </motion.div>
                  <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 2, duration: 0.5 }}
                    className="text-red-400 font-semibold flex items-center gap-2"
                  >
                    <span>▲</span>
                    <span>Threat: Identity verification request pattern (1,247 reported incidents)</span>
                  </motion.div>
                  <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 2.2, duration: 0.5 }}
                    className="text-blue-400 flex items-center gap-2"
                  >
                    <span>ℹ</span>
                    <span>Recommendation: Do not provide phone number or SSN digits</span>
                  </motion.div>
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      </motion.div>

      {/* Scroll indicator */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 2, duration: 1 }}
        className="absolute bottom-8 left-1/2 transform -translate-x-1/2"
      >
        <motion.div
          animate={{ y: [0, 10, 0] }}
          transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
          className="flex flex-col items-center gap-2 text-gray-400"
        >
          <span className="text-sm">Scroll</span>
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </motion.div>
      </motion.div>
    </section>
  )
}
