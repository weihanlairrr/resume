#%%
import streamlit as st
from PIL import Image

#%% style設定
with st.chat_message("user"):
    st.write("您好，我是Albert！歡迎來到我透過 Streamlit 製作的個人頁面")

st.markdown("""
   <style>
   div[data-testid="metric-container"] {
   background-color: rgba(20, 40, 62, 0.9);
   border: 1px solid rgba(20, 40, 62, 0.9);   
   padding: 5% 5% 3% 10%;
   border-radius: 5px;
   color: #ffc781; 
   overflow-wrap: break-word;
   }

   /* breakline for metric text*/
   div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > 
   div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color:#FCFCFC;
   }
   
   /* metric font size*/
   div[data-testid="stMetricValue"] {font-size: 26px; }
   
   div:nth-child(7) > [class^="css-"] > div:nth-child(1) > div > div > div > button {
       background-color: rgba(20, 40, 62, 0.9);
       color:#fcfcfc;
       border-radius: 0.8rem 
       }
   
   /* button*/
   div[id^="bui-"] > button:nth-child(1) {
   background-color: #33DD00;
   color: #EEFFFF
   
   </style>
   """
   , unsafe_allow_html=True)
       
#%% 語言選擇
def main(): 
    language=st.sidebar.selectbox("請選擇語言 Preferred Language",["中文","English(開發中）"])
