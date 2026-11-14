# 贡献指南（Contributing）

感谢你关注本项目！欢迎通过 Issue、Pull Request 或 Star、Watch 等方式参与开源协作。

## 一、反馈问题（Issue）

1. 在仓库 Issues 页面点击 New Issue。
2. 选择问题类型：Bug 报告 / 功能建议 / 文档改进。
3. 描述清楚：操作步骤、预期结果、实际结果、运行环境（操作系统、Python 版本）。
4. 如为 Bug，请附上报错信息或截图。

## 二、提交代码（Pull Request）

1. Fork 本仓库到自己的 GitHub 账号。
2. 从 `dev` 分支拉出功能分支：

   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/你的功能名
   ```

3. 在功能分支上完成修改并提交，提交信息清晰说明改动内容。
4. 推送分支并向 `dev` 分支发起 Pull Request。
5. 等待维护者 Review；如有修改意见，在原分支继续提交即可。

## 三、代码规范

- Python 代码遵循 PEP 8 基本风格，缩进使用 4 个空格。
- 新增功能需补充对应的测试用例或使用说明。
- 提交前确认程序可正常运行，不提交临时文件与敏感信息。

## 四、行为准则

请保持友好、尊重的沟通态度，共同维护开放协作的开源氛围。
