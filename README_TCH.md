[English](README.md) | 繁體中文
# AI 圖片 關鍵字讀取器
一個幫你獲得圖片資訊的工具。

目前完美適配 Stable diffusion。

這個工具也能幫你獲得其他AI圖片資訊。
# 目前支持的AI圖片
- [x] Stable diffusion
- [x] Naifu(4chan版本)
- [x] NovelAI(官網版本)
# 如何使用
* import
  * 導入想提取資訊的圖片，它會幫忙提取出資訊，並填到文字框中。
* save
  * 它會在和此提取器同個資料夾中創建一個同名的 txt 檔，並把所有資訊填到裡面。
* cmd 環境(純指令或 linux 環境)
  * 使用 python 啟動 ```ai_tag_extractor_cmd.py``` 輸入需要拆解資訊的圖片路徑
# 範例圖片
這個圖片是用 Stable diffusion 生成的。將會作為下方展示的範例圖片。

## Stable-diffusion 圖片
![test-stable-diffusion](/sample/stable-diffusion-test.png)
## Naifu(4chan 版本) 圖片
![test-naifu](/sample/naifu-sample.png)
## NovelAI 圖片
![test-novelai](/sample/novelai-sample.png)
# UI
![UI](image/add_clear.png)
# After import image file
![import](image/import.png)
# 保存成 txt
## stable-diffusion 格式
![save](image/save_txt.png)
## Naifu(4chan ver) 格式
![save_naifu](image/save_txt_naifu.png)
## NovelAI 格式
![save](image/save_txt_novelai.png)

# 紀錄
## 版本 1.0
* 可以導入圖片得到圖片資訊。
* 可以儲存圖片資訊。
* 可以支持 stable-diffusion。
* 可以支持 Naifu(4chan版本)。
## 版本 1.1
* 現在支持 NovelAI 官網圖片的格式。
## 版本 1.1.1
* 修復導入錯誤檔案的 run time error。
## 版本 1.2
* 新增清除按鈕
* 新增狀態提示
* ![add_clear](image/add_clear.png)
## 版本 1.2.1
* 新增 ```ai_tag_extractor_cmd.py``` 可以在 cmd 和 linux 環境使用
