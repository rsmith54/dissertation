import os
import sys

matchString = ""
if len(sys.argv)>2:
  matchString = sys.argv[2]

def latexFigureOutputter(figureName) :
    stringToReturn = r'\begin{figure}[tbph]'+ '\n'+ \
        r'\begin{center}' + ' \n'

    for iFigureName in figureName:
        stringToReturn += r'\includegraphics[width=0.35\textwidth]{'+iFigureName.replace('.eps','').replace('.pdf','')+'}' + '\n'

    stringToReturn += '\end{center} \n' + \
    '\caption{} \n' + \
    '\label{fig:'+figureName[0].replace('.eps','').replace('.pdf','').split('/')[-1]+'} \n' + \
    '\end{figure} \n'

    return stringToReturn

    # return r'\begin{figure}[tbph]'+ '\n'+ \
    # r'\begin{center}' + ' \n' + \
    # r'\includegraphics[width=0.45\textwidth]{'+figureName[0].replace('.eps','').replace('.pdf','')+'}' + '\n' + \
    # r'\includegraphics[width=0.45\textwidth]{'+figureName[1].replace('.eps','').replace('.pdf','')+'}' + '\n' + \
    # r'\includegraphics[width=0.45\textwidth]{'+figureName[2].replace('.eps','').replace('.pdf','')+'}' + '\n' + \
    # r'\includegraphics[width=0.45\textwidth]{'+figureName[3].replace('.eps','').replace('.pdf','')+'}' + '\n' + \
    # '\end{center} \n' + \
    # '\caption{} \n' + \
    # '\label{fig:'+figureName[0].replace('.eps','').replace('.pdf','').split('/')[3]+'} \n' + \
    # '\end{figure} \n'

for root, dirs, files in os.walk(sys.argv[1], topdown=False):
   counter = 0

   files = [f for f in files if not 'converted-to' in f and matchString in f ]

   chunks = [files[x:x+6] for x in xrange(0, len(files), 6)]
   for chunk in chunks:
       counter = counter + 1
       pathname = [ os.path.join(root, path).replace('./','') for path in chunk]
       if len(pathname) > 0 and ('.eps' in pathname[0] or '.pdf' in pathname[0]):
           if counter % 4 == 0 :
             print('\clearpage')
             counter = 0
           print(latexFigureOutputter(pathname))
