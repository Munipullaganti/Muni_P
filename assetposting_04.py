import pyautogui
import time


class saplogon(object):
    
    def __init__(self,user,pwd,inst,tcode,ccd,astn,ttype,ddt,avdt,amtpst,inptet,pstprd,dtype,offsetacc,ref,assm):
        
        self.userid = user
        self.password = pwd
        self.instance = inst
        self.pst = tcode
        self.compcode = ccd
        self.assetnum = astn
        self.transtype = ttype
        self.docdate = ddt
        self.astvaldate = avdt
        self.amountpstd = amtpst
        self.detailtext = inptet 
        self.postperiod = pstprd
        self.doctype = dtype
        self.offsetaccount = offsetacc
        self.reference = ref
        self.assignment = assm
        
        
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
        
    def aspost(self):
        pyautogui.typewrite(self.pst)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite(self.compcode)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(self.assetnum)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(self.transtype)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(self.docdate)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(self.astvaldate)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(self.amountpstd)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(self.detailtext)
        time.sleep(1)
        pyautogui.press('f6')
        time.sleep(1)
        pyautogui.typewrite(self.postperiod)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(self.doctype)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.typewrite(self.offsetaccount)
        pyautogui.press('tab')
        pyautogui.typewrite(self.reference)
        pyautogui.press('tab')
        pyautogui.typewrite(self.assignment)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 's')
        
        
        
###################################################################
        
