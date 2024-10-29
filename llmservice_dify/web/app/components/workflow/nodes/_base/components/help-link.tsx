import { memo } from 'react'
import { useTranslation } from 'react-i18next'
import { RiBookOpenLine } from '@remixicon/react'
import { useNodeHelpLink } from '../hooks/use-node-help-link'
import TooltipPlus from '@/app/components/base/tooltip'
import type { BlockEnum } from '@/app/components/workflow/types'

type HelpLinkProps = {
  nodeType: BlockEnum
}
const HelpLink = ({
  nodeType,
}: HelpLinkProps) => {
  const { t } = useTranslation()
  const link = useNodeHelpLink(nodeType)

  return (
    <TooltipPlus
      popupContent={t('common.userProfile.helpCenter')}
    >
      <a
        href={link}
        target='_blank'
        className='flex items-center justify-center mr-1 w-6 h-6'
      >
        <RiBookOpenLine className='w-4 h-4 text-gray-500' />
      </a>
    </TooltipPlus>

  )
}

export default memo(HelpLink)
