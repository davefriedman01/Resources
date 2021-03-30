# VC Version Control

### GitHub<br>
- GitHub [Home](https://github.com)<br>
- GitHub [Docs](https://docs.github.com/en)<br>
- GitHub [Git Guide](https://github.com/git-guides/)<br>
- GitHub [Learning Lab](https://lab.github.com)<br>
  - GitHub [Learning Lab: Introduction to GitHub](https://lab.github.com/githubtraining/introduction-to-github)<br>
- GitHub [Cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet/)<br>
- GitHub [YouTube](https://www.youtube.com/channel/UC7c3Kb6jYCRj4JOHHZTxKsQ)
- GitHub Training & Guides [YouTube](https://www.youtube.com/channel/UCP7RrmoueENv9TZts3HXXtw)<br>
  - GitHub Training & Guides [Git LFS Large File Storage](https://www.youtube.com/watch?v=uLR1RNqJ1Mw)<br>
- GitHub [Wiki](https://en.wikipedia.org/wiki/GitHub)<br>
- GitHub Pages [Home](https://pages.github.com)<br>
<details><summary>YouTube Talks, Tutorials, etc.</summary><br>

- "Git & GitHub Crash Course For Beginners". (2017). Traversy Media. [YouTube](https://www.youtube.com/watch?v=SWYqp7iY_Tc).<br>
- "Git and GitHub for Beginners - Crash Course". (2020). freeCodeCamp.org. [YouTube](https://www.youtube.com/watch?v=RGOj5yH7evk).<br>
</details>

### GitLab<br>
- GitLab [Home](https://about.gitlab.com)<br>
- GitLab [Docs](https://docs.gitlab.com)<br>
  - GitLab and SSH Keys [Docs](https://docs.gitlab.com/ee/ssh/README.html)<br>
- GitLab [Wiki](https://en.wikipedia.org/wiki/GitLab)<br>

### Git<br>
- Git [Home](https://git-scm.com)<br>
- Git [Docs](https://git-scm.com/doc)<br>
- Git [Wiki](https://en.wikipedia.org/wiki/Git)<br>
- Chacon, Scott & Ben Straub. (2014). [_Pro Git: Everything You Need to Know About Git, 2nd Ed_](https://git-scm.com/book/en/v2). Apress.<br>
<details><summary>Git CL</summary><br>

`git --version` Verify that git is successfully installed on your system<br>

**Run this command when you want to update your GitHub repo:<br>
`git add . && git commit -m "your commit message" && git push`<br>
or separately:<br>
`git add .`<br>
`git commit -m "your commit message"`<br>
`git push`<br>**

Check the status of files and folders in your local project directory (i.e., tracked or no, added or no, committed or no, pushed or no, etc.):<br>
[`git status`](https://git-scm.com/docs/git-status)<br>

Run this set of commands the first time you connect your local project directory to your new GitHub repo:<br>
`echo "# Your Repo Name and Description, For Example" >> README.md`<br>
[`git init`](https://git-scm.com/docs/git-init)<br>
[`git add README.md`](https://git-scm.com/docs/git-add)<br>
[`git commit -m "your commit message"`](https://git-scm.com/docs/git-commit)<br>
[`git branch -M main`](https://git-scm.com/docs/git-branch)<br>
[`git remote add origin git@github.com:<github-username>/<github-repo-name>.git`](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emaddem)<br>
[`git push -u origin main`](https://git-scm.com/docs/git-push)<br>

[`git remote`](https://git-scm.com/docs/git-remote) Gets the local name you assigned to your remote GitHub repo when you ran `git remote add...` (typically, `origin`)<br>
[`git remote get-url origin`](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emget-urlem)<br>
[`git remote set-url origin git@github.com:<github-username>/<github-repo-name>.git`](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emset-urlem) This is useful when you change the name of your GitHub repo and you also need to change its name in your local configuration to maintain a connection<br>

[`git clone <url>`](https://www.git-scm.com/docs/git-clone)<br>

[`git config -l` or `git config --list`](https://git-scm.com/docs/git-config#Documentation/git-config.txt--l)<br>

`git lfs version`<br>
`git lfs track`<br>
`git lfs ls-files`<br>
`git lfs clone --depth=1 https://github.com/<github-username>/<github-repo-name>.git`<br>
</details>
<details><summary>YouTube Talks, Tutorials, etc.</summary><br>

- "Git Tutorial for Beginners: Command-Line Fundamentals". (2015). Corey Schafer. [YouTube](https://www.youtube.com/watch?v=HVsySz-h9r4).<br>
</details>

### VC Version Control<br>
- VC [Wiki](https://en.wikipedia.org/wiki/Version_control)<br>
- VC [MIT's Missing Semester](https://missing.csail.mit.edu/2020/version-control/)<br>
