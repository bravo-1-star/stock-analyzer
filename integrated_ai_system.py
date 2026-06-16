# -*- coding: utf-8 -*-
"""
AI智能分析系统 - 多模型集成版
集成: ChatGPT、Claude、Gemini、GitHub、VSCode
"""

import json
import os
import sys
import subprocess
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

lib_path = os.path.join(os.path.dirname(__file__), 'lib')
if os.path.exists(lib_path):
    sys.path.insert(0, lib_path)

import pandas as pd
import numpy as np


class AIAnalyzer:
    """AI分析器"""
    
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        """加载配置"""
        config_path = os.path.join(os.path.dirname(__file__), '.env')
        config = {
            'openai_api_key': None,
            'anthropic_api_key': None,
            'gemini_api_key': None,
            'github_token': None,
            'github_repo': 'stock-analyzer'
        }
        
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        config[key.lower()] = value
        
        return config
    
    def analyze_with_chatgpt(self, stock_data: Dict) -> str:
        """使用ChatGPT分析"""
        try:
            from openai import OpenAI
            if not self.config.get('openai_api_key'):
                return "❌ ChatGPT: 未配置API密钥"
            
            client = OpenAI(api_key=self.config['openai_api_key'])
            
            prompt = f"""
你是一位专业的股票分析师。请分析以下股票数据：

股票代码: {stock_data['code']}
股票名称: {stock_data['name']}
当前价格: ¥{stock_data['price']}
涨跌停限制: ±10%
跌停价: ¥{stock_data['limit_down']}
涨停价: ¥{stock_data['limit_up']}

技术指标:
- MA5: ¥{stock_data['ma5']}
- MA20: ¥{stock_data['ma20']}
- MA60: ¥{stock_data['ma60']}
- RSI: {stock_data['rsi']}
- MACD: {stock_data['macd']}
- MACD信号: {stock_data['signal']}

近期涨跌:
- 1日: {stock_data['change_1d']}%
- 5日: {stock_data['change_5d']}%
- 20日: {stock_data['change_20d']}%

请给出：
1. 技术面分析
2. 明日走势预测（涨跌幅和价格）
3. 操作建议（买入/卖出/持有）
4. 止损止盈建议

要求：
- 预测价格必须在涨跌停范围内
- 使用专业但易懂的语言
- 直接给出结论，不要废话
"""
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"❌ ChatGPT分析失败: {str(e)}"
    
    def analyze_with_claude(self, stock_data: Dict) -> str:
        """使用Claude分析"""
        try:
            import anthropic
            if not self.config.get('anthropic_api_key'):
                return "❌ Claude: 未配置API密钥"
            
            client = anthropic.Anthropic(api_key=self.config['anthropic_api_key'])
            
            prompt = f"""
你是一位专业的股票分析师。请分析以下股票数据：

股票代码: {stock_data['code']}
股票名称: {stock_data['name']}
当前价格: ¥{stock_data['price']}
涨跌停限制: ±10%
跌停价: ¥{stock_data['limit_down']}
涨停价: ¥{stock_data['limit_up']}

技术指标:
- MA5: ¥{stock_data['ma5']}
- MA20: ¥{stock_data['ma20']}
- MA60: ¥{stock_data['ma60']}
- RSI: {stock_data['rsi']}
- MACD: {stock_data['macd']}
- MACD信号: {stock_data['signal']}

近期涨跌:
- 1日: {stock_data['change_1d']}%
- 5日: {stock_data['change_5d']}%
- 20日: {stock_data['change_20d']}%

请给出：
1. 技术面分析
2. 明日走势预测（涨跌幅和价格）
3. 操作建议（买入/卖出/持有）
4. 止损止盈建议

要求：
- 预测价格必须在涨跌停范围内
- 使用专业但易懂的语言
- 直接给出结论，不要废话
"""
            
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text
        
        except Exception as e:
            return f"❌ Claude分析失败: {str(e)}"
    
    def analyze_with_gemini(self, stock_data: Dict) -> str:
        """使用Gemini分析"""
        try:
            import google.generativeai as genai
            if not self.config.get('gemini_api_key'):
                return "❌ Gemini: 未配置API密钥"
            
            genai.configure(api_key=self.config['gemini_api_key'])
            model = genai.GenerativeModel("gemini-pro")
            
            prompt = f"""
你是一位专业的股票分析师。请分析以下股票数据：

股票代码: {stock_data['code']}
股票名称: {stock_data['name']}
当前价格: ¥{stock_data['price']}
涨跌停限制: ±10%
跌停价: ¥{stock_data['limit_down']}
涨停价: ¥{stock_data['limit_up']}

技术指标:
- MA5: ¥{stock_data['ma5']}
- MA20: ¥{stock_data['ma20']}
- MA60: ¥{stock_data['ma60']}
- RSI: {stock_data['rsi']}
- MACD: {stock_data['macd']}
- MACD信号: {stock_data['signal']}

近期涨跌:
- 1日: {stock_data['change_1d']}%
- 5日: {stock_data['change_5d']}%
- 20日: {stock_data['change_20d']}%

请给出：
1. 技术面分析
2. 明日走势预测（涨跌幅和价格）
3. 操作建议（买入/卖出/持有）
4. 止损止盈建议

要求：
- 预测价格必须在涨跌停范围内
- 使用专业但易懂的语言
- 直接给出结论，不要废话
"""
            
            response = model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            return f"❌ Gemini分析失败: {str(e)}"


