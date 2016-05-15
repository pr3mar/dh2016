# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:18:07 2016

@author: Angelina
"""

import pickle, pandas, os, glob, time


#Recursive walk through directory:
def read_files(rootdir):
    '''Open the directories path'''
    
    for dirname in os.listdir(rootdir):
        print dirname
        for filename in os.listdir(os.path.join(rootdir, dirname)):
            if filename == "_sent_mail": #FROM -> TO 
                print "SENT"  +  str(filename)
                #read the files          
                for f in os.listdir(os.path.join(rootdir, dirname, filename)): 
                    for f_after in glob.glob(os.path.join(rootdir, dirname, filename, f)):
                        parse_file(f_after)
                  
                    
            elif filename  == "inbox": #TO -> FROM
                print "RECEIVED " +  str(filename)
                for f in os.listdir(os.path.join(rootdir, dirname, filename)): 
                    for f_after in glob.glob(os.path.join(rootdir, dirname, filename, f)):
                        parse_file(f_after)
            
            else:
                pass
                
        #Ignore undisclosed sender
            
#        Date: Tue, 5 Feb 2002 13:12:06 -0800 (PST)
#        From: david.dronet@enron.com
#        To: john.griffith@enron.co
        

        #Another message between the user1 and user2 " -----Original Message-----"

 #       arr = numpy(arr)

        #Create DataFrame and save:
  #      create_df(arr)
   

def parse_file(f):
    fd = open(f, "r").read()
    for line in fd:
    
#        date_index_start = line.find("Date: ") 
#        date_index_end = line.find(":")+5
#        date = convert_date(line[(date_index_start+1) : (date_index_end+1)])
#        
        email_from_index_start = line.find("From: ")
        email_from_index_end = line.find("enron.com")+9
        email_from = line[(email_from_index_start+1) : (email_from_index_end+1)]    
        
        #There are multiple recipients:
        email_to_index_start = line.find("To: ")
        emails_to_index_end = line.find("Subject: ")        
        emails_list = line[(email_to_index_start+1) : (emails_to_index_end-1)]
        email_to = emails_list.split(", ") #the list od recipients
       
        email_text_index_start = line.find(".PST")+4    
        email_text_index_end = fd.seek(-1, 2)      
        email_text = line[(email_text_index_start+1) : (email_text_index_end)]              
                                
         

def create_df(arr):
    '''Creates structure that contains: msg_id, date, from, to, text'''
    columns = ["From", "To", "Date", "Text"] #From and To are emails, Date is in Unix format
    filename = 'output_data_sentiment_analysis.csv'
    df = pandas.DataFrame(data = arr, columns = columns)
    df.to_csv(filename, sep='\t') 
     

def convert_date(str):    
    date_format='%d %b %Y %H:%M:%S'
    date = time.strptime(str, date_format)
    return date
    
 

#BE CAREFUL ABOUT:
# -QUOTED MESSAGES in the files
#- search inbox and _sent_mail 

main_dir = "enron_mail_20150507"
sub_dir = "maildir"

#os_dir = os.path("C:/Users/Angelina/Desktop/DragonHack2016/enron_mail_20150507/maildir")
os_dir = os.path.join(os.getcwd(), main_dir, sub_dir)
read_files(os_dir)


