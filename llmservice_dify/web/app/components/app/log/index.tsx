'use client'
import type { FC, SVGProps } from 'react'
import React, { useState } from 'react'
import useSWR from 'swr'
import { usePathname } from 'next/navigation'
import { Pagination } from 'react-headless-pagination'
import { useDebounce } from 'ahooks'
import { omit } from 'lodash-es'
import dayjs from 'dayjs'
import { ArrowLeftIcon, ArrowRightIcon } from '@heroicons/react/24/outline'
import { Trans, useTranslation } from 'react-i18next'
import Link from 'next/link'
import List from './list'
import Filter from './filter'
import s from './style.module.css'
import Loading from '@/app/components/base/loading'
import { fetchChatConversations, fetchCompletionConversations } from '@/service/log'
import { APP_PAGE_LIMIT } from '@/config'
import type { App, AppMode } from '@/types/app'
export type ILogsProps = {
  appDetail: App
}

export type QueryParam = {
  period?: number | string
  annotation_status?: string
  keyword?: string
  sort_by?: string
}

const ThreeDotsIcon = ({ className }: SVGProps<SVGElement>) => {
  return <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" className={className ?? ''}>
    <path d="M5 6.5V5M8.93934 7.56066L10 6.5M10.0103 11.5H11.5103" stroke="#374151" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
}

const EmptyElement: FC<{ appUrl: string }> = ({ appUrl }) => {
  const { t } = useTranslation()
  const pathname = usePathname()
  const pathSegments = pathname.split('/')
  pathSegments.pop()
  return <div className='flex items-center justify-center h-full'>
    <div className='bg-background-section-burn w-[560px] h-fit box-border px-5 py-4 rounded-2xl'>
      <span className='text-text-secondary system-md-semibold'>{t('appLog.table.empty.element.title')}<ThreeDotsIcon className='inline relative -top-3 -left-1.5' /></span>
      <div className='mt-2 text-text-tertiary system-sm-regular'>
        <Trans
          i18nKey="appLog.table.empty.element.content"
          components={{ shareLink: <Link href={`${pathSegments.join('/')}/overview`} className='text-util-colors-blue-blue-600' />, testLink: <Link href={appUrl} className='text-util-colors-blue-blue-600' target='_blank' rel='noopener noreferrer' /> }}
        />
      </div>
    </div>
  </div>
}

const Logs: FC<ILogsProps> = ({ appDetail }) => {
  const { t } = useTranslation()
  const [queryParams, setQueryParams] = useState<QueryParam>({
    period: 7,
    annotation_status: 'all',
    sort_by: '-created_at',
  })
  const [currPage, setCurrPage] = React.useState<number>(0)
  const debouncedQueryParams = useDebounce(queryParams, { wait: 500 })

  // Get the app type first
  const isChatMode = appDetail.mode !== 'completion'

  const query = {
    page: currPage + 1,
    limit: APP_PAGE_LIMIT,
    ...(debouncedQueryParams.period !== 'all'
      ? {
        start: dayjs().subtract(debouncedQueryParams.period as number, 'day').startOf('day').format('YYYY-MM-DD HH:mm'),
        end: dayjs().endOf('day').format('YYYY-MM-DD HH:mm'),
      }
      : {}),
    ...(isChatMode ? { sort_by: debouncedQueryParams.sort_by } : {}),
    ...omit(debouncedQueryParams, ['period']),
  }

  const getWebAppType = (appType: AppMode) => {
    if (appType !== 'completion' && appType !== 'workflow')
      return 'chat'
    return appType
  }

  // When the details are obtained, proceed to the next request
  const { data: chatConversations, mutate: mutateChatList } = useSWR(() => isChatMode
    ? {
      url: `/apps/${appDetail.id}/chat-conversations`,
      params: query,
    }
    : null, fetchChatConversations)

  const { data: completionConversations, mutate: mutateCompletionList } = useSWR(() => !isChatMode
    ? {
      url: `/apps/${appDetail.id}/completion-conversations`,
      params: query,
    }
    : null, fetchCompletionConversations)

  const total = isChatMode ? chatConversations?.total : completionConversations?.total

  return (
    <div className='flex flex-col h-full'>
      <p className='text-text-tertiary system-sm-regular'>{t('appLog.description')}</p>
      <div className='flex flex-col py-4 flex-1'>
        <Filter isChatMode={isChatMode} appId={appDetail.id} queryParams={queryParams} setQueryParams={setQueryParams} />
        {total === undefined
          ? <Loading type='app' />
          : total > 0
            ? <List logs={isChatMode ? chatConversations : completionConversations} appDetail={appDetail} onRefresh={isChatMode ? mutateChatList : mutateCompletionList} />
            : <EmptyElement appUrl={`${appDetail.site.app_base_url}/${getWebAppType(appDetail.mode)}/${appDetail.site.access_token}`} />
        }
        {/* Show Pagination only if the total is more than the limit */}
        {(total && total > APP_PAGE_LIMIT)
          ? <Pagination
            className="flex items-center w-full h-10 text-sm select-none mt-8"
            currentPage={currPage}
            edgePageCount={2}
            middlePagesSiblingCount={1}
            setCurrentPage={setCurrPage}
            totalPages={Math.ceil(total / APP_PAGE_LIMIT)}
            truncableClassName="w-8 px-0.5 text-center"
            truncableText="..."
          >
            <Pagination.PrevButton
              disabled={currPage === 0}
              className={`flex items-center mr-2 text-gray-500  focus:outline-none ${currPage === 0 ? 'cursor-not-allowed opacity-50' : 'cursor-pointer hover:text-gray-600 dark:hover:text-gray-200'}`} >
              <ArrowLeftIcon className="mr-3 h-3 w-3" />
              {t('appLog.table.pagination.previous')}
            </Pagination.PrevButton>
            <div className={`flex items-center justify-center flex-grow ${s.pagination}`}>
              <Pagination.PageButton
                activeClassName="bg-primary-50 dark:bg-opacity-0 text-primary-600 dark:text-white"
                className="flex items-center justify-center h-8 w-8 rounded-full cursor-pointer"
                inactiveClassName="text-gray-500"
              />
            </div>
            <Pagination.NextButton
              disabled={currPage === Math.ceil(total / APP_PAGE_LIMIT) - 1}
              className={`flex items-center mr-2 text-gray-500 focus:outline-none ${currPage === Math.ceil(total / APP_PAGE_LIMIT) - 1 ? 'cursor-not-allowed opacity-50' : 'cursor-pointer hover:text-gray-600 dark:hover:text-gray-200'}`} >
              {t('appLog.table.pagination.next')}
              <ArrowRightIcon className="ml-3 h-3 w-3" />
            </Pagination.NextButton>
          </Pagination>
          : null}
      </div>
    </div>
  )
}

export default Logs