class GitHubManager:
    """GitHub管理器"""
    
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        """加载配置"""
        config_path = os.path.join(os.path.dirname(__file__), '.env')
        config = {
            'github_token': None,
            'github_repo': 'stock-analyzer',
            'github_user': 'stock-analyst'
        }
        
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)
                        config[key.lower()] = value
        
        return config
    
    def init_repo(self) -> str:
        """初始化GitHub仓库"""
        try:
            if os.path.exists('.git'):
                return "✅ GitHub仓库已存在"
            
            subprocess.run(['git', 'init'], check=True, capture_output=True)
            subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True, capture_output=True)
            
            return "✅ GitHub仓库初始化完成"
        
        except Exception as e:
            return f"❌ GitHub初始化失败: {str(e)}"
    
    def commit_and_push(self, message: str = "Update analysis") -> str:
        """提交并推送"""
        try:
            subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
            subprocess.run(['git', 'commit', '-m', message], check=True, capture_output=True)
            
            if self.config.get('github_token'):
                remote_url = f"https://{self.config['github_token']}@github.com/{self.config['github_user']}/{self.config['github_repo']}.git"
                subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True, capture_output=True)
                subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True, capture_output=True)
                return "✅ 代码已推送到GitHub"
            
            return "⚠️ GitHub未配置Token，已提交但未推送"
        
        except Exception as e:
            return f"❌ 提交失败: {str(e)}"
    
    def create_release(self, version: str = "1.0.0") -> str:
        """创建版本发布"""
        try:
            subprocess.run(['git', 'tag', '-a', f'v{version}', '-m', f'Release {version}'], check=True, capture_output=True)
            
            if self.config.get('github_token'):
                subprocess.run(['git', 'push', '--tags'], check=True, capture_output=True)
                return f"✅ 版本 v{version} 已发布"
            
            return f"⚠️ 标签已创建但未推送: v{version}"
        
        except Exception as e:
            return f"❌ 创建发布失败: {str(e)}"


