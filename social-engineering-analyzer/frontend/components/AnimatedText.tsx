'use client'

import { motion } from 'framer-motion'
import { useEffect, useState } from 'react'

interface AnimatedTextProps {
  text: string | string[]
  className?: string
  delay?: number
  stagger?: number
}

/**
 * Animated text component with smooth reveal
 * Similar to promptingcompany.com moving text
 */
export default function AnimatedText({ text, className = '', delay = 0, stagger = 0.05 }: AnimatedTextProps) {
  const [isVisible, setIsVisible] = useState(false)
  const texts = Array.isArray(text) ? text : [text]

  useEffect(() => {
    const timer = setTimeout(() => setIsVisible(true), delay)
    return () => clearTimeout(timer)
  }, [delay])

  return (
    <div className={`text-reveal ${className}`}>
      {texts.map((line, index) => (
        <motion.span
          key={index}
          initial={{ opacity: 0, y: 50 }}
          animate={isVisible ? { opacity: 1, y: 0 } : { opacity: 0, y: 50 }}
          transition={{
            duration: 0.6,
            delay: delay + index * stagger,
            ease: [0.22, 1, 0.36, 1], // Smooth easing
          }}
          className="block"
        >
          {line}
        </motion.span>
      ))}
    </div>
  )
}

/**
 * Marquee/Scrolling text component
 */
export function ScrollingText({ children, speed = 50 }: { children: React.ReactNode; speed?: number }) {
  return (
    <div className="overflow-hidden whitespace-nowrap">
      <motion.div
        className="inline-block"
        animate={{
          x: [0, -100 + '%'],
        }}
        transition={{
          x: {
            repeat: Infinity,
            repeatType: 'loop',
            duration: speed,
            ease: 'linear',
          },
        }}
      >
        <span className="inline-block mr-8">{children}</span>
        <span className="inline-block">{children}</span>
      </motion.div>
    </div>
  )
}

