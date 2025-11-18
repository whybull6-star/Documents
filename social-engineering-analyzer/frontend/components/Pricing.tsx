'use client'

import { useState, useEffect } from 'react'
import { useWallet } from '@/hooks/useWallet'
import { useSubscription } from '@/hooks/useSubscription'

export default function Pricing() {
  const { address, isConnected } = useWallet()
  const { isSubscribed, daysRemaining, isLoading, isPurchasing, error, purchaseSubscription, checkSubscription } = useSubscription()

  // Check subscription status when wallet connects
  useEffect(() => {
    if (isConnected && address) {
      checkSubscription(address)
    }
  }, [isConnected, address]) // eslint-disable-line react-hooks/exhaustive-deps

  const plans = [
    {
      name: 'Free',
      price: '0',
      priceLabel: 'Forever Free',
      description: 'Perfect for trying out the service',
      features: [
        '100 analyses per month',
        'Advanced AI threat detection',
        'Real-time pattern matching',
        'Basic API access',
        'Community support',
        'Email notifications',
        'Threat history tracking',
      ],
      cta: 'Get Started Free',
      popular: false,
      isFree: true,
    },
    {
      name: 'Pro',
      price: '8.99',
      priceLabel: '$8.99 USD',
      description: 'For power users and professionals',
      features: [
        'Unlimited analyses per month',
        'Premium AI threat detection',
        'Advanced pattern matching & clustering',
        'Full API access with webhooks',
        'Priority support',
        'Detailed threat reports & exports',
        'Custom threat pattern detection',
        'Batch analysis capabilities',
        'Historical analysis dashboard',
        'Early access to new features',
      ],
      cta: isSubscribed ? `Active (${daysRemaining} days left)` : 'Subscribe Now',
      ctaDisabled: isSubscribed || !isConnected,
      popular: true,
      isFree: false,
    },
  ]

  const handleSubscribe = async () => {
    console.log('Subscribe button clicked!')
    console.log('isConnected:', isConnected)
    console.log('isSubscribed:', isSubscribed)
    console.log('address:', address)
    
    if (!isConnected) {
      alert('Please connect your wallet first')
      return
    }

    if (isSubscribed) {
      console.log('Already subscribed, returning')
      return // Already subscribed
    }

    console.log('Calling purchaseSubscription...')
    try {
      await purchaseSubscription()
      // Success notification handled in hook
      if (address) {
        await checkSubscription(address)
      }
    } catch (err) {
      console.error('Subscription error:', err)
    }
  }

  return (
    <section id="pricing" className="py-20 px-4 sm:px-6 lg:px-8 bg-white">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Simple Pricing
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Pay with xDAI on Gnosis chain. No credit cards needed.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
          {plans.map((plan, index) => (
            <div
              key={index}
              className={`p-8 rounded-xl border-2 ${
                plan.popular
                  ? 'border-primary-600 shadow-xl scale-105 bg-gradient-to-br from-primary-50 to-white'
                  : 'border-gray-200 bg-white'
              }`}
            >
              {plan.popular && (
                <div className="text-center mb-4">
                  <span className="bg-primary-600 text-white px-4 py-1 rounded-full text-sm font-semibold">
                    Most Popular
                  </span>
                </div>
              )}
              
              <h3 className="text-2xl font-bold mb-2">{plan.name}</h3>
              <p className="text-gray-600 mb-6">{plan.description}</p>
              
              <div className="mb-6">
                <div className="flex items-baseline">
                  <span className="text-5xl font-bold">
                    {plan.price === '0' ? 'Free' : `$${plan.price}`}
                  </span>
                  {plan.price !== '0' && (
                    <span className="text-gray-600 ml-2">/month</span>
                  )}
                </div>
                {plan.price !== '0' && (
                  <p className="text-sm text-gray-500 mt-1">{plan.priceLabel}</p>
                )}
              </div>
              
              <ul className="space-y-3 mb-8">
                {plan.features.map((feature, fIndex) => (
                  <li key={fIndex} className="flex items-start">
                    <svg
                      className="w-5 h-5 text-primary-600 mr-2 mt-0.5 flex-shrink-0"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        fillRule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                        clipRule="evenodd"
                      />
                    </svg>
                    <span className="text-gray-700 text-sm">{feature}</span>
                  </li>
                ))}
              </ul>
              
              {error && plan.popular && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
                  <p className="text-red-600 text-sm text-center font-medium mb-1">{error}</p>
                  {error.includes('not configured') && (
                    <p className="text-xs text-red-500 text-center">
                      See <code className="bg-red-100 px-1 rounded">SETUP_SUBSCRIPTION.md</code> for deployment instructions
                    </p>
                  )}
                </div>
              )}
              
              {plan.isFree ? (
                <a
                  href="#wallet-analysis"
                  className="w-full py-3 rounded-lg font-semibold transition border-2 border-primary-600 text-primary-600 hover:bg-primary-50 inline-block text-center"
                >
                  {plan.cta}
                </a>
              ) : (
                <button
                  onClick={(e) => {
                    e.preventDefault()
                    console.log('Button clicked for plan:', plan.name)
                    if (!plan.isFree) {
                      handleSubscribe()
                    }
                  }}
                  disabled={plan.ctaDisabled || isPurchasing || isLoading}
                  className={`w-full py-3 rounded-lg font-semibold transition ${
                    plan.popular
                      ? isSubscribed
                        ? 'bg-gray-200 text-gray-600 cursor-default'
                        : 'bg-primary-600 text-white hover:bg-primary-700 disabled:opacity-50 disabled:cursor-not-allowed'
                      : 'border-2 border-primary-600 text-primary-600 hover:bg-primary-50'
                  }`}
                >
                  {isPurchasing && plan.popular ? 'Processing...' : plan.cta}
                </button>
              )}
              
              {!isConnected && plan.popular && (
                <p className="text-xs text-gray-500 text-center mt-2">
                  Connect wallet to subscribe
                </p>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