class VSCodeManager:
    """VSCode管理器"""
    
    def __init__(self):
        self.workspace_dir = os.path.dirname(__file__)
    
    def create_workspace(self) -> str:
        """创建VSCode工作区"""
        try:
            workspace = {
                "folders": [
                    {"path": "."}
                ],
                "settings": {
                    "python.pythonPath": "${workspaceFolder}/.venv/bin/python",
                    "editor.rulers": [80, 120],
                    "editor.formatOnSave": True,
                    "python.linting.enabled": True,
                    "python.linting.pylintEnabled": True,
                    "python.linting.flake8Enabled": True
                },
                "launch": {
                    "configurations": [
                        {
                            "name": "Python: Multi Model Predictor",
                            "type": "python",
                            "request": "launch",
                            "program": "${workspaceFolder}/multi_model_predictor.py",
                            "console": "integratedTerminal"
                        },
                        {
                            "name": "Python: Improved Analysis",
                            "type": "python",
                            "request": "launch",
                            "program": "${workspaceFolder}/improved_analysis.py",
                            "console": "integratedTerminal"
                        }
                    ]
                }
            }
            
            workspace_path = os.path.join(self.workspace_dir, 'stock-analyzer.code-workspace')
            with open(workspace_path, 'w', encoding='utf-8') as f:
                json.dump(workspace, f, indent=2, ensure_ascii=False)
            
            return f"✅ VSCode工作区已创建: stock-analyzer.code-workspace"
        
        except Exception as e:
            return f"❌ 创建工作区失败: {str(e)}"
    
    def install_extensions(self) -> str:
        """安装VSCode扩展"""
        extensions = [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "donjayamanne.python-extension-pack",
            "eamodio.gitlens",
            "GitHub.copilot",
            "njpwerner.autodocstring",
            "ms-toolsai.jupyter",
            "yzhang.markdown-all-in-one"
        ]
        
        results = []
        for ext in extensions:
            try:
                subprocess.run(['code', '--install-extension', ext], capture_output=True)
                results.append(f"✅ {ext}")
            except:
                results.append(f"⚠️ {ext} (可能已安装)")
        
        return "\n".join(results)
    
    def open_workspace(self) -> str:
        """打开VSCode工作区"""
        try:
            subprocess.run(['code', 'stock-analyzer.code-workspace'])
            return "✅ VSCode已打开工作区"
        except Exception as e:
            return f"❌ 打开工作区失败: {str(e)}"


class StockDataFetcher:
    """股票数据获取器"""
    
    def __init__(self):
        self.daily_limit = 0.10
    
    def get_data(self, code: str, days: int = 180) -> pd.DataFrame:
        """获取前复权数据"""
        try:
            import baostock as bs
            
            market = 'sh' if code.startswith('6') else 'sz'
            bs_code = f"{market}.{code}"
            
            lg = bs.login()
            if lg.error_code != '0':
                bs.logout()
                return self._generate_data(code, days)
            
            rs = bs.query_history_k_data_plus(
                bs_code,
                "date,open,high,low,close,volume",
                start_date=(datetime.now()-timedelta(days=days+30)).strftime('%Y-%m-%d'),
                end_date=datetime.now().strftime('%Y-%m-%d'),
                frequency="d",
                adjustflag="2"
            )
            
            data_list = []
            while rs.error_code == '0' and rs.next():
                data_list.append(rs.get_row_data())
            
            bs.logout()
            
            if len(data_list) >= 60:
                df = pd.DataFrame(data_list, columns=[
                    'date', 'open', 'high', 'low', 'close', 'volume'
                ])
                df['date'] = pd.to_datetime(df['date'])
                df = df.set_index('date')
                for col in ['open', 'high', 'low', 'close', 'volume']:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                return df.dropna()
            
        except Exception as e:
            print(f"获取数据失败: {e}")
        
        return self._generate_data(code, days)
    
    def _generate_data(self, code: str, days: int) -> pd.DataFrame:
        """生成模拟数据"""
        np.random.seed(int(code[-4:]))
        dates = pd.date_range(end=datetime.now(), periods=days, freq='B')
        base_price = 549.00
        
        returns = np.random.normal(0.0005, 0.008, days)
        prices = base_price * (1 + returns).cumprod()
        
        trend = np.linspace(-0.1, 0.05, days)
        prices = prices * (1 + trend)
        
        df = pd.DataFrame({
            'open': prices * np.random.uniform(0.99, 1.01, days),
            'high': prices * np.random.uniform(1.0, 1.02, days),
            'low': prices * np.random.uniform(0.98, 1.0, days),
            'close': prices,
            'volume': np.random.randint(5_000_000, 30_000_000, days)
        }, index=dates)
        
        return df
    
    def calculate_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """计算特征"""
        df = df.copy()
        
        df['ma5'] = df['close'].rolling(5).mean()
        df['ma20'] = df['close'].rolling(20).mean()
        df['ma60'] = df['close'].rolling(60).mean()
        
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        
        df['ema12'] = df['close'].ewm(span=12, adjust=False).mean()
        df['ema26'] = df['close'].ewm(span=26, adjust=False).mean()
        df['macd'] = df['ema12'] - df['ema26']
        df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()
        
        df['change'] = df['close'].pct_change() * 100
        
        return df.dropna()
    
    def get_stock_data(self, code: str) -> Dict:
        """获取股票数据字典"""
        df = self.get_data(code, days=100)
        df = self.calculate_features(df)
        
        latest = df.iloc[-1]
        
        stock_names = {
            '300502': '新易胜',
            '600309': '万华化学',
            '002460': '赣锋锂业',
            '300308': '中际旭创',
            '002466': '天齐锂业',
            '603005': '晶方科技',
            '600584': '中芯国际'
        }
        
        return {
            'code': code,
            'name': stock_names.get(code, '未知'),
            'price': round(latest['close'], 2),
            'ma5': round(latest['ma5'], 2),
            'ma20': round(latest['ma20'], 2),
            'ma60': round(latest['ma60'], 2),
            'rsi': round(latest['rsi'], 2),
            'macd': round(latest['macd'], 2),
            'signal': round(latest['signal'], 2),
            'change_1d': round(latest['change'], 2),
            'change_5d': round(df['change'].tail(5).mean(), 2),
            'change_20d': round(df['change'].tail(20).mean(), 2),
            'limit_down': round(latest['close'] * (1 - self.daily_limit), 2),
            'limit_up': round(latest['close'] * (1 + self.daily_limit), 2)
        }


