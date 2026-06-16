# API密钥获取详细指南

## 📋 目录
1. [OpenAI API密钥获取](#1-openai-api密钥获取)
2. [Anthropic API密钥获取](#2-anthropic-api密钥获取)
3. [Google Gemini API密钥获取](#3-google-gemini-api密钥获取)
4. [GitHub Token获取](#4-github-token获取)
5. [配置文件修改方法](#5-配置文件修改方法)

---

## 1. OpenAI API密钥获取

### 步骤：

1. **访问OpenAI官网**
   - 打开浏览器，访问：https://platform.openai.com/

2. **注册/登录账号**
   - 如果没有账号，点击"Sign up"注册
   - 如果已有账号，点击"Log in"登录

3. **进入API密钥管理页面**
   - 登录后，访问：https://platform.openai.com/api-keys
   - 或点击右上角头像 → "View API keys"

4. **创建新密钥**
   - 点击"Create new secret key"按钮
   - 给密钥命名（例如："stock-analyzer"）
   - 点击"Create secret key"

5. **复制密钥**
   - ⚠️ **重要**：密钥只显示一次，立即复制保存
   - 密钥格式：`sk-proj-xxxxxxxxxxxxx`

6. **粘贴到配置文件**
   - 打开 `.env` 文件
   - 将 `OPENAI_API_KEY=your-openai-api-key-here` 替换为：
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
   ```

### 💰 费用说明：
- GPT-4o-mini：$0.15/1M输入tokens，$0.60/1M输出tokens
- 新账号有免费额度（约$5）

---

## 2. Anthropic API密钥获取

### 步骤：

1. **访问Anthropic官网**
   - 打开浏览器，访问：https://console.anthropic.com/

2. **注册/登录账号**
   - 点击"Sign Up"注册新账号
   - 或点击"Log In"登录已有账号

3. **进入API密钥页面**
   - 登录后，访问：https://console.anthropic.com/settings/api-keys

4. **创建新密钥**
   - 点击"Create Key"按钮
   - 给密钥命名（例如："stock-analyzer"）
   - 点击"Create"

5. **复制密钥**
   - ⚠️ **重要**：密钥只显示一次，立即复制保存
   - 密钥格式：`sk-ant-xxxxxxxxxxxxx`

6. **粘贴到配置文件**
   ```
   ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
   ```

### 💰 费用说明：
- Claude 3 Sonnet：$3/1M输入tokens，$15/1M输出tokens
- 新账号有免费额度（约$5）

---

## 3. Google Gemini API密钥获取

### 步骤：

1. **访问Google AI Studio**
   - 打开浏览器，访问：https://ai.google.dev/

2. **登录Google账号**
   - 使用你的Google账号登录

3. **获取API密钥**
   - 点击"Get API key"按钮
   - 或访问：https://ai.google.dev/api-keys

4. **创建新密钥**
   - 点击"Create API key"按钮
   - 选择Google Cloud项目（或创建新项目）

5. **复制密钥**
   - 密钥格式：`AIzaSyxxxxxxxxxxxxx`
   - 点击复制按钮保存密钥

6. **粘贴到配置文件**
   ```
   GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxx
   ```

### 💰 费用说明：
- Gemini Pro：免费（有请求限制）
- Gemini Pro Vision：免费（有请求限制）

---

## 4. GitHub Token获取

### 步骤：

1. **访问GitHub设置**
   - 登录GitHub账号
   - 访问：https://github.com/settings/tokens

2. **创建新Token**
   - 点击"Generate new token"
   - 选择"Generate new token (classic)"

3. **配置Token权限**
   - Note: 填写"stock-analyzer"
   - Expiration: 选择"No expiration"或自定义时间
   - Select scopes: 勾选以下权限：
     - ✅ repo（完整仓库访问）
     - ✅ workflow（工作流访问）

4. **生成Token**
   - 点击"Generate token"按钮

5. **复制Token**
   - ⚠️ **重要**：Token只显示一次，立即复制保存
   - Token格式：`ghp_xxxxxxxxxxxxx`

6. **粘贴到配置文件**
   ```
   GITHUB_TOKEN=ghp_xxxxxxxxxxxxx
   GITHUB_USER=你的GitHub用户名
   ```

---

## 5. 配置文件修改方法

### 方法一：使用VSCode编辑

1. 打开VSCode
2. 打开项目文件夹：`d:\trae\fenxi3_demo`
3. 找到 `.env` 文件
4. 将对应的占位符替换为你的真实密钥

### 方法二：使用记事本编辑

1. 打开记事本
2. 打开文件：`d:\trae\fenxi3_demo\.env`
3. 替换对应的占位符
4. 保存文件

### 方法三：使用命令行编辑

```powershell
# 使用VSCode打开
code d:\trae\fenxi3_demo\.env

# 或使用记事本打开
notepad d:\trae\fenxi3_demo\.env
```

---

## ✅ 配置完成后测试

配置完成后，运行以下命令测试：

```powershell
# 测试AI模型连接
python integrated_ai_system.py

# 测试多模型预测
python multi_model_predictor.py

# 测试改进版分析
python improved_analysis.py
```

---

## ⚠️ 安全提示

1. **不要分享API密钥**
   - API密钥是个人私密信息，不要分享给他人

2. **不要上传到公开仓库**
   - `.env` 文件已添加到 `.gitignore`，不会被Git追踪
   - 确保不要将密钥上传到GitHub公开仓库

3. **定期更换密钥**
   - 如果密钥泄露，立即在对应平台删除并重新生成

4. **监控使用量**
   - 定期检查各平台的API使用量和费用

---

## 🆘 常见问题

### Q1: OpenAI API密钥无效？
- 检查密钥格式是否正确（以 `sk-` 开头）
- 检查账号是否有余额
- 检查密钥是否被删除

### Q2: Claude API调用失败？
- 检查密钥格式（以 `sk-ant-` 开头）
- 检查账号是否有余额
- 检查API版本是否正确

### Q3: Gemini API报错？
- 检查密钥格式（以 `AIzaSy` 开头）
- 检查Google Cloud项目是否启用
- 检查API配额是否用完

### Q4: GitHub Token无效？
- 检查Token权限是否正确（需要repo权限）
- 检查Token是否过期
- 检查用户名是否正确

---

## 📞 需要帮助？

如果在配置过程中遇到问题，请告诉我：
1. 哪个API密钥配置有问题
2. 具体的错误信息
3. 你已经完成的步骤

我会帮你解决！