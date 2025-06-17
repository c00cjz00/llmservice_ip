---
title: iService_系統/主機通用問題

---

# iService_系統/主機通用問題

### Q: 查詢主機帳號 
A:
登入計算主機需使用「主機帳號」、「主機密碼」 ＋ 「OTP 認證碼」，若忘記設定的主機帳號，查詢的方式如下：
Step 1. 登入 iService 後，點入「會員中心」 ＞ 「主機帳號資訊」
Step 2. 便可找到主機帳號


### Q: 如何長久保存資料或進行資料備份到外部雲端儲存或是備分至用戶自己的電腦上 
A:
購買HPC主機的高效能平行檔案系統儲存空間，來存放大量的靜態資料或非運算用檔案，其實不符合用戶的經濟效益。
當用戶有大量靜態資料想要長久保存或進行備份，
建議您於登入節點使用s3cmd命令，將檔案上傳到外部雲端物件儲存(Object Storage)保存。

關於申請TWCC COS儲存服務，詳如[說明](https://www.twcc.ai/intro/STORAGE)

關於存取TWCC COS與S3用戶端工具使用，詳如[COS儲存說明一](https://man.twcc.ai/@twccdocs/howto-twnia2-access-cos-zh)與[說明二](https://man.twcc.ai/@twccdocs/doc-cos-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fcosbackup-zh)

如果用戶想將資料備份至自己的電腦，請參閱各HPC計算主機有關資料傳輸節點的說明
[Taiwania1號用戶](https://iservice.nchc.org.tw/download_file.php?f=T91UfGjyGP5HOUe9HMG9Z9Dn2vuLSAvViZsCKzBV_kKuk-i7VkMwfWPgyKhhliyP7fwR5jWy02syNq7b6ojdRQ)
[Taiwania2號用戶](https://man.twcc.ai/@twccdocs/doc-hfs-main-zh/%2F%40twccdocs%2Fguide-hfs-connect-to-data-transfer-node-zh)
[Taiwania3號用戶](https://man.twcc.ai/@TWCC-III-manual/SyGsFqRSt)



### Q: 如何在國網中心的HPC系統加密你的檔案或是目錄? 
A:
當您在HPC系統想要加密您的資料時，可以在命令列下使用以下指令
- 壓縮並加密
```
tar -czvf - your_file_or_your_directory | openssl des3 -salt -k password -out /path/to/file.tar.gz
```
 
- 解密並解壓縮
```
openssl des3 -d -k password -salt -in /path/to/file.tar.gz | tar xzf
```


### Q: iService 網站開發原則與政策
A:
* 安全開發程序和作法
我們的服務採用多層次安全機制，包括多因素驗證、資料加密、入侵檢測和預防、網絡安全措施等等。我們還使用安全開發生命週期來確保我們的服務在開發過程中實現最高的安全標準。
* 政策相容性
我們的服務符合各種國際標準，包括ISO 27001, ISO 20000等。我們也遵守當地法律法規和隱私要求，並且在隱私和數據保護方面承諾提供高水平的保護和監管措施。
* 監控和合規性
確保服務的運作始終處於最高的安全狀態。我們也定期接受獨立的安全測試和稽核，以確保我們的服務符合最嚴格的安全標準。
* 數據保護和隱私
我們承諾保護用戶的數據安全和隱私，並且僅在必要的情況下收集和使用數據。我們的服務提供完整的隱私政策和資訊安全政策，以讓用戶更加明確地了解我們對數據的使用和保護。



### Q: HPC登入節點兩階段驗證APP載具註冊與使用說明#自行重建載具#OTP 
A:
1. APP 載具註冊
    a. 登入 iService 後，點選 會員資訊->主機帳號資訊，進入載具註冊建立頁面。
    b. 點選 "建立OTP載具” 按鈕。收取APP載具註冊通知信，依信件內容進行APP載具註冊作業。
2. 登入節點驗證
    a. 連線至登入節點
    b. 輸入兩階段驗證方式（2FA login method ）, 請選擇 1 or 2 or 3
        - 選擇 ( 1 ). Mobile APP OTP : (若手機無網路也可使用)打開手機APP，取得  OTP 驗證碼。
        - 選擇( 2 ). Mobile APP Push：(要有網路)打開手機APP，以指紋或臉部辨識進行驗證。
        - 選擇( 3 ). Email OTP：收取信件，取得 OTP 驗證碼。

    c. 輸入主機帳號的密碼
    d.依所選擇的兩階段驗證方式(2FA login method)，進行驗證作業
3. 自行重建載具
若您更換手機或重新安裝APP，需重新進行載具安裝作業時，請至會員資訊->主機帳號資訊，進入修改主機帳號基本資料，點選[刪除載具]後，即可重新進行上方 1.b. [建立OTP載具]，進行新的註冊作業。注意：用戶線上刪除載具並重置載具後須30天後才能再次執行此功能。


### Q: Thinlinc 如何登入OTP
A:
* 方法一：APP OTP
![image](https://hackmd.io/_uploads/B1XYD2KWxg.png)

* 方法二：PUSH OTP
![image](https://hackmd.io/_uploads/Hki5P2t-ex.png)

* 方法三：Email OTP (三分鐘內僅會發送一次email，三分鐘內第二次驗證請使用同一組OTP)
![image](https://hackmd.io/_uploads/r182D2F-xg.png)
