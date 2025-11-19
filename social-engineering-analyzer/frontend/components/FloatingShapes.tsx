'use client'

import { motion } from 'framer-motion'

export default function FloatingShapes() {
  const shapes = [
    {
      initial: { x: '10%', y: '20%', rotate: 0 },
      animate: {
        x: ['10%', '15%', '8%', '12%', '10%'],
        y: ['20%', '25%', '18%', '22%', '20%'],
        rotate: [0, 90, 180, 270, 360],
      },
      transition: { duration: 20, repeat: Infinity, ease: 'easeInOut' },
      className: 'w-32 h-32',
      color: 'from-primary-400/20 to-blue-400/10',
    },
    {
      initial: { x: '80%', y: '60%', rotate: 0 },
      animate: {
        x: ['80%', '85%', '78%', '82%', '80%'],
        y: ['60%', '65%', '58%', '62%', '60%'],
        rotate: [360, 270, 180, 90, 0],
      },
      transition: { duration: 25, repeat: Infinity, ease: 'easeInOut' },
      className: 'w-24 h-24',
      color: 'from-emerald-400/20 to-teal-400/10',
    },
    {
      initial: { x: '50%', y: '80%', rotate: 0 },
      animate: {
        x: ['50%', '55%', '48%', '52%', '50%'],
        y: ['80%', '85%', '78%', '82%', '80%'],
        rotate: [0, -90, -180, -270, -360],
      },
      transition: { duration: 18, repeat: Infinity, ease: 'easeInOut' },
      className: 'w-20 h-20',
      color: 'from-purple-400/20 to-pink-400/10',
    },
    {
      initial: { x: '20%', y: '70%', rotate: 0 },
      animate: {
        x: ['20%', '25%', '18%', '22%', '20%'],
        y: ['70%', '75%', '68%', '72%', '70%'],
        rotate: [360, 270, 180, 90, 0],
      },
      transition: { duration: 22, repeat: Infinity, ease: 'easeInOut' },
      className: 'w-16 h-16',
      color: 'from-cyan-400/20 to-blue-400/10',
    },
  ]

  return (
    <div className="absolute inset-0 overflow-hidden pointer-events-none">
      {shapes.map((shape, index) => (
        <motion.div
          key={index}
          initial={shape.initial}
          animate={shape.animate}
          transition={shape.transition}
          className={`absolute ${shape.className} bg-gradient-to-br ${shape.color} rounded-full blur-xl`}
        />
      ))}
      
      {/* Floating geometric shapes */}
      {[...Array(6)].map((_, i) => (
        <motion.div
          key={`geometric-${i}`}
          className="absolute"
          initial={{
            x: `${20 + i * 15}%`,
            y: `${30 + (i % 3) * 20}%`,
            opacity: 0.1,
          }}
          animate={{
            y: [`${30 + (i % 3) * 20}%`, `${35 + (i % 3) * 20}%`, `${25 + (i % 3) * 20}%`, `${30 + (i % 3) * 20}%`],
            rotate: [0, 180, 360],
            scale: [1, 1.2, 1],
          }}
          transition={{
            duration: 15 + i * 2,
            repeat: Infinity,
            ease: 'easeInOut',
            delay: i * 0.5,
          }}
        >
          <svg
            width="40"
            height="40"
            viewBox="0 0 40 40"
            fill="none"
            className="text-primary-500/20"
          >
            <polygon
              points="20,5 35,15 35,25 20,35 5,25 5,15"
              fill="currentColor"
              opacity="0.3"
            />
          </svg>
        </motion.div>
      ))}
    </div>
  )
}

