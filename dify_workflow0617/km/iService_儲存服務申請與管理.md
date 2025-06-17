---
title: iService_儲存服務申請與管理

---


# iService_儲存服務申請與管理

### Q: 台灣杉三號計畫目錄 (/project) 空間購買說明 
A:
功能位置：登入iService > 會員中心 > 申購管理 > 申購T3 Project儲存空間 > 開始進行申購
1. 此計畫目錄空間可提供計劃成員進行資料共享，預設權限為全體計畫成員皆可進行存取，後續可透過計畫成員管理或ACL指令進行變更資料的存取權限。
2. 本服務僅限計畫建立者與計畫管理者方能進行購買。
3. 購買期間以一年為單位( 365 天) ，每100GB之一年單價為國科會計畫 $250、學術計畫 $1,260、政府與法人計畫 $2,520及企業與個人計畫 $5,040 。
4. 若因計畫到期而不足一年，則依天數比例收費 。應付金額 = (服務停止日期 - 預計使用日期 + 1) / 365 x 購買容量 x 單價
5. 此服務之費用將由錢包進行扣款，請務必留意錢包可用餘額是否足夠 。


### Q: 高速檔案系統HFS(TWCC/T3共用)操作說明 
A:
* 功能位置：登入>會員中心 > 申購管理 > 設定高速檔案系統(TWCC/T3 HFS) > 開始進行設定
* 點選右上角的九宮格系統會依據個人所開啟的服務與權限顯示對應的功能選項。
例如：甲有參與開啟TWCC服務的計畫，並且擁有管理權限，則功能選項將會出現A與D；若參與的計畫有開啟TWCC與F1服務，並且擁有管理權限，則右上方的功能選項將會出現A到D。

* [HowTo:變更個人訂閱計畫](https://man.twcc.ai/@twccdocs/doc-hfs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-hfs-change-personal-subscription-zh)：
    1. 關於空間調整：綁定計費的計畫管理員可對用戶變更可使用的空間上限值，一般計畫成員若須調高可用空間上限，請與計畫建立者或管理者聯繫，不論是升高或降低，變更將立即生效。
    2. 扣款計畫變更:計畫成員在同時參與多個計畫且有兩個以上計畫被允許綁定為扣款計畫的情況下，可隨時變更扣款計畫。系統結算時以該日最後一次變更的計畫為扣款計畫。

* [HowTo:管理成員與訂閱歷程](https://man.twcc.ai/@twccdocs/doc-hfs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-hfs-manage-member-subscription-zh)

* [HowTo:變更成員的訂閱權限與可用空間](https://man.twcc.ai/@twccdocs/doc-hfs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fhowto-hfs-change-member-subscription-zh)
扣款計畫管理權限：計畫建立者或管理員可設定是否允許計畫成員綁定計畫為空間用量的扣款計畫或設定成員可使用空間上限，並進行每日扣款作業。

* [訂閱與收費政策](https://man.twcc.ai/@twccdocs/doc-hfs-main-zh/https%3A%2F%2Fman.twcc.ai%2F%40twccdocs%2Fguide-hfs-subscription-and-billing-policies-zh)
空間收費：每日計費，每天根據前一日的用量平均值進行扣款，以更實際地反應用戶的使用情況。
![image](https://hackmd.io/_uploads/S1bGW3K-ge.png)


### Q: 高速檔案系統HFS(F1-x86、ARM)與Project設定說明 
A:
* [F1-HFS-x86/ARM變更個人計畫設定(綁定/異動/可用空間)](https://man.twcc.ai/@f1-manual/iService#F1-HFS-x86ARM%E8%AE%8A%E6%9B%B4%E5%80%8B%E4%BA%BA%E8%A8%88%E7%95%AB%E8%A8%AD%E5%AE%9A%E7%B6%81%E5%AE%9A%E7%95%B0%E5%8B%95%E5%8F%AF%E7%94%A8%E7%A9%BA%E9%96%93)：

1. 關於空間調整：綁定計費的計畫管理員可對用戶變更可使用的空間上限值，一般計畫成員若須調高可用空間上限，請與計畫建立者或管理者聯繫，不論是升高或降低，變更將立即生效。

2. 扣款計畫變更: 計畫成員在同時參與多個計畫且有兩個以上計畫被允許綁定為扣款計畫的情況下，可隨時變更扣款計畫。 系統結算時以該日最後一次變更的計畫為扣款計畫。


* [F1-HFS-x86/ARM 調整成員的綁定權限與可用空間](https://man.twcc.ai/@f1-manual/iService#F1-HFS-x86ARM-%E8%AA%BF%E6%95%B4%E6%88%90%E5%93%A1%E7%9A%84%E7%B6%81%E5%AE%9A%E6%AC%8A%E9%99%90%E8%88%87%E5%8F%AF%E7%94%A8%E7%A9%BA%E9%96%93)：
扣款計畫管理權限：計畫管理員可設定是否允許計畫成員綁定計畫為空間用量的扣款計畫，以進行每日扣款作業。


* [F1-x86-Project共用空間管理(設定和檢視)](https://man.twcc.ai/@f1-manual/iService#F1-x86-Project%E5%85%B1%E7%94%A8%E7%A9%BA%E9%96%93%E7%AE%A1%E7%90%86%E8%A8%AD%E5%AE%9A%E5%92%8C%E6%AA%A2%E8%A6%96)：
共用空間為專案下所有成員共同使用的空間，若您的身分為計畫建立者/管理者，您可以管理各專案下的共用空間。


*　[訂閱與收費政策](https://man.twcc.ai/@f1-manual/BJCsa5RSA#%E7%A9%BA%E9%96%93%E9%A1%8D%E5%BA%A6)：
空間收費：每日計費，每天根據前一日的用量平均值進行扣款，以更實際地反應用戶的使用情況。
HFS儲存空間：(*Home、Work與Project 費率相同) (單位：元)

| 計畫類型  | 每日1 GB | 
| -------- | -------- | 
| 國科會計畫    | 0.0069 | 
| 學術計畫      | 0.035  | 
| 政府與法人計畫 | 0.07  | 
| 企業與個人計畫 | 0.14  |

