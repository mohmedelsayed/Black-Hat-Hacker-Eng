print("\n\n")
import os , time
import shutil
#----------------------------------------------------------------

#الشرح
#الاسكربت دا عشان لو في مثلا كورس جوا مجلد Java Script For Pentester اخدت منه Copy وحطيته بالغلط وحطيته في مجلد Web Appplication Pentest وعاوز امسحهم بروح مشغل السكربت واعطيله المدخل الاول وهو المسار اللي هحفظ فيه اللوج والمدخل التاني وهو مسار المجلد الاصلي بتاع Web Application Pentest اللي الحاجه اتنسخت جواه بالغلط  وهو الReference اللي هقارن بيه الملفات والمدخل التالت وهو مسار الفولدر بتاع الكورس Java For Pentester اللي انا اخدت منه نسخه بالغلط جوا فولدر ال Web Application Pentest  والفولدر الرابع وهو المكان اللي هحط فيه الفايلات المنقوله بالغلط او المتكرره اللي البرنامج هينقلهالي وبعدين ابقي امسح بقي الفايلات دي او اعمل فها اللي انا عاوزو..




os.getcwd()
log_file                     = input('[*] Enter Path to Save Log in it : ')
Folder_Target1               = input('[*] Reference Path to Compare Other Files With It : ')
Folder_Target2               = input('[*] Path to The Files Will Compare with The files in the Reference : ')
Folder_Target_aftercut       = input('[*] Path to Folder to move files in it : ')
log                          = open(log_file + "/log.txt", 'w+')
files_one                    = []
files_two                    = []
files_after_filterd          = []
x = 1
log.writelines("\n\nReference In : " + Folder_Target1 + " : \n--------------------------------------------------------------------------------------\n\n\n")
for files in os.listdir(Folder_Target1):
           files_one.append(files)
           log.writelines("[" + str(x) +"]  " +files+ ' Found ! '+'\n')
           x+=1

log.writelines("\n\n\n\n\n------------------------------------------------------------------\n\n\n")
x = 1
log.writelines("\n\nOther Folder In : " + Folder_Target2 + " : \n--------------------------------------------------------------------------------------\n\n\n")
for files1 in os.listdir(Folder_Target2):
           files_two.append(files1)
           log.writelines("[" + str(x) + "]  " + files1 +' Found ! '+'\n')
           x += 1
x=1
log.writelines("\n\nMOVED In : " + Folder_Target_aftercut + " : \n--------------------------------------------------------------------------------------\n\n\n")
for x1 in files_one :
    for y1 in files_two:
        if x1 == y1 :
            files_after_filterd.append(x1)
            shutil.move(Folder_Target2 + "/" + x1,Folder_Target_aftercut)
print("\n\nFile Matched is : \n--------------------\n\n\n")
log.writelines("\n\nFile Matched is : \n--------------------\n\n\n")
if files_after_filterd :
    for f in files_after_filterd :
        print(" ["+ str(x) +"] File  :  "+ f +"     [ MOVED SUCCESSFULLY ! ]" + "\n")
        log.writelines(" ["+ str(x) +"] File  :  "+ f +"     [ MOVED SUCCESSFULLY ! ]" + "\n")
        x+=1


else :
        print("Zero File  Matched !")
        log.writelines("Zero File  Matched !")

log.close()