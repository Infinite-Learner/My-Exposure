from docxtpl import DocxTemplate
import pandas as pd
doc = DocxTemplate('Temp.docx')
df= pd.read_csv('ODD\2022-2023\II\A\data.csv')
for row in df.iterrows():
        if(df['Design']=="AP/CSE"):
                Design="Asst.Prof"
                Dept="Computer Science and Engingineering"
        elif(df['Design']=="AP/ECE"):
                        Design="Asst.Prof"
                        Dept="Electronics and Communication Engingineering"
        elif(df['Design']=="AP/Maths" or df['Design']=="AP/Chem" or df['Design']=="AP/Eng"):
                        Design="Asst.Prof"
                        Dept="School of Basic Engineering and Science"
        elif(row['Design']=="AP/MBA"):
                        Design="Asst.Prof"
                        Dept="Master of Business Administration"
        context={'Sub_Code':row['Code'],
            'Sub_Name':row['Name'],
            'Year':row['Yr'],
            'Sem':row['Se'],
            'AC':row['A'],
            'Prof':row['Profs'],
            'Design':Design,
            'Dept':Dept
        }
        doc.render(context)
        doc.save(f"ODD\2022-2023\II\A\{row['Code']}.docx")