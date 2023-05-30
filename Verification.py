
# Verification

# Import libraries
import pandas as pd
import numpy as np

# Import dataset
xls = pd.ExcelFile('Watch-history.xlsx')
lib_books = pd.read_excel(xls, 'Library-books')
lib_videos= pd.read_excel(xls, 'Library-videos')
my_lib_books = pd.read_excel(xls, 'My Library-books')
my_lib_videos = pd.read_excel(xls, 'My Library-videos')
web_platforms = pd.read_excel(xls, 'Web-Platforms')
my_web_platforms = pd.read_excel(xls, 'My Web-Platforms')



# Verification for Lib_books vs lib_videos

# merge lib_books with lib_videos
# first merge DataFrames based on 
# DataFrame where library books StartTime == Library Videos StarTime
lib_books_videos = pd.merge(lib_books, lib_videos, on=['AccessionNo'])

# verification function 
"""
veryfies if the start time of one DataFrame falls between the start time and end time of another DataFrame
"""

# verification function 
# veryfies if the start time of one DataFrame falls between the start time and end time of another DataFrame
def verify(merged_table, starttime2, starttime1,  endtime1, endtime2): #starttime 1== df1 starttime 2 df 2
    
    result = merged_table[starttime1].where((merged_table[starttime2] >= merged_table[starttime1]) & (merged_table[starttime2] <= merged_table[endtime1]) & (merged_table[endtime1] <= merged_table[endtime2])).notna()
    return result[result == True]


