'use client'
import { useTranslation } from 'react-i18next'
import { Fragment } from 'react'
import { useSWRConfig } from 'swr'
import {
  RiDeleteBinLine,
  RiLoopLeftLine,
  RiMoreFill,
  RiStickyNoteAddLine,
} from '@remixicon/react'
import { Menu, Transition } from '@headlessui/react'
import { syncDataSourceNotion, updateDataSourceNotionAction } from '@/service/common'
import Toast from '@/app/components/base/toast'

type OperateProps = {
  payload: {
    id: string
    total: number
  }
  onAuthAgain: () => void
}
export default function Operate({
  payload,
  onAuthAgain,
}: OperateProps) {
  const itemClassName = `
    flex px-3 py-2 hover:bg-gray-50 text-sm text-gray-700
    cursor-pointer
  `
  const itemIconClassName = `
  mr-2 mt-[2px] w-4 h-4 text-gray-500
  `
  const { t } = useTranslation()
  const { mutate } = useSWRConfig()

  const updateIntegrates = () => {
    Toast.notify({
      type: 'success',
      message: t('common.api.success'),
    })
    mutate({ url: 'data-source/integrates' })
  }
  const handleSync = async () => {
    await syncDataSourceNotion({ url: `/oauth/data-source/notion/${payload.id}/sync` })
    updateIntegrates()
  }
  const handleRemove = async () => {
    await updateDataSourceNotionAction({ url: `/data-source/integrates/${payload.id}/disable` })
    updateIntegrates()
  }

  return (
    <Menu as="div" className="relative inline-block text-left">
      {
        ({ open }) => (
          <>
            <Menu.Button className={`flex items-center justify-center w-8 h-8 rounded-lg hover:bg-gray-100 ${open && 'bg-gray-100'}`}>
              <RiMoreFill className='w-4 h-4' />
            </Menu.Button>
            <Transition
              as={Fragment}
              enter="transition ease-out duration-100"
              enterFrom="transform opacity-0 scale-95"
              enterTo="transform opacity-100 scale-100"
              leave="transition ease-in duration-75"
              leaveFrom="transform opacity-100 scale-100"
              leaveTo="transform opacity-0 scale-95"
            >
              <Menu.Items
                className="
                  absolute right-0 top-9 w-60 max-w-80
                  divide-y divide-gray-100 origin-top-right rounded-lg bg-white
                  shadow-lg
                "
              >
                <div className="px-1 py-1">
                  <Menu.Item>
                    <div
                      className={itemClassName}
                      onClick={onAuthAgain}
                    >
                      <RiStickyNoteAddLine className={itemIconClassName} />
                      <div>
                        <div className='leading-5'>{t('common.dataSource.notion.changeAuthorizedPages')}</div>
                        <div className='leading-5 text-xs text-gray-500'>
                          {payload.total} {t('common.dataSource.notion.pagesAuthorized')}
                        </div>
                      </div>
                    </div>
                  </Menu.Item>
                  <Menu.Item>
                    <div className={itemClassName} onClick={handleSync}>
                      <RiLoopLeftLine className={itemIconClassName} />
                      <div className='leading-5'>{t('common.dataSource.notion.sync')}</div>
                    </div>
                  </Menu.Item>
                </div>
                <Menu.Item>
                  <div className='p-1'>
                    <div className={itemClassName} onClick={handleRemove}>
                      <RiDeleteBinLine className={itemIconClassName} />
                      <div className='leading-5'>{t('common.dataSource.notion.remove')}</div>
                    </div>
                  </div>
                </Menu.Item>
              </Menu.Items>
            </Transition>
          </>
        )
      }
    </Menu>
  )
}