#%% 中文
    if language=="中文":
        
    #%% 大頭貼與姓名、學歷、履歷 
        col1, col2 = st.columns(2,gap="large")
        with col1:
            大頭照 = Image.open('IMG_3014.PNG')
            st.image(大頭照)
            
            st.write("\n")
            social_icons_data = {
                # Platform: [URL, Icon]
                "LinkedIn": ["https://www.linkedin.com/in/%E9%9F%8B%E7%BF%B0-%E8%B3%B4-015557246", "https://i.imgur.com/Zyi7lgS.png"],
                "Line": ["https://line.me/ti/p/s2Qmw5Ynwo", "https://i.imgur.com/vKFbWy5.png"],
                }
        
            social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 5px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]
        
            st.write(f"""
            <div style="display: flex; justify-content: center; margin-bottom: 50px;">
                {''.join(social_icons_html)}
            </div>""", 
            unsafe_allow_html=True)
        
            
        with col2:    
            st.title("賴韋翰  Albert")
            st.markdown("臺灣大學 - 政治學系公共行政組") 
            st.markdown("臺灣科技大學  - 智慧財產學士學位學程（輔）") 
            
            st.write("📫   ", " albert102206@gmail.com")
            st.write("\n")
            st.write("\n")
            
            
            col3,col4,col5 = st.columns(3,gap="medium")
            with col3:
                with open("中文履歷.pdf", "rb") as fileChinese: 
                    st.download_button( 
                        label="中文CV", 
                        data=fileChinese, 
                        file_name="賴韋翰中文履歷.pdf", 
                        mime="application/octet-stream" )
            with col4:
                with open("104履歷.pdf", "rb") as file104: 
                    st.download_button( 
                        label="104 CV", 
                        data=file104, 
                        file_name="賴韋翰104履歷.pdf", 
                        mime="application/octet-stream" )  
            with col5:
                with open("英文履歷.pdf", "rb") as fileEng: 
                    st.download_button( 
                        label="Eng. CV", 
                        data=fileEng, 
                        file_name="賴韋翰英文履歷.pdf", 
                        mime="application/octet-stream" )
         
            
    #%% 實習經驗
        st.subheader("工作經歷")
        st.write("---")
        
        UberEats= st.checkbox("**Uber Eats**")
        if UberEats:
            st.markdown("#### Account Management | 實習生",help="協助外送店家通過政府新規定之洗錢防制驗證，以保留他們繼續使用平台的資格")
            st.markdown("2022 6~8月")
            st.write("\n")
            col6,col7,col8 = st.columns(3,gap="medium")
            col6.metric(label="客戶成功數",value='400間↑',help="是指成功協助完成 Uber Eats 洗錢防制驗證的店家數。")
            col7.metric(label="轉換為營業額",value='3000萬↑',help="若外送店家未通過洗錢防制驗證，將失去使用外送平台的資格")
            col8.metric(label="獲選為",value='Team Lead',help="根據客戶數據制定每週團隊策略，並為成效負責")
            
            col9,col10 = st.columns(2,gap="medium")
            col9.metric(label="自主開發績效統計工具 節省每日工作時間" ,value="約30分鐘",help="透過 Google Sheet")
    
            st.write("\n")
            st.write("\n")
            
        瑞信=st.checkbox("**瑞信兒童醫療基金會**")
        if 瑞信:
            st.markdown("#### 第10屆瑞信兒童醫療貢獻獎 | 訪查員",help="分派至候選人所在醫院進行訪查，蒐集評選所需之臨床性資訊，並整理出值得獲獎的理由")
            st.markdown("2022 9~12月")
            st.write("\n")
            
            col12,col13,colllll = st.columns(3,gap="medium")
            col12.metric(label="負責之候選人成功獲頒",value='兒童護理奬',help="可參考 https://reurl.cc/2LXyR4")
            
            st.write("\n")
            st.write("\n")
         
        iPower=st.checkbox("**iPOWER培力學社**")
        if iPower:
            st.markdown("#### 淺水灣公益咖啡節：算我益咖 | 活動實習生",help="協助NPO規劃活動以募得推動偏鄉教育所需之經費")
            st.markdown("2022 9~12月")
            st.write("\n")
    
            col14,col15,col16 = st.columns(3,gap="medium") 
            col14.metric(label="當日募款額達",value='50000元↑',help="在因惡劣天氣影響活動的情況下，當日仍達此募款金額")        
            col15.metric(label="協助當地店家規劃活動",value='7間咖啡廳',help="規劃活動空間、路線、撰寫相關文案")
            col16.metric(label="使粉專2週內曝光率",value="＋2422％",help="透過KOL行銷，且過程未耗費任何金錢成本")
                   
            st.write("\n")
            st.write("\n")
             
        st.write("\n")
         
    
    #%% 在學經歷
        st.subheader("社團經歷")
        st.write("---")
        
        ntueater= st.checkbox("**美食報導策略媒體研究社（吃貨台大）**",help="Instagram連結：https://reurl.cc/3xGp00")  
        col17,col18,col19 = st.columns(3,gap="medium")
        with col17:   
            if ntueater:
                st.markdown("#### 社長")
                st.markdown("2022 Jun - 2023 Feb")   
        with col18:
            if ntueater:
                ntueater_logo=Image.open("吃貨台大logo.png")
                ntueater_logo=ntueater_logo.resize((65,65))
                st.image(ntueater_logo)
    
        if ntueater:
            col21,col22,col23 = st.columns(3,gap="medium") 
            col21.metric(label="管理中型商業性質社團",value="20人")
            col22.metric(label="合作店家數",value="20間",help="範圍包括社群行銷、實體銷售、贊助合作")
            col23.metric(label="接洽社課講師數",value="7人")
            N1,N2 = st.columns(2,gap="medium") 
            N1.metric(label="管理大型 Facebook＆Instagram 粉絲專頁",value="avg. 3.15萬追蹤")
            st.write("\n")
            
            choice1 = st.radio("主辦之活動", ["吃貨台大美食市集：吃貨不單行", "第一屆吃貨台大美食攝影大賽"])
            if choice1=="吃貨台大美食市集：吃貨不單行":
                col24,col25,col26 = st.columns(3,gap="medium") 
                col24.metric(label="爭取贊助品價值達",value="20000元",help="共10間贊助餐廳")
                col25.metric(label="協助店家在校銷售產品",value="5間",help="每日1小時內售罄、5天總計近500份")
                col26.metric(label="淨收益換算為社員社費",value="18位")
            if choice1=="第一屆吃貨台大美食攝影大賽":
                col27,col28,col29 = st.columns(3,gap="medium") 
                col27.metric(label="期間達粉專粉絲成長目標",value="3% / 750人",help="透過吸引眾多美食KOL參與增加粉專曝光與討論度，為期1個月")
                col28.metric(label="平均獲客成本(CAC) 僅",value="2.5元")
        st.write("\n")
        st.write("\n")
  
    #%% 其他
        col30, col31 = st.columns(2,gap="large")
        with col30:
            st.subheader("語言能力") 
            st.write("---")
                  
            col32,col33,col34=st.columns(3,gap="small")
            英文= col32.checkbox("**英文**")
            if 英文:      
                col33.markdown("<h5 style='text-align: center; margin-top: 2.3px;'> 精通 </h5>", unsafe_allow_html=True) 
                col34.markdown("<h5 style='text-align: left; margin-top: 2.3px; color: #ffc781'> TOEIC 925 </h5>", unsafe_allow_html=True,help="成績送達時間：2023/05")
                  
            col35,col36,col37=st.columns(3,gap="small")
            日文= col35.checkbox("**日文**")
            if 日文:       
                col36.markdown("<h5 style='text-align: center; margin-top: 2.3px;'> 中級 </h5>", unsafe_allow_html=True)          
            
        with col31:
            st.subheader("工作技能") 
            st.write("---")
            電腦程式設計 = st.checkbox("**電腦程式設計**")
            if 電腦程式設計:
                col38,col39 = st.columns(2,gap="small")
                col38.metric(label="程式語言",value="Python")
                col39.metric(label="應用工具",value="Streamlit")
                
            辦公文書處理 = st.checkbox("**辦公文書處理**")
            if 辦公文書處理:
                col40,col41 = st.columns(2,gap="small")
                col40.metric(label="工具",value="G-suite")
            電商官網管理 = st.checkbox("**電商官網管理**")
            if 電商官網管理:
                col42,col43 = st.columns(2,gap="small")
                col42.metric(label="工具",value="GA4")
                col43.metric(label="工具",value="Google Ads")
            活動規劃 = st.checkbox("**活動規劃**")
            if 活動規劃:
                col44,col45 = st.columns(2,gap="small")
                col44.metric(label="實務經驗",value="3場")
        
        st.write("\n")
        st.write("\n")
        st.subheader("證照") 
        st.write("---")
        
        
        hahow = st.checkbox("**Hahow 好學校**")
        if hahow:
            choice2 = st.radio("能力類別", ["Excel", "GA4","程式語言"])
            if choice2=="Excel":
                st.markdown("<h5 style='text-align: left; color: #ffc781'> Excel 達人：學會所有商務應用的需求！ </h5>", unsafe_allow_html=True)
            if choice2=="GA4":
                st.markdown("<h5 style='text-align: left; color: #ffc781'> GA4 新手完全攻略！用數據分析下商業決策 </h5>", unsafe_allow_html=True)
            if choice2=="程式語言":
                st.markdown("<h5 style='text-align: left; color: #ffc781'> Python 入門特訓 - 基礎實作到證照攻略 </h5>", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: left; color: #ffc781'> Python 爬蟲入門特訓 ─ 資料抓取與處理應用 </h5>", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: left; color: #ffc781'> Streamlit x ChatGPT 快速打造資料分析網頁 </h5>", unsafe_allow_html=True)
            st.write("\n")
            st.write("\n")
            
        google = st.checkbox("**Google**")
        if google:
            choice3 = st.radio("2023 數位人才探索計劃", ["Google Analytics 學程", "Google Ads 學程"])
            if choice3=="Google Analytics 學程":
                st.markdown("<h5 style='text-align: left; color: #ffc781'> Google Analytics 個人認證 </h5>", unsafe_allow_html=True)
            if choice3=="Google Ads 學程":
                col46,col47,col48 = st.columns(3,gap="small")
                col46.markdown("<h5 style='text-align: left; color: #ffc781'> 搜尋廣告認證 </h5>", unsafe_allow_html=True)
                col47.markdown("<h5 style='text-align: left; color: #ffc781'> 多媒體廣告認證</h5>", unsafe_allow_html=True)
                col48.markdown("<h5 style='text-align: left; color: #ffc781'> 應用程式廣告認證 </h5>", unsafe_allow_html=True)
                col49,col50,col51 = st.columns(3,gap="small")
                col49.markdown("<h5 style='text-align: left; color: #ffc781'> 評估認證 </h5>", unsafe_allow_html=True)
                col50.markdown("<h5 style='text-align: left; color: #ffc781'> 影音廣告認證 </h5>", unsafe_allow_html=True)
                col51.markdown("<h5 style='text-align: left; color: #ffc781'> 廣告素材認證 </h5>", unsafe_allow_html=True)
            st.write("\n")
            st.write("\n")
            
        TOEIC = st.checkbox("**TOEIC**")
        if TOEIC:
            st.markdown("<h5 style='text-align: left; color: #ffc781'> 925分（聽力495；閱讀430） </h5>", unsafe_allow_html=True)
                        
#%% 

if __name__ == '__main__':
    main()  


         
        
        
        

    
        




    
        

    
            
        








































