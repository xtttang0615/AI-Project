# AI Learning & Drug Discovery Practice

个人学习人工智能与药物发现的小项目集合。

## 目录说明
- `notebooks/`：Jupyter 学习笔记与实验流程  
- `scripts/`：Python 工具脚本（如汉明距离计算）  
- `models/`：训练保存的模型（如 MLP on diabetes）  
- `data/`：未来存放数据集  
- `learning_notes/`：课程笔记（原“AI学习”文件夹）  
- `W1_Mon/`：图神经网络实践（GCN on Cora）  
- `.venv/`：Python 虚拟环境（请勿提交到 Git）

## 环境配置
```bash
python -m venv .venv
source .venv/Scripts/activate   # Git Bash / Windows
pip install -r requirements.txt
> 注：`requirements.txt` 记录了所有依赖包，用于一键安装环境。
