# twstock-information-query-system

### 作品介紹
大三學期末時，想將所學應用於開發上，因此獨力開發股票查詢平台，利用twstock API擷取台灣股市資訊，並且方便資料的呈現，選用Django Web框架建立可查詢與互動的web app，並且為了方便使用者使用，開發過程時以RWD響應式網頁設計且配合Bootstrap進行網站美工(UI/UX)，使得本系統亦可於手機端上呈現。本系統也部屬至ngrok上，讓任何人得以使用行動裝置或電腦均可以連線至本系統上操作。未來預計利用長短期記憶模型(LSTM)預測未來股票走向，以近一步強化本系統功能。此股票查詢平台可分為兩大主要功能。

### 功能
| 簡易查詢股市資訊，透過輸入股票代號或名稱進行搜尋 | 顯示股票歷史資訊走勢圖 | 
|-------|-----|
|查詢時間、股票代號、股票名稱、股票全名最佳買入價、最佳買入數量|連結sqlite3資料庫(總成交股數、總成交金額、開盤價、盤中最高價、盤中最低價、收盤價、漲跌價差、成交筆數)|
|最佳賣出價、最佳賣出數量|輸入年分或月份，顯示該股票年或月開盤/收盤價走勢圖|
|開盤價、最高價、最低價|提供使用者下載結果圖表|


###  本作品中，我撰寫了以下主要功能：
>1.	建立Django基本框架
>2.	以RWD設計網頁模板，並考慮使用者體驗(UX)進行設計
>3.	使用Bootstrap(包括HTML、CSS及JavaScript)對頁面美工(UI)
>4.	利用Chart.js進行資料視覺化(股票K線繪製)
>5.	前端使用Ajax非同步技術進行資料的請求，達到動態網頁呈現 
>6.	後端twstock API股票資訊擷取
>7.	協助sqlite3資料庫建置
>8.	將系統部屬至Ngrok

###  成果截圖：
股票資訊查詢系統-主頁面
![1](https://user-images.githubusercontent.com/58781800/140335230-dc44fb56-1266-497d-aef4-6e5a023cfbd6.png)

sqlite3資料庫資訊
![2](https://user-images.githubusercontent.com/58781800/140336381-63ed9fe3-4d1b-495b-912c-e484f92feb2c.png)

行動裝置上呈現-1<br>
![3](https://user-images.githubusercontent.com/58781800/140336391-494f49ae-1fb4-41d5-af0e-8f42c816ea65.jpg)

行動裝置上呈現-2<br>
![4](https://user-images.githubusercontent.com/58781800/140336401-09961e02-9014-4bcf-b9fc-ec93ec9718a9.jpg)
