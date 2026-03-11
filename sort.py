import os
import shutil 

#file structure creation function
def makeFolder(sceneNum, directory, file):

    # Create directories
    os.makedirs(directory)
    print(f"'{directory}' created successfully.")


    # Source path 
    source =  "sort/" + file

    # Destination path 
                    
    destination = directory

    shutil.move(source, destination) 

path = "sort"

obj = os.scandir(path)

check = []

for entry in obj:
    if  entry.is_file():
        #get scene name from file name
        file = entry.name
       
       #extract scene number token
        sceneNum = ""
        for x in file:  
            if (x != "_"):
                sceneNum += x
            else:
                break

        # Specify the nested directory structure
        directory = sceneNum + "/" + sceneNum + "_datasheets"
        
        #add first item to repeat checker, create first folder structure
        if not check:
            makeFolder(sceneNum, directory, file)
            check.append(sceneNum)
            
        #repeat checker   
        else:
            
            isRepeat = False

            for x in check:
                if x == sceneNum:
                    isRepeat = True
                    
           #move file into existing folder for multicam slates
            if isRepeat == True:
                
                filepathSource = "sort/" + file
                
                shutil.move(filepathSource, directory)

           #creates folder structure for new slates     
            else:
                check.append(sceneNum)
                makeFolder(sceneNum, directory, file)
           
                    
