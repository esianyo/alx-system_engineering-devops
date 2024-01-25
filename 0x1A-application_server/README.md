# 0x1A. Application Server - DevOps/SysAdmin Project

## Overview

This project focuses on understanding the role of an application server in a web infrastructure and how to work with it. The main topics covered include web servers, servers, and web stack debugging.

## Concepts

- **Web Server**: A web server is a server that hosts websites and responds to requests from clients (typically web browsers). It serves content to the World Wide Web.
- **Server**: A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network.
- **Web Stack Debugging**: Web stack debugging is the process of diagnosing and fixing issues within the layers of the web stack (Operating system, web server, database, and programming language).

## Resources

- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (Do not install Gunicorn using virtualenv, just install everything globally)
- [Running Gunicorn](http://docs.gunicorn.org/en/stable/run.html)
- [Be careful with the way Flask manages slash in route - strict_slashes](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)
- [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

## Requirements

### General

- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments

### Bash Scripts

- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
