# 🌸 BanG Dream! 生日提醒

一个运行在 **GitHub Actions** 上的 Python 脚本，通过企业微信机器人 Webhook 自动发送 BanG Dream! 角色及其声优的生日祝福。

---

## ✨ 功能速览

* **GitHub Actions 自动运行**：~~每日日本时间0点自动运行，无需额外服务器。~~ 因推送延迟原因默认不启用 如需启用请查看`部署步骤`第3步
* **企业微信机器人兼容**：默认支持企业微信机器人消息格式。
* **Webhook 安全管理**：Webhook URL 通过 GitHub Secrets 配置，确保安全。
* **内置生日数据**：
    * 包含 **BanG Dream! 全部十个乐队**的角色生日：Poppin'Party、Afterglow、Pastel*Palettes、Roselia、Hello, Happy World!、Morfonica、RAISE A SUILEN、MyGO!!!!!、Ave Mujica、梦限大MewType。
    * 包含 **BanG Dream! 九个乐队的现任角色声优**生日（不含梦限大MewType）。

---

## 🚀 快速开始

### 部署步骤

1.  **Fork 此仓库**：将本仓库 Fork 到您的 GitHub 账户。
2.  **配置 Webhook URL**：
    * 在您的 Fork 仓库中，进入 `Settings` -> `Secrets and variables` -> `Actions` 。
    * 点击 `New repository secret`。
    * **名称 (Name)**：`WEBHOOK_URL`
    * **值 (Value)**：填入您的**企业微信机器人 Webhook URL**。
3.  **启用 GitHub Actions自动推送**：
    * 前往 `.github/workflows/birthday.yml` 取消第4-6行注释（删除行前的`#`）
    * 进入您的 Fork 仓库的 `Actions` 选项卡。
    * 启用工作流。

---
## ▶️ 运行示例

### 邦多利生日提醒
现在是日本时间7月14日，Poppin'Party的主唱、吉他手，**户山香澄**的生日，祝她生日快乐🎉！

---
## ⚙️ 自定义与维护

* **修改生日数据**：编辑 `birthdays.json` 文件以添加、修改或删除生日信息。文件格式如下：
    * **角色生日**：`["角色名", "乐队名", "职位", "MM-DD"]`
    * **声优生日**：`["声优姓名", "角色名", "乐队名", "职位", "MM-DD"]`
