# 0x0D. Web stack debugging #0

This project is part of the DevOps and SysAdmin track at Holberton School. It is designed to help students understand the concepts of web stack debugging.

## Task 0: Give me a page!

In this task, we need to get Apache to run on a Docker container and return a page containing "Hello Holberton" when querying the root of it.

### Steps to Reproduce the Problem:

1. Run a Docker container with the image `holbertonschool/265-0`, mapping the container's port 80 to the host's port 8080:

```bash
docker run -p 8080:80 -d -it holbertonschool/265-0
```

2. Check the running Docker containers:

```bash
docker ps
```

3. Use `curl` to make a request to port 8080:

```bash
curl 0:8080
```

You should see an error message: `curl: (52) Empty reply from server`.

### Expected Result:

After connecting to the container and fixing the issue, `curl` should return a page that contains "Hello Holberton":

```bash
curl 0:8080
Hello Holberton
```

The command(s) used to fix the issue should be pasted in the answer file.

## References:

- [Docker concept page](https://docs.docker.com/get-started/overview/)

## Author:

Esianyo Dzisenu
