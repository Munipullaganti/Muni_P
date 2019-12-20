
import pyautogui
import time


class saplogon(object):
    
    def __init__(self,user,pwd,inst,tcode,ascls,ccd,ades,aown,ser,cc,bid,evg,uslife):
        
        self.userid = user
        self.password = pwd
        self.instance = inst
        self.ast = tcode
        self.aclass = ascls
        self.compcode = ccd
        self.desc = ades
        self.aowner = aown
        self.seri = ser
        self.costc = cc
        self.bulid = bid
        self.evalg = evg
        self.useful = uslife
        
    def activate_pre_invoke(self):
        pyautogui.hotkey('win', 'd')
    
    def activate_saplogon(self):
        try:
            pyautogui.hotkey('win','r')
            pyautogui.typewrite('saplogon')
            pyautogui.press('enter')
            return True
        except:
            return False
        
    def activate_post_invoke(self):
            pyautogui.hotkey('win', 'up')
    
    def open_instance(self):
        try:
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.typewrite(self.instance)
            pyautogui.press('enter')
            return True
        except:
            return False
        
    def saplogin(self):
        pyautogui.typewrite(self.userid)
        pyautogui.press('tab')
        pyautogui.typewrite(self.password)
        pyautogui.press('enter')
        
    def ascreate(self):
        pyautogui.typewrite(self.ast)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite(self.aclass)
        pyautogui.press('tab')
        pyautogui.typewrite(self.compcode)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(2)
        pyautogui.typewrite(self.desc)
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(self.aowner)
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite(self.seri)
        pyautogui.press('f6')
        time.sleep(3)
        pyautogui.typewrite(self.costc)
        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.typewrite(self.bulid)
        time.sleep(1)
        pyautogui.press('f6')
        time.sleep(1)
        pyautogui.typewrite(self.evalg)
        time.sleep(1)
        pyautogui.press('f6')
        time.sleep(1)
        pyautogui.press('f6')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite(self.useful)
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter') 
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')
        
        
#######################################################
import time
        
if __name__ == '__main__':
    mysap = saplogon('JTHIMMAIAH', 'welcome1$', 'ITG', 'as01', '1740', 'US96', 'test', 'test', 'NSN', 'US96500911','CCA04','USTC','4')
    mysap.activate_pre_invoke()
    time.sleep(2)
    mysap.activate_saplogon()
    time.sleep(6)
    mysap.activate_post_invoke()
    time.sleep(2)
    mysap.open_instance()
    time.sleep(5)
    mysap.saplogin()
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    mysap.ascreate()
    pyautogui.press('enter')
    time.sleep(3)
    
    
    
    