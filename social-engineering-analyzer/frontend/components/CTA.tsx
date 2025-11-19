'use client'

import { motion, useInView } from 'framer-motion'
import { useRef } from 'react'

export default function CTA() {
  const ref = useRef<HTMLDivElement>(null)
  const isInView = useInView(ref, { once: true, amount: 0.2 })

  return (
    <section 
      ref={ref}
      className="relative py-32 px-4 sm:px-6 lg:px-8 bg-[#3a2f1f] overflow-hidden"
    >
      {/* Subtle wavy organic background patterns */}
      <div className="absolute inset-0 opacity-30">
        <div className="absolute top-0 right-0 w-96 h-96 bg-primary-800/20 rounded-full blur-3xl" style={{
          clipPath: 'polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%)',
        }} />
        <div className="absolute bottom-0 left-0 w-80 h-80 bg-primary-700/20 rounded-full blur-3xl" style={{
          clipPath: 'polygon(40% 0%, 60% 0%, 100% 40%, 100% 60%, 60% 100%, 40% 100%, 0% 60%, 0% 40%)',
        }} />
      </div>

      {/* Main content container - centered and well-spaced */}
      <div className="max-w-7xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 30 }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="relative bg-gradient-to-br from-primary-800 via-primary-900 to-primary-950 rounded-3xl overflow-visible shadow-2xl"
        >
          {/* Wavy organic patterns in corners */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-primary-700/10 rounded-full blur-2xl opacity-50" />
          <div className="absolute bottom-0 right-0 w-48 h-48 bg-primary-600/10 rounded-full blur-2xl opacity-50" />
          
          <div className="relative flex flex-col lg:flex-row items-center lg:overflow-visible">
            {/* Left side - Text content */}
            <div className="flex-1 p-12 lg:p-16 text-left space-y-8 lg:max-w-2xl z-10">
              <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={isInView ? { opacity: 1, x: 0 } : { opacity: 0, x: -20 }}
                transition={{ delay: 0.2, duration: 0.6 }}
              >
                <span className="text-primary-300 font-semibold text-sm uppercase tracking-wider">
                  GET STARTED
                </span>
              </motion.div>
              
              <motion.h2
                initial={{ opacity: 0, x: -20 }}
                animate={isInView ? { opacity: 1, x: 0 } : { opacity: 0, x: -20 }}
                transition={{ delay: 0.3, duration: 0.6 }}
                className="text-4xl md:text-5xl lg:text-6xl font-bold text-primary-100 leading-tight"
              >
                Ready to Protect Yourself?
              </motion.h2>
              
              <motion.p
                initial={{ opacity: 0, x: -20 }}
                animate={isInView ? { opacity: 1, x: 0 } : { opacity: 0, x: -20 }}
                transition={{ delay: 0.4, duration: 0.6 }}
                className="text-lg md:text-xl text-white/90 leading-relaxed"
              >
                We're building the infrastructure for secure Web3 interactions. A resilient and credibly neutral platform open to anyone without privilege or prejudice. Be a part of protecting the decentralized web.
              </motion.p>
              
              <motion.div
                initial={{ opacity: 0, x: -20 }}
                animate={isInView ? { opacity: 1, x: 0 } : { opacity: 0, x: -20 }}
                transition={{ delay: 0.5, duration: 0.6 }}
                className="flex flex-col sm:flex-row gap-4 pt-4"
              >
                <motion.a
                  href="#wallet-analysis"
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                  className="bg-primary-600 hover:bg-primary-500 text-white px-8 py-4 rounded-lg font-semibold text-center transition-colors duration-300 shadow-lg"
                >
                  Start Free Trial
                </motion.a>
                <motion.button
                  whileHover={{ scale: 1.02, borderColor: 'rgba(255, 255, 255, 0.6)' }}
                  whileTap={{ scale: 0.98 }}
                  className="border-2 border-primary-300/50 text-primary-200 hover:text-white px-8 py-4 rounded-lg font-semibold transition-all duration-300 bg-transparent"
                >
                  Learn More
                </motion.button>
              </motion.div>
            </div>

            {/* Right side - Image that protrudes */}
            <div className="relative w-full lg:w-1/2 h-96 lg:h-[600px] flex items-center justify-center lg:overflow-visible">
              {/* Image container with organic rounded edges that protrude */}
              <motion.div
                initial={{ opacity: 0, x: 40, scale: 0.9 }}
                animate={isInView ? { opacity: 1, x: 0, scale: 1 } : { opacity: 0, x: 40, scale: 0.9 }}
                transition={{ delay: 0.6, duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
                className="relative w-full h-full lg:absolute lg:right-0 lg:translate-x-8 lg:w-[120%] lg:h-[120%]"
                style={{
                  clipPath: 'polygon(20% 10%, 80% 5%, 95% 30%, 100% 70%, 85% 95%, 25% 100%, 5% 70%, 0% 30%)',
                }}
              >
                {/* Abstract image - using gradient with organic shapes */}
                <div className="absolute inset-0 bg-gradient-to-br from-blue-900 via-purple-900 to-primary-800 rounded-3xl overflow-hidden">
                  {/* Sky gradient */}
                  <div className="absolute inset-0 bg-gradient-to-b from-blue-800 via-purple-700 to-primary-900" />
                  
                  {/* Organic shapes overlay */}
                  <div className="absolute inset-0">
                    {/* Metallic structures */}
                    <div className="absolute bottom-0 left-1/2 transform -translate-x-1/2 w-80 h-80 bg-gradient-to-t from-slate-700 via-slate-500 to-slate-300 rounded-full opacity-40 blur-xl" />
                    <div className="absolute bottom-10 left-1/4 w-32 h-32 bg-gradient-to-br from-emerald-400/30 to-primary-400/30 rounded-2xl rotate-45 opacity-60" />
                    <div className="absolute bottom-20 right-1/4 w-24 h-24 bg-gradient-to-br from-cyan-400/30 to-blue-400/30 rounded-xl rotate-12 opacity-50" />
                    
                    {/* Glowing nodes */}
                    <div className="absolute top-1/3 left-1/3 w-3 h-3 bg-primary-400 rounded-full shadow-lg shadow-primary-400/50 animate-pulse" />
                    <div className="absolute top-1/2 right-1/3 w-2 h-2 bg-cyan-400 rounded-full shadow-lg shadow-cyan-400/50 animate-pulse" style={{ animationDelay: '0.5s' }} />
                    <div className="absolute bottom-1/3 left-1/2 w-2.5 h-2.5 bg-emerald-400 rounded-full shadow-lg shadow-emerald-400/50 animate-pulse" style={{ animationDelay: '1s' }} />
                  </div>
                  
                  {/* Connecting lines */}
                  <svg className="absolute inset-0 w-full h-full opacity-30">
                    <line x1="33%" y1="33%" x2="50%" y2="50%" stroke="rgba(16, 185, 129, 0.4)" strokeWidth="1" />
                    <line x1="67%" y1="33%" x2="50%" y2="50%" stroke="rgba(16, 185, 129, 0.4)" strokeWidth="1" />
                    <line x1="50%" y1="50%" x2="50%" y2="67%" stroke="rgba(16, 185, 129, 0.4)" strokeWidth="1" />
                  </svg>
                </div>
                
                {/* Protruding edge effect */}
                <div className="absolute -right-8 top-1/2 transform -translate-y-1/2 w-16 h-32 bg-gradient-to-l from-primary-800 to-transparent opacity-50 blur-sm" />
              </motion.div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}
