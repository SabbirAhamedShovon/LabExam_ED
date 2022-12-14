import glob
import shutil
import os
import zipfile
import runpy

source_path = './source/*'
list_all = glob.glob(source_path)
if len(list_all) > 0:
    list_text= []
    for address in list_all:
        if '.txt' in address:
            list_text.append(address)
        elif '.py' in address:
            runpy.run_path(address)
    
    if len(list_text)>0:
        obj_name = list_text[0]
        shutil.copy(obj_name,'./server')


        #now we will use our copy file. 
        used_file_path = './server/*.txt'
        used_file_name = glob.glob(used_file_path)[0]


        with open(used_file_name,'r') as file:
            lines = file.readlines()

        zip_file = zipfile.ZipFile('./server/zip_file.zip','a')
        i = 1
        j = 1
        while(i<30):
            i =j*10
            ll= 'some' + '_' + str(j)+'.' + 'txt'
            j+=1
            new_path = f"./server/{ll}"


            #make 3 processed file as requirement and zip them in server file.
            shutil.copy(used_file_name,new_path)   
            f = open(new_path,'w')
            f.write('')
            f.close()
            with open(new_path,'a') as result_file:
                for k in range(i):
                    if len(lines)>k:
                        result_file.write(lines[k])
            zip_file.write(new_path,compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()



        #text file that is copied from source file is removing
        os.remove(used_file_name)



        #access 3 processd file for deleting from server.
        old_file = glob.glob('./server/*.txt')
        for file in old_file:
            os.remove(file)



        #send the zip file to destination file.
        shutil.copy('./server/zip_file.zip','./destination/zip_file.zip')



        #remove the zip file from server
        os.remove('./server/zip_file.zip')



        #unzip the file in destination as requirment
        unzip = zipfile.ZipFile('./destination/zip_file.zip','r')
        unzip.extractall('./destination/unzipfile')
        unzip.close()


        #As it is not said to remove the source file from the source file. So I keep it.
        #For that reason i dont use Death loop.