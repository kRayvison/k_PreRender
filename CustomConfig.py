#encoding:utf-8
import sys
import os
# 文件名 RayvisionCustomConfig.py 文件夹 MAYA_HOME

def doCopyInstall(*args):
    _PLUGINS_COPY_SERVER = r"B:\custom_config\1859970\Maya2018.4"
    _PLUGINS_COPY_LOCAL = r"D:\work\Autodesk\Maya2018.4"
    _EXTRACTING_LOCAL = r'"C:\Program Files\Autodesk\Maya2018.4"'
    _EXTRACTING_7Z = r"Maya2018.4.7z"
    _EXTRACTING_TAR = r'"D:\work\Autodesk\Maya2018.4\Maya2018.4.7z"'
    print("doCopyInstall Maya2018.4 running ... ")

    print("PLUGINS_COPY_LOCAL: %s\n")
    _PATH = os.environ.get('PATH')
    _APP_EXTRACT_RUN_DIR = r"C:\7-Zip"
    os.environ['PATH'] = (_PATH + r";" if _PATH else "") + _APP_EXTRACT_RUN_DIR
    if not os.path.exists(_EXTRACTING_LOCAL):
        os.system("md " + _EXTRACTING_LOCAL)

    print("INSTALLING " + _EXTRACTING_7Z + " ...")
    os.system("robocopy /S /NDL /NFL %s %s %s" % (_PLUGINS_COPY_SERVER, _PLUGINS_COPY_LOCAL, _EXTRACTING_7Z))

    print("\nEXTRACTING:" + _EXTRACTING_TAR + " ...")
    subprocess.call(_APP_EXTRACT_RUN_DIR + r"/7z.exe x -y -aos " + _EXTRACTING_TAR + " -o" + _EXTRACTING_LOCAL)



def doConfigSetup(*args):
    print (r'args[0] is %s') %args[0]
    clientInfo = args[0]
    print ("config stratr")
    taskId = clientInfo["taskId"]


    #获取maya版本号
    SWV=clientInfo.swVer()
    print (r'maya ver is %s') %SWV

    #custom_app = r"B:\custom_config\1865943\MAYA_HOME"
    custom_app = os.path.realpath(__file__)
    custom_app = os.path.dirname(custom_app)
    custom_app = os.path.join(custom_app, 'MAYA_HOME')

    if SWV=='2017':
        #修改maya文档路径   原路径 C:/Users/dengtao/Documents/maya
        os.environ["MAYA_APP_DIR"] = custom_app
        print ("Set MAYA_APP_DIR => %s" %custom_app)

        #启用 旧版的 render layer 模式
        os.environ['MAYA_ENABLE_LEGACY_RENDER_LAYERS'] = '1'
        print ('render layer is enable')

    #maya 颜色空间管理
    os.environ['MAYA_COLOR_MANAGEMENT_POLICY_LOCK'] = '1'
    os.environ['MAYA_RENDER_SETUP_INCLUDE_ALL_LIGHTS'] = '0'
    os.environ['MAYA_RENDER_SETUP_USE_UNTITLED_COLLECTIONS'] = '0'
    #os.environ['OCIO'] = r'D:\work\OpenColorIO-Configs-master\aces_1.0.3\config.ocio'
    os.environ['OCIO_ACTIVE_DISPLAYS'] = 'ACES'
    os.environ['OCIO_ACTIVE_VIEWS'] = 'Rec.709:Raw'

    #maya2018经常会渲染崩溃, 设置Viewport 2.0 中渲染时始终使用 DirectX 11  会减少崩溃现象
    os.environ['MAYA_OPENCL_IGNORE_DRIVER_VERSION'] = '1'
    os.environ['MAYA_VP2_DEVICE_OVERRIDE'] = 'VirtualDeviceDx11'

    #关闭当前maya 重启一个新的maya 等待60秒
    os.system(r'wmic process where name="maya.exe" delete')
    print "kill maya.exe process"
    manager_exe = "C:/Program Files/Autodesk/Maya2018/bin/maya.exe"
    os.system('start "" "%s"' % manager_exe)
    print "run C:/Program Files/Autodesk/Maya2018/bin/maya.exe"
    time.sleep(60)
    print "waiting for 60 seconds"

    #结束rlm进程
    os.system(r'wmic process where name="rlm.exe" delete')

    #拷贝文件夹
    srcDir1=r"B:/AMPED"  
    dstDir1=r"C:/AMPED"
    os.system ("robocopy /s  %s %s" % (srcDir1, dstDir1))
    #启动指定进程
    os.system(r'start C:/AMPED/rlm.exe')


    #为usersetup.py 添加环境变量
    PYTHONPATH=''
    MAYA_SCRIPT_PATH = os.environ.get('MAYA_SCRIPT_PATH')
    os.environ['MAYA_SCRIPT_PATH'] = (_MAYA_SCRIPT_PATH + r";" if _MAYA_SCRIPT_PATH else "") + PYTHONPATH
    _PYTHONPATH = os.environ.get('PYTHONPATH')
    os.environ['PYTHONPATH'] = (_PYTHONPATH + r";" if _PYTHONPATH else "") + PYTHONPATH

    #
    hostFile = r"C:/Windows/System32/drivers/etc/hosts"
    ip = "10.60.100.103"
    net = "tai-isilon"
    f= open(hostFile,'r')
    lines = f.readlines()
    f.close()
    for line in lines[:]:
        if line.strip():
            if ip in  line.strip() or net in  line.strip() :
                lines.remove(line)
        else:
            lines.remove(line)
    lines.append("\n%s %s\n" %(ip, net))
    print "\nhost  %s == %s\n" %(ip, net)
    f= open(hostFile,'w')
    for line in lines:
        f.write(line)
    f.close()


def set_env(env,val):
    """添加环境变量的函数"""
    env_val = os.environ.get(env)
    os.environ[env] = (env_val  + r";"  if env_val else "") + val
    print "the env %s is %s" % (env, os.environ[env])
    return os.environ[env]