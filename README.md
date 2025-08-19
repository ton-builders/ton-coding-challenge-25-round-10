# TON Coding Challenge 2025 Round 10

> 时间：2025/08/14 - 2025/08/22

为了帮助大家快速掌握 TON 生态的开发技能，我们特别设计了有趣的编程入门挑战赛。快来参与并有机会赢取 Telegram Premium 大会员！详细的比赛规则请查看群组公告。

https://t.me/toneachat

> 如何参与？
>
> Fork 本仓库的代码，回答下面的问题，然后发起一个 Pull Requests 就算成功参与。

---

课件地址：https://ton-org.notion.site/Tolk-2385274bd2cf80db9deac2717ac17bf1

领奖信息收集：
1. 你的 Telegram 用户名 = @WorkSaveTravelRepeat
2. 你的主网 TON 钱包地址 = UQB33XTZtteUv4k6XksMYKWkAhWZY26MLf3xz29KRDa6lnmP


## 任务 1：通过 API 调用合约的 get 方法
### 任务描述：

1. 找一个钱包合约，调用其 get_public_key 方法

### 你的答案：

1. 将你的 get 方法调用代码提交到本项目的根目录，文件名为 =
import requests

wallet_address = "0:76bdbe2be02806a345d7c9f086e472d2b3b9734317acc6bc4f3761528583e650"

url = f"https://tonapi.io/v2/accounts/{wallet_address}/methods/get_public_key"

resp = requests.get(url)
print(resp.json())



---

## 任务 2：通过 TON Console 查询 NFT 信息

### 任务描述：

1. 找一个 NFT 集合，查询这个 NFT 集合的详细信息

### 你的答案：

1. 将你的 NFT 查询代码提交到本项目的根目录，文件名为 = 
import requests

collection_address = "0:b3358165102319dc590f09d22dfafd3d7a2a826249eba06c869b874bfbe2d9d2"

url = f"https://tonapi.io/v2/nft/collections/{collection_address}"

resp = requests.get(url)
print(resp.json())

---


