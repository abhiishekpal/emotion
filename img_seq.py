import glob as gb
import os
from shutil import copy
emotions_list = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] 
emotions_folders = gb.glob(r"emotions\*") #Returns a list of all folders with participant numbers
def imageWithEmotionEtraction():
    print('dasd')
    print(emotions_folders)
    for x in emotions_folders:
        participant = "%s" %x[-4:] #store current participant number
        for sessions in gb.glob("%s\\*" %x): 
            for files in gb.glob("%s\\*" %sessions):
                current_session = files[20:-30]
                file = open(files, 'r')
                
                emotion = int(float(file.readline())) 
                #get path for last image in sequence, which contains the emotion
                sourcefile_emotion = gb.glob("images\\%s\\%s\\*" %(participant, current_session))[-1] 
                #do same for neutral image
                sourcefile_neutral = gb.glob("images\\%s\\%s\\*" %(participant, current_session))[0] 
                #Generate path to put neutral image
                print(sourcefile_emotion, sourcefile_neutral)
                dest_neut = "selected_set\\neutral\\%s" %sourcefile_neutral[25:] 
                #Do same for emotion containing image
                dest_emot = "selected_set\\%s\\%s" %(emotions_list[emotion], sourcefile_emotion[25:]) 
                
#                 copyfile(sourcefile_neutral, dest_neut) #Copy file
#                 copyfile(sourcefile_emotion, dest_emot) #Copy file

folder_emo = 'emotions'
folder_img = 'images'

def extractImages():
    
    for fol1 in os.listdir(folder_emo):
        for fol2 in os.listdir(folder_emo+'/'+fol1):
            ct = 0
            lis = []
            file_label = ""
            for  file_label in os.listdir(folder_emo+'/'+fol1+'/'+fol2):
                ct+=1
            if(ct==0):
                continue
            
            file = open(folder_emo+'/'+fol1+'/'+fol2+'/'+file_label,'r')
            emotion = int(float(file.readline())) 
            
            
            for file_image in os.listdir(folder_img+'/'+fol1+'/'+fol2):
                lis.append(file_image)
            print(lis)
            lis = sorted(lis)
            source_neutral = folder_img + '/'+fol1+'/'+fol2+'/'+lis[0]
            source_emotion = folder_img + '/'+fol1+'/'+fol2+'/'+lis[-1]
            
            dest_neutral = 'selected_set/neutral'
            dest_emotion = 'selected_set/'+emotions_list[emotion]
            
            copy(source_neutral, dest_neutral) #Copy file
            copy(source_emotion, dest_emotion) #Copy file
            
            
if __name__ == '__main__':
    
#     imageWithEmotionEtraction()        
    extractImages()