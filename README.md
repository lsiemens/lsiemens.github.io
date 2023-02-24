lsiemens.github.io / lsiemens.com
=================================

Welcome to the repository for the blog I-Process. [I-Process](http://lsiemens.com)
can be found at http://lsiemens.com, and is produced using jekyll. 

Have any feedback for me? File an issue on this project and I will get
back to you as soon as I can.

Setup
=====
Instructions for setting up jekyll from "https://jekyllrb.com/docs/installation/ubuntu/".
Install ruby with the command `sudo apt install ruby-full build-essential zlib1g-dev`.
Then append the following lines to your `~/.bashrc` file.

```
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
```

Now that the environment is setup, install jekyll and bundler with
`gem install jekyll bundler`. Then use the make file to install required
gems with the command `make gem_update`. The site can be tested locally
with the commands `make all` or `make draft`.

