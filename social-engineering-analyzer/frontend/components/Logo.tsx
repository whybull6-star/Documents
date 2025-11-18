'use client'

type LogoProps = {
  size?: number
}

/**
 * Minimal Lurantis mark:
 * - Soft green circle
 * - Single straight diagonal slash (no curve)
 * - Slightly oversized inside the circle so it reads clearly
 */
export default function Logo({ size = 30 }: LogoProps) {
  const strokeWidth = 2

  return (
    <div
      className="inline-flex items-center justify-center rounded-full bg-primary-600"
      style={{ width: size, height: size }}
    >
      <svg
        viewBox="0 0 24 24"
        aria-hidden="true"
        className="text-white"
        style={{ width: size * 0.68, height: size * 0.68 }}
      >
        {/* Outer circle is provided by the background; this is just the inner slash */}
        {/* Single straight diagonal, centered visually */}
        <line
          x1="8"
          y1="16"
          x2="16"
          y2="8"
          stroke="currentColor"
          strokeWidth={strokeWidth}
          strokeLinecap="round"
        />
      </svg>
    </div>
  )
}


