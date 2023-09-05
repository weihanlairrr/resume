#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:11:54 2023

@author: laiwei
"""

#%% English
    if language=="English":
        
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
            st.markdown("##### NTU  - Political Science ") 
            st.markdown("##### Taiwan Tech  - Intellectual Property Rights（Minor）") 
            
            st.write("📫   ", " albert102206@gmail.com")
            st.write("\n")
            
            col3,col4,col5 = st.columns(3,gap="medium")
            with col3:
                with open("中文履歷.pdf", "rb") as fileChinese: 
                    st.download_button( 
                        label="Chin. CV", 
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
        st.header("Working Experience")
        st.write("---")
        
        st.markdown("#### Internship ")
        UberEats= st.checkbox("**Uber Eats**")
        if UberEats:
            st.markdown("#### Account Management | Intern",help="Assisting merchants in complying with the anti-money laundering regulations to maintain their eligibility to use the platform")
            st.markdown("2022 Jun-Aug")
            st.write("\n")
            col6,col7,col8 = st.columns(3,gap="medium")
            col6.metric(label="clients succeeded",value='400↑',help="Number of restaurants which successfully passed the AML verification")
            col7.metric(label="revenue secured",value='30M NTD↑',help="A client will lose her eligibility to use Uber Eats if she fails to pass the AML verification")
            col8.metric(label="selected as",value='Team Lead',help="Developed weekly team strategies based on client data and took accountability for their results")
            
            col9,col10 = st.columns(2,gap="medium")
            col9.metric(label="Developed a performance tracking tool and helped save work time" ,value="30 mins / day",help="done with Google Sheet")
    
            st.write("\n")
            st.write("\n")
            
        瑞信=st.checkbox("**Raising Children Medical Foundation**")
        if 瑞信:
            st.markdown("#### 10th Child Medical Care Award | Interviewer",help="分派至候選人所在醫院進行訪查，蒐集評選所需之臨床性資訊，並整理出值得獲獎的理由")
            st.markdown("2022 Sep-Dec")
            st.write("\n")
            
            col12,col13,colllll = st.columns(3,gap="medium")
            col12.metric(label="負責之候選人成功獲頒",value='兒童護理奬',help="可參考 https://reurl.cc/2LXyR4")
            
            st.write("\n")
            st.write("\n")
         
        iPower=st.checkbox("**iPOWER Alliance**")
        if iPower:
            st.markdown("#### 淺水灣公益咖啡節：算我益咖 | 活動實習生",help="協助NPO規劃活動以募得推動偏鄉教育所需之經費")
            st.markdown("2022 Sep-Dec")
            st.write("\n")
    
            col14,col15,col16 = st.columns(3,gap="medium") 
            col14.metric(label="當日募款額達",value='50000元↑',help="在因惡劣天氣影響活動的情況下，當日仍達此募款金額")        
            col15.metric(label="協助當地店家規劃活動",value='7間咖啡廳',help="規劃活動空間、路線、撰寫相關文案")
            col16.metric(label="使粉專2週內曝光率",value="＋2422％",help="透過KOL行銷，且過程未耗費任何金錢成本")
                   
            st.write("\n")
            st.write("\n")
             
        st.write("\n")
         
    
    #%%在學經歷
        st.header("社團經歷")
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
            
            choice = st.radio("主辦之活動", ["吃貨台大美食市集：吃貨不單行", "第一屆吃貨台大美食攝影大賽"])
            if choice=="吃貨台大美食市集：吃貨不單行":
                col24,col25,col26 = st.columns(3,gap="medium") 
                col24.metric(label="爭取贊助品價值達",value="20000元",help="共10間贊助餐廳")
                col25.metric(label="協助店家在校銷售產品",value="5間",help="每日1小時內售罄、5天總計近500份")
                col26.metric(label="淨收益換算為社員社費",value="18位")
            if choice=="第一屆吃貨台大美食攝影大賽":
                col27,col28,col29 = st.columns(3,gap="medium") 
                col27.metric(label="期間達粉專粉絲成長目標",value="3% / 750人",help="透過吸引眾多美食KOL參與增加粉專曝光與討論度，為期1個月")
                col28.metric(label="平均獲客成本(CAC) 僅",value="2.5元")