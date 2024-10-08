# Web Development for Noobs
This repo will help you get started with web development and displaying your website via Github pages. The result will be accessible at [https://joashgobin.github.io/](https://joashgobin.github.io/).

## Getting started with Github pages
- Create a Github account at [https://github.com/join](https://github.com/join)

- Create a public repo with the name:
```sh
<username>.github.io
```

- Download the git CLI at [https://git-scm.com/downloads](https://git-scm.com/downloads) and add it to PATH

- Open git in the terminal and run the commands:
```sh
git init
git add .
git commit -m "First commit"
git branch -M main
git remote add origin git@github.com:<username>/<username>.github.io
git push -u origin main
```

Now every commit you make will be available at:
```sh
https://<username>.github.io
```

after the Github deployment process is complete.