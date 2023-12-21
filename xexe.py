import subprocess
import platform
import os

project_name = input("What is the name of your project?")
system_os = platform.system()
directory_name = project_name


def install_react_native(project_name):
    subprocess.run(["npx", "react-native", "init", project_name, "--template", "react-native-template-typescript"])

def install_package(system_os, directory_name):
    os.chdir(directory_name)
    
    react_navigation = input("Do you want to add React Navigation? y/N: \n")
    stack_navigation = input("Do you want to add Stack Navigation? y/N: \n")
    # drawer_navigation = input("Do you want to add Drawer Navigation? y/N: \n")
    # bottom_tabs_navigation = input("Do you want to add Bottom Tabs Navigation? y/N: \n")

    if react_navigation.lower() == "y": 
      subprocess.run(["yarn", "add", "@react-navigation/native"]) 
      subprocess.run(["yarn", "add", "react-native-screens", "react-native-safe-area-context"])
      if system_os == "Darwin" :
         subprocess.run(["npx","pod-install", "ios"])
      else:
        return      
    else: 
      return
    
    if stack_navigation.lower() == "y":
      subprocess.run(["yarn", "add", "@react-navigation/stack"])
      subprocess.run(["yarn", "add", "react-native-gesture-handler"])
      subprocess.run(["yarn", "add", "@react-native-masked-view/masked-view"])
      if system_os == "Darwin" :
         subprocess.run(["npx","pod-install", "ios"])
      else:
        return    
    else:
       return
    
    # if drawer_navigation:
    #   subprocess.run(["yarn", "add", "@react-navigation/native"])
    # else:
    #    return
    
    # if bottom_tabs_navigation:
    #   subprocess.run(["yarn", "add", "@react-navigation/native"])
    # else:
    #    return

if __name__ == "__main__":
    print("Starting React Native project....")
    install_react_native(project_name)
    install_package(system_os, directory_name)
    print("The instalation is over, thank you :3")