class IntegratedSystem:
    """集成系统"""
    
    def __init__(self):
        self.ai_analyzer = AIAnalyzer()
        self.github_manager = GitHubManager()
        self.vscode_manager = VSCodeManager()
        self.data_fetcher = StockDataFetcher()
    
    def analyze_stock(self, code: str):
        """综合分析股票"""
        print("\n" + "="*90)
        print(f" 🤖 AI智能分析系统 - {code} 综合分析报告")
        print("="*90)
        
        print("\n📡 获取股票数据...")
        stock_data = self.data_fetcher.get_stock_data(code)
        
        print(f"\n{'='*90}")
        print(" 📊 股票基本信息")
        print("="*90)
        print(f"\n   股票代码: {stock_data['code']}")
        print(f"   股票名称: {stock_data['name']}")
        print(f"   当前价格: ¥{stock_data['price']}")
        print(f"   跌停价:   ¥{stock_data['limit_down']}")
        print(f"   涨停价:   ¥{stock_data['limit_up']}")
        
        print(f"\n{'='*90}")
        print(" 🤖 AI模型分析")
        print("="*90)
        
        print(f"\n--- ChatGPT分析 ---")
        print(self.ai_analyzer.analyze_with_chatgpt(stock_data))
        
        print(f"\n--- Claude分析 ---")
        print(self.ai_analyzer.analyze_with_claude(stock_data))
        
        print(f"\n--- Gemini分析 ---")
        print(self.ai_analyzer.analyze_with_gemini(stock_data))
        
        print(f"\n{'='*90}")
        print(" 🏗️ 开发环境状态")
        print("="*90)
        
        print(f"\n--- GitHub状态 ---")
        print(self.github_manager.init_repo())
        
        print(f"\n--- VSCode状态 ---")
        print(self.vscode_manager.create_workspace())
        
        print("\n" + "="*90)
        print(" 📝 配置说明")
        print("="*90)
        print(f"""
要使用AI模型分析，请在 .env 文件中配置以下API密钥：

OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
GEMINI_API_KEY=your-gemini-key
GITHUB_TOKEN=your-github-token
GITHUB_USER=your-github-username
GITHUB_REPO=your-repo-name

获取方式：
- OpenAI: https://platform.openai.com/api-keys
- Anthropic: https://console.anthropic.com/settings/api-keys
- Google Gemini: https://ai.google.dev/api-keys
- GitHub: https://github.com/settings/tokens
""")
        print("="*90)
    
    def setup_environment(self):
        """设置开发环境"""
        print("\n" + "="*90)
        print(" 🏗️ 设置开发环境")
        print("="*90)
        
        print("\n📦 安装VSCode扩展...")
        print(self.vscode_manager.install_extensions())
        
        print("\n📦 初始化GitHub仓库...")
        print(self.github_manager.init_repo())
        
        print("\n📦 创建VSCode工作区...")
        print(self.vscode_manager.create_workspace())
        
        print("\n✅ 环境设置完成！")
        print("="*90)


def main():
    """主函数"""
    system = IntegratedSystem()
    system.analyze_stock('300502')


if __name__ == "__main__":
    main()