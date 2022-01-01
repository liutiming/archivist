# Archivist
![archivist](https://socialify.git.ci/liutiming/archivist/image?description=1&descriptionEditable=Easily%20archive%20%F0%9F%93%A6%20Download%20folder%20to%20Google%20Drive%20%E2%98%81%EF%B8%8F&issues=1&language=1&name=1&owner=1&stargazers=1&theme=Light)

Script for archiving Download folder by uploading **unmodified** files to a Google Drive folder. **Modified** files will remain in the Download folder for manual sorting. 

## Rationale 
While reading articles/documents online, I sometimes have to download them and make annotations. I want to archive the Download folder to Google Drive once in a while to free up hard disk space, but I also want to sort the annotated files separately because they contain my thinking process. This script will upload all unmodified files 

## Functionalities 
- Determines whether the file has been modified by the difference between the created time and modified time. If the difference is less than one minute, it will be uploaded. 
- Determines whether there is enough hard disk space in the Google Drive folder. It only moves the file when there is still 5GB of free space after uploading the file. 
- Check for active internet connection
- No extra dependencies needed

## Assumptions 
- .mp4 and .wav files are not treated as modified files because I rarely modify/annotate them by hand. They often have different modified and created time so would require extra design to deal with. 
- All file directories are based on my local computer's format 
- Windows OS

## Potential improvement
- GUI 
