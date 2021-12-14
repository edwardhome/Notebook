---
tags: conda, 系統環境
---

# 使用Window內建之Powershell
一般`Windows`使用者使用[conda](conda用法)通常應該是在內建的`Powershell`進行操作，但是在部份的電腦中常常遇到無法有效開啟`conda`的環境問題。

![圖片](https://i.imgur.com/B3bofa5.png)

首先使用`conda`指令，發現`powershell`可以成功的呼叫出`conda`相關說明與指令，但是卻無法切換環境，**powershell**也無法在前面出現`(base)`。

![conda指令訊息](https://i.imgur.com/kW2wfts.png)

## 使用者原則問題
重點在於`powershell`的 *.ps1* 檔案，這個是PowerShell寫的指令碼文字，你可以在記事本中寫一段PowerShell程式碼，然後將其儲存為“xxx.ps1”ps1檔案是PowerShell寫好的指令碼檔案。在Windows系統中，預設情況下是不允許執行.ps1檔案的。

這時候會發現執行了`conda init powershell`之後再打開`powershell`後會發現類似以下的訊息：
```shell
. : 因為這個系統上已停用指令碼執行，所以無法載入 C:UsersUSERNAMEDocumentsWindows
PowerShellprofile.ps1 檔案。如需詳細資訊，請參閱 about_Execution_Policies，網址為
https:/go.microsoft.com/fwlink/?LinkID=135170。
位於 線路:1 字元:3
+ . 'C:UsersUSERNAMEDocumentsWindowsPowerShellprofile.ps1'
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

## 解決方式
使用 `Powershell ISE`進行原則修改，利用系統管理員的身份打開。
![powershell ISE](https://i.imgur.com/dCBKlVN.png)

並在頁面中輸入以下指令:
```shell
Get-ExecutionPolicy
```
![powershell ISE](https://i.imgur.com/HedMet4.png)
此時電腦預設應該是`Restricted`，這時候我們要輸入修改的指令

```shell
Set-ExecutionPolicy RemoteSigned
```

最後在將程式關掉，Powershell以**系統管理員身份**重新開啟，並重新輸入`conda init powershell`指令，使其寫入指令檔後再次關閉`Powershell`，重新開啟後，應該就能看到前方寫著`(base)`的環境狀態了，這時候也能透過`conda activate [name]`進行環境上的切換了。

# 同場加映
如何使用不同形式的文字列，使終端機的環境與路徑不僅僅只有文字。
![主題切換](https://i.imgur.com/DdtZPlA.png)


## 安裝方式
這裡要使用的是`oh-my-push`。
首先先在終端機中輸入以下指令
```shell
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser

```
其中會詢問是否安裝，一律選擇是(Y)即可。
在安裝完成後，便可以新增主題設定文件，這時候可以透過下列指令進行安裝。

```shell
if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force } 
notepad $PROFILE
```

沒意外的話，這時後會跳出一個記事本要求你輸入文字
分別填入這三行文字，便可以使用上圖所以顯示的畫面喔。
```
Import-Module posh-git 
Import-Module oh-my-posh 
Set-Theme Paradox
```
[一鍵安裝下載](http://nuueolab405.ddns.net:5000/sharing/WA7xiJDQT)

另外，該文字使用了一般等寬字體沒有的文字因此建議修改終端機的文字字型，以利整體文字顯示正常喔。
這裡推薦使用[**等距更紗黑體 TC**](https://github.com/be5invis/Sarasa-Gothic/releases/download/v0.16.1/sarasa-gothic-ttf-0.16.1.7z)，更換powershell的字型必須要在powershell打開後，右鍵點擊狀態列，選擇預設值，會出現一個新的頁籤，可以針對powershell內部顯示的部份進行調整，選擇所喜歡的字體後，便可以使用美美的終端機進行`python開發`。




