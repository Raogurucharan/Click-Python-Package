import os
import subprocess
import json
import click
import cookiecutter
import sys
from cookiecutter import __version__
#os.remove("cookiecutter.json")  #removing file
try:
    os.remove("cookiecutter.json")
except OSError:
    pass

@click.command("")
@click.argument('command')
@click.argument('category')
@click.argument('pathname')
#@click.command(context_settings=dict(help_option_names=['-h', '--help']))
#@click.option('-l', '--list-installed', is_flag=True, help='List currently installed templates.')

def create_project(command, category, pathname ):
    
    if command != 'create':
        click.echo(f"Unknown command.")
    if category != 'project':
        click.echo(f"Unknown category.")
    if(not pathname):
        click.echo('Invalid path name.')

    try:                           
        os.remove("sample1.json")   #trying to remove the file
    except OSError:                 #if there is error we pass
        pass

    dictionary ={
        "directory_name": "helloworld",
        "file_name": "main",
        "greeting_recipient": "Aha"
    }

    with open("sample1.json", "w") as outfile:   #creating a json file
        json.dump(dictionary, outfile)          #Dumping the contents of file


    pwd = os.getcwd()
    os.system("cookiecutter " + pwd + "/templates/helloworld")

    #print("congrats! Project is created ")
    #os.remove("sample.json")
    #f = open(r"/templates/Testoing.json", "a")
    #os.remove("cookiecutter.json") 
    # click.echo(f"Hello {name}!") 


def deleteFile():
    try:                           
        os.remove("sample1.json")   #trying to remove the file
    except OSError:                 #if there is error we pass
        pass


if __name__ == '__main__':
    create_project()
    deleteFile()


#Notes;

#os.remove("cookiecutter.json") 
# python cli.py create project
# file_name="cookiecutter"
# file=file_name + ".json"
# file_path = os.path.join(os.getcwd(), file) 
#f = open(r"C:\Users\***\Desktop\dftemp\dftemp\templates\Test.json", "a")
# https://stackoverflow.com/questions/89228/how-to-execute-a-program-or-call-a-system-command
#os.remove("cookiecutter.json")  #removing file
#os.remove("sample.json")
# with open(os.path.join("/dftemp/templates/helloworld", "sample1.json"), 'w') as f:
# json.dump(dictionary, f)
