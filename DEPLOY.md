# 发布到 GitHub Pages

仓库已经包含 `.github/workflows/pages.yml`。推送到 `main` 后会自动构建并发布文档站。

## 需要填写的信息

发布前只需要确定：

- `YOUR_GITHUB_USERNAME`：你的 GitHub 用户名或组织名；
- 仓库名：默认 `awesome-eeg-learning`；
- 仓库可见性：默认推荐 `public`；
- `CITATION.cff` 中的作者姓名（可选）。

把 `README.md`、`mkdocs.yml` 和 `CITATION.cff` 中的 `YOUR_GITHUB_USERNAME` 替换为真实用户名。如果不需要个人作者署名，可从 `CITATION.cff` 删除占位作者。

## 安装并登录 GitHub CLI（Windows）

```powershell
winget install --id GitHub.cli
gh auth login
gh auth status
```

登录时选择 `GitHub.com`、`HTTPS`、`Login with a web browser`。

## 创建远程仓库并推送

在项目根目录执行：

```powershell
gh repo create awesome-eeg-learning --public --source . --remote origin --push
```

## 启用 Pages

打开 GitHub 仓库的 `Settings → Pages`，将 `Build and deployment / Source` 设为 `GitHub Actions`。然后打开 `Actions`，查看 `Deploy documentation to GitHub Pages` 工作流。

成功后地址通常为：

```text
https://YOUR_GITHUB_USERNAME.github.io/awesome-eeg-learning/
```

如果使用组织、不同仓库名或自定义域名，需要同步修改 `mkdocs.yml` 的 `site_url`、`repo_url` 和 `repo_name`。

