import { memo } from 'react'
import cn from '@/utils/classnames'

type BadgeProps = {
  className?: string
  text: string
  uppercase?: boolean
}

const Badge = ({
  className,
  text,
  uppercase = true,
}: BadgeProps) => {
  return (
    <div
      className={cn(
        'inline-flex items-center px-[5px] h-5 rounded-[5px] border border-divider-deep  leading-3 text-text-tertiary',
        uppercase ? 'system-2xs-medium-uppercase' : 'system-xs-medium',
        className,
      )}
    >
      {text}
    </div>
  )
}

export default memo(Badge)