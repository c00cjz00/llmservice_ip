---
title: iService_軟體使用/化學資料庫服務

---

# iService_軟體使用/化學資料庫服務

### Q:化學資料庫服務申請說明
A: 
- 申請資格：化學資料庫服務目前僅開放學術機構使用
- 軟體使用說明，請參考[化學資料庫使用說明](https://iservice.nchc.org.tw/nchc_service/nchc_service_qa_single.php?qa_code=492)
- 申請流程說明：
    1. 登入iService 服務網 (新客戶要先註冊新會員) 會員申請，請參考如何進行[會員註冊](https://iservice.nchc.org.tw/nchc_service/nchc_service_qa_single.php?qa_code=32)。
    2. 登入服務網後，請選擇 【會員中心】-->【會員資訊】-->【服務啟用】
    ![image](https://hackmd.io/_uploads/B1eMI1jKblg.png)
    到該頁面後，請將服務類別切換為【平台服務】
    ![image](https://hackmd.io/_uploads/HkIDysKZxl.png)
    接著點擊右側圖示 ，依序填寫申請單內容後，按下一步，送出申請單即可。
    ![image](https://hackmd.io/_uploads/ryMOJjYZlg.png)
    本中心收到申請單後，將進行審核。
    審核結果將以信件通知，審核通過後，請以主機帳號及密碼登入主機使用服務。




### Q:化學資料庫服務使用說明
A: 
* 使用說明： 
    1. 在桌上電腦安裝遠端連線軟體 MobaXterm （免費）
       http://mobaxterm.mobatek.net/download-home-edition.html
       並觀看軟體使用示範片： http://mobaxterm.mobatek.net/demo.html
    2. 在 MobaXterm 內開啟 SSH Session，指定連線電腦(Remote host)為140.110.17.65
       MobaXterm 設定注意事項:
       在 MobaXterm 頂端選項列的 Setting 可設定 MobaXterm 的各項功能的環境。選 X11，顯示 X 視窗的選項設定。其中 OpenGL acceleration 設定為 Software，若使用的 PC/Windows 上有獨立顯示卡，可選 Hardware。
    3. 使用已設定完成的iService會員的主機帳號及密碼，登入140.110.17.65 (與登入大型計算主機方式相同)，登入後輸入 source  /pkg/chem/setccdc。
    4. 開始使用各類資料庫:
    啟動 Web版本CSD 劍橋晶體結構資料庫網頁搜尋介面，輸入
      `webcsd`
    啟動 ICSD 無機晶體結構資料庫網頁搜尋介面，輸入
       `icsd`
    5. 如須啟動ConQuest晶體結構資料庫進階搜尋介面，第一次登入後依據下列步驟完成license key資訊設定。
        5.1 輸入 `cd  /pkg/chem/CSD_2022/bin`
        5.2 輸入 `./ccdc_activator_gui`
        5.3 出現CCDC Software Activation視窗後，將 DD63A9-2FDCCB-41CF80-64645F-1A9CFD-611599 填入"Please enter your license key"欄位內，然後按下"Activate"，然後"OK"關閉視窗。
        5.4 輸入`cq`

    6. 搜尋結果檔案會存放在 140.110.17.65 自己帳號home目錄下的Downloads資料夾內，可透過MobaXterm的SFPT session傳回自有桌上電腦。
    7. 為維護伺服器主機系統服務品質，請用戶自行定期刪除所下載之*.cif 晶體結構檔案，避免造成系統儲存容量不足的情況。


### Q: 化學資料庫申請續用說明 
A: 
申請流程說明：
1. 登入服務網後，請選擇 【會員中心】-->【會員資訊】-->【服務啟用】
![image](https://hackmd.io/_uploads/SJFnljF-ex.png)
2.到該頁面後，請將服務類別切換為【平台服務】
![image](https://hackmd.io/_uploads/SkDTxjKbgx.png)
3.找到服務名稱：化學資料庫，點擊右側圖示 。
![image](https://hackmd.io/_uploads/BktAxjtbgg.png)
4.直接點選【申請續用】系統將提示申請續用後預計服務起訖日期，按確認後即送出申請單。
![image](https://hackmd.io/_uploads/SyIybiFWeg.png)
5.本中心收到申請單後，將進行審核。
審核結果將以信件通知，審核通過後，請以主機帳號及密碼登入主機使用服務。


### Q:查詢軟體Liscense發放的使用情況
A: 
透過服務網查詢各種軟體Liscense 發放使用情況

步驟如下:
1.登入服務網，選擇【會員中心】-->【計算主機負載資訊】-->【軟體License 發放使用情況】
![image](https://hackmd.io/_uploads/Sy8Xbst-gg.png)

2. 選擇要查詢的軟體，即可看到該軟體目前的使用情況
![image](https://hackmd.io/_uploads/B1kEbjF-xl.png)