# compare lib_video starttime('StartTime_y') to lib_books starttime and endtime.
overlap_1  = verify(lib_books_videos, 'StartTime_y','StartTime_x', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(lib_books_videos.iloc[overlap_1]).to_excel("Library-videos_vs_Library-books.xlsx", index=False)


# compare lib_books starttime('StartTime_x'), to lib_videos starttime and endtime
overlap_2 = verify(lib_books_videos, 'StartTime_x','StartTime_y', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(lib_books_videos.iloc[overlap_2]).to_excel("Library-books_vs_Library-videos.xlsx", index=False)


# Verification for Lib_books vs My lib books


# merge lib_books with My_lib_books
# first merge DataFrames based on 
lib_books.rename(columns={'EndTime':'Endtime'},inplace=True) # had to rename the End times for one of the tables 
lib_books_mybooks = pd.merge(lib_books, my_lib_books, on=['AccessionNo'])

# compare my_lib_books starttime('StartTime_y') to lib_books starttime and endtime.
overlap_3 = verify(lib_books_mybooks , 'StartTime_y','StartTime_x', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(lib_books_mybooks.iloc[overlap_3]).to_excel("My_Library-books_vs_Library-books.xlsx", index=False)

# compare lib_books starttime('StartTime_x'), to my_lib_books starttime and endtime
overlap_4 = verify(lib_books_mybooks, 'StartTime_x','StartTime_y', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(lib_books_mybooks.iloc[overlap_4]).to_excel("Library-books_vs_My_Library-books.xlsx", index=False)


# Verification for lib_books vs my_lib_videos

# merge lib_books with my_lib_videos
# first merge DataFrames based on 
lib_books_myvideos = pd.merge(lib_books, my_lib_videos, on=['AccessionNo'])
lib_books_myvideos.head()

# compare my_lib_videos starttime('StartTime_y') to lib_books starttime and endtime.
overlap_5 =verify(lib_books_myvideos , 'StartTime_y','StartTime_x', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(lib_books_myvideos.iloc[overlap_5]).to_excel("Library-videos_vs_Library-books.xlsx", index=False)

# compare lib_books starttime('StartTime_x'), to my_lib_videos starttime and endtime
overlap_6 = verify(lib_books_myvideos, 'StartTime_x','StartTime_y', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(lib_books_myvideos.iloc[overlap_6]).to_excel("Library-books_vs_Library-videos.xlsx", index=False)

# Verification for lib_books vs web_platforms

# merge lib_books with web_platforms
# first merge DataFrames based on 
lib_books.rename(columns={'Endtime':'EndTime'},inplace=True) # had to rename the End times for one of the tables 
lib_books_web = pd.merge(lib_books, web_platforms, on=['AccessionNo'])

# compare web_platform starttime('StartTime_y') to lib_books starttime and endtime.
overlap_7 = verify(lib_books_web , 'StartTime_y','StartTime_x', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(lib_books_web.iloc[overlap_7]).to_excel("web_platforms_vs_lib_books.xlsx", index=False)

# compare lib_books starttime('StartTime_x'), to web_platform starttime and endtime
overlap_8 = verify(lib_books_web, 'StartTime_x','StartTime_y', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(lib_books_web.iloc[overlap_8]).to_excel("lib_books_vs_web_platforms.xlsx", index=False)

# Verification for lib_books vs my_web_platforms

# merge lib_books with my_web_platform
# first merge DataFrames based on  
lib_books.rename(columns={'Endtime':'EndTime'},inplace=True) # had to rename the End times for one of the tables 
lib_books_myweb= pd.merge(lib_books, my_web_platforms, on=['AccessionNo'])

# compare my_web_platform starttime('StartTime_y') to lib_books starttime and endtime.
overlap_9 = verify(lib_books_myweb , 'StartTime_y','StartTime_x', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(lib_books_myweb.iloc[overlap_9]).to_excel("my_web_platforms_vs_lib_books.xlsx", index=False)


# compare lib_books starttime('StartTime_x'), to my_web_platform starttime and endtime
overlap_10 = verify(lib_books_myweb, 'StartTime_x','StartTime_y', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(lib_books_myweb.iloc[overlap_10]).to_excel("lib_books_vs_My_web_platforms.xlsx", index=False)


# Verification for lib_videos vs my_lib_books

# merge lib_videos with my_lib_books
# first merge DataFrames based on  
lib_vid_mybooks= pd.merge(lib_videos, my_lib_books, on=['AccessionNo'])

# compare lib_videos starttime('StartTime_y') to my_lib_books starttime and endtime.
overlap_11 = verify(lib_vid_mybooks , 'StartTime_y','StartTime_x', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(lib_vid_mybooks.iloc[overlap_11]).to_excel("lib_videos_vs_my_lib_books.xlsx", index=False)


# compare my_lib_books starttime('StartTime_x'), to lib_videos starttime and endtime
overlap_12 = verify(lib_vid_mybooks, 'StartTime_x','StartTime_y', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(lib_vid_mybooks.iloc[overlap_12]).to_excel("my_lib_books_vs_lib_videos.xlsx", index=False)



# Verification for lib_videos vs my_lib_videos

# merge lib_videos with my_lib_videos
# first merge DataFrames based on  
lib_vid_myvid= pd.merge(lib_videos, my_lib_videos, on=['AccessionNo'])


# compare lib_videos starttime('StartTime_y') to my_lib_videos starttime and endtime.
overlap_13 = verify(lib_vid_myvid , 'StartTime_y','StartTime_x', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(lib_vid_myvid.iloc[overlap_13]).to_excel("lib_videos_vs_my_lib_videos.xlsx", index=False)


# compare lib_videos starttime('StartTime_x'), to my_lib_videos starttime and endtime
overlap_14 = verify(lib_vid_myvid, 'StartTime_x','StartTime_y', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(lib_vid_myvid.iloc[overlap_14]).to_excel("lib_videos_vs_my_lib_videos.xlsx", index=False)



# Verification for lib_videos vs web_platforms

# merge lib_videos with web_platform
# first merge DataFrames based on  
lib_vid_web= pd.merge(lib_videos, web_platforms, on=['AccessionNo'])

# compare web_platform starttime('StartTime_y') to lib_videos starttime and endtime.
overlap_15 = verify(lib_vid_web , 'StartTime_y','StartTime_x', 'Endtime_x', 'Endtime_y').index.to_list()
pd.DataFrame(lib_vid_web.iloc[overlap_15]).to_excel("web_platforms_vs_lib_videos.xlsx", index=False)



# compare lib_videos starttime('StartTime_x'), to web_platform starttime and endtime
overlap_16 = verify(lib_vid_web, 'StartTime_x','StartTime_y', 'Endtime_y', 'Endtime_x').index.to_list()
pd.DataFrame(lib_vid_web.iloc[overlap_16]).to_excel("lib_videos_vs_web_platforms.xlsx", index=False)



#Verification for lib_videos vs my_web_platforms

# merge lib_videos with my_web_platform
# first merge DataFrames based on
lib_vid_myweb= pd.merge(lib_videos, my_web_platforms, on=['AccessionNo'])

# compare my_web_platform starttime('StartTime_y') to lib_videos starttime and endtime.
overlap_17 = verify(lib_vid_myweb , 'StartTime_y','StartTime_x', 'Endtime_x', 'Endtime_y').index.to_list()
pd.DataFrame(lib_vid_myweb.iloc[overlap_17]).to_excel("my_web_platforms_vs_lib_videos.xlsx", index=False)


# compare lib_videos starttime('StartTime_x'), to my_web_platform starttime and endtime
overlap_18 = verify(lib_vid_myweb, 'StartTime_x','StartTime_y', 'Endtime_y', 'Endtime_x').index.to_list()
pd.DataFrame(lib_vid_myweb.iloc[overlap_18]).to_excel("lib_videos_vs_my_web_platforms.xlsx", index=False)



# Verification for my_lib_books vs my_lib_videos

# merge my_lib_books with my_lib_videos
# first merge DataFrames based on  

lib_mybook_vid= pd.merge(my_lib_books, my_lib_videos, on=['AccessionNo'])

# compare my_lib_videos starttime('StartTime_y') to my_lib_books starttime and endtime.
overlap_19 = verify(lib_mybook_vid , 'StartTime_y','StartTime_x', 'EndTime_x', 'EndTime_y').index.to_list()
pd.DataFrame(lib_mybook_vid .iloc[overlap_19]).to_excel("my_lib_videos_vs_my_lib_books.xlsx", index=False)


# compare my_lib_books starttime('StartTime_x'), to my_lib_videos starttime and endtime
overlap_20 = verify(lib_mybook_vid, 'StartTime_x','StartTime_y', 'EndTime_y', 'EndTime_x').index.to_list()
pd.DataFrame(lib_mybook_vid.iloc[overlap_20]).to_excel("my_lib_books_vs_my_lib_videos.xlsx", index=False)



# Verification for my_lib_books vs web_platform

# merge my_lib_books with web_platform
# first merge DataFrames based on  
mybook_web= pd.merge(my_lib_books, web_platforms, on=['AccessionNo'])

# compare web_platform starttime('StartTime_y') to my_lib_books starttime and endtime.
overlap_21 = verify(mybook_web , 'StartTime_y','StartTime_x', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(mybook_web.iloc[overlap_21]).to_excel("web_platforms_vs_my_lib_books.xlsx", index=False)


# compare my_lib_books starttime('StartTime_x'), to web_platform starttime and endtime
overlap_22 = verify(mybook_web, 'StartTime_x','StartTime_y', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(mybook_web.iloc[overlap_22]).to_excel("my_lib_books_vs_web_platforms.xlsx", index=False)

# Verification for my_lib_books vs my_web_platform
# merge my_lib_books with my_web_platform
mybook_myweb= pd.merge(my_lib_books, my_web_platforms, on=['AccessionNo'])
# compare my_web_platorms starttime('StartTime_y'), to my_books_videos starttime and endtime
overlap_23 = verify(mybook_myweb, 'StartTime_x','StartTime_y', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(mybook_myweb.iloc[overlap_23]).to_excel("my_web_platform_vs_My_lib_books.xlsx", index=False)

# compare my_books_videos starttime('StartTime_x'), to my_web_platorms starttime and endtime
overlap_24 = verify(mybook_myweb, 'StartTime_x','StartTime_y', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(mybook_myweb.iloc[overlap_24]).to_excel("My_lib_books_vs_my_web_platform_.xlsx", index=False)


# Verification for my_lib_videos vs my_web_platforms

# merge my_lib_videos with my_web_platform
# first merge DataFrames based on  
myvid_myweb= pd.merge(my_lib_videos, my_web_platforms, on=['AccessionNo'])

# compare my_web_platform starttime('StartTime_y') to my_lib_books starttime and endtime.
overlap_25 = verify(myvid_myweb , 'StartTime_y','StartTime_x', 'EndTime', 'Endtime').index.to_list()
pd.DataFrame(myvid_myweb.iloc[overlap_25]).to_excel("lib_books_vs_web_platforms.xlsx", index=False)


# compare my_lib_books starttime('StartTime_x'), to my_web_platform starttime and endtime
overlap_26 = verify(myvid_myweb, 'StartTime_x','StartTime_y', 'Endtime', 'EndTime').index.to_list()
pd.DataFrame(myvid_myweb.iloc[overlap_26]).to_excel("my_lib_books_vs_my_web_platform.xlsx", index=False)



# Verification for web_platforms vs my_web_platforms

# merge web_platforms with my_web_platform
# first merge DataFrames based on  
myweb= pd.merge(web_platforms, my_web_platforms, on=['AccessionNo'])

# compare my_web_platforms starttime('StartTime_y') to web_platforms starttime and endtime.
overlap_27 = verify(myweb , 'StartTime_y','StartTime_x', 'Endtime_x', 'Endtime_y').index.to_list()
pd.DataFrame(myweb.iloc[overlap_27]).to_excel("my_web_platforms_vs_web_platforms.xlsx", index=False)


# compare web_platforms starttime('StartTime_x'), to my_web_platform starttime and endtime
overlap_28 = verify(myweb, 'StartTime_x','StartTime_y', 'Endtime_y', 'Endtime_x').index.to_list()
pd.DataFrame(myweb.iloc[overlap_28]).to_excel("web_platforms_vs_my_web_platforms.xlsx", index=False)
